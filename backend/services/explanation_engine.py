def generate_explanation(profile, scholarship, reasons, score):
    explanation = []

    # CGPA
    if reasons.get("cgpa") is True:
        explanation.append(
            f"✓ CGPA {profile.get('cgpa')} meets requirement (≥ {scholarship.get('cgpa_cutoff')})"
        )
    elif reasons.get("cgpa") is False:
        explanation.append(
            f"✗ CGPA {profile.get('cgpa')} does not meet requirement (≥ {scholarship.get('cgpa_cutoff')})"
        )

    # Income
    if reasons.get("income") is True:
        explanation.append(
            f"✓ Income ₹{profile.get('income')} is within limit (≤ ₹{scholarship.get('income_limit')})"
        )
    elif reasons.get("income") is False:
        explanation.append(
            f"✗ Income ₹{profile.get('income')} exceeds limit (≤ ₹{scholarship.get('income_limit')})"
        )

    # Category
    if reasons.get("category") is True:
        explanation.append(
            f"✓ Category matches ({profile.get('category')})"
        )
    elif reasons.get("category") is False:
        explanation.append(
            f"✗ Category does not match ({profile.get('category')})"
        )

    # Gender
    if reasons.get("gender") is True:
        explanation.append("✓ Gender requirement satisfied")
    elif reasons.get("gender") is False:
        explanation.append("✗ Gender requirement not satisfied")

    # State
    if reasons.get("state") is True:
        explanation.append(
            f"✓ State matches ({profile.get('state')})"
        )
    elif reasons.get("state") is False:
        explanation.append(
            f"✗ State does not match ({profile.get('state')})"
        )

    # Minority
    if reasons.get("minority") is True:
        explanation.append("✓ Minority requirement satisfied")
    elif reasons.get("minority") is False:
        explanation.append("✗ Minority requirement not satisfied")

    

    return explanation
