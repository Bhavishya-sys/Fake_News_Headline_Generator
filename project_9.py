import random

subjects = [
    "Sharukh khan",
    "Virat kohli ji",
    "Nirmala sitharaman",
    "A Mumbai cat",
    "A Group of monkeys",
    "Primeminster Modi",
    "Auto Riksha driver from delhi",
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declare wars on",
    "orders",
    "celebrates",
]

places_or_things = [
    "at Red fort",
    " in Mumbai local trains",
    " a Plate of samosa",
    "inside parliment",
    "at ganga ghat",
    " During ipl match",
    " at indai gate",
]


while True :
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS :  {subject} {action} {place_or_thing} "
    print("\n "+ headline)

    user_input = input("\n Do you want new headline? (yes/no)").strip().lower()
    if user_input == "no":
        break


print("\n Thanks for using the Fake News Headline Generator. Have a Fun Day")