import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QListWidget, QVBoxLayout, QWidget
)
from PyQt5.QtCore import Qt


class ChoreTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chore Tracker App")
        self.CHORE_LIST = ["Clean Room", "Do Laundry", "Load Dishwasher", "Vacuum"]
        self.completed_chore_list = []

        # Set up the main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Create GUI components
        self.chore_label = QLabel("Select a Chore:")
        self.main_layout.addWidget(self.chore_label)

        self.chore_combo = QComboBox()
        self.chore_combo.addItems(self.CHORE_LIST)
        self.main_layout.addWidget(self.chore_combo)

        self.mark_completed_button = QPushButton("Mark as Completed")
        self.mark_completed_button.clicked.connect(self.mark_completed)
        self.main_layout.addWidget(self.mark_completed_button) 

        self.progress_label = QLabel("Progress:")
        self.main_layout.addWidget(self.progress_label)

        self.progress_listbox = QListWidget()
        self.main_layout.addWidget(self.progress_listbox)


    def update_progress_text(self):
        self.progress_listbox.clear()
        self.progress_listbox.addItems(self.completed_chore_list)

    def mark_completed(self):
        selected_chore = self.chore_combo.currentText()
        if selected_chore:
            self.completed_chore_list.append(selected_chore)
            self.CHORE_LIST.remove(selected_chore)
            self.chore_combo.clear()
            self.chore_combo.addItems(self.CHORE_LIST)
            self.update_progress_text()
            self.record_completion(selected_chore)

    #TODO: Display the completed chore on the progress_listbox
    def record_completion(self, chore):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Chore '{chore}' completed at {timestamp}")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ChoreTracker()
    window.show()
    sys.exit(app.exec_())