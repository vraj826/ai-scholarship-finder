def check_eligibility(profile, scholarship):
    reasons = {
        "cgpa": None,
        "income": None,
        "category": None,
        "gender": None,
        "state": None,
        "minority": None
    }

    # ---------- NORMALIZE PROFILE ----------
    profile_category = str(profile.get("category", "")).strip().upper()
    profile_gender = str(profile.get("gender", "")).strip().lower()
    profile_state = str(profile.get("state", "")).strip().lower()
    profile_minority = str(profile.get("minority", "")).strip().lower()

    # ---------- NORMALIZE SCHOLARSHIP ----------
    scholarship_categories = [
        str(c).strip().upper()
        for c in scholarship.get("category", [])
    ]

    scholarship_gender = scholarship.get("gender")
    scholarship_state = scholarship.get("state")
    scholarship_minority = scholarship.get("minority")

    # ---------- CGPA ----------
    reasons["cgpa"] = profile.get("cgpa", 0) >= scholarship.get("cgpa_cutoff", 0)

    # ---------- INCOME ----------
    reasons["income"] = profile.get("income", float("inf")) <= scholarship.get("income_limit", 0)

    # ---------- CATEGORY (FIXED) ----------
    reasons["category"] = profile_category in scholarship_categories

    # ---------- GENDER ----------
    if scholarship_gender:
        reasons["gender"] = profile_gender == str(scholarship_gender).strip().lower()
    else:
        reasons["gender"] = None

    # ---------- STATE ----------
    if scholarship_state:
        reasons["state"] = profile_state == str(scholarship_state).strip().lower()
    else:
        reasons["state"] = None

    # ---------- MINORITY ----------
    if scholarship_minority:
        reasons["minority"] = profile_minority in [
            str(m).strip().lower() for m in scholarship_minority
        ]
    else:
        reasons["minority"] = None

    # ---------- FINAL DECISION ----------
    mandatory_checks = ["cgpa", "income", "category"]

    for check in mandatory_checks:
        if reasons[check] is False:
            return False, reasons

    if reasons["gender"] is False:
        return False, reasons

    if reasons["state"] is False:
        return False, reasons

    if reasons["minority"] is False:
        return False, reasons

    return True, reasons
