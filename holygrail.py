def start_up():
    print("   ")
    print("--THE HOLY GRAIL RIDDLES--")
    print("   ")
    print("TYPE BEGIN TO START OR TYPE QUIT TO EXIT")

def welcome():
    print("   ")
    print("Welcome to the secret cave! Located in Las Vegas.")
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
    elif "no" in yes_or_no_list:
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

    print("   ")
    questions_list.append( input("What is your name?  "))

    print("   ")
    print("Great!")
    print("   ")
    questions_list.append( input("What is your quest?  "))

    print("   ")
    print("Really? Well then the final question!")
    print("   ")
    questions_list.append( input("What is your favorite color?  "))

    answer_list.append( len(questions_list[0]))
    answer_list.append( len(questions_list[1]))
    answer_list.append( len(questions_list[2]))

    truth = sum(answer_list)
    print("   ")
    print("Your answers gives me the number...")
    print(truth)

    print("   ")
    print("And that means you are...")
    if truth < 30:
        print("   ")
        print("Oh the quiet type are you? Well do I have a riddle for you.")
        print("   ")
        Rid1()
    elif truth >= 30 and truth <= 60:
        print("   ")
        print("A average adventuring type. Above average in general. You shall have this riddle!")
        print("   ")
    elif truth > 60:
        print("   ")
        print("A very wordy person. Maybe a wizard? Well a fitting riddle I will give you!")
        print("   ")
    else:
        print("   ")
        print("Wait a second some thing is fishy here. And it is not my fish Eric.")
        print("   ")
        print("You get out you cheater. You are not worthy!")
        print("   ")
        print("--THE END.--")


def Rid1():
    pass

def Rid2():
    Rid2_ans = []
    print("   ")
    print("There are five cups on the table infront of you.")
    print("   ")
    print("The first three are full of water while the fourth and fifth is empty.")
    print("   ")
    print("Only one cup needs to be moved to make make the first, third, and fifth cups full of water.")
    print("   ")
    Rid2_ans.append( input("Give me the number of which cup needs to move.  "))

    if Rid2_ans == "2":
        congrats()
    else:
        fail()


def Rid3():
    pass

    

start_up()
while True:
    new_item = input("> ").lower()
    if new_item == "begin":
        welcome()
    elif new_item == "result":
        secret()
    elif new_item == "quit":
        exit()
    else:
        print("-Please enter a valid command-")

def congrats():
    print("   ")
    print("--CONGRADULATIONS! YOU HAVE FOUND THE HOLY GRAIL--")
    print("   ")
    print("--GIVE THE COMMAND RESULT AT THE BEGINING TO FIND YOUR SECRET--")

def fail():
    print("   ")
    print("--YOU HAVE FAILED. PLEASE LEAVE AND NEVER RETURN!--")

def secret():
    print("HOW DID YOU FIND THIS PLACE?!?")
    print("YOU MUST HAVE THE GRAIL.")
