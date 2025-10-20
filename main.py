phoenix_game = "Phoenix"
print(f"Welcome to",phoenix_game,"!")
print("============================")
print("Before we begin, what's your characters name?")
name = input()
print(">",name)
print(f"Great,",name,"!","let's begin the adventure!")
player = {
    "name" : name,
    "health" : 100,
    "coin" : 0
}
import random
events = ["find a coin","meet a monster","do nothing"]
event = random.choice(events)
print(f"While exploring, you {event}!")

if event == "find a coin":
    player["coin"] =  1
    print(name,"found a coin",name,"now has",player["coin"],"number of coins")

elif event == "meet a monster":
    player["health"] = 90
    print(name,"got hurt during the combat with the monster, health is now",player ["health"])