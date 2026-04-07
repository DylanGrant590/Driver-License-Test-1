import random
from difflib import SequenceMatcher
import csv
from datetime import datetime

PASS_MARK = 0.75
SIMILARITY_THRESHOLD = 0.8
SCORE_FILE = "scores.csv"


class Question:
    def __init__(self, question, answer, category):
        self.question = question
        self.answer = answer.lower()
        self.category = category


class Test:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.wrong = []

    def is_close_enough(self, user_answer, correct_answer):
        ratio = SequenceMatcher(None, user_answer, correct_answer).ratio()
        return ratio >= SIMILARITY_THRESHOLD

    def choose_category(self):
        categories = list(set(q.category for q in self.questions))
        print("\nAvailable Categories:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        print(f"{len(categories)+1}. All Categories")

        choice = input("Choose a category: ").strip()

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(categories):
                selected = categories[choice - 1]
                return [q for q in self.questions if q.category == selected]

        return self.questions

    def choose_number_of_questions(self, questions):
        while True:
            try:
                num = int(input(f"How many questions do you want (1–{len(questions)})? "))
                if 1 <= num <= len(questions):
                    return random.sample(questions, num)
            except:
                pass
            print("Invalid input. Try again.")

    def save_score(self, total, percentage):
        file_exists = False
        try:
            with open(SCORE_FILE, "r"):
                file_exists = True
        except FileNotFoundError:
            pass

        with open(SCORE_FILE, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Date", "Score", "Total", "Percentage"])

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                self.score,
                total,
                f"{percentage:.1f}%"
            ])

    def run(self):
        print("----------------------------------------------")
        print("Welcome to the Jamaican Driver's License Test!")
        print("----------------------------------------------")

        selected_questions = self.choose_category()
        selected_questions = self.choose_number_of_questions(selected_questions)

        print(f"\nYou need {int(PASS_MARK * 100)}% to pass.\n")

        begin = input("Would you like to begin the test? (yes/no): ").strip().lower()
        if begin != "yes":
            print("Goodbye!")
            return

        print("\nOkay, let's begin.\n")

        random.shuffle(selected_questions)

        for i, q in enumerate(selected_questions, 1):
            print(f"Q{i}: {q.question}")
            user_answer = input("Your answer: ").strip().lower()

            if self.is_close_enough(user_answer, q.answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect. Answer: {q.answer.capitalize()}\n")
                self.wrong.append(q)

        self.show_results(len(selected_questions))

    def show_results(self, total):
        percentage = (self.score / total) * 100

        print("----------------------------------------------")
        print(f"You got {self.score}/{total} correct ({percentage:.1f}%)")

        if percentage >= PASS_MARK * 100:
            print("Result: PASSED")
        else:
            print("Result: FAILED")

        if self.wrong:
            print("\nAreas to review:")
            categories = {}
            for q in self.wrong:
                categories[q.category] = categories.get(q.category, 0) + 1

            for category, count in sorted(categories.items(), key=lambda x: -x[1]):
                print(f"  {category}: {count} wrong")

        self.save_score(total, percentage)

        print("\nScore saved to file.")
        print("----------------------------------------------")


# ---------------- DATA ---------------- #
QUESTIONS = [
    Question("The driver of any motor vehicle, when traveling down a hill, must not coast with the gears or transmission of the vehicle in neutral. True or False?",
             "true", "Road Rules"),
    Question("A short road on which vehicles join or leave a main road is called?",
             "slip road", "Terminology"),
    Question("What is the first rule of the road?",
             "keep well to the left unless you are about to overtake or turn right", "Road Rules"),
    Question("Whom do you consider most, of all road users?",
             "all road users but most of all pedestrians", "Road Rules"),
    Question("When the road is divided into three lanes and there is no other marking or direction, what is the center lane used for?",
             "for overtaking only", "Road Rules"),
    Question("How close to a fire hydrant are you allowed to park?",
             "9m (30 feet)", "Parking"),
    Question("What is a cul-de-sac?",
             "it is a dead end road", "Terminology"),
    Question("After overtaking a vehicle, what should you do before rejoining the line?",
             "check your rear view mirror", "Road Rules"),
    Question("If two vehicles of different sizes meet on a hill, which one has the right of way?",
             "the larger one", "Right of Way"),
    Question("Give two causes of skidding:",
             "faulty driving, smooth tyres", "Safety"),
]


# --------------- RUN ------------------ #
if __name__ == "__main__":
    test = Test(QUESTIONS)
    test.run()
