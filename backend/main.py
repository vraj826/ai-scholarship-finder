from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db import connect_to_mongo, close_mongo_connection
from routes import auth, profile, scholarships

app = FastAPI(title="AI Scholarship Finder API")

# =========================
# CORS Configuration
# =========================
# Frontend origins (local + production)
ALLOWED_ORIGINS = [
    "http://localhost:5173",                 # Local Vite
    "http://localhost:3000",                 # Optional fallback
    "https://ai-scholarship-finder-1.vercel.app"  # Vercel frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Application Lifecycle
# =========================
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

# =========================
# API Routes
# =========================
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(scholarships.router)

# =========================
# Health & Root
# =========================
@app.get("/")
async def root():
    return {"message": "AI Scholarship Finder API is running 🚀"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
