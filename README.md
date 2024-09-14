
# Flask and React Project

This project consists of a backend server built with Python Flask and a frontend application built with React. The Flask server provides a RESTful API, and the React app consumes this API to display data to the user.


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

