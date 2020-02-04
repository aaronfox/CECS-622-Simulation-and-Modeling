# Aaron Fox
# CECS 622-01
# Dr. Adel Elmaghraby
# Assignment 2 - Problem 2

import sys  # For exiting program properly
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout  # for GUI
from PyQt5.QtCore import Qt  # To enable maximizing of the GUI

# Use Matplotlib for the embedded graphing display of the dots inside the circle/square
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.patches as patches  # For bounding square

import random  # For its random.uniform function
import math  # For using square root to find distance points are from circle center
import numpy as np  # For the use of a Gaussian distribution of the customer purchases

# All of the gui is based out of this Window class using Python PyQt5 GUI framework
class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # Allow for easy maximizing of the GUI
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

        # Current day of simulation
        self.current_day = 0

        # Figure instance for plotting
        self.figure = plt.figure()

        # self.canvas is the widget that displays the figure,
        # taking the figure instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # Adds toolbar to top of GUI for saving pictures, zooming in graph, etc.
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Add input boxes for user to input values
        # Q1 and Q2 represent initial inventory quantities
        self.Q1 = QLineEdit()
        self.Q1.setText("1000")
        self.Q1_label = QLabel()
        self.Q1_label.setText("Enter value for Q1: ")

        # Q2 Input and Label
        self.Q2 = QLineEdit()
        self.Q2.setText("1200")
        self.Q2_label = QLabel()
        self.Q2_label.setText("Q2: ")

        # P1 and P2 are the amounts being deducted from Q1 and Q2 respectively
        # every 1 to 4 days. NOTE: P1 << Q1 and P2 << Q2
        # P1 Input and Label
        self.P1 = QLineEdit()
        self.P1.setText("105")
        self.P1_label = QLabel()
        self.P1_label.setText("P1: ")

        # P2 Input and Label
        self.P2 = QLineEdit()
        self.P2.setText("95")
        self.P2_label = QLabel()
        self.P2_label.setText("P2: ")

        # Button connected to generation of points on figure to visually
        # display the uniform random distribution of points inside/outside the circle
        self.button = QPushButton('Run Simulation')
        self.button.clicked.connect(self.run_simulation)

        # set the layout (vertical)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        # For evaluating data in bar chart
        self.day_to_evaluate_value = QLineEdit()
        self.day_to_evaluate_value.setText("1")
        self.day_to_evaluate_label = QLabel()
        self.day_to_evaluate_label.setText("Enter Day to Evaluate: ")

        self.go_to_day_button = QPushButton("Go to Day")
        self.go_to_day_button.clicked.connect(self.go_to_day_button_clicked)

        self.next_day_button = QPushButton("Next Day")
        self.next_day_button.clicked.connect(self.next_day_clicked)

        self.prev_day_button = QPushButton("Prev Day")
        self.prev_day_button.clicked.connect(self.prev_day_clicked)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout1.addWidget(self.day_to_evaluate_label)
        horizontal_layout1.addWidget(self.day_to_evaluate_value)
        horizontal_layout1.addWidget(self.go_to_day_button)
        horizontal_layout1.addWidget(self.prev_day_button)
        horizontal_layout1.addWidget(self.next_day_button)
        layout.addLayout(horizontal_layout1)

        # END bar chart GUI manipulation buttons

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.Q1_label)
        horizontal_layout.addWidget(self.Q1)
        horizontal_layout.addWidget(self.Q2_label)
        horizontal_layout.addWidget(self.Q2)
        horizontal_layout.addWidget(self.P1_label)
        horizontal_layout.addWidget(self.P1)
        horizontal_layout.addWidget(self.P2_label)
        horizontal_layout.addWidget(self.P2)
        layout.addLayout(horizontal_layout)

        # Add Generate button to layout
        layout.addWidget(self.button)

        self.setLayout(layout)

        # Keep track of values of Q1 and Q2 inventories here
        self.Q1_inventory = int(self.Q1.text())
        self.Q2_inventory = int(self.Q2.text())
        self.P1_request = int(self.P1.text())
        self.P2_request = int(self.P2.text())

        # random.randint generate uniform distribution of integers between 1 and 4, inclusive of both
        self.P1_purchase_request_wait_time = random.randint(1, 4)
        self.P2_purchase_request_wait_time = random.randint(1, 4)

        # Place all simulation results here
        self.simulation_inventory_results = []

        # Create initial empty bar plot for aesthetic purposes
        self.initial_plot()

        # Second Figure for line plot
        # Figure instance for plotting
        self.figure2 = plt.figure()

        # self.canvas is the widget that displays the figure,
        # taking the figure instance as a parameter to __init__
        self.canvas2 = FigureCanvas(self.figure2)
        layout.addWidget(self.canvas2)
        self.lineplot_init()
        # self.next_day_clicked()
        # self.next_day_clicked()

    # Go to day as specified by user
    def go_to_day_button_clicked(self):
        if not self.simulation_inventory_results:
            return
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)

        self.current_day = int(self.day_to_evaluate_value.text())
        # self.day_to_evaluate_value.setText(str(self.current_day))

        labels = ['Q1', 'Q2']
        label_locs = [1, 2]
        width = .40
        ax.bar(label_locs, [self.simulation_inventory_results[self.current_day][0],
                            self.simulation_inventory_results[self.current_day][1]], width, label='Q1')

        # print('test')
        # Set Graph labels, title, x-axis
        ax.set_ylabel('Inventory Available')
        ax.set_title('Inventory for Store')
        ax.set_xticks(label_locs)
        ax.set_xticklabels(labels)

        # refresh canvas
        self.canvas.draw()

    # Plot next day on bar graph
    def next_day_clicked(self):
        # Make sure that there are simulation results to graph
        if not self.simulation_inventory_results:
            return
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)

        self.current_day = self.current_day + 1
        self.day_to_evaluate_value.setText(str(self.current_day))

        labels = ['Q1', 'Q2']
        label_locs = [1, 2]
        width = .40
        ax.bar(label_locs, [self.simulation_inventory_results[self.current_day][0], self.simulation_inventory_results[self.current_day][1]], width, label='Q1')

        # Set Graph labels, title, x-axis
        ax.set_ylabel('Inventory Available')
        ax.set_title('Inventory for Store')
        ax.set_xticks(label_locs)
        ax.set_xticklabels(labels)

        # refresh canvas
        self.canvas.draw()

     # Plot previous day on bar graph
    def prev_day_clicked(self):
        # Ensure there are results to graph
        if not self.simulation_inventory_results:
            return
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)

        self.current_day = self.current_day - 1
        self.day_to_evaluate_value.setText(str(self.current_day))

        labels = ['Q1', 'Q2']
        label_locs = [1, 2]
        width = .40
        ax.bar(label_locs, [self.simulation_inventory_results[self.current_day][0],
                            self.simulation_inventory_results[self.current_day][1]], width, label='Q1')

        # Set Graph labels, title, x-axis
        ax.set_ylabel('Inventory Available')
        ax.set_title('Inventory for Store')
        ax.set_xticks(label_locs)
        ax.set_xticklabels(labels)

        # refresh canvas
        self.canvas.draw()

    # Initial Line plot to make GUI look initially pretty for aesthetic purpises
    def lineplot_init(self):
        self.figure2.clear()
        # create an axis
        ax=self.figure2.add_subplot(1, 1, 1)

        # Set Graph labels, title, x-axis
        ax.set_ylabel('Inventory Available')
        ax.set_xlabel('Day')
        ax.set_title('Inventory for Store')
        self.canvas2.draw()


    # Plot the line graph illustrating changes in each inventory
    def plot_line_graph(self):
        self.figure2.clear()
        # create an axis
        ax=self.figure2.add_subplot(1, 1, 1)

        # Set Graph labels, title, x-axis
        ax.set_ylabel('Inventory Available')
        ax.set_xlabel('Day')
        ax.set_title('Inventory for Store')

        Q1_nums=[]
        Q2_nums=[]
        for i in range(len(self.simulation_inventory_results)):
            Q1_nums.append(self.simulation_inventory_results[i][0])
            Q2_nums.append(self.simulation_inventory_results[i][1])

        ax.plot(range(len(Q1_nums)), Q1_nums, label='Q1 Inventory')
        ax.plot(range(len(Q2_nums)), Q2_nums, label='Q2 Inventory')
        ax.legend()

        # refresh canvas
        self.canvas2.draw()


    # Initial plot to make the GUI look initially pretty for aesthetic purposes
    def initial_plot(self):
        self.figure.clear()

        # create an axis
        ax=self.figure.add_subplot(1, 1, 1)
        # plt.gca().set_aspect('equal', adjustable='box')

        labels=['Q1', 'Q2']
        label_locs=[1, 2]
        width=.40
        ax.bar(label_locs, [self.Q1_inventory,
               self.Q2_inventory], width, label='Q1')

        # Set Graph labels, title, x-axis
        ax.set_ylabel('Inventory Available')
        ax.set_title('Inventory for Store')
        ax.set_xticks(label_locs)
        ax.set_xticklabels(labels)

        # refresh canvas
        self.canvas.draw()

    # Runs simulation to on inventories based on input purchase request and inventory quantity amounts
    def run_simulation(self):

        # START Run all of simulation in this block
        # Create array of days up to 50 and then display results
        # Initial inventory
        Q1_inventory_remaining=self.Q1_inventory
        Q2_inventory_remaining=self.Q2_inventory
        number_of_days_to_run_simulation=50

        # Create list of inventory for every day
        inventories=[[Q1_inventory_remaining, Q2_inventory_remaining]]
        # Run simulation for the input number of dats to run the simulation
        for i in range(number_of_days_to_run_simulation):
            if self.P1_purchase_request_wait_time == 0:
                Q1_inventory_remaining=Q1_inventory_remaining + self.P1_request
                self.P1_purchase_request_wait_time=random.randint(1, 4)
            else:
                self.P1_purchase_request_wait_time=self.P1_purchase_request_wait_time - 1

            if self.P2_purchase_request_wait_time == 0:
                Q2_inventory_remaining=Q2_inventory_remaining + self.P2_request
                self.P2_purchase_request_wait_time=random.randint(1, 4)
            else:
                self.P2_purchase_request_wait_time=self.P2_purchase_request_wait_time - 1

            # Every day, have customers purchase a certain amount of inventory from business
            # Assume customers can purchase up
            # Mean value of days of inventory bought of the original stock value
            mean_days_of_stock_purchased_by_customers=90
            # mean and standard deviation, respectively
            mu, sigma=self.Q1_inventory/mean_days_of_stock_purchased_by_customers, 100.5
            distribution_set=np.random.normal(mu, sigma, 1000)

            # Ensure randomly chosen number is not negative (very unlikely given the
            # Gaussian distribution, but still possible)
            i=0
            normal_random_q1=distribution_set[i]
            while normal_random_q1 < 1:
                i=i + 1
                normal_random_q1=distribution_set[i]

            # Ensure independency of values of Q1 and Q2 by making sure they use two separate distributions

            # Mean value of days of inventory bought of the original stock value
            mean_days_of_stock_purchased_by_customers_q2=90
            # mean and standard deviation, respectively
            mu, sigma=self.Q2_inventory/mean_days_of_stock_purchased_by_customers_q2, 100.5
            distribution_set_q2=np.random.normal(mu, sigma, 1000)

            i=0
            normal_random_q2=distribution_set_q2[i]
            while normal_random_q2 < 1:
                i=i + 1
                normal_random_q2=distribution_set_q2[i]

            # Decrement respective amounts of stock according to these two independent Gaussian distribution selections
            Q1_inventory_remaining=Q1_inventory_remaining - \
                math.ceil(normal_random_q1)
            Q2_inventory_remaining=Q2_inventory_remaining - \
                math.ceil(normal_random_q2)

            # Ensure quantities do not go into the negatives
            if Q1_inventory_remaining < 0:
                Q1_inventory_remaining=0

            if Q2_inventory_remaining < 0:
                Q2_inventory_remaining=0

            inventories.append(
                [Q1_inventory_remaining, Q2_inventory_remaining])
        # END Run of all simulation
        self.simulation_inventory_results=inventories
        print(self.simulation_inventory_results)
        self.plot_line_graph()

        # Clear the figure in case stuff is on it already
        self.figure.clear()

        # create an axis
        ax=self.figure.add_subplot(1, 1, 1)

        # Get input N (amount of numbers to generate) from input
        # Make sure the input is a number and is not 0 (to prevent divide by 0 error)
        if (self.Q1.text().isnumeric() and int(self.Q1.text()) != 0
            and self.Q2.text().isnumeric() and int(self.Q2.text()) != 0
            and self.P1.text().isnumeric() and int(self.P1.text()) != 0
            and self.P2.text().isnumeric() and int(self.P2.text()) != 0):
            self.Q1_inventory=int(self.Q1.text())
            self.Q2_inventory=int(self.Q2.text())
            self.P1_request=int(self.P1.text())
            self.P2_request=int(self.P2.text())

            # Prep basics of bar graph
            labels=['Q1', 'Q2']
            label_locs=[1, 2]
            width=.40
            ax.bar(label_locs, [self.Q1_inventory,
                                self.Q2_inventory], width, label='Q1')

            # Set Graph labels, title, x-axis
            ax.set_ylabel('Inventory Available')
            ax.set_title('Inventory for Store')
            ax.set_xticks(label_locs)
            ax.set_xticklabels(labels)


            # refresh canvas
            self.canvas.draw()
        else:
            print("Inputs do not contain a valid number")

if __name__ == '__main__':
    app=QApplication(sys.argv)

    main=Window()
    main.show()

    sys.exit(app.exec_())
