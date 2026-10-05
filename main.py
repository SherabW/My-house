# import tkinter as tk

# root =tk.Tk()
# root.title("My First Canvas")

# canvas = tk.Canvas(root, width=500,
#                    height=350,bg="White")
# canvas.pack()
# canvas.create_rectangle(40, 40, 220, 150, fill="coral")
# canvas.create_oval(200, 50, 440, 190, fill="lightblue")
# canvas.create_line(50, 250, 500, 250, width=4)
# canvas.create_text(275, 310, text="Hello Canvas", font=("Arial",20))

# root.mainloop()



import tkinter as tk

root = tk.Tk()
root.title("My House")

canvas = tk.Canvas(root, width=500, height=350, bg="white")
canvas.pack()

# House body - rectangle
canvas.create_rectangle(
    120, 150, 380, 300,
    fill="lightblue",
    outline="black",
    width=2
)

# Roof - triangle
canvas.create_polygon(
    100, 150,
    250, 50,
    400, 150,
    fill="red",
    outline="black",
    width=2
)

# Door
canvas.create_rectangle(
    220, 220, 280, 300,
    fill="brown",
    outline="black"
)

# Window
canvas.create_rectangle(
    145, 190, 195, 240,
    fill="lightyellow",
    outline="black"
)

# Another window
canvas.create_rectangle(
    305, 190, 355, 240,
    fill="lightyellow",
    outline="black"
)



root.mainloop()
