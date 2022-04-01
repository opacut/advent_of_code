from classes import Fish, School

f = open("6/input.txt", "r")
lines = [int(x) for x in f.read().split(",")]
print(lines)

# each fish spawns another fish in 7 days
# first cycle takes 2 more days
spawn_rate = 7
grow_up_rate = 2
no_of_days = 256

school = School(fishes=[Fish(timer=no) for no in lines])

print("Initial state: "+str(school.display()))
increments = []
for day in range(no_of_days):
    init_fishes = len(school.fishes)
    school.advance()
    end_fishes = len(school.fishes)
    print(f"Day {day}")
    increments.append(end_fishes - init_fishes)
    #print(f"Increment: {end_fishes - init_fishes}")
#print(f"Increments: {increments}")
print(f"After {str(no_of_days)} days, there are {str(len(school.fishes))} fish.")
