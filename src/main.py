from player import *
from config import *
from ui import *
# from csv_funcs import * # for all the CSV-related functions

class Player(QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self) # for setting up the UI (it's unfinished for now)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Windows')  # Set the application style to 'Windows'
    window = Player()  # Create an instance of the player window
    window.show()  # Show the window
    sys.exit(app.exec())  # Run the application event loop