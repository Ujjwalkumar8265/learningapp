import random

words = {
    "et": "and",
    "in": "in",
    "est": "is",
    "non": "not",
    "qui": "who",
    "cum": "with",
    "ad": "to",
    "ut": "that",
    "per": "through",
    "sed": "but",
    "ex": "out of",
    "aut": "or",
    "si": "if",
    "de": "about",
    "enim": "for",
    "quod": "because",
    "at": "but",
    "hoc": "this",
    "ille": "that",
    "illa": "she",
    "ipsum": "itself",
    "nunc": "now",
    "tamen": "however",
    "sunt": "are",
    "omnis": "all",
    "nihil": "nothing",
    "aliquid": "something",
    "homo": "man",
    "mulier": "woman",
    "puer": "boy",
    "puella": "girl",
    "domus": "house",
    "terra": "earth",
    "aqua": "water",
    "ignis": "fire",
    "caelum": "sky",
    "sol": "sun",
    "luna": "moon",
    "stella": "star",
    "dies": "day",
    "nox": "night",
    "tempus": "time",
    "vita": "life",
    "mors": "death",
    "amor": "love",
    "bellum": "war",
    "pax": "peace",
    "veritas": "truth",
    "falsitas": "falsehood",
    "virtus": "virtue",
    "vitium": "vice",
    "fortis": "strong",
    "debilis": "weak",
    "magnus": "great",
    "parvus": "small",
    "bonus": "good",
    "malus": "bad",
    "novus": "new",
    "vetus": "old",
    "altus": "high",
    "humilis": "low",
    "longus": "long",
    "brevis": "short",
    "celer": "fast",
    "tardus": "slow",
    "clarus": "clear",
    "obscurus": "dark",
    "amicus": "friend",
    "hostis": "enemy",
    "rex": "king",
    "regina": "queen",
    "servus": "slave",
    "liber": "free",
    "populus": "people",
    "civitas": "state",
    "urbs": "city",
    "via": "road",
    "mare": "sea",
    "mons": "mountain",
    "silva": "forest",
    "campus": "field",
    "flumen": "river",
    "animal": "animal",
    "corpus": "body",
    "mens": "mind",
    "anima": "soul",
    "vox": "voice",
    "verbum": "word",
    "scriptum": "writing",
    "lectio": "reading",
    "numerus": "number",
    "ordo": "order",
    "chaos": "chaos",
    "lux": "light",
    "tenebrae": "darkness",
    "spes": "hope",
    "timor": "fear",
    "gaudium": "joy",
    "dolor": "pain",
}

def quiz_user(words_dict):
    latin_words = list(words_dict.keys())
    random.shuffle(latin_words)
    score = 0

    for latin_word in latin_words:
        print(f"What is the English translation of '{latin_word}'?")
        user_answer = input("YOUR ANSWER: ").strip().lower()
        correct_answer = words_dict[latin_word].lower()

        if user_answer == correct_answer:
            print("Correct answer!\n")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is '{words_dict[latin_word]}'.\n")

    print(f"Quiz completed! Your final score is: {score}/{len(words_dict)}")

def main():
    print("Welcome to the Latin Language Learning App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()