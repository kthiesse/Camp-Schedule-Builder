import random
import copy

def main():
    MasterStaff,MasterLifeguard,MasterBelayer = load_Staff()
    
    # 1 [[WF],[CW],[CS],[CR],[NA],[AR]]
    # 2 [[  ],[  ],[  ],[  ],[  ],[  ]]
    # 3 [[  ],[  ],[  ],[  ],[  ],[  ]]
    # 4 [[  ],[  ],[  ],[  ],[  ],[  ]]
    # 5 [[  ],[  ],[  ],[  ],[  ],[  ]]
    # 6 [[  ],[  ],[  ],[  ],[  ],[  ]]
    schedule = [[],[],[],[],[],[]]

    i=0
    while i < 6:
        activitySlot = build_Schedule(copy.deepcopy(MasterStaff), MasterLifeguard, MasterBelayer)
        schedule[i] = activitySlot
        i=i+1
    print_Schedule(schedule)



def waterfront_Populate(lifeguard, staff):
    activity = []
    choice = random.choice(lifeguard)
    activity.append(choice)
    staff.remove(choice)
    return activity, staff


def climbingWall_Populate(belayer, staff):
    activity = []
    i=0
    while i < 2:
        while True:
            choice = random.choice(belayer)
            if choice in staff:
              break
            else:
                continue
        activity.append(choice)
        staff.remove(choice)
        i = i+1
    return activity, staff


def activity_Populate(staff,amount):
    activity = []
    i = 0
    choice = ""
    while i < amount:
        choice = random.choice(staff)
        staff.remove(choice)
        activity.append(choice)
        i = i+1
    return activity,staff



def build_Schedule(staff, lifeguard, belayer):
    slot = [[],[],[],[],[],[]]
    waterfront, staff = waterfront_Populate(lifeguard, staff)
    slot[0]= waterfront
    climbingWall, staff = climbingWall_Populate(belayer, staff)
    slot[1] = climbingWall
    i = 2
    while i < 6:
        activity,staff = activity_Populate(staff, 1)
        slot[i] = activity
        i = i+1
    return slot

def print_Schedule(schedule):
    i = 0
    while i < 6:
        print("Timeslot "+ str(i+1))
        print("Waterfront: " + str(schedule[i][0]))
        print("Climbing Wall: " + str(schedule[i][1]))
        print("Camp Skills: "+ str(schedule[i][2]))
        print("Crafts: " + str(schedule[i][3]))
        print("Nature: " + str(schedule[i][4]))
        print("Archery: " + str(schedule[i][5]))
        print("\n")
        i=i+1
        
def load_Staff():
    staffFile= open("staff.txt","r")
    staff = []
    for line in staffFile:
        staff.append(line.strip())
    staffFile.close()
    
    lifeguardFile = open("lifeguard.txt","r")
    lifeguard = []
    for line in lifeguardFile:
        lifeguard.append(line.strip())
    lifeguardFile.close()
    
    belayerFile = open("belayer.txt","r")
    belayer = []
    for line in belayerFile:
        belayer.append(line.strip())
    belayerFile.close()
    
    return staff, lifeguard, belayer

main()
