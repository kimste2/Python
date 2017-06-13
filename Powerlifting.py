'''
Powerlifitng is a sport composed of three lifts: the squat, bench and deadlift in that order.
There are three attempts at each lift. The winner is whom ever has the highest total. Competitions
are held in either kilos or pounds. 
'''

lifter = {
    "name":[],
    "units":[],
    "squat": [],
    "bench": [],
    "deadlift": []
}

lifter["name"] = input("Please enter your name: ")
print(lifter["name"])

lifter["units"] = input("Please enter competition units: \"kilos\" or \"pounds\": ")