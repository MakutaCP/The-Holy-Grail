def start_up():
    print("   ")
    print("--THE HOLY GRAIL RIDDLES--")
    print("   ")
    print("TYPE BEGIN TO START OR TYPE QUIT TO EXIT")

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

class Player:
    Rid1 = False
    Rid2 = False
    Rid3 = False
    Rid4 = False
    Rid5 = False

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
    if truth < 30:
        print("   ")
        print("Oh the strong quiet type are you? Well do I have a riddle for you.")
        print("   ")
        Rid1()
    elif truth >= 30 and truth < 50:
        pass
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
    pass

def Rid3():
    pass

def Rid4():
    pass

def Rid5():
    pass
    

start_up()
while True:
    new_item = input("> ").lower()
    if new_item == "next":
        questions()
    elif new_item == "begin":
        welcome()
    elif new_item == "quit":
        exit()
    else:
        print("-Please enter a valid command-")