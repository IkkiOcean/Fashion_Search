
from flask import Flask
from flask_cors import cross_origin
from flask import request

import pandas as pd
import numpy as np
import chromadb
from chromadb.utils import embedding_functions
import google.generativeai as genai
import os
import gdown #downloads from gdrive
import opendatasets as od  #downloads from kaggle


kaggle_url = "https://www.kaggle.com/datasets/djagatiya/myntra-fashion-product-dataset"
db_url = 'YOUR GOOGLE DRIVE URL TO STORE THE MODEL CREATED'

if os.path.exists('myntra-fashion-product-dataset'):
    print("Myntra dataset already preset")
else:
    print('Downloading myntra dataset from kaggle')
    od.download(kaggle_url) 
if os.path.exists('db'):
    print("db exists already")
else:
    print('Downloading Embedding documents from database')
    gdown.download_folder(db_url)


app = Flask(__name__)
fashion_data = pd.read_csv('myntra-fashion-product-dataset/Fashion Dataset v2.csv')
api_key  = 'API_KEY'
genai.configure(api_key = api_key)
model = genai.GenerativeModel('gemini-pro')

client = chromadb.PersistentClient(path="db/")  # data stored in 'db' folder
# em = embedding_functions.SentenceTransformerEmbeddingFunction(model_name='sentence-transformers/all-MiniLM-L6-v2')
em  = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=api_key)
fashion_collection = client.get_collection(name='fashion_items', embedding_function=em)

def fashion_search(query, n_results = 3):
    
    threshold = 0.2

    results_df = pd.DataFrame()

    try:
        results = fashion_collection.query(
            query_texts=query,
            n_results= n_results
        )

        Keys = []
        Values = []

        for key, val in results.items():
            if val is None:
                continue
            for i in range(len(val[0])):  # Iterate over the actual length of val
                Keys.append(str(key) + str(i))
                if len(val[0]) > i:  # Check if the current index exists in val
                    Values.append(str(val[0][i]))

       
        print("Not found in cache. Found in the main collection.")

        result_dict = {'Metadatas': results['metadatas'][0], 'Documents': results['documents'][0], 'Distances': results['distances'][0], "IDs": results["ids"][0]}
        results_df = pd.DataFrame.from_dict(result_dict)


    except:
        print("No valid results found in cache!")
        

    return results_df.sort_values('Distances')['IDs'].to_list(), results_df.sort_values('Distances')[["Metadatas","IDs"]]
def generate_response_fashion(query, top_3_RAG):
    
    messages = f""""You are a helpful AI assistant in the fashion domain, specialized in providing accurate answers to fashion-related queries."
         You have received a query from a user looking for fashion-related information. The query is: "{query}".
                                        Additionally, you have obtained the top 3 relevant results from the fashion dataset in the dataframe '{top_3_RAG}'.

                                        The 'Documents' column in this dataframe contains descriptions of fashion items, and the 'Metadatas' column contains additional information such as item name, Brand and color.

                                        Your task is to use the information provided in '{top_3_RAG}' to generate a response to the query "{query}". Ensure that your response is informative and relevant to the user's query. Utilize the metadata to cite the relevant fashion items.

                                        Please adhere to the following guidelines:
                                        1. Provide accurate and relevant information based on the user query and the top 3 search results.
                                        2. You may use any relevant details from the dataframe to craft your response.
                                        3. If any of the fashion items contain tables or structured information, format and present it clearly.
                                        4. Use the metadata to cite the names, Brands of the relevant fashion items.
                                        5. Ensure that you do not mention any kind of ID of any product in your response
                                        6. If you are unable to provide a complete answer, offer guidance on where the user can find further information within the cited fashion items.
                                        7. As a user-facing assistant, focus on delivering a direct and concise response without delving into technical details.
                                        8. Please note that detailed price and rating information might change from time to time. For more details,you should recommend to visit our website page.
                                        9. Do no include any image or link in the response.

                                        Your response should directly address the user's query and include citations for the referenced fashion items. Present the information in a well-organized and easily understandable format.
                                        """
    

    response = model.generate_content(
    contents= messages
    )
    try: 
        res = response.text
    except:
        res = "Here are the results for your query"

    return res





@app.route('/get-result', methods = ["GET"])
@cross_origin()
def handle_query():
    query = request.args.get('query')
    result_ids, data = fashion_search(query)
    result_ids = [int(x) for x in result_ids]
    result_data = fashion_data[fashion_data['p_id'].isin(result_ids)].copy()
    result_data['ratingCount'] = result_data['ratingCount'].fillna(0)
    result_data['avg_rating'] = result_data['avg_rating'].fillna(0)
    result_data.drop(['p_attributes'], axis=1, inplace =True)
    response = generate_response_fashion(query, data)
    result_data['metadata'] = response
    # response, p_ids = generate_response_fashion(query, top_3)
    return result_data.to_dict('records'), 200

app.run()
