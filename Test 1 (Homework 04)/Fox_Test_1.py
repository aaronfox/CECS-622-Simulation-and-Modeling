# Aaron Fox
# CECS 622-01
# Dr. Elmaghraby
# Test 1 (Rumors Simulation Project)

# Used for selecting a random starting student to start spreading the rumor
# and for shuffling students to later pair them
import random # Using randint and shuffle

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
# + Likewise, students can keep track of who has told them the rumor so they can't "spread" the rumor to someone
#   who has already told them the rumor.
# + If both students in a pair have heard the rumor and haven't previously spread the rumor to the other,
#   they each still have the possibility to tell the other student about the rumor (if the random likelihood is true),
#   and a randomly chosen student in the pair is chosen to first tell the rumor. If the first student's attempt is
#   not successful, then the second student can try to spread the rumor to the first.


# The Student class keeps track of if the student has heard the rumor, the number of times
# that the student has heard the rumor, their unique student ID, the likelihood of each student
# spreading the rumor, and the students whom they have spread the rumor to
class Student:
    def __init__(self, student_id, times_heard_rumor=0, likelihood_of_spreading=0.5):
        # Unique student id to identify each student and keep track of which student
        # each student has talked to
        self.student_id = student_id

        # Keeps track of who has heard the rumor. This is important because the very
        # first student knows the rumor but has not heard it from anyone at the party yet, so technically
        # their times_heard_rumor is 0
        self.has_heard_rumor = False

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


    def __repr__(self):
        return "Student ID: " + str(self.student_id)

    def __str__(self):
        return str("Student ID: " + str(self.student_id) + ", Has heard rumor: "\
            + str(self.has_heard_rumor) + ", Number of times heard rumor: " + str(self.times_heard_rumor)\
            + ", Likelihood of spreading rumor: " + str(self.likelihood_of_spreading)\
            + ", Students spread rumor to: " + str(self.students_spread_rumor_to))

    def set_heard_rumor(self, has_heard_rumor):
        self.has_heard_rumor = has_heard_rumor

    def get_id(self):
        return self.student_id

    def append_students_spread_rumor_to(self, other_student_id):
        self.students_spread_rumor_to.append(other_student_id)

    def increment_times_heard_rumor(self):
        # Ensure set heard rumor is true for the student
        self.set_heard_rumor(True)
        self.times_heard_rumor = self.times_heard_rumor + 1

    def get_times_heard_rumor(self):
        return self.times_heard_rumor

    # Returns the list of students that this class has spread to. this
    # is done to ensure that a student that has heard of a rumor from someone cannot tell them the same rumor again
    def get_students_spread_to(self):
        return self.students_spread_rumor_to

    # Determines if this student is capable of spreading the rumor
    # and makes sure that student hasn't already told that student
    # and that the student isn't telling a student that told them
    def can_spread_rumor(self, student_id_to_tell_rumor_to, other_students_spread_rumor_to):
        if self.has_heard_rumor == True:
            if self.times_heard_rumor < 2:  # Magic number 2 here represents the prompt stating that 
                                            # "After a person has heard the rumor 2 times, he/she will 
                                            # assume everyone has heard the rumor and will no longer try to spread it further"
                if student_id_to_tell_rumor_to not in self.students_spread_rumor_to:
                    if self.get_id() not in other_students_spread_rumor_to:
                        print(self.__repr__() + " can spread to Student ID: " + str(student_id_to_tell_rumor_to) + "!")
                        return True

        print(self.__repr__() + " CANNOT spread to Student ID: " + str(student_id_to_tell_rumor_to))
        return False

