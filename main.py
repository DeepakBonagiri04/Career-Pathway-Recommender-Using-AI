from logic.career_chain import generate_recommendation

def main():
    print("🎓 Let's find the best career path for you based on your interests, hobbies, and strengths!\n")

    # Collect user input
    interests = input("1. What are your favorite subjects in school/college? (e.g., Maths, Biology, History): ").strip()
    hobbies = input("2. What are some hobbies or activities you enjoy? (e.g., Cricket, Coding, Drawing): ").strip()
    scores = input("3. How are your recent academic scores or which subjects are your strengths? (e.g., 95 in Maths): ").strip()

    # Get career recommendation
    print("\n🧠 Generating your personalized career recommendation...\n")
    recommended_careers = ["Actuary", "Data Scientist", "Software Developer", "Mechanical Engineer", "Research Mathematician"]
    response = generate_recommendation(recommended_careers, interests, hobbies, scores)

    # Show result
    print("🎯 Recommended Career Path(s):\n")
    print(response)

if __name__ == "__main__":
    main()
