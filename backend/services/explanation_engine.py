def generate_explanation(profile, scholarship, reasons):
    """
    Generate a human-readable explanation of eligibility
    """
    explanation = []

    # =========================
    # CGPA
    # =========================
    min_cgpa = scholarship.get("min_cgpa")
    if min_cgpa is not None:
        if reasons.get("cgpa"):
            explanation.append(
                f"✔ CGPA {profile.get('cgpa')} meets requirement (≥ {min_cgpa})"
            )
        else:
            explanation.append(
                f"✘ CGPA {profile.get('cgpa')} is below requirement (≥ {min_cgpa})"
            )

    # =========================
    # Income
    # =========================
    max_income = scholarship.get("max_income")
    if max_income is not None:
        if reasons.get("income"):
            explanation.append(
                f"✔ Income ₹{profile.get('income')} is within limit (≤ ₹{max_income})"
            )
        else:
            explanation.append(
                f"✘ Income ₹{profile.get('income')} exceeds limit (≤ ₹{max_income})"
            )

    # =========================
    # Category
    # =========================
    if scholarship.get("category"):
        if reasons.get("category"):
            explanation.append(
                f"✔ Category matches ({profile.get('category')})"
            )
        else:
            explanation.append(
                f"✘ Category does not match ({profile.get('category')})"
            )

    # =========================
    # Gender (optional)
    # =========================
    if scholarship.get("gender"):
        if reasons.get("gender"):
            explanation.append("✔ Gender requirement satisfied")
        else:
            explanation.append("✘ Gender requirement not satisfied")

    # =========================
    # State (optional)
    # =========================
    if scholarship.get("state"):
        if reasons.get("state"):
            explanation.append(
                f"✔ State matches ({profile.get('state')})"
            )
        else:
            explanation.append(
                f"✘ State does not match ({profile.get('state')})"
            )

    # =========================
    # Minority (optional)
    # =========================
    if scholarship.get("minority"):
        if reasons.get("minority"):
            explanation.append("✔ Minority requirement satisfied")
        else:
            explanation.append("✘ Minority requirement not satisfied")

    return explanation
