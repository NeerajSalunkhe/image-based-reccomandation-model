import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from model import extract_features  # Import the standalone function

class Recommender:
    def __init__(self, features_path='features.npy', filenames_path='filenames.pkl'):
        self.features = np.load(features_path)
        with open(filenames_path, 'rb') as f:
            self.filenames = pickle.load(f)

    def recommend(self, query_img_path, top_k=5, model=None):
        # Use the imported extract_features function (ignore model param)
        query_feat = extract_features(query_img_path).reshape(1, -1)

        sims = cosine_similarity(query_feat, self.features)[0]
        idxs = sims.argsort()[-top_k:][::-1]  # top k indices

        results = [{'filename': self.filenames[i], 'score': float(sims[i])} for i in idxs]
        return results
