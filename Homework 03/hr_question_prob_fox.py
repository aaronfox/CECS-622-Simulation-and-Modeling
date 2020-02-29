# Aaron Fox
# CECS 622-01
# Dr. Elmaghraby
# Assignment 3 Problem 3

import random # For randomly selecting choices from answers and randomly selecting where answer is

# get_answers_correct_percent gets the percentage of questions the candidate answered correctly
# INPUT:
# num_questions (int): determines the number of questions on each test (set to 20 by default in the prompt)
# num_multiple_choice (int): determines the number of choices(set to 5 by default in the prompt)
# last_answer_always_correct (bool): determines if the simulation should have the final choice always be correct or if the correct answer should be randomly placed among the choices
# iterations_to_run (int): determines the number of iterations to be run so that larger patterns of the probabilities could be revealed(e.g. the average of 50 iterations could be more telling than just running one iteration of the test which could be inherently skewed.)
# OUTPUT:
# answer_correct_percentages (list): list of the probabilities of choosing a correct answer (e.g. [0.21, 0.19])
def get_answers_correct_percent(num_questions, num_multiple_choice, last_answer_always_correct, iterations_to_run):
    num_correct_choices = 0

    answer_correct_percentages = []
    for i in range(iterations_to_run):
        num_correct_choices = 0
        if last_answer_always_correct:
            # Create ordered list of choices
            choices = []
            # First append all incorrect choices (False) to be first num_multiple_choice - 1 answer
            for i in range(num_multiple_choice - 1):
                choices.append(False)

            # Append correct answer (True) to be last choice
            choices.append(True)

            # Weights should be 1 for every choice for equal weighting
            weights = [1] * len(choices)

            # Run simulation by randomly choosing from one of the choices equally
            for i in range(num_questions):
                candidate_answer = (random.choices(choices, weights))[0]
                if candidate_answer == True:
                    num_correct_choices = num_correct_choices + 1

            answer_correct_percentages.append(num_correct_choices / num_questions)
        else:   # Otherwise, place correct answer randomly in list by shuffling around choices
            # Create ordered list of choices
            choices = []
            # First append all incorrect choices (False) to be first num_multiple_choice - 1 answer
            for i in range(num_multiple_choice - 1):
                choices.append(False)

            # Append correct answer (True) to be last choice
            choices.append(True)

            # Shuffle choices list so that correct answer is uniformly randomly inside list
            random.shuffle(choices)

            # Weights should be 1 for every choice for equal weighting
            weights = [1] * len(choices)

            # Run simulation by randomly choosing from one of the choices equally
            for i in range(num_questions):
                # Randomly and uniformly shuffle choices list each time
                random.shuffle(choices)

                candidate_answer = (random.choices(choices, weights))[0]
                if candidate_answer == True:
                    num_correct_choices = num_correct_choices + 1

            answer_correct_percentages.append(num_correct_choices / num_questions)
    return answer_correct_percentages

def average(nums):
    return sum(nums) / len(nums)

if __name__ == "__main__":
    print("Running HR Interview Question Probability Simulator...")

    # Test overall iterations
    average_of_averages_case_a = []
    average_of_averages_case_b = []
    number_of_averages_to_average = 100
    a_average_higher = 0
    for i in range(number_of_averages_to_average):
        # Case a: last answer is always correct
        last_answer_always_correct = True
        iterations_to_run = 100
        num_questions = 20
        a_results = get_answers_correct_percent(num_questions=num_questions, num_multiple_choice=5, last_answer_always_correct=last_answer_always_correct, iterations_to_run=iterations_to_run)
        # print("a_results == " + str(a_results))
        print("Average probability of correct answers for Case A in " + str(iterations_to_run) + " iterations: " + "{:07.5f}".format((average(a_results))))
        average_of_averages_case_a.append(average(a_results))

        # Case b: correct answer is randomly chosen
        last_answer_always_correct = False
        iterations_to_run = 100
        num_questions = 20
        b_results = get_answers_correct_percent(num_questions=num_questions, num_multiple_choice=5, last_answer_always_correct=last_answer_always_correct, iterations_to_run=iterations_to_run)
        # print("b_results == " + str(b_results))
        print("Average probability of correct answers for Case B in " +
              str(iterations_to_run) + " iterations: " + "{:07.5f}".format((average(b_results))))
        average_of_averages_case_b.append(average(b_results))

        if average(a_results) > average(b_results):
            a_average_higher = a_average_higher + 1

    print("average_of_averages_case_a == " + str(average(average_of_averages_case_a)))
    print("average_of_averages_case_b == " + str(average(average_of_averages_case_b)))
    print("a_average_higher == " + str(a_average_higher))

