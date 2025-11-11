import tkinter as tk
import time

class DigitalClockTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock with Timer")
        self.label = tk.Label(self.root, font=('calibri', 40, 'bold'), background='black', foreground='white')
        self.label.pack(padx=20, pady=20)
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.label.config(text=current_time)
        self.label.after(1000, self.update_clock)

def main():
    try:
        root = tk.Tk()
        app = DigitalClockTimerApp(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()