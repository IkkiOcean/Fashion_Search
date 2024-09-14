
# Fashion Search (Semantic Search Project)

Fashion Search AI is a deep learning project that provides a semantic search engine for fashion items. It is built using the Myntra dataset and leverages advanced natural language processing (NLP) techniques to allow users to search for fashion products using natural language queries. This project is ideal for building a search engine for fashion e-commerce platforms.

## Introduction

Fashion Search AI aims to enhance the search experience on fashion e-commerce platforms by using semantic search techniques. Instead of relying solely on keyword matching, the model understands the context and meaning behind user queries, providing more accurate and relevant search results.

## Features

- **Semantic Search**: Understands natural language queries and provides relevant search results.
- **Customizable**: Easy to train on different fashion datasets or modify for other e-commerce platforms.
- **Scalable**: Designed to handle large-scale fashion inventories.

## Dataset

The project uses the [Myntra Dataset](https://www.kaggle.com/myntra-dataset), which contains a diverse range of fashion items, including categories such as clothing, accessories, and footwear. The dataset includes images, descriptions, and metadata, making it suitable for training semantic search models.

## Model Architecture

The model is built using the following components:

- **Text Encoder**: A transformer-based model (e.g., BERT) is used to encode the textual descriptions of fashion items.
- **Image Encoder**: A CNN-based model (e.g., ResNet) is employed to extract features from product images.
- **Similarity Matching**: The embeddings from the text and image encoders are used to calculate the similarity between user queries and product descriptions/images, enabling semantic search.
## Installation

### Backend Setup


1. Download Myntra DataSet and extract in a file named ‘archive’ :
    
	Link : https://www.kaggle.com/datasets/ronakbokaria/myntra-products-dataset

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
 
   ```bash
   pip install -r requirements.txt
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd react-app
   ```

2. Install the required packages:
   ```bash
   npm install
   ```

## Running the Project

### Running the Backend

1. Navigate to the backend directory:
   ```bash
   cd ..
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Start the Flask server:
   ```bash
   Python server.py
   ```

   The backend server will be running at `http://127.0.0.1:5000`.

### Running the Frontend

1. Navigate to the frontend directory:
   ```bash
   cd react-app
   ```

2. Start the React app:
   ```bash
   npm start
   ```

   The frontend application will be running at `http://localhost:3000`.

## Project Structure

```plaintext
your-repo/
│
├─
├── server.py
│   ├ requirements.txt
│   
│
├── react-app/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│
└── README.md
```

## API Endpoints

- `GET /get-result` - Endpoint that returns a generative response.

