import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget to display the current expression
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, justify="right", font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define the buttons and their layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Function to create and configure buttons
def create_button(text, row, col):
    return tk.Button(window, text=text, command=lambda: on_click(text), width=5, height=2, font=("Arial", 12)).grid(row=row, column=col)

# Add buttons to the grid
row_val = 1
col_val = 0
for button_text in buttons:
    create_button(button_text, row_val, col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure row and column weights so that they expand proportionally
for i in range(1, 5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Run the application
window.mainloop()
