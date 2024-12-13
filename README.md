# Fruit Classification Web App

<<<<<<< HEAD
A Flask-based web application for classifying fruits as fresh or rotten using a pre-trained PyTorch model.
=======
A Flask-based web application for classifying fruits as fresh or rotten using CNN model.

##### Datasets Download [Fresh-Rotten]([https://developer.android.com/studio](https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification/data))

## Preview
>>>>>>> 5fde2b34fabe8492603a7ad2568b67e555dbcd33

## Features
1. Upload an image of a fruit through a simple web interface.
2. Classify fruits into the following categories:
<<<<<<< HEAD
    a. Fresh Apples
    b. Fresh Bananas
    c. Fresh Oranges
    d. Rotten Apples
    e. Rotten Bananas
    f. Rotten Oranges
=======
   - Fresh Apples
   - Fresh Banana
   - Fresh Oranges
   - Rotten Apples
   - Rotten Banana
   - Rotten Oranges
>>>>>>> 5fde2b34fabe8492603a7ad2568b67e555dbcd33
3. Powered by a ResNet18 model fine-tuned with PyTorch.

## Install Dependencies
Run the following command to install required Python packages:
`pip install -r requirements.txt`

## Run the Application
1. Start the Flask Server `python app.py`
2. Access the Web Application `http://127.0.0.1:5000/`

<<<<<<< HEAD
=======
## Endpoint
- **URL**: /predict
- **Method**: POST
- **Headers**
  - `Content-Type: Multipart/form-data`
  - `file` (file): The image file of the fruits.
- **Response**
  ```bash
  {
  "class": "Fresh Apples"
  }
  ```
>>>>>>> 5fde2b34fabe8492603a7ad2568b67e555dbcd33
