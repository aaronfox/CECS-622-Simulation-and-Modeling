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
def part_2():
    arrival_times = [12, 31, 63, 95, 99, 154, 198, 221, 304, 346, 411, 455, 537]
    service_times = [40, 32, 55, 48, 18, 50, 47, 18, 28, 54, 40, 72, 12]
    system_departure_times = []
    # The response time is the total amount of time a customer spends in both the queue and in service.
    system_response_times = []
    
    time = 0


if __name__ == "__main__":
    # Uncomment for Part 1a
    # part_1_a()
    # Uncomment for Part 1b
    # part_1_b()
    # Uncomment for Part 2
    part_2()
