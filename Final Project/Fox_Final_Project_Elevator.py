# Aaron Fox
# CECS 622-01
# Dr. Elmaghraby
# Final Project - Elevator Project

import math # for natural log
import random # For uniform random selection

class Person:
    def __init__(self):
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

    # Sets the arrival time of the person to the ground floor elevator (either line or no line)
    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    # Sets departure time of the person from the elevator (and also wait time since wait = departure - arrival)
    def set_departure_time(self, departure_time):
        self.departure_time = departure_time
        self.wait_time = self.departure_time - self.arrival_time

def run_elevator_simulation(mean_interarrival_time):
    # Keep generating new interarrival times after each arrival time

    # Generate times for people to arrive at elevator until time reaches 61 (which is 9:00)
    times_to_arrive = []
    current_time = 0
    # lambda = mean interarrival rate = 1 / meant interarrival time
    # See: https://www.kellogg.northwestern.edu/faculty/weber/decs-430/Notes%20on%20the%20Poisson%20and%20exponential%20distributions.pdf
    mean_interarrival_rate = round(1 / mean_interarrival_time)
    while current_time <= 61:
        interarrival_time = -1 * math.log(random.random()) / mean_interarrival_rate
        current_time = current_time + interarrival_time
        times_to_arrive.append(current_time)

    print(times_to_arrive)
    print(len(times_to_arrive))


    # Run for loop between 08:00-09:00 (0 = 08:00, ...,59 = 08:59, 60 = 9:00, etc.)
    # for minute in range(0, 61):
    #     pass
        # print(minute)
        # Get exponentially distributed times

if __name__ == "__main__":
    mean_interarrival_time = 0.1667
    run_elevator_simulation(mean_interarrival_time)
