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

# All of the gui is based out of this Window class using Python PyQt5 GUI framework
class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # Allow for easy maximizing of the GUI
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

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
        self.Q2.setText("1000")
        self.Q2_label = QLabel()
        self.Q2_label.setText("Q2: ")

        # P1 and P2 are the amounts being deducted from Q1 and Q2 respectively
        # every 1 to 4 days. NOTE: P1 << Q1 and P2 << Q2
        # P1 Input and Label
        self.P1 = QLineEdit()
        self.P1.setText("15")
        self.P1_label = QLabel()
        self.P1_label.setText("P1: ")

        # P2 Input and Label
        self.P2 = QLineEdit()
        self.P2.setText("10")
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

        # Estimate of pi value
        self.pi_estimate_text = QLabel()
        self.pi_estimate_text.setText("Estimated value of pi: ")
        layout.addWidget(self.pi_estimate_text)

        # Number of N numbers to generate input
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

        # Current day of simulation
        self.current_day = 0

        # Create initial empty plot for aesthetic purposes
        self.initial_plot()

    # Initial plot to make the GUI look initially pretty for aesthetic purposes
    def initial_plot(self):
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)
        # plt.gca().set_aspect('equal', adjustable='box')

        labels = ['Q1', 'Q2']
        label_locs = [1, 2]
        width = .40
        ax.bar(label_locs, [self.Q1_inventory, self.Q2_inventory], width, label='Q1')

        # Set Graph labels, title, x-axis
        ax.set_ylabel('Inventory Available')
        ax.set_title('Inventory for Store')
        ax.set_xticks(label_locs)
        ax.set_xticklabels(labels)

        # refresh canvas
        self.canvas.draw()

    # Runs simulation to on inventories based on input purchase request and inventory quantity amounts
    def run_simulation(self):
        # Clear the figure in case stuff is on it already
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)

        # Get input N (amount of numbers to generate) from input
        # Make sure the input is a number and is not 0 (to prevent divide by 0 error)
        if (self.Q1.text().isnumeric() and int(self.Q1.text()) != 0 
            and self.Q2.text().isnumeric() and int(self.Q2.text()) != 0
            and self.P1.text().isnumeric() and int(self.P1.text()) != 0
            and self.P2.text().isnumeric() and int(self.P2.text()) != 0):
            self.Q1_inventory = int(self.Q1.text())
            self.Q2_inventory = int(self.Q2.text())
            self.P1_request = int(self.P1.text())
            self.P2_request = int(self.P2.text())

            # Prep basics of bar graph
            labels = ['Q1', 'Q2']
            label_locs = [1, 2]
            width = .40
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
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
