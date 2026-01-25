from typing import List

VALID_CATEGORIES = ["General", "OBC", "SC", "ST"]
VALID_GENDERS = ["Male", "Female", "Other"]
VALID_MINORITIES = ["Muslim", "Christian", "Sikh", "Buddhist", "Jain", "Parsi", "None"]

VALID_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Delhi", "Jammu and Kashmir", "Ladakh", "Puducherry", "Chandigarh",
    "Andaman and Nicobar", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep"
]

def validate_category(category: str) -> bool:
    return category in VALID_CATEGORIES

def validate_gender(gender: str) -> bool:
    return gender in VALID_GENDERS

def validate_minority(minority: str) -> bool:
    return minority in VALID_MINORITIES

def validate_state(state: str) -> bool:
    return state in VALID_STATES