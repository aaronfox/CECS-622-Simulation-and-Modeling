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


# The tank class
class tank:
    def __init__(self, height, area, flow_in, flow_out):
        self.height = height
        self.area = area
        self.flow_in = flow_in
        self.flow_out = flow_out

    def print(self):
        print("Height == " + str(self.height))
        print("Area == " + str(self.area))
        print("Flow in == " + str(self.flow_in))
        print("Flow out == " + str(self.flow_out))


###### GUI for visualizing the tank values ######
# All of the gui is based out of this Window class using Python PyQt5 GUI framework
class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # Allow for easy maximizing of the GUI
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setWindowTitle("Coupled Tank Simulation")

        # Figure instance for plotting
        self.figure = plt.figure()

        # self.canvas is the widget that displays the figure,
        # taking the figure instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # Adds toolbar to top of GUI for saving pictures, zooming in graph, etc.
        self.toolbar = NavigationToolbar(self.canvas, self)

        # For keeping track of day evaluation of bar charts
        self.current_second = 0

        # For making sure they don't try to evaluate without having run sim
        self.has_run_sim = False

        # set the layout (vertical)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.go_to_second_label = QLabel()
        self.go_to_second_label.setText("Enter Second to Evaluate: ")
        self.go_to_second_value = QLineEdit()
        self.go_to_second_value.setText("0")
        self.go_to_second_button = QPushButton("Go to Second")
        self.go_to_second_button.clicked.connect(self.go_to_second_button_clicked)

        self.next_second_button = QPushButton("Next Second")
        self.next_second_button.clicked.connect(self.next_second_clicked)

        self.prev_second_button = QPushButton("Prev Second")
        self.prev_second_button.clicked.connect(self.prev_second_clicked)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout1.addWidget(self.go_to_second_label)
        horizontal_layout1.addWidget(self.go_to_second_value)
        horizontal_layout1.addWidget(self.go_to_second_button)
        horizontal_layout1.addWidget(self.prev_second_button)
        horizontal_layout1.addWidget(self.next_second_button)
        layout.addLayout(horizontal_layout1)

        # Second horizontal layout: All input info for Tank 1
        self.tank_1_area_label = QLabel()
        self.tank_1_area_label.setText("Tank 1 Area: ")
        self.tank_1_area = QLineEdit()
        self.tank_1_area.setText("2.0")

        self.tank_1_height_label = QLabel()
        self.tank_1_height_label.setText("Height: ")
        self.tank_1_height = QLineEdit()
        self.tank_1_height.setText("1.5")
    
        self.tank_1_flow_in_label = QLabel()
        self.tank_1_flow_in_label.setText("Flow In Rate: ")
        self.tank_1_flow_in = QLineEdit()
        self.tank_1_flow_in.setText("0.01")
        
        self.tank_1_flow_out_label = QLabel()
        self.tank_1_flow_out_label.setText("Flow Out Rate: ")
        self.tank_1_flow_out = QLineEdit()
        self.tank_1_flow_out.setText(".01")

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
        self.tank_2_area_label = QLabel()
        self.tank_2_area_label.setText("Tank 2 Area: ")
        self.tank_2_area = QLineEdit()
        self.tank_2_area.setText("2.0")

        self.tank_2_height_label = QLabel()
        self.tank_2_height_label.setText("Height: ")
        self.tank_2_height = QLineEdit()
        self.tank_2_height.setText("1.0")
        
        self.tank_2_flow_out_label = QLabel()
        self.tank_2_flow_out_label.setText("Flow Out Rate: ")
        self.tank_2_flow_out = QLineEdit()
        self.tank_2_flow_out.setText("0.02")

        horizontal_layout3 = QHBoxLayout()
        horizontal_layout3.addWidget(self.tank_2_area_label)
        horizontal_layout3.addWidget(self.tank_2_area)
        horizontal_layout3.addWidget(self.tank_2_height_label)
        horizontal_layout3.addWidget(self.tank_2_height)
        horizontal_layout3.addWidget(self.tank_2_flow_out_label)
        horizontal_layout3.addWidget(self.tank_2_flow_out)

        layout.addLayout(horizontal_layout3)

        # Fourth horizontal layout is to run the simulation!
        # Button connected to generation of points on figure to visually
        # display the uniform random distribution of points inside/outside the circle
        self.run_sim_button = QPushButton('Run Simulation')
        self.run_sim_button.clicked.connect(self.run_simulation)
        horizontal_layout4 = QHBoxLayout()
        horizontal_layout4.addWidget(self.run_sim_button)

        layout.addLayout(horizontal_layout4)

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
        if not self.has_run_sim:
            print("Please run at least one simulation first")
            return
        if self.current_second <= 0:
            print("Cannot go before 0 seconds in this simulation")
            return
        self.current_second = int(self.go_to_second_value.text())
        self.current_second = self.current_second - 1
        self.go_to_second_value.setText(str(self.current_second))
        self.go_to_second_button_clicked()

    # Plot next second of graph
    def next_second_clicked(self):
        if not self.has_run_sim:
            print("Please run at least one simulation first")
            return
        if self.current_second >= self.seconds_to_run:
            print("Cannot go after " + self.seconds_to_run + " seconds in this simulation.")
            print("Please adjust self.seconds_to_run to raise the limit if needed")
            return
        self.current_second = int(self.go_to_second_value.text())
        self.current_second = self.current_second + 1
        self.go_to_second_value.setText(str(self.current_second))
        self.go_to_second_button_clicked()

    # Go to second as specified by user
    def go_to_second_button_clicked(self):
        if not self.has_run_sim:
            print("Please run at least one simulation first")
            return
        if not self.go_to_second_value.text().isnumeric():
            print("Please enter an integer second value")
            return
        if int(self.go_to_second_value.text()) > self.seconds_to_run:
            print("Please enter an integer value less than or equal to " + str(self.seconds_to_run))
            return
        
        self.current_second = int(self.go_to_second_value.text())

        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(1, 1, 1)

        tank_1_val = self.tank_1_simulation_results[self.current_second][1]
        tank_2_val = self.tank_2_simulation_results[self.current_second][1]
        labels = ['Tank 1', 'Tank 2']
        label_locs = [1, 2]
        width = .40
        ax.bar(label_locs, [tank_1_val,
                            tank_2_val], width, label='Tanks')

        # Set Graph labels, title, x-axis
        ax.set_ylabel('Height of Fluid')
        ax.set_title('Height of Fluid in Coupled Tanks')
        ax.set_xticks(label_locs)
        ax.set_xticklabels(labels)

        # refresh canvas
        self.canvas.draw()
    
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
                            30], width, label='Tanks')

        # Set Graph labels, title, x-axis
        ax.set_ylabel('Height of Fluid')
        ax.set_title('Height of Fluid in Coupled Tanks')
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

    # Plot the line graph illustrating changes in each inventory
    def plot_line_graph(self):
        self.figure2.clear()
        # create an axis
        ax = self.figure2.add_subplot(1, 1, 1)

        # Set Graph labels, title, x-axis
        ax.set_ylabel('Height of Fluid')
        ax.set_xlabel('Second')
        ax.set_title('Height of Fluid in Coupled Tanks')

        tank_1_x = []
        tank_1_y = []
        tank_2_x = []
        tank_2_y = []
        for i in range(len(self.tank_1_simulation_results)):
            tank_1_x.append(self.tank_1_simulation_results[i][0])
            tank_1_y.append(self.tank_1_simulation_results[i][1])
            tank_2_x.append(self.tank_2_simulation_results[i][0])
            tank_2_y.append(self.tank_2_simulation_results[i][1])

        ax.plot(tank_1_x, tank_1_y, label='Tank 1')
        ax.plot(tank_2_x, tank_2_y, label='Tank 2')
        ax.legend()

        # refresh canvas
        self.canvas2.draw()

    # Makes sure a value is float
    def is_float(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    def run_simulation(self):
        print("Running simulation")
        self.has_run_sim = True
        # # Upper tank of the two coupled tanks
        # upper_tank = tank(height=2, area=10, flow_in=1, flow_out=2)
        # # Lower tank of the two coupled tanks
        # lower_tank = tank(height=3, area=40, flow_in=1, flow_out=2)

        # Get input numbers from input boxes to run sim
        if (self.is_float(self.tank_1_area.text()) and self.is_float(self.tank_1_area.text())
            and self.is_float(self.tank_1_height.text()) and self.is_float(self.tank_1_flow_in.text())
              and self.is_float(self.tank_1_flow_out.text()) and self.is_float(self.tank_2_area.text()) 
              and self.is_float(self.tank_2_height.text()) and self.is_float(self.tank_2_flow_out.text())):
           # Inside if loop, set all respective values 
           self.tank_1_area_value = float(self.tank_1_area.text())
           self.tank_1_height_value = float(self.tank_1_height.text())
           self.tank_1_flow_in_value = float(self.tank_1_flow_in.text())
           self.tank_1_flow_out_value = float(self.tank_1_flow_out.text())
           self.tank_2_area_value = float(self.tank_2_area.text())
           self.tank_2_height_value = float(self.tank_2_height.text())
           self.tank_2_flow_out_value = float(self.tank_2_flow_out.text())
        
        self.seconds_to_run = 1000

        self.tank_1_simulation_results = []
        self.tank_2_simulation_results = []

        # Since flow rates and areas are constant, we only need to calculate rate of change of heights once
        tank_1_rate_of_change_of_height = (self.tank_1_flow_in_value - self.tank_1_flow_out_value) / self.tank_1_area_value
        tank_2_rate_of_change_of_height = (self.tank_1_flow_out_value - self.tank_2_flow_out_value) / self.tank_2_area_value

        tank_1_current_height = self.tank_1_height_value
        tank_2_current_height = self.tank_2_height_value
        self.tank_1_simulation_results.append([0, tank_1_current_height])
        self.tank_2_simulation_results.append([0, tank_2_current_height])
        current_tank_2_rate_of_change_of_height = 0

        # Core of sim runs here
        for i in range(1, self.seconds_to_run + 1):
            tank_1_current_height = tank_1_current_height + tank_1_rate_of_change_of_height

            # Make sure height of upper tank allows for the proper amount of 
            # flow to bottom tank (e.g. if tank_1_current_height) is above current rate so that
            if tank_1_current_height < tank_2_rate_of_change_of_height:
                current_tank_2_rate_of_change_of_height = tank_1_current_height
            else:
                current_tank_2_rate_of_change_of_height = tank_2_rate_of_change_of_height

            if tank_1_current_height < 0:
                tank_1_current_height = 0.0

            tank_2_current_height = tank_2_current_height + current_tank_2_rate_of_change_of_height#tank_2_rate_of_change_of_height
            
            if tank_2_current_height < 0:
                tank_2_current_height = 0.0

            self.tank_1_simulation_results.append([i, tank_1_current_height])
            self.tank_2_simulation_results.append([i, tank_2_current_height])

        self.plot_line_graph()



###### END GUI #####

if __name__ == "__main__":
    print("Running Assignment 3 Problem 1")
    # # Upper tank of the two coupled tanks
    # upper_tank = tank(height=2, area=10, flow_in=1, flow_out=2)
    # # Lower tank of the two coupled tanks
    # lower_tank = tank(height=3, area=40, flow_in=1, flow_out=2)

    # upper_tank.print()
    # lower_tank.print()

    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
