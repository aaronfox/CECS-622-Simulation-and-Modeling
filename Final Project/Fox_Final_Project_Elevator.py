# Aaron Fox
# CECS 622-01
# Dr. Elmaghraby
# Final Project - Elevator Project

import math # for natural log
import random # For uniform random selection

# TODO: If there are more than 12 people waiting on the elevator, some people will use the stairs. A
# person going to the second floor will have a .50 chance of walking. A person going to the third
# floor will have a .33 chance of walking. A person going to the fourth floor will have a .10 chance
# of walking
class Person:
    def __init__(self, arrival_time):
        #
        self.floor = 1
        # random.choice uniformly selects one of the choices, which is fitting since each floor
        # to fo to had a 33% chance of being selected
        self.floor_to_go_to = random.choice([2, 3, 4])

        # This is the time the person had to wait to board and the time it takes to leave the elevator
        self.wait_time = 0

        # arrival_time is the time the person initially arrives at the ground elevator
        self.arrival_time = 0

        # departure_time is the time the person gets off the elevator
        self.departure_time = 0
        self.set_arrival_time(arrival_time)

        # Identify each person in order of who got off first
        self.id = 0

        self.time_boarded_elevator = 0

        self.attempted_to_walk = False

        self.walked = False

    def set_walked_true(self):
        self.walked = True

    def set_attempted_to_walk_true(self):
        self.attempted_to_walk = True

    # Sets the arrival time of the person to the ground floor elevator (either line or no line)
    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    # Sets departure time of the person from the elevator (and also wait time since wait = departure - arrival)
    def set_departure_time(self, departure_time):
        self.departure_time = departure_time
        self.wait_time = self.departure_time - self.arrival_time

    def get_time_boarded_elevator(self):
        return self.time_boarded_elevator

    def set_boarding_time(self, boarding_time):
        self.time_boarded_elevator = boarding_time

    def get_floor(self):
        return self.floor_to_go_to

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return "[Person #" + str(self.id) + ", Arrival Time: " + str(self.arrival_time) + ", Departure Time: " + str(self.departure_time) + ", Wait Time: " + str(self.wait_time) + ", Time Boarded Lift: " + str(self.time_boarded_elevator) + ", Walker: " + str(self.walked) + "]\n"


    def __repr__(self):
        return "[Person #" + str(self.id) + ", Arrival Time: " + str(self.arrival_time) + ", Departure Time: " + str(self.departure_time) + ", Wait Time: " + str(self.wait_time) + "]"

