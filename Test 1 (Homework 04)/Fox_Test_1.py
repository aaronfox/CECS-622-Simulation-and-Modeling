# Aaron Fox
# CECS 622-01
# Dr. Elmaghraby
# Test 1 (Rumors Simulation Project)

## Story ##
# + N students are at a party (N is an even integer 2 ≤ N ≤ 10,000)
# + At some point, all students pair off at random and talk for exactly one minute.
# + At the end of the minute, all students again pair off with another person at random.
# + One student wants to start a rumor. He spreads the rumor to his conversation partner at noon.
# + Every person who has knowledge of the rumor obeys these rules:
#    1. The likelihood of spreading a rumor to another person is 0.5
#    2. After a person has heard the rumor 2 times, he/she will assume everyone has heard the
#       rumor and will no longer try to spread it further

## Assumptions
# + Students can pair up with the same student again as often happens at parties in the real world
# + If a student has shared the rumor once with a student already and meets up with them again,
#   then that student cannot share the rumor again and it won't count toward the 2 times
#   that the receiving student has heard a rumor.

# The Student class keeps track of if the student has heard the rumor, the number of times
# that the student has heard the rumor, their unique student ID, the likelihood of each student
# spreading the rumor, and the students whom they have spread the rumor to
class Student:
    def __init__(self, student_id, times_heard_rumor=0, likelihood_of_spreading=0.5):
        # Unique student id to identify each student and keep track of which student
        # each student has talked to
        self.student_id = student_id

        # The number of times that the student has heard the rumor.
        # If this is 0, then the student has not heard the rumor.
        # If this is 2, then the student stops spreading the rumor
        self.times_heard_rumor = times_heard_rumor

        # The chance of spreading a rumor to another student
        self.likelihood_of_spreading = likelihood_of_spreading

        # Maintain a list of unique student_ids that this student has spread the rumor
        # to to ensure that the student doesn't try to spread the rumor to one
        # person twice and increase another student's times_heard_rumor twice
        self.students_spread_rumor_to = []

