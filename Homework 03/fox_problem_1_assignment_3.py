# Aaron Fox
# CECS 622-01
# Dr.  Elmaghraby
# Assignment 3 Problem 1
# The "coupled tank" tank problem has a tank with two differential equations
# as follows:
# A_1 * (dh_1/dt) = F_1 - F_2
# A_2 * (dh_2/dt) = F_2 - F_0

import sys

from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout  # for GUI
from PyQt5.QtCore import Qt  # To enable maximizing of the GUI

# Use Matplotlib for the embedded graphing display of the dots inside the circle/square
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

# GUI for visualizing the tank values
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

        # set the layout (vertical)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.go_to_second_button = QPushButton("Go to second")
        self.go_to_second_button.clicked.connect(self.go_to_second_button_clicked)

        self.next_second_button = QPushButton("Next second")
        self.next_second_button.clicked.connect(self.next_second_clicked)

        self.prev_second_button = QPushButton("Prev second")
        self.prev_second_button.clicked.connect(self.prev_second_clicked)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout1.addWidget(self.go_to_second_button)
        horizontal_layout1.addWidget(self.prev_second_button)
        horizontal_layout1.addWidget(self.next_second_button)
        layout.addLayout(horizontal_layout1)

        # Second horizontal layout: All input info for Tank 1
        self.tank_1_area = QLineEdit()
        self.tank_1_area.setText("10")
        self.tank_1_area_label = QLabel()
        self.tank_1_area_label.setText("Tank 1 Area: ")

        self.tank_1_height = QLineEdit()
        self.tank_1_height.setText("1")
        self.tank_1_height_label = QLabel()
        self.tank_1_height_label.setText("Height: ")

        self.tank_1_flow_in = QLineEdit()
        self.tank_1_flow_in.setText("1")
        self.tank_1_flow_in_label = QLabel()
        self.tank_1_flow_in_label.setText("Flow In Rate: ")

        self.tank_1_flow_out = QLineEdit()
        self.tank_1_flow_out.setText("2")
        self.tank_1_flow_out_label = QLabel()
        self.tank_1_flow_out_label.setText("Flow Out Rate: ")

        horizontal_layout2 = QHBoxLayout()
        horizontal_layout2.addWidget(self.tank_1_area_label)
        horizontal_layout2.addWidget(self.tank_1_area)
        horizontal_layout2.addWidget(self.tank_1_height_label)
        horizontal_layout2.addWidget(self.tank_1_height)
        horizontal_layout2.addWidget(self.tank_1_flow_in_label)
        horizontal_layout2.addWidget(self.tank_1_flow_in)
        horizontal_layout2.addWidget(self.tank_1_flow_out_label)
        horizontal_layout2.addWidget(self.tank_1_flow_out)

        layout.addLayout(horizontal_layout2)

        # third horizontal layout: All input info for Tank 1
        self.tank_2_area = QLineEdit()
        self.tank_2_area.setText("20")
        self.tank_2_area_label = QLabel()
        self.tank_2_area_label.setText("Tank 2 Area: ")

        self.tank_2_height = QLineEdit()
        self.tank_2_height.setText("2")
        self.tank_2_height_label = QLabel()
        self.tank_2_height_label.setText("Height: ")

        self.tank_2_flow_in = QLineEdit()
        self.tank_2_flow_in.setText("2")
        self.tank_2_flow_in_label = QLabel()
        self.tank_2_flow_in_label.setText("Flow In Rate: ")

        self.tank_2_flow_out = QLineEdit()
        self.tank_2_flow_out.setText("2")
        self.tank_2_flow_out_label = QLabel()
        self.tank_2_flow_out_label.setText("Flow Out Rate: ")

        horizontal_layout3 = QHBoxLayout()
        horizontal_layout3.addWidget(self.tank_2_area_label)
        horizontal_layout3.addWidget(self.tank_2_area)
        horizontal_layout3.addWidget(self.tank_2_height_label)
        horizontal_layout3.addWidget(self.tank_2_height)
        horizontal_layout3.addWidget(self.tank_2_flow_in_label)
        horizontal_layout3.addWidget(self.tank_2_flow_in)
        horizontal_layout3.addWidget(self.tank_2_flow_out_label)
        horizontal_layout3.addWidget(self.tank_2_flow_out)

        layout.addLayout(horizontal_layout3)

        # Add parent layout as layout
        self.setLayout(layout)

        # Create initial empty bar plot for aesthetic purposes
        self.initial_plot()

        # Second Figure instance for line plot
        self.figure2 = plt.figure()

        # self.canvas is the widget that displays the figure,
        # taking the figure instance as a parameter to __init__
        self.canvas2 = FigureCanvas(self.figure2)
        layout.addWidget(self.canvas2)
        self.lineplot_init()

    # Plot previous second of graph
    def prev_second_clicked(self):
        print("Clicked previous second")

    # Plot next second of graph
    def next_second_clicked(self):
        print("Clicked next second")

    # Go to second as specified by user
    def go_to_second_button_clicked(self):
        print("Clicked go to second")
    
    # Initial plot to make the GUI look initially pretty for aesthetic purposes
    def initial_plot(self):
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)
        # plt.gca().set_aspect('equal', adjustable='box')

        labels = ['Tank 1', 'Tank 2']
        label_locs = [1, 2]
        width = .40
        ax.bar(label_locs, [40,
                            30], width, label='Q1')

        # Set Graph labels, title, x-axis
        ax.set_ylabel('Liters in Tank')
        ax.set_title('Liters in Coupled Tanks')
        ax.set_xticks(label_locs)
        ax.set_xticklabels(labels)

        # refresh canvas
        self.canvas.draw()

    # Initial Line plot to make GUI look initially pretty for aesthetic purpises
    def lineplot_init(self):
        self.figure2.clear()
        # create an axis
        ax = self.figure2.add_subplot(1, 1, 1)

        # Set Graph labels, title, x-axis
        ax.set_ylabel('Inventory Available')
        ax.set_xlabel('Day')
        ax.set_title('Inventory for Store')
        self.canvas2.draw()

# The tank class
class tank:
    def __init__(self, height, area, flow_in, flow_out):
        pass
        self.height = height
        self.area = area
        self.flow_in = flow_in
        self.flow_out = flow_out
    
    def print(self):
        print("Height == " + str(self.height))
        print("Area == " + str(self.area))
        print("Flow in == " + str(self.flow_in))
        print("Flow out == " + str(self.flow_out))

if __name__ == "__main__":
    print("Running Assignment 3 Problem 1")
    # Upper tank of the two coupled tanks
    upper_tank = tank(height=2, area=10, flow_in=1, flow_out=2)
    # Lower tank of the two coupled tanks
    lower_tank = tank(height=3, area=40, flow_in=1, flow_out=2)

    upper_tank.print()
    lower_tank.print()

    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
