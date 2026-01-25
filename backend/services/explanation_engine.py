def generate_explanation(profile, scholarship, is_eligible, reasons, score):
    """
    Generate human-readable explanation for eligibility decision.
    """
    explanation = []
    
    if is_eligible:
        explanation.append(f"✅ You are eligible! Match Score: {score}")
        
        # CGPA
        if reasons["cgpa"]:
            explanation.append(f"✔ CGPA {profile['cgpa']} meets requirement (≥ {scholarship['cgpa_cutoff']})")
        
        # Income
        if reasons["income"]:
            explanation.append(f"✔ Income ₹{profile['income']:,} is within limit (≤ ₹{scholarship['income_limit']:,})")
        
        # Category
        if reasons["category"]:
            explanation.append(f"✔ Category '{profile['category']}' matches requirement")
        
        # Gender
        if reasons["gender"] is True:
            explanation.append(f"✔ Gender '{profile['gender']}' matches requirement")
        
        # State
        if reasons["state"] is True:
            explanation.append(f"✔ State '{profile['state']}' matches requirement")
        
        # Minority
        if reasons["minority"] is True:
            explanation.append(f"✔ Minority status '{profile['minority']}' matches requirement")
    else:
        explanation.append("❌ You are not eligible for this scholarship")
        
        # CGPA
        if reasons["cgpa"] is False:
            explanation.append(f"✘ CGPA {profile['cgpa']} is below requirement (need ≥ {scholarship['cgpa_cutoff']})")
        
        # Income
        if reasons["income"] is False:
            explanation.append(f"✘ Income ₹{profile['income']:,} exceeds limit (must be ≤ ₹{scholarship['income_limit']:,})")
        
        # Category
        if reasons["category"] is False:
            explanation.append(f"✘ Category '{profile['category']}' does not match (need one of: {', '.join(scholarship['category'])})")
        
        # Gender
        if reasons["gender"] is False:
            explanation.append(f"✘ This scholarship is only for '{scholarship['gender']}' students")
        
        # State
        if reasons["state"] is False:
            explanation.append(f"✘ This scholarship is only for '{scholarship['state']}' residents")
        
        # Minority
        if reasons["minority"] is False:
            minority_list = ', '.join(scholarship['minority']) if scholarship['minority'] else ''
            explanation.append(f"✘ This scholarship requires minority status from: {minority_list}")
    
    return explanation