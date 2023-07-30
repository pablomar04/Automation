import tkinter as tk
from datetime import datetime

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Date-Limited App")
        self.root.geometry("300x200")
        self.time_label = tk.Label(root, text="Time remaining: --")
        self.target_date = datetime(2023, 12, 31, 23, 59, 59)  # Target date and time (adjust as needed)
        self.update_timer()

    def update_timer(self):
        current_date = datetime.now()
        remaining_time = self.target_date - current_date

        if remaining_time.total_seconds() <= 0:
            self.show_expired_message()
        else:
            days, seconds = remaining_time.days, remaining_time.seconds
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            time_string = "{:02d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds)
            self.time_label.config(text="Time remaining: {}".format(time_string))
            self.root.after(1000, self.update_timer)

    def show_expired_message(self):
        self.time_label.config(text="Date expired! Closing the app...")
        self.root.after(2000, self.root.destroy)  # Close the app after 2 seconds

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    #app.time_label = tk.Label(root, text="Time remaining: --")
    app.time_label.pack(pady=10)
    root.mainloop()

