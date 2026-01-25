from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.db import connect_to_mongo, close_mongo_connection
from routes import auth, profile, scholarships

app = FastAPI(title="AI Scholarship Finder API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Events
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

# Routes
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(scholarships.router)

@app.get("/")
async def root():
    return {"message": "AI Scholarship Finder API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}