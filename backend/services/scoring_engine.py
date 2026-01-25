def calculate_score(profile, scholarship):
    """
    Calculate match score based on scholarship weights.
    """
    score = 0
    weights = scholarship["weights"]
    
    # CGPA scoring
    if "cgpa" in weights:
        if profile["cgpa"] >= scholarship["cgpa_cutoff"]:
            # Extra points for exceeding cutoff
            excess = profile["cgpa"] - scholarship["cgpa_cutoff"]
            score += weights["cgpa"] + int(excess * 2)
    
    # Income scoring
    if "income" in weights:
        if profile["income"] <= scholarship["income_limit"]:
            # More points for lower income
            income_ratio = profile["income"] / scholarship["income_limit"]
            score += int(weights["income"] * (1 - income_ratio))
    
    # Category match
    if "category_match" in weights:
        if profile["category"] in scholarship["category"]:
            score += weights["category_match"]
    
    # Gender match
    if "gender_match" in weights:
        if scholarship["gender"] and profile["gender"] == scholarship["gender"]:
            score += weights["gender_match"]
    
    # State match
    if "state_match" in weights:
        if scholarship["state"] and profile["state"] == scholarship["state"]:
            score += weights["state_match"]
    
    # Minority match
    if "minority_match" in weights:
        if scholarship["minority"] and profile["minority"] in scholarship["minority"]:
            score += weights["minority_match"]
    
    return score