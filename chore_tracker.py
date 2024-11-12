# Imports
import tkinter as tk
from tkinter import ttk

class ChoreTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chore Tracker App")
        self.chore_list = ["Clean Room", "Do Laundry", "Help with Dishes"]
        self.completed_chore_list = []

        # Create GUI components
        self.chore_label = tk.Label(root, text="Select a Chore:")
        self.chore_label.pack()

        self.chore_combo = ttk.Combobox(root, values=self.chore_list)
        self.chore_combo.pack()

        self.mark_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.mark_completed_button.pack()

        self.progress_label = tk.Label(root, text="Progress:")
        self.progress_label.pack()

        self.progress_text = tk.Text(root, height=10, width=40)
        self.progress_text.pack()

    def mark_completed(self):
        selected_chore = self.chore_combo.get()
        if selected_chore:
            self.completed_chore_list.append(selected_chore)
            self.chore_combo.set("")
            self.update_progress_text()

    def update_progress_text(self):
        self.progress_text.delete(1.0, tk.END)
        for chore in self.completed_chore_list:
            self.progress_text.insert(tk.END, chore + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChoreTrackerApp(root)
    root.mainloop()
