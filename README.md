# 🎓 AI Scholarship Finder

**Smart scholarship matching for students**

AI Scholarship Finder is a full-stack web application that helps students discover scholarships they are **actually eligible for**, based on their academic, financial, and personal profile — eliminating guesswork and confusion.

🔗 **Live Demo**  
- Frontend: https://ai-scholarship-finder-1.vercel.app  
- Backend API: https://ai-scholarship-finder-z9we.onrender.com  

---

## 🚀 Problem It Solves

Finding the right scholarship is difficult because:
- Eligibility criteria are scattered and unclear
- Students don’t know *why* they are or aren’t eligible
- General-category and non-government quota students are often left out

> Being a student who took admission through a **Non-Government** quota and comes from a **GENERAL** category, it was difficult to find scholarships that actually applied to me.  
> This project was built to solve that exact problem.

AI Scholarship Finder:
- Matches students with **eligible scholarships only**
- Clearly explains **why you qualify or why you don’t**
- Saves hours of manual searching and confusion

---

## ✨ Features

- 🔐 JWT-based authentication
- 👤 Student profile onboarding
- 🎯 Eligibility-based scholarship matching
- 🧠 Rule-based eligibility engine (CGPA, income, category, gender, state, minority)
- 📊 Clear eligibility & rejection explanations
- 🔄 What-If Simulator (simulate CGPA/income changes)
- 🌐 Fully deployed (Vercel + Render)

---

## 🛠️ Tech Stack

### Frontend
- React (Vite)
- Axios
- React Router
- Custom CSS dashboard
- Deployed on **Vercel**

### Backend
- FastAPI
- MongoDB (Atlas)
- Motor (async MongoDB client)
- JWT Authentication
- Pydantic
- Deployed on **Render**

### Database
- MongoDB Atlas (NoSQL)

---

## 📁 Project Structure

```
ai-scholarship-finder/
│
├── backend/
│ ├── main.py
│ ├── database/
| ├── models/
│ ├── routes/
│ ├── schemas/
│ ├── services/
│ ├── utils/
| ├── Dockerfile
│ └── requirements.txt
│
├── frontend/
│ ├── src/
| ├── index.html
│ ├── package-lock.json
│ ├── package.json
│ ├── vite.config.js
| └── vercel.json
│
├── .gitignore
└── README.md
```

---

## ⚙️ Run Locally

### 1️⃣ Clone the Repository
```
git clone https://github.com/your-username/ai-scholarship-finder.git
cd ai-scholarship-finder
```
---
### 2️⃣ Backend Setup (FastAPI)
```
cd backend
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
Create a .env file inside backend/:
```
MONGODB_URL=your_mongodb_atlas_connection_string    # Replace this field
DATABASE_NAME=scholarship_finder
JWT_SECRET_KEY=your_secret_key
```
Run backend:
```
uvicorn main:app --reload
```
Backend runs at:
```
http://localhost:8000
```
---
### 3️⃣ Frontend Setup (React + Vite)
```
cd frontend
npm install
npm run dev
```
Frontend runs at:
```
http://localhost:5173
```

---

## 🔐 Environment Variables

### Backend

- `MONGODB_URL`
- `DATABASE_NAME`
- `JWT_SECRET_KEY`

### Frontend

- Axios base URL configured for backend API

---

## 🧪 Use Cases

- Students discover scholarships they truly qualify for
- Understand why some scholarships don’t match
- Simulate eligibility by adjusting CGPA or income
- Avoid misinformation and manual searching

---

## 🚧 Challenges Faced

- MongoDB schema mismatches causing eligibility bugs
- Handling optional vs mandatory eligibility conditions
- Python 3.13 incompatibility on Render
- CORS & JWT issues between Vercel and Render
- Aligning backend logic with real-world scholarship data
- Each issue was resolved through schema validation, defensive coding, and better separation of logic.

---

## 🔮 Future Enhancements

- Admin dashboard for scholarship management
- AI-powered ranking & recommendations
- Deadline alerts
- Advanced filters (degree, field of study)
- Eligibility analytics

---

## 📄 License

Open-source project built for learning, hackathons, and real-world impact.

---