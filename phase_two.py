player_fear = 0
player_inventory = ["flashlight", "knife"]


def going_to_light():
    global player_fear
    print("\n")
    print("You look away at the hill, and you see a faint glow.")
    choice = input("Do you want to approach the glow ? (Yes/No)")
    if choice == "No":
        print("You stay in the car \n")
        print("After a few hours in your car, the cold begins to be felt")
        print("Suddenly you hear the shrill howl of a wolf")
        player_fear += 1
        print("The fear makes you go toward the light \n")

    if "flashlight" in player_inventory:
        print("You have a flashlight \n")
    else:
        print("You do not have a flashlight \n")
        player_fear += 1
    print("The closer you get to the glow, the more you see the shapes of a house appear.")
    print("you arrive in front of the landing of the door\n")


going_to_light()
