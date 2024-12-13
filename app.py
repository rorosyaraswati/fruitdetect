import torch
import torchvision.models as models
from flask import Flask, request, jsonify, render_template
from torchvision.transforms import Compose, Resize, ToTensor
from PIL import Image

# Initialize Flask app
app = Flask(__name__)

# Define class labels
class_labels = ['freshapples', 'freshbanana', 'freshoranges', 
                'rottenapples', 'rottenbanana', 'rottenoranges']

# Define preprocessing
transform = Compose([
    Resize((224, 224)),
    ToTensor()
])

# Load pre-trained model 
model = models.resnet18(pretrained=False)  # Use your specific model here
model.fc = torch.nn.Linear(model.fc.in_features, len(class_labels))  # Adjust final layer
model.load_state_dict(torch.load('model_fruits360.pth'))
model.eval()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Load and preprocess image
    image = Image.open(file.stream)
    image = transform(image).unsqueeze(0)  # Add batch dimension
    
    # Predict
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
    
    predicted_class = class_labels[predicted.item()]
    return jsonify({'class': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)