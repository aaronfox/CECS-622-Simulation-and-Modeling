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
    # Run for loop for hours 08:00-09:00 (0 = 08:00, ...,59 = 08:59, 60 = 9:00, etc.)
    for time in times_to_arrive:
        # If time below 60, can still add to queue
        if time < 60:
            # If elevator full, append to queue
            if len(elevator_occupants) >= 12:
                queue.append(Person(time))
            else:
                # Else, append to elevator queue
                elevator_occupants.append(Person(time))
        else:
            #don't add to queue
            pass

if __name__ == "__main__":
    mean_interarrival_time = 0.1667
    run_elevator_simulation(mean_interarrival_time)
