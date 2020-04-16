# Aaron Fox
# CECS 622-01
# Dr. Elmaghraby
# Homework 4

# For plotting
import matplotlib.pyplot as plt

### Part 1: Chi-Squared Test ###

def part_1_a():
    ## Compute the histogram over the 10 subintervals: [0, 0.1), [0.1, 0.2) … [0.9, 1.0). ##
    random_numbers = [0.21, 0.88, 0.37, 0.06, 0.98, 0.61, 0.89, 0.28, 0.70, 0.94, 0.46, 0.92, 0.34, 0.08, 0.79, 0.82, 0.36, 0.62, 0.27, 0.10]
    bins_list = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    n, bins, patches = plt.hist(random_numbers, bins=bins_list, facecolor='blue', alpha=0.5)
    plt.title("Histogram of 20 Randomly Generated Numbers in Excel")
    plt.xticks(ticks=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    plt.xlabel("Bin Range")
    plt.ylabel("Count")
    plt.show()

    ## Perform the Chi-square Goodness-of-fit test with alpha = 0.05 ##
    # Null hypothesis is that the data is consistent with a random uniform distribution (e.g. every bin should have a 10% likelihood)
    # Bin:           |   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |   9  |  10  |
    # Expected %:    |  10  |  10  |  10  |  10  |  10  |  10  |  10  |  10  |  10  |  10  |
    # Observed Count:|   2  |   1  |   3  |   3  |   1  |   0  |   2  |   2  |   3  |   3  |
    # Expected Count:|   2  |   2  |   2  |   2  |   2  |   2  |   2  |   2  |   2  |   2  |
    # With alpha = 0.05
    expected_counts = [2] * 10
    observed_counts = [2, 1, 3, 3, 1, 0, 2, 2, 3, 3]

    chi_squared_stat = 0.0
    for i in range(len(observed_counts)):
        expected_count = expected_counts[i]
        observed_count = observed_counts[i]
        chi_squared_stat = chi_squared_stat + ((observed_count - expected_count) ** 2) / expected_count

    print("For this random sampling in Excel , chi-squared statistic == " + str(chi_squared_stat))

    # With N Categories - 1 = 9 degrees of freedom and alpha = 0.05,
    # using chart found in the Appendix,
    # the probability of exceeding the critical value is 16.919
    # Since chi-squared value = 5.0 < 16.919, we can ACCEPT the
    # null hypothesis that the generated data follows
    # the uniform distribution specified by Excel. We can therefore reject
    # the alternate hypothesis that the generated data in Excel does not follow
    # the random uniform distribution specified by Excel.


def part_1_b():
    ## Part b:  Compare the grades using Chi-squared test to decide whether the overall
    ## distributions are statistically different or not. ##

    # Data:
    # Grade:    |  A  |  B  |  C  |  D  |  F  | Total |
    # This Year:| 20  | 22  | 13  | 13  |  2  |  70   |
    # Last Year:| 10  | 19  | 25  |  4  |  1  |  59   |
    # Totals:   | 30  | 41  | 38  | 17  |  3  | 129   |

    # Example calculation for This Year of A:
    # 20/70 * 100 = 28.571...
    # Data as a Percentage:
    # Grade:    |   A    |   B    |   C    |   D    |   F    |  Total  |
    # This Year:| 28.571 | 31.429 | 18.571 | 18.571 |  2.857 |  100.0  |
    # Last Year:| 16.949 | 32.203 | 42.373 |  6.780 |  1.695 |  100.0  |
    # Totals:   | 23.256 | 31.783 | 29.457 | 13.178 |  2.326 |  100.0  |

    # Example calculation for this year of A
    # 0.23256 * 70 = 16.279 (percentage of total for both distributions of category * total for year)
    # Example calculation for this year of A
    # 0.23256 * 59 = 13.721
    # Expected Counts:
    # Grade:    |   A    |  B     |   C    |   D    |    F   | Total |
    # This Year:| 16.279 | 22.248 | 20.620 |  9.225 |  1.628 |  70   |
    # Last Year:| 13.721 | 18.752 | 17.380 |  7.775 |  1.372 |  59   |
    # Totals:   |   30   |   41   |   38   |   17   |    3   | 129   |
    # With alpha = 0.05
    # Place expected counts into array, starting from left to right of each line starting with This Year
    expected_counts = [16.279, 22.248, 20.620, 9.225, 1.628, 13.721, 18.752, 17.380, 7.775, 1.373]
    observed_counts = [20, 22, 13, 13, 2, 10, 19, 25, 4, 1]
    # Data:
    # Grade:    |  A  |  B  |  C  |  D  |  F  | Total |
    # This Year:| 20  | 22  | 13  | 13  |  2  |  70   |
    # Last Year:| 10  | 19  | 25  |  4  |  1  |  59   |
    # Totals:   | 30  | 41  | 38  | 17  |  3  | 129   |

    chi_squared_stat = 0.0
    for i in range(len(observed_counts)):
        expected_count = expected_counts[i]
        observed_count = observed_counts[i]
        chi_squared_stat = chi_squared_stat + ((observed_count - expected_count) ** 2) / expected_count

    print("Part 1.b: For this random sampling of grades, chi-squared statistic == " + str(chi_squared_stat))

    # With N Categories - 1 = 4 degrees of freedom and a
    # chi-squared test statistic value = 11.586, we can determine that 
    # the p-value of the probability is 0.05 using the calculator for P-value found at
    # https://stattrek.com/online-calculator/chi-square.aspx. Since a p-value less
    # than or equal to 0.05 is statistically significant, it shows that there is strong
    # evidence AGAINST the null hypothesis, indicating that there is less than a 5% chance that null
    # hypothesis is correct. As such, we can REJECT the
    # null hypothesis that the overall distributions of this year and last year follow 
    # the same distribution and are not statistically different. We can therefore ACCEPT
    # the alternate hypothesis that the overall distributions of this year and last year
    # do not follow the same distribution and are statistically different.

### Part 2: Queue Analysis ###
## Parts a and b ##
def part_2__a_and_b():
    arrival_times = [12, 31, 63, 95, 99, 154, 198, 221, 304, 346, 411, 455, 537]
    service_times = [40, 32, 55, 48, 18, 50, 47, 18, 28, 54, 40, 72, 12]
    # arrival_times = [2, 4, 7]
    # service_times = [3, 1, 4]
    # arrival_times = [0, 2, 3]
    # service_times = [2, 1, 3]
    # The departure times are the time in which the customer is completely serviced
    system_departure_times = []
    # The response time is the total amount of time a customer spends in both the queue and in service.
    system_response_times = []
    
    time = 0
    customers_serviced = 0
    customers_arrived = 0
    queue = []
    wasted_minutes = 0
    customer_just_arrived = False  # customer_just_arrived ensure that a customer isn't serviced in the same minute they arrive
    while customers_serviced != len(arrival_times):
        # Check if new arrival of customer should be added to queue
        # print("Time == " + str(time))
        if customers_arrived != len(arrival_times) and time == arrival_times[customers_arrived]:
            # print("Appending to queue at t = " + str(time))
            queue.append(service_times[customers_arrived])
            customer_just_arrived = True
            customers_arrived = customers_arrived + 1
        elif customer_just_arrived:
            customer_just_arrived = False

        if len(queue) >= 1 and not (len(queue) == 1 and customer_just_arrived):
            queue[0] = queue[0] - 1

            # Check if first customer in queue is finished servicing
            if queue[0] == 0:
                # print("Popping customer from queue at t = " + str(time))
                # Delete fully serviced customer from queue since it's done being serviced
                del queue[0]
                # Add data of customer to respective system response and departure times
                system_departure_times.append(time)
                system_response_times.append(time - arrival_times[customers_serviced])
                customers_serviced = customers_serviced + 1
        elif not (len(queue) == 1 and customer_just_arrived):
            print("wasted minute at t = " + str(time))
            wasted_minutes = wasted_minutes + 1
        time = time + 1


    print("System Response Times: " + str(system_response_times))
    print("System Departure Times: " + str(system_departure_times))
    print("Wasted minutes: " + str(wasted_minutes))
    
    # Last system departure time is the overall minutes used
    total_time = system_departure_times[-1]
    print("Percent Server Utilization: " + str((total_time - wasted_minutes) / total_time * 100) + "%")

## Part c ##
def part_2_c():
    arrival_times = [12, 31, 63, 95, 99, 154,
                     198, 221, 304, 346, 411, 455, 537]
    service_times = [40, 32, 55, 48, 18, 50, 47, 18, 28, 54, 40, 72, 12]
    service_times = [[0, 40], [1, 32], [2, 55], [3, 48], [4, 18], [5, 50], [6, 47], [7, 18], [8, 28], [9, 54], [10, 40], [11, 72], [12, 12]]
    # arrival_times = [2, 4, 7]
    # service_times = [3, 1, 4]
    # arrival_times = [0, 2, 3]
    # service_times = [2, 1, 3]
    # arrival_times = [2, 3, 5, 6]
    # service_times = [[0, 3], [1, 5], [2, 5], [3, 2]]
    # The departure times are the time in which the customer is completely serviced
    system_departure_times = [0] * len(arrival_times)
    # The response time is the total amount of time a customer spends in both the queue and in service.
    system_response_times = [0] * len(arrival_times)

    time = 0
    customers_serviced = 0
    customers_arrived = 0
    queue = []
    wasted_minutes = 0
    # customer_just_arrived ensure that a customer isn't serviced in the same minute they arrive
    customer_just_arrived = False
    while customers_serviced != len(arrival_times):
        # Check if new arrival of customer should be added to queue
        if customers_arrived != len(arrival_times) and time == arrival_times[customers_arrived]:
            queue.append(service_times[customers_arrived])
            customer_just_arrived = True
            customers_arrived = customers_arrived + 1
        elif customer_just_arrived:
            customer_just_arrived = False

        # Case 1: Nobody is in queue
        if len(queue) == 0:
            wasted_minutes = wasted_minutes + 2 # + 2 since both servers are wasting minutes

        # Case 2: length of queue is 1
        if len(queue) == 1 and not customer_just_arrived:
            queue[0][1] = queue[0][1] - 1
            # If only one customer, then one server is not being used
            wasted_minutes = wasted_minutes + 1
        elif len(queue) == 1 and customer_just_arrived:  # Otherwise, customer just arrived
            wasted_minutes = wasted_minutes + 1

        # Case 3: Queue length = 2 (No wasted minutes when 2+ in queue)
        if len(queue) == 2:
            # if customer just arrived, only count first person in queue
            if customer_just_arrived:
                queue[0][1] = queue[0][1] - 1
            else:
                queue[0][1] = queue[0][1] - 1
                queue[1][1] = queue[1][1] - 1

        # Case 4: Queue length > 2 (no wasted minutes and don't need to check for customer just arriving)
        if len(queue) > 2:
            queue[0][1] = queue[0][1] - 1
            queue[1][1] = queue[1][1] - 1

        if len(queue) == 1:
            # Check if queue spot 0 is serviced
            if queue[0][1] == 0:
                print("Popping customer from queue at t = " + str(time))
                # Delete fully serviced customer from queue since it's done being serviced
                # Add data of customer to respective system response and departure times
                system_departure_times[queue[0][0]] = time
                system_response_times[queue[0][0]] = time - arrival_times[queue[0][0]]
                customers_serviced = customers_serviced + 1
                del queue[0]
        elif len(queue) >= 2:
            # Check if either queue spot 0 or 1 are serviced
            if queue[0][1] == 0 and queue[1][1] == 0:
                print("Popping customer from queue at t = " + str(time))
                # Delete fully serviced customer from queue since it's done being serviced
                # Add data of customer to respective system response and departure times
                system_departure_times[queue[0][0]] = time
                system_response_times[queue[0][0]] = time - arrival_times[queue[0][0]]
                customers_serviced = customers_serviced + 1
                del queue[0]

                ## Repeat for next finished item in queue
                print("Popping another customer from queue at t = " + str(time))
                # Add data of customer to respective system response and departure times
                system_departure_times[queue[0][0]] = time
                system_response_times[queue[0][0]] = time - arrival_times[queue[0][0]]
                customers_serviced = customers_serviced + 1
                del queue[0]
            elif queue[0][1] == 0 and queue[1][1] != 0:
                print("Popping customer from queue at t = " + str(time))
                # Delete fully serviced customer from queue since it's done being serviced
                # Add data of customer to respective system response and departure times
                system_departure_times[queue[0][0]] = time
                system_response_times[queue[0][0]] = time - arrival_times[queue[0][0]]
                customers_serviced = customers_serviced + 1
                del queue[0]

            elif queue[0][1] != 0 and queue[1][1] == 0:
                print("Popping customer from queue at t = " + str(time))
                # Delete fully serviced customer from queue since it's done being serviced
                # Add data of customer to respective system response and departure times
                system_departure_times[queue[1][0]] = time
                system_response_times[queue[1][0]] = time - arrival_times[queue[1][0]]
                customers_serviced = customers_serviced + 1
                del queue[1]

        time = time + 1


    print("System Response Times: " + str(system_response_times))
    print("System Departure Times: " + str(system_departure_times))
    print("Wasted minutes: " + str(wasted_minutes))

    # Last system departure time is the overall minutes used
    total_time = max(system_departure_times) * 2
    print("Percent Server Utilization: " + str((total_time - wasted_minutes) / total_time * 100) + "%")

if __name__ == "__main__":
    # Uncomment for Part 1a
    # part_1_a()
    # Uncomment for Part 1b
    # part_1_b()
    # Uncomment for Part 2a and 2b
    # part_2__a_and_b()
    # Uncomment for Part 2c
    part_2_c()
