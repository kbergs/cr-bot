from lose_war import lose_war
from screen import Screen
from dailies import donate
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

# TODO: Set up timer to validate screen.current
# TODO: Set up timer to complete dailies

# TODO: Low priority: implement features for users not in clans

# Initialize Screen Object
screen = Screen()

# Define the functionality for the buttons
def on_button_click_war():
    lose_war()

def on_button_click_lock():
    print("Button 2 clicked!")

def on_button_click_dailies():
    donate(screen)

def on_button_click_dailies_w():
    print("dailies")
    lose_war()

# Create the application window
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle('Simple PyQt5 GUI')

# Create a layout to arrange the buttons
layout = QVBoxLayout()

# Create buttons and connect them to their respective functions
button_war = QPushButton('Use up war decks')
button_war.clicked.connect(on_button_click_war)

button_lock = QPushButton('Lock screen position')
button_lock.clicked.connect(on_button_click_lock)

button_dailies = QPushButton('Dailies')
button_dailies.clicked.connect(on_button_click_dailies)

button_dailies_w = QPushButton('Dailies (with war)')
button_dailies_w.clicked.connect(on_button_click_dailies_w)

# Add buttons to the layout
layout.addWidget(button_war)
layout.addWidget(button_lock)
layout.addWidget(button_dailies)
layout.addWidget(button_dailies_w)

# Set the layout for the window
window.setLayout(layout)

# Show the window
window.show()

# Start the event loop
app.exec_()