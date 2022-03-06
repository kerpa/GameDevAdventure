# starting scene

def starting_scene():
    print("You are in the middle of a scottish plain. \n"
          "The night is dark and you can barely see anything. \n"
          "The rain is pouring down and you hear the sound of thunder. \n \n"
          "Suddenly your car breaks down and you are stranded. \n")
    print("You should definitely look under the car to see what's going on. \n")


def choice_car():
    car_choice_input = input("Do you want to look under the car? (type: A) \n"
                             "Or do you want to look at the trunk? (type: B) \n >")
    if car_choice_input == "B":
        print("You see a flashlight and a knife. \n")
        player_inventory.append("flashlight")
        player_inventory.append("knife")
    elif car_choice_input == "A":
        print("Your mere knowledge is not enough to find anything.")
    else:
        print("Please choose A or B.")
        choice_car()


def end_phase_one():
    print("Far on the hill you see a small light. \n"
          "At this point you have no idea what to do. \n"
          "You should probably go to the light. \n")


def phase_one():
    starting_scene()
    choice_car()
    end_phase_one()
