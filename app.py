import tkinter as tk

# main window and master
root = tk.Tk()
root.geometry("400x300+100+50")

# creating 3*3 grid
for i in range(3):
    # rows to expand proportionally
    root.rowconfigure(i, weight=1)
    for j in range(3):
        # columns to expand proportionally
        root.columnconfigure(j, weight=1)
        button = tk.Button(root, text=f'({i},{j})')
        # adding sticky to the grid to make it fill the space in all 4 directions when expanded
        button.grid(row=i, column=j, sticky='nsew')

# puts everything on the display, and responds to user input until the program terminates
root.mainloop()