from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os
from model import extract_features, model
from recommend import Recommender
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
recommender = Recommender()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploaded"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Image-based Recommendation API"}

@app.post("/recommend/")
async def recommend(file: UploadFile = File(...)):
    try:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        results = recommender.recommend(file_location, model=model)
        return JSONResponse(content={"recommendations": results})
    
    except Exception as e:
        print(f"[ERROR] {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

# Mount static images directory to serve images
images_path = os.path.join(os.path.dirname(__file__), "images")
app.mount("/images", StaticFiles(directory=images_path), name="images")
