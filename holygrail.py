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
    #Just some for fun questions here and the first sudden ending
    yes_or_no_list = []
    yes_or_no_list.clear

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
        print("Oh. You must be looking for the bathrooms then. Those are three doors down on the left.")
        print("   ")
        print("Off you go then.")
        print("   ")
        print("--THE END?--")
        print("--TYPE BEGIN TO START AGAIN OR TYPE QUIT TO EXIT-- ")
    else:
        print("   ")
        print("What was that? It is so hard to hear in this helmet.")
        print("   ")
        What()

def ask_questions(questions_list):
    #This function is called below and asks the questions before returning the values
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
    return questions_list

def questions():
    #This function takes the length of the answers, adds them together,
    #and returns the number which is used to give one of three riddles.
    empty_list = []
    answer_list = []

    questions_list = ask_questions(empty_list)

    answer_list.append( len(questions_list[0]))
    answer_list.append( len(questions_list[1]))
    answer_list.append( len(questions_list[2]))

    truth = sum(answer_list)
    print("   ")
    print("Your answers gave me the number...")
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
        print("An average adventuring type. Above average in general. You shall have this riddle!")
        print("   ")
        Rid2()
    elif truth > 60:
        print("   ")
        print("A very wordy person. Maybe a wizard? Well a fitting riddle I will give you!")
        print("   ")
        Rid3()
    else:
        print("   ")
        print("Wait a second something is fishy here. And it is not my fish Eric.")
        print("   ")
        print("You get out you cheater. You are not worthy!")
        print("   ")
        print("--THE END.--")
        print("--TYPE BEGIN TO START AGAIN OR TYPE QUIT TO EXIT-- ")


def congrats():
    print("   ")
    print("--CONGRATULATIONS! YOU HAVE FOUND THE HOLY GRAIL--")
    print("   ")
    print("--TYPE BEGIN TO START AGAIN OR TYPE QUIT TO EXIT--")

def fail():
    print("   ")
    print("--YOU HAVE FAILED. PLEASE LEAVE AND NEVER RETURN!--")
    print("   ")
    print("--TYPE BEGIN TO START AGAIN OR TYPE QUIT TO EXIT-- ")

def Rid1():
    Rid1_ans = []
    print("   ")
    print("There are 3 cups on the table in front of you.")
    print("   ")
    print("The 1st is red, the 2nd is blue, and the 3rd is yellow.")
    print("   ")
    Rid1_ans.append(input("Give me the number of the cup that does not make the color green. That is the Holy Grail.  "))

    if Rid1_ans[0] == "1":
        congrats()
    else:
        fail()
    

def Rid2():
    Rid2_ans = []
    print("   ")
    print("There are 5 cups on the table infront of you.")
    print("   ")
    print("From left to right the first 3 are full of water while the 4th and 5th are empty.")
    print("   ")
    print("Only 1 cup needs to be moved to make the 1st, 3rd, and 5th cups full of water.")
    print("   ")
    Rid2_ans.append( input("Give me the number of which cup needs to move. That is the Holy Grail.  "))

    if Rid2_ans[0] == "2":
        congrats()
    else:
        fail()


def Rid3():
    Rid3_ans = []
    print("   ")
    print("Five cups on the table, three saints up above,")
    print("Two full of hate, three full of love,")
    print("Two hates not together, for fear of a crime,")
    print("Two loves together, forever in time,")
    print("The one love alone is the Holy Grail you seek,")
    print("Not next to the loves, as a gift to the meek,")
    print("The 1st on the left is not the Grail, not the boon")
    print("But the hate on the other end shall be your doom.")
    print("   ")
    print("Which cup is the Holy Grail?")
    print("   ")
    Rid3_ans.append( input("Give me the number of the Grail. The answer wll be 1,2,3,4, or 5.  "))



    if Rid3_ans[0] == "4":
        congrats()
    else:
        fail()


    

start_up()
while True:
    #Allows for the repeat of the game as well as quiting. 
    new_item = input("> ").lower()
    if new_item == "begin":
        welcome()
    elif new_item == "quit":
        exit()
    else:
        print("-Please enter a valid command-")
