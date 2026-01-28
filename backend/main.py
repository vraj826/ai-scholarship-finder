from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.db import connect_to_mongo, close_mongo_connection
from routes import auth, profile, scholarships

app = FastAPI(title="AI Scholarship Finder API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://task-master-pro-f04a35db.base44.app",
        "https://ai-scholarship-finder-1.vercel.app",
    ],
    allow_origin_regex=r"https://ai-scholarship-finder-1-.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(scholarships.router)

@app.get("/")
async def root():
    return {"message": "AI Scholarship Finder API is running 🚀"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
