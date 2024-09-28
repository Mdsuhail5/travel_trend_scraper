# data_collection/image_processor.py

import os
import cv2
import pytesseract
from PIL import Image
import numpy as np
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text

def extract_features(image_path):
    model = VGG16(weights='imagenet', include_top=False)
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    return features.flatten()

def process_images(input_directory):
    results = []
    for filename in os.listdir(input_directory):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_directory, filename)
            text = extract_text_from_image(image_path)
            features = extract_features(image_path)
            results.append({
                'filename': filename,
                'text': text,
                'features': features
            })
    return results