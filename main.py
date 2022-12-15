import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage


class PomodoroTimer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x300')
        self.root.title('Pomodoro Timer')
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="tomato.png"))
        
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=('Ubuntu', 16))
        self.s.configure("TButton", font=('Ubuntu', 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=18, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.pomodoro_timer_label = ttk.Label(self.tab1, text="25:00", font=("Ubuntu", 48))
        self.pomodoro_timer_label.pack(pady=20)

        self.short_break_timer_label = ttk.Label(self.tab2, text="5:00", font=("Ubuntu", 48))
        self.short_break_timer_label.pack(pady=20)

        self.long_break_timer_label = ttk.Label(self.tab3, text="15:00", font=("Ubuntu", 48))
        self.long_break_timer_label.pack(pady=20)

        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

        self.root.mainloop()

    def start_timer_thread(self):
        pass

    def star_timer(self):
        pass

    def reset_clock(self):
        pass

    def skip_clock(self):
        pass

PomodoroTimer()