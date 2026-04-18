import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Tk")
        self.root.geometry("350x500")
        self.root.resizable(False, False)

        # Colors and Fonts
        self.bg_color = "#121212"
        self.display_bg = "#1e1e1e"
        self.btn_bg = "#000000"
        self.text_color = "#ffffff"
        self.font_style = ("Arial", 18, "bold")

        self.root.configure(bg=self.bg_color)

        # Expression storage
        self.expression = ""

        # Display Screen
        self.display_var = tk.StringVar(value="0")
        self.display_label = tk.Label(
            root, textvariable=self.display_var, font=("Arial", 32, "bold"),
            anchor="e", bg=self.display_bg, fg=self.text_color,
            padx=20, pady=40
        )
        self.display_label.pack(expand=True, fill="both")

        # Buttons Grid
        self.buttons_frame = tk.Frame(root, bg=self.bg_color)
        self.buttons_frame.pack(expand=True, fill="both")

        buttons = [
            'C', '(', ')', '<',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '.', '0', '=', '/',
            '',  '',  '^', '√'
        ]

        row = 0
        col = 0
        for btn_text in buttons:
            if btn_text == "":
                tk.Label(self.buttons_frame, bg=self.bg_color).grid(row=row, column=col, sticky="nsew")
            else:
                button = tk.Button(
                    self.buttons_frame, text=btn_text, font=self.font_style,
                    bg=self.btn_bg, fg=self.text_color, relief="flat",
                    highlightthickness=1, highlightbackground="#333333",
                    command=lambda x=btn_text: self.on_button_click(x)
                )
                button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Configure grid weights so buttons expand equally
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)
        for i in range(6):
            self.buttons_frame.rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                # Replace visual operators with python logic
                expr = self.expression.replace('^', '**').replace('√', 'math.sqrt')
                result = eval(expr)
                self.expression = str(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
        elif char == "C":
            self.expression = ""
        elif char == "<":
            self.expression = self.expression[:-1]
        elif char == "√":
            # Direct square root support
            self.expression += "sqrt("
        else:
            self.expression += str(char)

        # Update Display
        self.display_var.set(self.expression if self.expression else "0")

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()