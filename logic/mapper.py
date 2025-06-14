def map_to_careers(interests, hobbies, scores):
    interests = interests.lower()
    hobbies = hobbies.lower()
    scores = scores.lower()

    career_matches = []

    # STEM
    if any(sub in interests for sub in ["math", "physics", "chemistry", "biology", "computer", "engineering"]):
        career_matches.append("STEM")

    # Arts
    if any(sub in hobbies for sub in ["drawing", "painting", "music", "acting", "design"]):
        career_matches.append("Arts")

    # Sports
    if "sports" in hobbies or "cricket" in hobbies or "football" in hobbies:
        career_matches.append("Sports")

    # Commerce
    if any(sub in interests for sub in ["economics", "business", "accounts", "finance"]):
        career_matches.append("Commerce")

    # Social Sciences
    if any(sub in interests for sub in ["history", "psychology", "geography", "political"]):
        career_matches.append("Social Science")

    # Vocational
    if any(sub in hobbies for sub in ["cooking", "crafting", "repair", "mechanic"]):
        career_matches.append("Vocational")

    # Default fallback
    if not career_matches:
        career_matches.append("General")

    return list(set(career_matches))[:3] 

# if __name__ == "__main__":
#     careers = map_to_careers(
#         interests="I like physics and maths",
#         hobbies="I enjoy football and painting",
#         scores="85 in science"
#     )
#     print("Suggested Careers:", careers)
