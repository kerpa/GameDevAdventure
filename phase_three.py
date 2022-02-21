def main_door():
    print("\n A heavy door looms before you")
    main_door_choice = input(
        "\n Do you want to knock on the door ? (Yes/No) \n >")
    if main_door_choice == "No":
        print("\n You suddenly hear a noise at the window to your left.")
        print("\n You peek through the window")
        print("\n You observe through the thin curtain, many paintings of richly dressed men"
              "and women as well as the end of a long dining table")
    elif main_door_choice == "Yes":
        print("\n You hear the sound of a plate getting smashed")
        main_door_choice_2 = input(
            "\n Do you want to retry knock on the door ? (Yes/No) \n >")
        if main_door_choice_2 == "Yes":
            print("\nNobody seems to answer you")
    else:
        print("\n Should be Yes or No")
        main_door()


def wait():
    wait_choice = input("\n Do you want to try to wait? (Yes/No) \n >")
    if wait_choice == "Yes":
        print("\n You are waiting")
        wait()
    elif wait_choice == "No":
        print("\n You try to find a way in")
        print("\n After several minutes you discover another door at the back of the house")
    else:
        print("\n Should be Yes or No")
        wait()


def phase_three():
    main_door()
    wait()


phase_three()
