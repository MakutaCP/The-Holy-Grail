def start_up():
    print("   ")
    print("--THE HOLY GRAIL RIDDLES--")
    print("   ")
    print("TYPE BEGIN TO START")

def welcome():
    print("   ")
    print("Welcome to the secret cave.")
    print("   ")
    print("You have found the resting place of the Holy Grail.")
    print("   ")
    print("I am going to give you the chance to earn it.")
    print("   ")
    What()

def What():

    yes_or_no_list = []

    yes_or_no_list.append(input("You would like to earn the grail yes?  ").lower())

    if "yes" in yes_or_no_list:
        print("   ")
        print("Very Good. First I will give you three questions.")
        print("   ")
        print("Your answers will determine your riddle.")
        print("   ")
        questions()

    if "no" in yes_or_no_list:
        print("   ")
        print("Oh. You must be looking for the batrooms then. Those are three doors down on the left.")
        print("   ")
        print("Off you go then.")
        print("   ")
        print("--THE END?--")

    else:
        print("   ")
        print("What was that? It is so hard to hear in this helmet.")
        print("   ")
        What()



def questions():
    questions_list = []
    answer_list = []

    questions_list.append( input("What is your name?  "))

    print("Great!")
    questions_list.append( input("What is your quest?  "))

    print("Really? Well then the final question!")
    questions_list.append( input("What is your favorite color?  "))

    answer_list.append( len(questions_list[0]))
    answer_list.append( len(questions_list[1]))
    answer_list.append( len(questions_list[2]))

    truth = sum(answer_list)
    if truth > 50:
        pass
    

start_up()
while True:
    new_item = input("> ").lower()
    if new_item == "next":
        questions()
    if new_item == "begin":
        welcome()
    else:
        print("-Please type next to continue.-")