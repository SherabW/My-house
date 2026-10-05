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

# -------------------------
# SUN - upper left
# -------------------------
canvas.create_oval(
    40, 40, 90, 90,
    fill="yellow",
    outline="orange",
    width=2
)

# Sun rays
canvas.create_line(65, 30, 65, 15, width=2)
canvas.create_line(65, 100, 65, 115, width=2)
canvas.create_line(30, 65, 15, 65, width=2)
canvas.create_line(100, 65, 115, 65, width=2)

# -------------------------
# HOUSE BODY - rectangle
# -------------------------
canvas.create_rectangle(
    120, 150, 380, 300,
    fill="lightblue",
    outline="black",
    width=2
)

# -------------------------
# ROOF - triangle
# -------------------------
canvas.create_polygon(
    100, 150,
    250, 50,
    400, 150,
    fill="red",
    outline="black",
    width=2
)

# -------------------------
# DOOR
# -------------------------
canvas.create_rectangle(
    220, 220, 280, 300,
    fill="brown",
    outline="black"
)

# -------------------------
# WINDOW 1
# -------------------------
canvas.create_rectangle(
    145, 190, 195, 240,
    fill="lightyellow",
    outline="black"
)

# -------------------------
# WINDOW 2
# -------------------------
canvas.create_rectangle(
    305, 190, 355, 240,
    fill="lightyellow",
    outline="black"
)

# -------------------------
# DOG HOUSE - right side
# -------------------------

# Dog house body
canvas.create_rectangle(
    395, 245, 475, 300,
    fill="brown",
    outline="black",
    width=2
)

# Dog house roof - triangle
canvas.create_polygon(
    385, 245,
    435, 205,
    485, 245,
    fill="red",
    outline="black",
    width=2
)

# Dog house entrance
canvas.create_oval(
    420, 260, 450, 300,
    fill="black",
    outline="black"
)

# -------------------------
# DOG - beside dog house
# -------------------------

# Dog body
canvas.create_oval(
    385, 285, 425, 315,
    fill="orange",
    outline="black"
)

# Dog head
canvas.create_oval(
    365, 270, 400, 300,
    fill="orange",
    outline="black"
)

# Dog ear
canvas.create_oval(
    360, 265, 375, 285,
    fill="brown",
    outline="black"
)

# Dog eye
canvas.create_oval(
    388, 278, 393, 283,
    fill="black"
)

# Dog nose
canvas.create_oval(
    365, 285, 370, 290,
    fill="black"
)

# Dog tail
canvas.create_line(
    420, 290, 435, 280,
    width=3
)

# -------------------------
# GROUND
# -------------------------
canvas.create_line(
    30, 315, 490, 315,
    width=3
)

root.mainloop()

