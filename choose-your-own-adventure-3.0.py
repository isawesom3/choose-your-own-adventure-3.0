#my name
name = "Sqiddyinkster🤣"
#introduction
print(f"Welcome to {name}'s choose ur own adventure game! Let's get started.")
print("You find yourself in a dark cave with 3 pathways. One is red and one is blue and one is green..")
path_choice = input("Which path do you go? Type 'red' for the red path or 'blue' for the blue path or 'green' for the green path: ")
#first choice
if path_choice == "red":
    print("You walk straight into a battle between- whoa whoa whoa, wait a second. IS THAT YODA AND IRON MAN???? dang. they both need you help to win.")
    choice_1 = input("Who do you want to help? Type '1' to help Yoda or '2' for Iron Man: ")
    if choice_1 == "1":
        print("You side with Yoda! You can either throw a stick at Iron Man, or make use of your karate moves.  ")
        choice_6 = input("Do you throw the stick, or bust out some karate moves? type '1' for the stick or '2' for the karate: ")
        if choice_6 == "1":
            print("""__________SUCCESS__________                      You throw a stick at Iron Man. A direct hit on the arc reacter! his suit powers down. Yoda gets you home. """)
        else:
            print("""__________GAME OVER__________                    You throw a kick. bad move! he vaporizes you.""")
    else:
        print("You are now an Avenger! you side with Iron Man. You see a missile and a lizard. ")
        choice_7 = input("Do you throw the missile or the lizard at Yoda? type '1' for the missile or '2' for the lizard.")
        if choice_7 == "1":
            print("""__________GAME OVER__________                    You throw the missile! it blows you and the entire battleground up.""")
        else:
            print("""__________SUCCESS__________                    You throw the lizard. the lizard is a Ysalamir, which can create force neutral bubbles. he defeats Yoda. Iron Man flies you home.""")
elif path_choice == "blue":
    print("You walk into the blue path and find a turtle who asks you to eat a fish.")
    choice_2 = input("Do you eat the fish? Type '1' for yes or '2' for no: ")
    if choice_2 == "1":
        print("The turtle thanks you and gives you a magical shell that can grant one wish.")
        choice_8 = input("What is your wish? do you go home of ask for money? type '1' for home and '2' for money.")
        if choice_8 == "1":
            print("""__________SUCCESS__________                      you go home and live your life """)
        else:
                ("__________GAME OVER__________                     You have money but you can't get home! you starve to death.")
    else:
        print("""__________GAME OVER__________
        The turtle becomes angry and throws you out of the universe""")
elif path_choice == "green":
    print("You walk into the green path and find a billion dollars. you have escaped. back at you new mansion, you are looking for a vehicle. you see a helicopter with a steep discount, but you also see a lamborgini that looks nice.")
    choice_3 = input("Do you take the helicopter or lamborgini? Type '1' for the lambo or '2' for the helicopter.: ")
    if choice_3 == "1":
        print(" You have gotten a Lamborgini!")
        choice_4 = input(" you are offered another billion dollars to transport a bag to canada. do you take it? type '1' for no or '2' for yes.")
        if choice_4 == "1":
            print("""__________SUCCESS__________                   good choice! you live out the rest of your life in peace.""")
        else:
            print(""" __________GAME OVER__________
            What could go wrong? you drive the bag to canada and it explodes. better luck next time.""")
    else:
        print("You are now the owner of a helicopter! ")
        choice_5 = input(" you are offered another billion dollars to transport a bag to canada. do you take it? type '1' for no or '2' for yes.")
        if choice_5 == "1":
            print("""__________SUCCESS__________                   good choice! you live out the rest of your life in peace.""")
        else:
            print(""" __________GAME OVER__________
            What could go wrong? you fly the bag to canada and it explodes. better luck next time.""")
else:
    print("Invalid choice. Please select either 'red' or 'blue' or 'green'.")
    
