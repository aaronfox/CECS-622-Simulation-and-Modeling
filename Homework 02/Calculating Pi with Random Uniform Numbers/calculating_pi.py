# Aaron Fox
# CECS 622-01
# Dr. Adel Elmaghraby

import sys # For exiting program properly
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout # for GUI
from PyQt5.QtCore import Qt  # To enable maximizing of the GUI

# Use Matplotlib for the embedded graphing display of the dots inside the circle/square
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.patches as patches  # For bounding square

import random # For its random.uniform function
import math # For using square root to find distance points are from circle center

# All of the gui is based out of this Window class using Python PyQt5 GUI framework
class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # Allow for easy maximizing of the GUI
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

        # For keeping track of points that fall inside circle
        self.number_of_points_within_cirle = 0
        # For keeping track of poitns that fall outside the circle
        self.number_of_points_outside_cirle = 0

        # Figure instance for plotting
        self.figure = plt.figure()

        # self.canvas is the widget that displays the figure,
        # taking the figure instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # Adds toolbar to top of GUI for saving pictures, zooming in graph, etc.
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Add input box for user to request N uniform numbers
        self.random_number_input = QLineEdit()
        self.random_number_input_label = QLabel()
        self.random_number_input_label.setText(
            "Enter N random uniform numbers to generate: ")

        # Button connected to generation of points on figure to visually
        # display the uniform random distribution of points inside/outside the circle
        self.button = QPushButton('Generate')
        self.button.clicked.connect(self.generate)

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
        horizontal_layout.addWidget(self.random_number_input_label)
        horizontal_layout.addWidget(self.random_number_input)
        layout.addLayout(horizontal_layout)

        # Add Generate button to layout
        layout.addWidget(self.button)

        self.setLayout(layout)

        # Create initial empty plot for aesthetic purposes
        self.initial_plot()

    # Initial plot to make the GUI look initially pretty for aesthetic purposes
    def initial_plot(self):
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)
        plt.gca().set_aspect('equal', adjustable='box')

        # Create a circle patch
        circle = patches.Circle(xy=(.5, .5), radius=.5,
                                linewidth=1, edgecolor='r', facecolor='none')

        # Add the patch to the Axes
        ax.add_patch(circle)

        # refresh canvas
        self.canvas.draw()

    # Generates and displays the circle, graph, and the uniform random points on the graph 
    def generate(self):
        # Clear the figure in case stuff is on it already
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)

        # Make the aspect ratio equal and adjustable so that the circle looks like a proper circle
        plt.gca().set_aspect('equal', adjustable='box')

        # Create a circle
        circle = patches.Circle(xy=(.5, .5), radius=.5,
                                linewidth=1, edgecolor='r', facecolor='none')

        # Add the patch to the Axes
        ax.add_patch(circle)

        # Get input N (amount of numbers to generate) from input
        # Make sure the input is a number and is not 0 (to prevent divide by 0 error)
        if self.random_number_input.text().isnumeric() and int(self.random_number_input.text()) != 0:
            N = int(self.random_number_input.text())

            # Generate N random numbers
            uniform_numbers = self.generate_uniform_numbers(N)

            ### Plot all uniform number pairs ###
            # Create lists of each x and y pair to plot them on a scatter plot
            uniform_number_x = []
            uniform_number_y = []

            # Keep track of the number of points inside circle
            number_points_inside = 0
            for i in range(len(uniform_numbers)):
                uniform_number_x.append(uniform_numbers[i][0])
                uniform_number_y.append(uniform_numbers[i][1])
                # If the distance of the point from the circle is less than or equal to 0.5, 
                # then that point falls within the circle
                # Accoount for the fact that the center of the circle is at (0.5, 0.5), so distance
                # formula for distance from center is sqrt((x - 0.5)^2 + (y - 0.5)^2)
                if math.sqrt((uniform_numbers[i][0] - 0.5)** 2 + (uniform_numbers[i][1] - 0.5) ** 2) <= 0.5:
                    number_points_inside = number_points_inside + 1

            print("number_points_inside == " + str(number_points_inside))
            print("total_points == " + str(len(uniform_numbers)))

            # Plot all points found in uniform numbers
            plt.scatter(uniform_number_x, uniform_number_y)

            # Estimated value
            # Multiply by four based on dividing area of circle (pi/4) by area of square (1), which
            # means the estimated value should be around pi/4 / 1 = pi/4. Thus, multiplying result by
            # 4 means that it should yield an estimated value of pi
            estimated_value = 4 * (number_points_inside / len(uniform_numbers))
            # Update estimated pi value label
            self.pi_estimate_text.setText("Estimated value of pi: " + str(estimated_value))

            # refresh canvas
            self.canvas.draw()
        else:
            print("Input does not contain a valid number")

    # Generates N uniform random numbers 
    def generate_uniform_numbers(self, N):
        uniform_numbers = []
        for i in range(0, N):
            uniform_numbers.append(
                [random.uniform(0, 1), random.uniform(0, 1)])
        return uniform_numbers


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
