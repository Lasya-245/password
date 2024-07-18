#TASK 2

import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.configure(bg="#87CEEB")  # Set background color to sky blue
        
        # Create a frame for the calculator
        self.calc_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.calc_frame.pack(padx=10, pady=10)
        
        # Create entry field for input numbers
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.calc_frame, textvariable=self.entry_var, font=("Helvetica", 20), bd=0, bg="#eee", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")
        
        # Buttons for numbers and operations with respective colors
        buttons = [
            ("7", 1, 0, "#FFD700"), ("8", 1, 1, "#FFD700"), ("9", 1, 2, "#FFD700"), ("/", 1, 3, "#FF6347"),
            ("4", 2, 0, "#FFD700"), ("5", 2, 1, "#FFD700"), ("6", 2, 2, "#FFD700"), ("*", 2, 3, "#FF6347"),
            ("1", 3, 0, "#FFD700"), ("2", 3, 1, "#FFD700"), ("3", 3, 2, "#FFD700"), ("-", 3, 3, "#FF6347"),
            ("0", 4, 0, "#FFD700"), (".", 4, 1, "#FFD700"), ("=", 4, 2, "#32CD32"), ("+", 4, 3, "#32CD32")
        ]
        
        for (text, row, column, color) in buttons:
            button = tk.Button(self.calc_frame, text=text, font=("Helvetica", 16), width=5, height=2, bd=0,
                               command=lambda t=text: self.on_button_click(t), bg=color, fg="white")
            button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
        
        # Clear button with custom color
        clear_button = tk.Button(self.calc_frame, text="C", font=("Helvetica", 16), width=5, height=2, bd=0,
                                 command=self.clear_entry, bg="#FF4500", fg="white")
        clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        
        # Exit button with custom color
        exit_button = tk.Button(self.calc_frame, text="Exit", font=("Helvetica", 16), width=5, height=2, bd=0,
                                command=root.quit, bg="#2E8B57", fg="white")
        exit_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")
        
        # Bind keyboard events
        self.root.bind('<Return>', lambda event: self.on_button_click('='))
        self.root.bind('<Escape>', lambda event: root.quit())
        
    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry_var.get())
                self.entry_var.set(str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        elif text == 'C':
            self.clear_entry()
        else:
            self.entry_var.set(self.entry_var.get() + text)
    
    def clear_entry(self):
        self.entry_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
