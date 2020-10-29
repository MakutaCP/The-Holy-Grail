def start_up():
    print("Welcome to the secret cave.")
    print("You have found the resting place of the Holy Grail.")
    print("I am going to give you the chance to earn it.")

def questions():
    print("What is your name?  ")

start_up()
while True:
    new_item = input("> ")
    if new_item == "NEXT":
        questions()

#grail = "The Holy Grail"

#grail = False
#if grail is True:
    #print("Well Done! You have beaten the game!")
#else:
    #print("Welcome to the adenture!")


player_list = []

def add_to_list(item):
    player_list.append(item)

