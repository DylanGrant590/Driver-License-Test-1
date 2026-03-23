QUESTIONS = [
    {
        "question": "The driver of any motor vehicle, when traveling down a hill, must not coast "
                    "with the gears or transmission of the vehicle in neutral. True or False?",
        "answer": "true",
        "category": "Road Rules",
    },
    {
        "question": "A short road on which vehicles join or leave a main road is called?",
        "answer": "slip road",
        "category": "Terminology",
    },
    {
        "question": "What is the first rule of the road?",
        "answer": "keep well to the left unless you are about to overtake or turn right",
        "category": "Road Rules",
    },
    {
        "question": "Whom do you consider most, of all road users?",
        "answer": "all road users but most of all pedestrians",
        "category": "Road Rules",
    },
    {
        "question": "When the road is divided into three lanes and there is no other marking or "
                    "direction, what is the center lane used for?",
        "answer": "for overtaking only",
        "category": "Road Rules",
    },
    {
        "question": "How close to a fire hydrant are you allowed to park?",
        "answer": "9m (30 feet)",
        "category": "Parking",
    },
    {
        "question": "What is a cul-de-sac?",
        "answer": "it is a dead end road",
        "category": "Terminology",
    },
    {
        "question": "After overtaking a vehicle, what should you do before rejoining the line?",
        "answer": "check your rear view mirror",
        "category": "Road Rules",
    },
    {
        "question": "If two vehicles of different sizes meet on a hill, which one has the right of way?",
        "answer": "the larger one",
        "category": "Right of Way",
    },
    {
        "question": "Give two causes of skidding:",
        "answer": "faulty driving, smooth tyres",
        "category": "Safety",
    },
    {
        "question": "If you wish to turn right when traveling on a one way street, what should you do?",
        "answer": "keep to the right of the road",
        "category": "Road Rules",
    },
    {
        "question": "What is a soft shoulder?",
        "answer": "the unpaved side of the road which is not intended for vehicular traffic",
        "category": "Terminology",
    },
    {
        "question": "How far should you travel behind an emergency vehicle?",
        "answer": "approximately 150m (500 feet)",
        "category": "Safety",
    },
    {
        "question": "Who has the right of way on a hill?",
        "answer": "the vehicle coming down, but a heavier vehicle has the right of way up or down",
        "category": "Right of Way",
    },
    {
        "question": "Who has the right of way at a crossing not controlled by police, traffic lights, or signs?",
        "answer": "no one",
        "category": "Right of Way",
    },
    {
        "question": "When should a driver make use of the right of way?",
        "answer": "when it is safe to do so",
        "category": "Right of Way",
    },
    {
        "question": "Should a driver yield the right of way if a pedestrian enters the crossing?",
        "answer": "yes",
        "category": "Right of Way",
    },
    {
        "question": "What is meant by yield right of way?",
        "answer": "to give way",
        "category": "Terminology",
    },
    {
        "question": "When may you use a slip road at the traffic light?",
        "answer": "on any light",
        "category": "Road Rules",
    },
    {
        "question": "If you are driving along and your rear wheels skid, what should you do?",
        "answer": "steer in the direction of the skid",
        "category": "Safety",
    },
]

PASS_MARK = 0.75
SIMILARITY_THRESHOLD = 0.8


def is_close_enough(user_answer, correct_answer):
    from difflib import SequenceMatcher
    ratio = SequenceMatcher(None, user_answer, correct_answer).ratio()
    return ratio >= SIMILARITY_THRESHOLD


def run_test():
    print("----------------------------------------------")
    print("Welcome to the Jamaican Driver's License Test!")
    print("----------------------------------------------")
    print(f"\nThere are {len(QUESTIONS)} questions. You need {int(PASS_MARK * 100)}% to pass.\n")

    begin = input("Would you like to begin the test? (yes/no): ").strip().lower()
    if begin != "yes":
        print("Goodbye!")
        return

    print("\nOkay, let's begin.\n")

    import random
    questions = QUESTIONS[:]
    random.shuffle(questions)

    score = 0
    wrong = []

    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        user_answer = input("Your answer: ").strip().lower()

        if is_close_enough(user_answer, q["answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. Answer: {q['answer'].capitalize()}\n")
            wrong.append(q)

    # Results
    total = len(QUESTIONS)
    percentage = (score / total) * 100

    print("----------------------------------------------")
    print(f"You got {score}/{total} correct ({percentage:.1f}%)")

    if percentage >= PASS_MARK * 100:
        print("Result: PASSED")
    else:
        print("Result: FAILED")

    # Category breakdown
    if wrong:
        print("\nAreas to review:")
        categories = {}
        for q in wrong:
            categories[q["category"]] = categories.get(q["category"], 0) + 1
        for category, count in sorted(categories.items(), key=lambda x: -x[1]):
            print(f"  {category}: {count} wrong")

    print("----------------------------------------------")


if __name__ == "__main__":
    run_test()
