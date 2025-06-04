# 🧠 AI Content-Based Image Recommender System

This is an AI-powered **content-based image recommendation system** that recommends visually similar products (e.g., bags, toothbrushes) using deep learning and web technologies.

---

## 📦 Tech Stack

- 🧠 **TensorFlow (MobileNetV2)** for image feature extraction  
- ⚡ **FastAPI** backend (Python 3.10)  
- 🖼️ **Next.js (React)** frontend for uploading images and showing results  
- 📊 **pandas** for data handling  

---

## 📁 Project Structure

```
content-recommender/
├── backend/
│   ├── main.py
│   ├── model.py
│   └── recommend.py
│
└── frontend/
    ├── package.json
    └── src/app/page.js
```

---

## 🐍 Backend Setup (Python 3.10 + FastAPI + TensorFlow)

### ✅ Prerequisites

- Python **3.10** installed  
- Node.js and npm installed (for frontend)

You can check installed Python versions with:

```bash
py --list
```

---

### 📦 Step 1: Set up backend environment

```bash
cd backend

# (Optional) Create virtual environment for Python 3.10
py -3.10 -m venv venv
venv\Scripts\activate  # On Windows
```

---

### 📦 Step 2: Install dependencies

```bash
# Use Python 3.10 to install all packages
py -3.10 -m pip install --upgrade pip

# Install required packages
py -3.10 -m pip install fastapi uvicorn python-multipart tensorflow pandas pillow
```

---

### ▶️ Step 3: Run the backend server

```bash
# From backend folder
py -3.10 -m uvicorn main:app --reload
```

This starts FastAPI at:  
📍 `http://127.0.0.1:8000`

---

## ⚛️ Frontend Setup (Next.js)

### 📦 Step 1: Install frontend dependencies

```bash
cd frontend

# Install node modules
npm install
```

---

### ▶️ Step 2: Run the frontend server

```bash
npm run dev
```

Your frontend is running at:  
📍 `http://localhost:3000`

---

## 🔁 How It Works

1. Upload a product image via the frontend.
2. Backend extracts features using MobileNetV2.
3. Finds and returns similar images based on visual similarity.
4. Frontend displays the uploaded image and recommendations.

---

## ⚠️ Troubleshooting

- ✅ **TensorFlow errors?** Ensure you're using Python 3.10  
- ✅ **"Method Not Allowed"?** Make sure you're using POST to `/recommend/`  
- ✅ **CORS issue?** CORS middleware is already configured for local dev  

---

## 🧪 Optional: Install everything via `requirements.txt`

You can create a `requirements.txt` in the backend folder:

```
fastapi
uvicorn
python-multipart
tensorflow
pandas
pillow
```

Then install everything with:

```bash
py -3.10 -m pip install -r requirements.txt
```

---

## 📝 License

MIT License — free to use, modify, and distribute.

---

## 🙋 Want Help?

Feel free to open an issue or ask questions!
