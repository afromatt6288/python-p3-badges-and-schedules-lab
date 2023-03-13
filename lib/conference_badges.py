def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    name_list = [] 
    for name in names:
        name_list.append(f"Hello, my name is {name}.")
    return name_list

def assign_rooms(names):
    room_assignment =[]
    for n in range(len(names)):
        room_assignment.append(f"Hello, {names[n]}! You'll be assigned to room {n+1}!")
    return room_assignment

def printer(names):
    # print(batch_badge_creator(names) + assign_rooms(names))
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)
