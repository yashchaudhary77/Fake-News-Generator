import random
subject=[
    "Sharukh Khan",
    "salman Khan",
    "Aamir Khan",
    "Akshay Kumar",
    "Ranbir Kapoor",
    "Ranveer Singh",
    "Prime minister",
    "Sachin Tendulkar",
    "Virat Kohli",
    "MS Dhoni",
    "Rohit Sharma"    
]

action =[
    "lunches",
    "dances",
    "sings",
    "plays cricket",
    "acts in movies",
    "eats biryani",
    "drinks chocolateShake",
    "gyms",
    "declares war on "
]

place_or_things = [
    "at red fort",
    "in Taj Mahal",
    "in Mumbai",
    "in Delhi",
    "in Bangalore",
    "at india gate",
    "in Hyderabad",
    "in Chennai",
    "at usa",
    "in London"
]

while True:
    subject = random.choice(subject)
    action = random.choice(action)
    place = random.choice(place_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place} "
    print("\n" + headline)

    user_input = input("do you want another head line (yes/no):".strip().lower())
    if user_input == "no":
        print("Thank you for using the headline generator. Goodbye!")
        break