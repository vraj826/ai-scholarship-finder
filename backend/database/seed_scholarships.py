from database.db import get_database
import asyncio

SCHOLARSHIPS_DATA = [
    {
        "name": "National Merit Scholarship",
        "provider": "Ministry of Education",
        "amount": 50000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 600000,
        "cgpa_cutoff": 8.0,
        "gender": None,
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 10,
            "income": 15,
            "category_match": 5
        },
        "description": "Merit-based scholarship for high-performing students"
    },
    {
        "name": "Post-Matric Scholarship for SC Students",
        "provider": "Ministry of Social Justice",
        "amount": 75000,
        "category": ["SC"],
        "income_limit": 250000,
        "cgpa_cutoff": 6.0,
        "gender": None,
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 8,
            "income": 20,
            "category_match": 15
        },
        "description": "Financial support for SC students pursuing higher education"
    },
    {
        "name": "Post-Matric Scholarship for ST Students",
        "provider": "Ministry of Tribal Affairs",
        "amount": 75000,
        "category": ["ST"],
        "income_limit": 250000,
        "cgpa_cutoff": 6.0,
        "gender": None,
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 8,
            "income": 20,
            "category_match": 15
        },
        "description": "Financial support for ST students pursuing higher education"
    },
    {
        "name": "OBC Merit Scholarship",
        "provider": "Ministry of Social Justice",
        "amount": 60000,
        "category": ["OBC"],
        "income_limit": 450000,
        "cgpa_cutoff": 7.0,
        "gender": None,
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 10,
            "income": 18,
            "category_match": 12
        },
        "description": "Merit scholarship for OBC students"
    },
    {
        "name": "Minority Community Scholarship",
        "provider": "Ministry of Minority Affairs",
        "amount": 55000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 400000,
        "cgpa_cutoff": 6.5,
        "gender": None,
        "state": None,
        "minority": ["Muslim", "Christian", "Sikh", "Buddhist", "Jain", "Parsi"],
        "weights": {
            "cgpa": 8,
            "income": 16,
            "minority_match": 18
        },
        "description": "Scholarship for students from minority communities"
    },
    {
        "name": "Women Empowerment Scholarship",
        "provider": "Ministry of Women and Child Development",
        "amount": 65000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 500000,
        "cgpa_cutoff": 7.5,
        "gender": "Female",
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 12,
            "income": 14,
            "gender_match": 16
        },
        "description": "Empowering women through education"
    },
    {
        "name": "INSPIRE Scholarship for Higher Education",
        "provider": "Department of Science and Technology",
        "amount": 80000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 700000,
        "cgpa_cutoff": 8.5,
        "gender": None,
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 20,
            "income": 10,
            "category_match": 5
        },
        "description": "For students pursuing natural sciences"
    },
    {
        "name": "Maharashtra State Scholarship",
        "provider": "Government of Maharashtra",
        "amount": 45000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 400000,
        "cgpa_cutoff": 7.0,
        "gender": None,
        "state": "Maharashtra",
        "minority": None,
        "weights": {
            "cgpa": 10,
            "income": 15,
            "state_match": 20
        },
        "description": "State scholarship for Maharashtra students"
    },
    {
        "name": "Karnataka State Merit Scholarship",
        "provider": "Government of Karnataka",
        "amount": 40000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 350000,
        "cgpa_cutoff": 7.5,
        "gender": None,
        "state": "Karnataka",
        "minority": None,
        "weights": {
            "cgpa": 12,
            "income": 13,
            "state_match": 18
        },
        "description": "State scholarship for Karnataka students"
    },
    {
        "name": "Tamil Nadu State Scholarship",
        "provider": "Government of Tamil Nadu",
        "amount": 42000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 380000,
        "cgpa_cutoff": 7.2,
        "gender": None,
        "state": "Tamil Nadu",
        "minority": None,
        "weights": {
            "cgpa": 11,
            "income": 14,
            "state_match": 19
        },
        "description": "State scholarship for Tamil Nadu students"
    },
    {
        "name": "West Bengal Minority Scholarship",
        "provider": "Government of West Bengal",
        "amount": 38000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 350000,
        "cgpa_cutoff": 6.8,
        "gender": None,
        "state": "West Bengal",
        "minority": ["Muslim", "Christian", "Sikh", "Buddhist", "Jain", "Parsi"],
        "weights": {
            "cgpa": 9,
            "income": 15,
            "state_match": 15,
            "minority_match": 12
        },
        "description": "Scholarship for minority students in West Bengal"
    },
    {
        "name": "Gujarat SC/ST Scholarship",
        "provider": "Government of Gujarat",
        "amount": 48000,
        "category": ["SC", "ST"],
        "income_limit": 300000,
        "cgpa_cutoff": 6.5,
        "gender": None,
        "state": "Gujarat",
        "minority": None,
        "weights": {
            "cgpa": 8,
            "income": 18,
            "state_match": 17,
            "category_match": 15
        },
        "description": "State scholarship for SC/ST students in Gujarat"
    },
    {
        "name": "Rajasthan Women Scholarship",
        "provider": "Government of Rajasthan",
        "amount": 43000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 400000,
        "cgpa_cutoff": 7.0,
        "gender": "Female",
        "state": "Rajasthan",
        "minority": None,
        "weights": {
            "cgpa": 10,
            "income": 14,
            "state_match": 16,
            "gender_match": 15
        },
        "description": "Scholarship for women students in Rajasthan"
    },
    {
        "name": "Uttar Pradesh Merit Scholarship",
        "provider": "Government of Uttar Pradesh",
        "amount": 41000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 360000,
        "cgpa_cutoff": 7.3,
        "gender": None,
        "state": "Uttar Pradesh",
        "minority": None,
        "weights": {
            "cgpa": 11,
            "income": 14,
            "state_match": 18
        },
        "description": "Merit-based scholarship for UP students"
    },
    {
        "name": "Delhi OBC Scholarship",
        "provider": "Government of Delhi",
        "amount": 46000,
        "category": ["OBC"],
        "income_limit": 420000,
        "cgpa_cutoff": 7.2,
        "gender": None,
        "state": "Delhi",
        "minority": None,
        "weights": {
            "cgpa": 10,
            "income": 16,
            "state_match": 17,
            "category_match": 14
        },
        "description": "Scholarship for OBC students in Delhi"
    },
    {
        "name": "Punjab Minority Excellence Scholarship",
        "provider": "Government of Punjab",
        "amount": 44000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 390000,
        "cgpa_cutoff": 7.4,
        "gender": None,
        "state": "Punjab",
        "minority": ["Muslim", "Christian", "Sikh", "Buddhist", "Jain", "Parsi"],
        "weights": {
            "cgpa": 11,
            "income": 15,
            "state_match": 16,
            "minority_match": 13
        },
        "description": "Excellence scholarship for minority students in Punjab"
    },
    {
        "name": "Kerala High Achiever Scholarship",
        "provider": "Government of Kerala",
        "amount": 47000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 410000,
        "cgpa_cutoff": 8.0,
        "gender": None,
        "state": "Kerala",
        "minority": None,
        "weights": {
            "cgpa": 15,
            "income": 12,
            "state_match": 18
        },
        "description": "For high achievers in Kerala"
    },
    {
        "name": "Andhra Pradesh SC Scholarship",
        "provider": "Government of Andhra Pradesh",
        "amount": 39000,
        "category": ["SC"],
        "income_limit": 280000,
        "cgpa_cutoff": 6.3,
        "gender": None,
        "state": "Andhra Pradesh",
        "minority": None,
        "weights": {
            "cgpa": 8,
            "income": 19,
            "state_match": 16,
            "category_match": 16
        },
        "description": "Support for SC students in Andhra Pradesh"
    },
    {
        "name": "Telangana Women in STEM Scholarship",
        "provider": "Government of Telangana",
        "amount": 52000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 450000,
        "cgpa_cutoff": 7.8,
        "gender": "Female",
        "state": "Telangana",
        "minority": None,
        "weights": {
            "cgpa": 13,
            "income": 13,
            "state_match": 15,
            "gender_match": 17
        },
        "description": "Encouraging women in STEM fields in Telangana"
    },
    {
        "name": "Bihar ST Scholarship",
        "provider": "Government of Bihar",
        "amount": 37000,
        "category": ["ST"],
        "income_limit": 260000,
        "cgpa_cutoff": 6.2,
        "gender": None,
        "state": "Bihar",
        "minority": None,
        "weights": {
            "cgpa": 7,
            "income": 20,
            "state_match": 15,
            "category_match": 17
        },
        "description": "Financial aid for ST students in Bihar"
    },
    {
        "name": "Central Sector Scholarship",
        "provider": "Ministry of Education",
        "amount": 70000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 800000,
        "cgpa_cutoff": 8.2,
        "gender": None,
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 18,
            "income": 10,
            "category_match": 5
        },
        "description": "Central government merit scholarship"
    },
    {
        "name": "Prime Minister Scholarship for Excellence",
        "provider": "Prime Minister's Office",
        "amount": 100000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 1000000,
        "cgpa_cutoff": 9.0,
        "gender": None,
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 25,
            "income": 8,
            "category_match": 3
        },
        "description": "Prestigious scholarship for top performers"
    },
    {
        "name": "Begum Hazrat Mahal Scholarship",
        "provider": "Ministry of Minority Affairs",
        "amount": 56000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 380000,
        "cgpa_cutoff": 7.0,
        "gender": "Female",
        "state": None,
        "minority": ["Muslim", "Christian", "Sikh", "Buddhist", "Jain", "Parsi"],
        "weights": {
            "cgpa": 9,
            "income": 15,
            "gender_match": 15,
            "minority_match": 18
        },
        "description": "For minority girls pursuing higher education"
    },
    {
        "name": "Maulana Azad National Fellowship",
        "provider": "Ministry of Minority Affairs",
        "amount": 85000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 600000,
        "cgpa_cutoff": 7.8,
        "gender": None,
        "state": None,
        "minority": ["Muslim", "Christian", "Sikh", "Buddhist", "Jain", "Parsi"],
        "weights": {
            "cgpa": 12,
            "income": 14,
            "minority_match": 20
        },
        "description": "Research scholarship for minority students"
    },
    {
        "name": "Dr. Ambedkar Post-Matric Scholarship",
        "provider": "Ministry of Social Justice",
        "amount": 68000,
        "category": ["SC"],
        "income_limit": 300000,
        "cgpa_cutoff": 6.8,
        "gender": None,
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 9,
            "income": 18,
            "category_match": 18
        },
        "description": "Post-matric scholarship for SC students"
    },
    {
        "name": "Savitribai Phule Scholarship for Girls",
        "provider": "Ministry of Women and Child Development",
        "amount": 58000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 450000,
        "cgpa_cutoff": 7.3,
        "gender": "Female",
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 11,
            "income": 15,
            "gender_match": 17
        },
        "description": "Promoting girls' education across India"
    },
    {
        "name": "Rajiv Gandhi Fellowship",
        "provider": "University Grants Commission",
        "amount": 90000,
        "category": ["SC", "ST"],
        "income_limit": 500000,
        "cgpa_cutoff": 8.0,
        "gender": None,
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 15,
            "income": 12,
            "category_match": 20
        },
        "description": "Research fellowship for SC/ST students"
    },
    {
        "name": "Swami Vivekananda Merit Scholarship",
        "provider": "Ministry of Education",
        "amount": 62000,
        "category": ["General", "OBC"],
        "income_limit": 520000,
        "cgpa_cutoff": 8.3,
        "gender": None,
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 16,
            "income": 12,
            "category_match": 10
        },
        "description": "Merit-based scholarship for General and OBC students"
    },
    {
        "name": "National Fellowship for OBC Students",
        "provider": "University Grants Commission",
        "amount": 72000,
        "category": ["OBC"],
        "income_limit": 480000,
        "cgpa_cutoff": 7.6,
        "gender": None,
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 12,
            "income": 16,
            "category_match": 18
        },
        "description": "Fellowship for OBC students in research"
    },
    {
        "name": "Indira Gandhi Scholarship for Single Girl Child",
        "provider": "University Grants Commission",
        "amount": 54000,
        "category": ["General", "OBC", "SC", "ST"],
        "income_limit": 430000,
        "cgpa_cutoff": 7.1,
        "gender": "Female",
        "state": None,
        "minority": None,
        "weights": {
            "cgpa": 10,
            "income": 15,
            "gender_match": 20
        },
        "description": "For single girl child pursuing higher education"
    }
]

async def seed_scholarships():
    db = get_database()
    scholarships_collection = db.scholarships
    
    # Clear existing scholarships
    await scholarships_collection.delete_many({})
    
    # Insert new scholarships
    result = await scholarships_collection.insert_many(SCHOLARSHIPS_DATA)
    print(f"✅ Seeded {len(result.inserted_ids)} scholarships")

if __name__ == "__main__":
    from database.db import connect_to_mongo, close_mongo_connection
    
    async def main():
        await connect_to_mongo()
        await seed_scholarships()
        await close_mongo_connection()
    
    asyncio.run(main())