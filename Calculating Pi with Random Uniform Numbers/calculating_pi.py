import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # Figure instance for plotting
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Add input box for user to request N uniform numbers
        self.random_number_input = QLineEdit()
        self.random_number_input_label = QLabel()
        self.random_number_input_label.setText("Enter N random uniform numbers to generate: ")


        # Just some button connected to `plot` method
        self.button = QPushButton('Generate')
        self.button.clicked.connect(self.generate)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        
        # Number of N numbers to generate input 
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.random_number_input_label)
        horizontal_layout.addWidget(self.random_number_input)
        layout.addLayout(horizontal_layout)

        # Generate button
        layout.addWidget(self.button)

        
        self.setLayout(layout)

    def generate(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        # ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
