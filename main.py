import phase_one
import phase_two
import phase_three

player_fear = 0
player_inventory = []


with open('title.txt', 'r') as title:
    print(title.read())

phase_one.phase_one()
phase_two.going_to_light()
phase_three.phase_three()