def run_rumor_simulation(likelihood_of_spreading_rumor=0.5, number_of_students=10, minutes_to_run=10):
    if number_of_students % 2 != 0:
        print("Error: Input parameter number_of_students must be even. " + str(number_of_students) + " is not an even number.")
        return

    students = []
    # First, create an array of students
    for i in range(number_of_students):
        students.append(Student(student_id=i, times_heard_rumor=0, likelihood_of_spreading=likelihood_of_spreading_rumor))

    # Randomly set one student to have heard the rumor by setting times
    student_to_start_rumor = random.randint(0,number_of_students - 1)
    students[student_to_start_rumor].set_heard_rumor(True)

    # Run over every minute needed in given parameter minutes_to_run
    for minute in range(minutes_to_run):
        # Get random pairs of each student by randomly shuffling everybody and then pairing them into twos
        random.shuffle(students)
        print("students == " + str(students))
        # Iterate over every pair and evaluate results
        for i in range(0, number_of_students, 2):
            print("Pairing " + repr(students[i]) + " with " + repr(students[i + 1]))
            # Since initial student initially spreads rumor to first conversion partner at minute 0, make sure this happens here
            if minute == 0 and (students[i].get_id() == student_to_start_rumor or students[i + 1].get_id() == student_to_start_rumor):
                # Check first case where current even number student in shuffled students list is initial rumor spreader
                if students[i].get_id() == student_to_start_rumor:
                    students[i].append_students_spread_rumor_to(students[i + 1].get_id())
                    students[i + 1].increment_times_heard_rumor()
                    print("First spread from initial " + repr(students[i]) + " to " + repr(students[i + 1]))
                # Else, it's second case where current odd number student in shuffled students list is initial rumor spreader
                else:
                    students[i + 1].append_students_spread_rumor_to(students[i].get_id())
                    students[i].increment_times_heard_rumor()
                    print("First spread from initial " + repr(students[i + 1]) + " to " + repr(students[i]))
            else:
                # First case: First student in pair has heard rumor and second hasn't
                if students[i].has_heard_rumor and not students[i + 1].has_heard_rumor:
                    # Make sure that this student can logically spread rumor to other student
                    if students[i].can_spread_rumor(students[i + 1].get_id(), students[i + 1].get_students_spread_to()):
                        if random.random() < likelihood_of_spreading_rumor: 
                                students[i].append_students_spread_rumor_to(students[i + 1].get_id())
                                students[i + 1].increment_times_heard_rumor()
                                print("Spread from " + repr(students[i]) + " to " + repr(students[i + 1]))

                # Second case: First student in pair hasn't heard rumor but second student has
                elif not students[i].has_heard_rumor and students[i + 1].has_heard_rumor:
                   # Make sure that this student can logically spread rumor to other student
                    if students[i + 1].can_spread_rumor(students[i].get_id(), students[i].get_students_spread_to()):
                        if random.random() < likelihood_of_spreading_rumor: 
                                students[i + 1].append_students_spread_rumor_to(students[i].get_id())
                                students[i].increment_times_heard_rumor()
                                print("Spread from " + repr(students[i + 1]) + " to " + repr(students[i]))

                # Third case: Both students have heard rumor already. this is the tricky one
                elif students[i].has_heard_rumor and students[i + 1].has_heard_rumor:
                    # Check if both students have heard rumor based on assumption that even if both students
                    # know the rumor already, they still have a chance of telling the rumor to the other
                    # student in the pair again.
                    # Caveat: If one student successfully tells other student rumor first, then
                    #         the student who just got told the rumor can't retell the rumor to the same person

                    # Randomly see who gets to try to spread the rumor first
                    curr_pair_students = [i, i + 1]
                    index_of_first_student_in_pair_to_attempt = random.choice([0, 1])
                    first_student_to_attempt = curr_pair_students[index_of_first_student_in_pair_to_attempt]
                    second_student_to_attempt = ""
                    if index_of_first_student_in_pair_to_attempt == 0:
                        second_student_to_attempt = curr_pair_students[1]
                    else:
                        second_student_to_attempt = curr_pair_students[0]

                    first_student_successfully_spread_rumor = False

                    # Make sure that this student can logically spread rumor to other student
                    if students[first_student_to_attempt].can_spread_rumor(students[second_student_to_attempt].get_id(), students[second_student_to_attempt].get_students_spread_to()):
                        # Check if randomly generated float is less than likelihood of spreading rumor. If so, spread rumor
                        # If true, spread rumor to student who has not heard rumor
                        if random.random() < likelihood_of_spreading_rumor: 
                            first_student_successfully_spread_rumor = True
                            students[first_student_to_attempt].append_students_spread_rumor_to(students[second_student_to_attempt].get_id())
                            students[second_student_to_attempt].increment_times_heard_rumor()
                            print("Spread from " + repr(students[first_student_to_attempt]) + " to " + repr(students[second_student_to_attempt]))

                    # If first student's attempt at spreading rumor failed, then second student tries to spread rumor
                    if not first_student_successfully_spread_rumor:
                        # Make sure that this student can logically spread rumor to other student
                        if students[second_student_to_attempt].can_spread_rumor(students[first_student_to_attempt].get_id(), students[first_student_to_attempt].get_students_spread_to()):
                            # Check if randomly generated float is less than likelihood of spreading rumor. If so, spread rumor
                            # If true, spread rumor to student who has not heard rumor
                            if random.random() < likelihood_of_spreading_rumor: 
                                first_student_successfully_spread_rumor = True
                                students[second_student_to_attempt].append_students_spread_rumor_to(students[first_student_to_attempt].get_id())
                                students[first_student_to_attempt].increment_times_heard_rumor()
                                print("Spread from " + repr(students[second_student_to_attempt]) + " to " + repr(students[first_student_to_attempt]))



    for s in students:
        print(s)



run_rumor_simulation(likelihood_of_spreading_rumor=0.5, number_of_students=10, minutes_to_run=5)
