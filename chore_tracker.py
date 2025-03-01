# Imports
import tkinter as tk
import sqlite3
from tkinter import ttk
from datetime import datetime

class ChoreTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Chore Tracker App")
        self.CHORE_LIST = ["Clean Room", "Do Laundry", "Load Dishwasher", "Vacuum"]
        self.completed_chore_list = []

        # Initialize database connection and cursor
        self.conn = sqlite3.connect('chore_tracker.db')
        self.cursor = self.conn.cursor()
        self.setup_database()

        # Create GUI components
        self.chore_label = tk.Label(root, text="Select a Chore:")
        self.chore_label.pack()

        self.chore_combo = ttk.Combobox(root, values=self.CHORE_LIST)
        self.chore_combo.pack()

        self.mark_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.mark_completed_button.pack()

        self.progress_label = tk.Label(root, text="Progress:")
        self.progress_label.pack()

        self.progress_listbox = tk.Listbox(root, height=10, width=40)
        self.progress_listbox.pack()

    def setup_database(self):
        # Create tables
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS chores
                    (chore text)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS completed_chores
                    (chore text, timestamp text)''')
        self.conn.commit()

    def update_progress_text(self):
        self.progress_listbox.delete(0, tk.END)
        for chore in self.completed_chore_list:
            self.progress_listbox.insert(tk.END, chore)

    def mark_completed(self):
        selected_chore = self.chore_combo.get()
        if selected_chore:
            self.completed_chore_list.append(selected_chore)
            self.CHORE_LIST.remove(selected_chore)
            self.chore_combo['values'] = self.CHORE_LIST
            self.chore_combo.set("")
            self.update_progress_text()
        if selected_chore:
            self.record_completion(selected_chore)
    def record_completion(self, chore):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('''
            INSERT INTO completed_chores (chore, timestamp)
            VALUES (?, ?)
        ''', (chore, timestamp))
        self.conn.commit()    



if __name__ == "__main__":
    root = tk.Tk()
    app = ChoreTracker(root)
    root.mainloop()
