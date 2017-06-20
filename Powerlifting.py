'''
Powerlifitng is a sport composed of three lifts: the squat, bench and deadlift in that order.
There are three attempts at each lift. The winner is whom ever has the highest total. Competitions
are held in either kilos or pounds. 
'''
lift_attempts = 3
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
print(lifter["units"])

def get_squat():
    for x in range(0,3):
        make_lift = input("Did you make your squat attempt? ")
        make_lift.lower()
        if make_lift != "yes" and make_lift != "no":
            print("Invalid input! \n")
            get_squat()
        else:
            attempt = input("Please enter weight lifting: ")
            
get_squat()