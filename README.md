# Fruit Classification Web App

A Flask-based web application for classifying fruits as fresh or rotten using a pre-trained PyTorch model.

## Features
1. Upload an image of a fruit through a simple web interface.
2. Classify fruits into the following categories:
    a. Fresh Apples
    b. Fresh Bananas
    c. Fresh Oranges
    d. Rotten Apples
    e. Rotten Bananas
    f. Rotten Oranges
3. Powered by a ResNet18 model fine-tuned with PyTorch.

## Install Dependencies
Run the following command to install required Python packages:
`pip install -r requirements.txt`

## Run the Application
1. Start the Flask Server `python app.py`
2. Access the Web Application `http://127.0.0.1:5000/`
