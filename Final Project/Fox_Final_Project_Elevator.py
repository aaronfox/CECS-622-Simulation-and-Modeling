# Aaron Fox
# CECS 622-01
# Dr. Elmaghraby
# Final Project - Elevator Project

import math # for natural log
import random # For uniform random selection

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

    # Sets the arrival time of the person to the ground floor elevator (either line or no line)
    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    # Sets departure time of the person from the elevator (and also wait time since wait = departure - arrival)
    def set_departure_time(self, departure_time):
        self.departure_time = departure_time
        self.wait_time = self.departure_time - self.arrival_time

    def get_floor(self):
        return self.floor_to_go_to

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
    # Run loop to iterate over needed hours 08:00-09:00+ (0 = 08:00, ..., 59 = 08:59, 60 = 9:00, etc.)
    # Continue running loop until all people have joined, the queue is empty, and all elevator_occupants have departed the lift
    while i < len(times_to_arrive) - 1 or len(queue) != 0 or len(elevator_occupants) != 0:
        # TODO: use the variable has_time_moved_forward to check and make sure that time has moved forward. If not, increment by an amount
        has_time_moved_forward = False
        print("Length of queue == " + str(len(queue)))
        print("Length of elevator_occupants == " + str(len(elevator_occupants)))
        print("Current Time: " + str(current_time))

        # Always start on ground floor (floor 0)
        elevator_floor = 1

        # Only add people to queue/elevator if their time is less than or equal to the current time
        while i < len(times_to_arrive) - 1:
            # If time below 60, can still add to queue
            if next_time <= current_time:

                # If elevator full, append to queue
                if len(elevator_occupants) >= 12:
                    queue.append(Person(next_time))
                elif elevator_floor == 1:
                    # Else, append to elevator queue
                    elevator_occupants.append(Person(next_time))
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
                    print("adding from queue to elevator")
                    person_to_add = queue[0]
                    elevator_occupants.append(person_to_add)
                    del queue[0]
                    print("test: " + str(person_to_add.get_floor()))

            # Check if any occupant is going to second floor
            elevator_floor = 2
            someone_got_off_2nd = False
            for occupant in elevator_occupants:
                if occupant.get_floor() == 2:
                    # TODO: Get passengers off here and add data to add
                    print("going to second")
                    someone_got_off_2nd = True
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
                    # TODO: Get passengers off here and add data to add
                    print("going to third")
                    someone_got_off_3rd = True
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

            # Check if any occupant is going to second floor
            elevator_floor = 4
            someone_got_off_4th = False
            for occupant in elevator_occupants:
                if occupant.get_floor() == 4:
                    # TODO: Get passengers off here and add data to add
                    print("going to fourth")
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

        # TODO: implement this
        if has_time_moved_forward == False:
            # print("forcing time forward")
            # Edit this number by realizing that -ln(0.99) / 6 = 0.001675
            current_time = current_time + 0.001675

if __name__ == "__main__":
    mean_interarrival_time = 0.1667
    run_elevator_simulation(mean_interarrival_time)
