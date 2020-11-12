def start_up():
    print("Welcome to the secret cave.")
    print("You have found the resting place of the Holy Grail.")
    print("I am going to give you the chance to earn it.")

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

#grail = "The Holy Grail"

#grail = False
#if grail is True:
    #print("Well Done! You have beaten the game!")
#else:
    #print("Welcome to the adenture!")
