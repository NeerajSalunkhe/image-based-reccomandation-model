import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image
import os

# Load MobileNetV2 model without the classification head, output features from global pooling layer
model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    return features[0]

def build_features(image_folder):
    features = []
    filenames = []

    for fname in os.listdir(image_folder):
        if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            fpath = os.path.join(image_folder, fname)
            feat = extract_features(fpath)
            features.append(feat)
            filenames.append(fname)
            print(f"Processed {fname}")

    features = np.array(features)
    return features, filenames

if __name__ == "__main__":
    img_folder = "images"
    features, filenames = build_features(img_folder)
    np.save('features.npy', features)
    import pickle
    with open('filenames.pkl', 'wb') as f:
        pickle.dump(filenames, f)
    print("Feature extraction complete and saved.")
