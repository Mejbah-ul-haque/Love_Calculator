print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is your lover's name? \n")

def calculate_love_score(name1, name2):
    combined_str = (name1 + name2).lower()

    # Count letters from "TRUE" and "LOVE"
    # true_count = sum(combined_str.count(char) for char in "true")
    # love_count = sum(combined_str.count(char) for char in "love")

    t = combined_str.count("t")
    r = combined_str.count("r")
    u = combined_str.count("u")
    e = combined_str.count("e")

    true_count = t + r + u + e

    l = combined_str.count("l")
    o = combined_str.count("o")
    v = combined_str.count("v")
    e = combined_str.count("e")

    love_count = l + o + v + e

    love_score = int(str(true_count) + str(love_count))

    if love_score < 10 or love_score > 90:
        print("You go together like Coke and Mentos")
    elif 40 <= love_score <= 50:
        print("You are alright together")
    else:
        print("Hmm... you might want to get to know each other better")

calculate_love_score(name1, name2)