def run_elevator_simulation(mean_interarrival_time):
    # Generate times for people to arrive at elevator until time reaches 61 (which is 9:00)
    times_to_arrive = []
    current_time = 0
    # lambda = mean interarrival rate = 1 / meant interarrival time
    # See: https://www.kellogg.northwestern.edu/faculty/weber/decs-430/Notes%20on%20the%20Poisson%20and%20exponential%20distributions.pdf
    mean_interarrival_rate = round(1 / mean_interarrival_time)
    while current_time <= 63: # Have this go to 61 to ensure everyone is accounted for in case last random var is very small (like 0.001, which would yield a high interarrival time)
        interarrival_time = -1 * math.log(random.random()) / mean_interarrival_rate
        current_time = current_time + interarrival_time
        times_to_arrive.append(current_time)

    # print(times_to_arrive)
    print("There are " + str(len(times_to_arrive)) + " people that can come to the elevator.")

    # Keeping track of the number of people that walk to each floor
    number_of_people_walked_to_2nd_floor = 0
    number_of_people_walked_to_3rd_floor = 0
    number_of_people_walked_to_4th_floor = 0

    # Keep track of last time a person boarded the elevator
    last_time_boarded_elevator = 0

    # Keep track of number of workers in line at specific times
    number_of_workers_in_line_at_8_30 = 0
    number_of_workers_in_line_at_8_45 = 0
    number_of_workers_in_line_at_9_00 = 0

    # Queue for elevator
    elevator_occupants = []
    queue = []
    elevator_floor = 1 # Ground floor of G == 1 here
    i = 0
    current_time = 0
    next_time = times_to_arrive[i]
    i = i + 1
    all_persons = []
    id_num = 1
    has_checked_830 = False
    has_checked_845 = False
    has_checked_900 = False
    # Run loop to iterate over needed hours 08:00-09:00+ (0 = 08:00, ..., 59 = 08:59, 60 = 9:00, etc.)
    # Continue running loop until all people have joined, the queue is empty, and all elevator_occupants have departed the lift
    while i < len(times_to_arrive) - 1 or len(queue) != 0 or len(elevator_occupants) != 0:
        # Use the variable has_time_moved_forward to check and make sure that time has moved forward. If not, increment by an amount
        has_time_moved_forward = False
        # print("Length of queue == " + str(len(queue)))
        # print("Length of elevator_occupants == " + str(len(elevator_occupants)))
        # print("Current Time: " + str(current_time))

        # Always start on ground floor (floor 0)
        elevator_floor = 1

        # print(current_time)
        error_tolerance = 2
        # Get number of people in queue at 8:30, 8:45, and 9:00
        if not has_checked_830 and (current_time <= 30 + error_tolerance and current_time >= 30 - error_tolerance):
            has_checked_830 = True
            print(current_time)
            number_of_workers_in_line_at_8_30 = len(queue)
        if not has_checked_845 and (current_time <= 45 + error_tolerance and current_time >= 45 - error_tolerance):
            has_checked_845 = True
            print(current_time)
            number_of_workers_in_line_at_8_45 = len(queue)
        if not has_checked_900 and (current_time <= 60 + error_tolerance and current_time >= 60 - error_tolerance):
            has_checked_900 = True
            print(current_time)
            number_of_workers_in_line_at_9_00 = len(queue)


        # Only add people to queue/elevator if their time is less than or equal to the current time
        while i < len(times_to_arrive) - 1:
            # If time below 60, can still add to queue
            if next_time <= current_time:

                # If elevator full, append to queue
                if len(elevator_occupants) >= 12:
                    queue.append(Person(next_time))
                elif elevator_floor == 1:
                    # Else, append to elevator queue
                    next_person = Person(next_time)
                    next_person.set_boarding_time(current_time)
                    elevator_occupants.append(next_person)
                else:
                    # elevator is not full, but it is not on ground (shouldn't happen)
                    queue.append(Person(next_time))
                
                # Get next time if in index
                i = i + 1
                next_time = times_to_arrive[i]
            else:
                # Otherwise next time hasn't come yet so break out of while loop
                break

        # If elevator on ground floor (floor 1) which it should always be to start, then go up
        if elevator_floor == 1:
            # Append necessary amount of persons from queue since on ground floor
            if len(elevator_occupants) < 12:
                # Add persons from queue to elevator
                while len(elevator_occupants) < 12 and len(queue) >= 1:
                    person_to_add = queue[0]
                    person_to_add.set_boarding_time(current_time)
                    elevator_occupants.append(person_to_add)
                    del queue[0]

            # People still left in queue here may choose to take the stairs. Check.
            for person in queue:
                # Make sure a person only contemplates walking once. Otherwise a 50% chance of walking twice 
                # becomes a 75% chance and so on while a person remains in the queue
                if person.attempted_to_walk == False:
                    if person.get_floor() == 2:
                        if random.random() < 0.5:
                            number_of_people_walked_to_2nd_floor = number_of_people_walked_to_2nd_floor + 1
                            person.set_walked_true()
                            all_persons.append(person)
                            queue.remove(person)
                        else:
                            person.set_attempted_to_walk_true()
                    elif person.get_floor() == 3:
                        if random.random() < 0.33:
                            number_of_people_walked_to_3rd_floor = number_of_people_walked_to_3rd_floor + 1
                            person.set_walked_true()
                            all_persons.append(person)
                            queue.remove(person)
                        else:
                            person.set_attempted_to_walk_true()
                    elif person.get_floor() == 4:
                        if random.random() < 0.10:
                            number_of_people_walked_to_4th_floor = number_of_people_walked_to_4th_floor + 1
                            person.set_walked_true()
                            all_persons.append(person)
                            queue.remove(person)
                        else:
                            person.set_attempted_to_walk_true()

            # Check if any occupant is going to second floor
            elevator_floor = 2
            someone_got_off_2nd = False
            for occupant in elevator_occupants:
                if occupant.get_floor() == 2:
                    someone_got_off_2nd = True
                    occupant.set_id(id_num)
                    id_num = id_num + 1
                    occupant.set_departure_time(current_time)
                    all_persons.append(occupant)
                    elevator_occupants.remove(occupant)
            
            if someone_got_off_2nd:
                has_time_moved_forward = True
                # Only option is to come from ground floor
                # Going from ground floor to second floor takes 1 minute
                current_time = current_time + 1.0
                # Opening elevator door takes 0.5 minutes
                current_time = current_time + 0.5

            # Check if any occupant is going to third floor
            elevator_floor = 3
            someone_got_off_3rd = False
            for occupant in elevator_occupants:
                if occupant.get_floor() == 3:
                    someone_got_off_3rd = True
                    occupant.set_id(id_num)
                    id_num = id_num + 1
                    occupant.set_departure_time(current_time)
                    all_persons.append(occupant)
                    elevator_occupants.remove(occupant)
            
            # See where elevator came from
            # From second floor
            if someone_got_off_3rd:
                has_time_moved_forward = True
                if someone_got_off_2nd:
                    # Coming from second floor
                    # Going from second floor to third floor takes 0.5 minutes
                    current_time = current_time + 0.5
                    # Opening elevator door takes 0.5 minutes
                    current_time = current_time + 0.5
                else:
                    # Coming from Ground floor
                    # Going from ground floor to third floor takes 0.5 minutes
                    current_time = current_time + 1.5
                    # Opening elevator door takes 0.5 minutes
                    current_time = current_time + 0.5

            # Check if any occupant is going to fourth floor
            elevator_floor = 4
            someone_got_off_4th = False
            for occupant in elevator_occupants:
                if occupant.get_floor() == 4:
                    occupant.set_id(id_num)
                    id_num = id_num + 1
                    all_persons.append(occupant)
                    occupant.set_departure_time(current_time)
                    elevator_occupants.remove(occupant)
                    someone_got_off_4th = True

            if someone_got_off_4th:
                has_time_moved_forward = True
                if someone_got_off_3rd:
                    # Came from third floor
                    # Going from third floor to fourth floor takes 0.5 minutes
                    current_time = current_time + 0.5
                    # Opening elevator door takes 0.5 minutes
                    current_time = current_time + 0.5
                elif someone_got_off_2nd:
                    # Came from 2nd floor
                    # Going from second floor to fourth floor takes 0.75 minutes
                    current_time = current_time + 0.75
                    # Opening elevator door takes 0.5 minutes
                    current_time = current_time + 0.5
                else:
                    # Came from ground floor
                    # Going from ground floor to fourth floor takes 1.75 minutes
                    current_time = current_time + 1.75
                    # Opening elevator door takes 0.5 minutes
                    current_time = current_time + 0.5

        # Ensure time always moves forward to avoid stasis
        if has_time_moved_forward == False:
            # Since -ln(0.999999) / 6 = 0.000001675, it is very, very, very unlikely 
            # (re: practically impossible) that a person's intial term would skip over their time
            # at the very same time they arrived
            current_time = current_time + 0.000000166667


    # Find last time boarded elevator
    # print("All Persons: " + str(all_persons))
    # Write data to text file
    f = open(r'C:\Users\aaron\Classes_11th_Semester\CECS 622\CECS-622-Simulation-and-Modeling\Final Project\data_results.txt', "w")
    for person in all_persons:
        f.write(str(person))
        if last_time_boarded_elevator < person.get_time_boarded_elevator():
            last_time_boarded_elevator = person.get_time_boarded_elevator()

    # TODO: fix the bug where the statement of number of people that can come to the elevator is
    # sometimes bigger than the number of persons in the text file. A smaller number in the text file is okay,
    # but sometimes that number is larger.
    f.write("Total Persons walked/took lift: " + str(len(all_persons)) + "\n")
    f.write("Time last person boarded elevator: " + str(last_time_boarded_elevator) + "\n")
    f.write("There were " + str(number_of_workers_in_line_at_8_30) +" people in line at 8:30\n")
    f.write("There were " + str(number_of_workers_in_line_at_8_45) +" people in line at 8:45\n")
    f.write("There were " + str(number_of_workers_in_line_at_9_00) +" people in line at 9:00\n")
    f.write("A total of " + str(number_of_people_walked_to_2nd_floor + number_of_people_walked_to_3rd_floor + number_of_people_walked_to_4th_floor) + " people walked.\n")
    f.write("People that walked to the second floor: " + str(number_of_people_walked_to_2nd_floor) + "\n")
    f.write("People that walked to the third floor: " + str(number_of_people_walked_to_3rd_floor) + "\n")
    f.write("People that walked to the fourth floor: " + str(number_of_people_walked_to_4th_floor) + "\n")
    f.close()

if __name__ == "__main__":
    mean_interarrival_time = 0.1667
    run_elevator_simulation(mean_interarrival_time)
