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

# ==========================================
# WINDOW
# ==========================================

root = tk.Tk()
root.title("Animated Community")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=900,
    height=600,
    bg="#87CEEB"
)

canvas.pack()

# ==========================================
# SKY
# ==========================================

canvas.create_rectangle(
    0, 0, 900, 380,
    fill="#87CEEB",
    outline=""
)

# ==========================================
# MOUNTAINS
# ==========================================

canvas.create_polygon(
    0, 300,
    150, 130,
    300, 300,
    fill="#607D8B",
    outline="#455A64"
)

canvas.create_polygon(
    180, 300,
    380, 110,
    570, 300,
    fill="#546E7A",
    outline="#455A64"
)

canvas.create_polygon(
    450, 300,
    650, 140,
    850, 300,
    fill="#607D8B",
    outline="#455A64"
)

canvas.create_polygon(
    650, 300,
    780, 170,
    900, 300,
    fill="#546E7A",
    outline="#455A64"
)

# ==========================================
# SNOW CAPS
# ==========================================

canvas.create_polygon(
    150, 130,
    120, 165,
    150, 150,
    170, 165,
    fill="white",
    outline=""
)

canvas.create_polygon(
    380, 110,
    345, 145,
    380, 132,
    410, 150,
    fill="white",
    outline=""
)

canvas.create_polygon(
    650, 140,
    615, 175,
    650, 160,
    680, 178,
    fill="white",
    outline=""
)

# ==========================================
# SUN
# ==========================================

sun = canvas.create_oval(
    60, 60, 120, 120,
    fill="yellow",
    outline="orange",
    width=3
)

# ==========================================
# CLOUDS
# ==========================================

cloud1 = []

cloud1.append(
    canvas.create_oval(
        170, 70, 220, 105,
        fill="white",
        outline=""
    )
)

cloud1.append(
    canvas.create_oval(
        200, 55, 255, 105,
        fill="white",
        outline=""
    )
)

cloud1.append(
    canvas.create_oval(
        235, 70, 290, 105,
        fill="white",
        outline=""
    )
)

cloud1.append(
    canvas.create_rectangle(
        190, 75, 270, 105,
        fill="white",
        outline=""
    )
)

cloud2 = []

cloud2.append(
    canvas.create_oval(
        650, 90, 700, 125,
        fill="white",
        outline=""
    )
)

cloud2.append(
    canvas.create_oval(
        680, 75, 740, 125,
        fill="white",
        outline=""
    )
)

cloud2.append(
    canvas.create_oval(
        720, 90, 770, 125,
        fill="white",
        outline=""
    )
)

cloud2.append(
    canvas.create_rectangle(
        675, 95, 745, 125,
        fill="white",
        outline=""
    )
)

# ==========================================
# GROUND
# ==========================================

canvas.create_rectangle(
    0, 300, 900, 600,
    fill="#6DBE45",
    outline=""
)

# ==========================================
# ROAD
# ==========================================

canvas.create_rectangle(
    0, 470, 900, 550,
    fill="#444444",
    outline=""
)

# Road lines
for x in range(0, 900, 100):
    canvas.create_rectangle(
        x, 505,
        x + 60, 512,
        fill="white",
        outline=""
    )

# ==========================================
# MAIN HOUSE
# ==========================================

# House body
canvas.create_rectangle(
    150, 330, 350, 470,
    fill="#D9F0FF",
    outline="black",
    width=2
)

# Red roof
canvas.create_polygon(
    125, 330,
    250, 240,
    375, 330,
    fill="red",
    outline="black",
    width=2
)

# Door
canvas.create_rectangle(
    225, 400, 275, 470,
    fill="#7B4A2F",
    outline="black",
    width=2
)

# Door handle
canvas.create_oval(
    260, 435, 267, 442,
    fill="yellow",
    outline="black"
)

# Windows
canvas.create_rectangle(
    170, 365, 215, 405,
    fill="#FFE680",
    outline="black",
    width=2
)

canvas.create_rectangle(
    285, 365, 330, 405,
    fill="#FFE680",
    outline="black",
    width=2
)

# Window crosses
canvas.create_line(192, 365, 192, 405, width=2)
canvas.create_line(170, 385, 215, 385, width=2)

canvas.create_line(307, 365, 307, 405, width=2)
canvas.create_line(285, 385, 330, 385, width=2)

# ==========================================
# COMMUNITY HOUSE 1
# ==========================================

canvas.create_rectangle(
    25, 350, 120, 430,
    fill="#F4C2A1",
    outline="black"
)

canvas.create_polygon(
    10, 350,
    72, 300,
    135, 350,
    fill="#B71C1C",
    outline="black"
)

canvas.create_rectangle(
    55, 385, 80, 430,
    fill="#6D4C41",
    outline="black"
)

# ==========================================
# COMMUNITY HOUSE 2
# ==========================================

canvas.create_rectangle(
    400, 345, 500, 430,
    fill="#FFD180",
    outline="black"
)

canvas.create_polygon(
    385, 345,
    450, 295,
    515, 345,
    fill="#C62828",
    outline="black"
)

canvas.create_rectangle(
    435, 385, 465, 430,
    fill="#6D4C41",
    outline="black"
)

# ==========================================
# SCHOOL / COMMUNITY BUILDING
# ==========================================

canvas.create_rectangle(
    570, 320, 760, 430,
    fill="#FFF3E0",
    outline="black",
    width=2
)

canvas.create_polygon(
    550, 320,
    665, 250,
    780, 320,
    fill="#8E24AA",
    outline="black",
    width=2
)

# School sign
canvas.create_rectangle(
    610, 330, 720, 355,
    fill="white",
    outline="black"
)

canvas.create_text(
    665, 343,
    text="SCHOOL",
    font=("Arial", 12, "bold")
)

# School windows
for x in [590, 640, 690, 740]:
    canvas.create_rectangle(
        x, 370, x + 30, 400,
        fill="#81D4FA",
        outline="black"
    )

# School door
canvas.create_rectangle(
    650, 395, 680, 430,
    fill="#6D4C41",
    outline="black"
)

# ==========================================
# TREES
# ==========================================

def create_tree(x, y):
    # trunk
    canvas.create_rectangle(
        x - 8, y, x + 8, y + 55,
        fill="#795548",
        outline=""
    )

    # leaves
    canvas.create_oval(
        x - 35, y - 40,
        x + 35, y + 25,
        fill="#2E7D32",
        outline="#1B5E20"
    )

    canvas.create_oval(
        x - 20, y - 65,
        x + 35, y - 5,
        fill="#388E3C",
        outline="#1B5E20"
    )


create_tree(90, 440)
create_tree(520, 430)
create_tree(800, 430)

# ==========================================
# DOG HOUSE
# ==========================================

canvas.create_rectangle(
    385, 450, 455, 500,
    fill="#8D6E63",
    outline="black",
    width=2
)

canvas.create_polygon(
    375, 450,
    420, 415,
    465, 450,
    fill="red",
    outline="black"
)

canvas.create_oval(
    405, 465, 435, 500,
    fill="black",
    outline="black"
)

# ==========================================
# DOG
# ==========================================

# body
canvas.create_oval(
    470, 455, 535, 490,
    fill="#8B4513",
    outline="black"
)

# head
canvas.create_oval(
    525, 440, 570, 480,
    fill="#8B4513",
    outline="black"
)

# ear
canvas.create_oval(
    520, 440, 535, 465,
    fill="#5C3317",
    outline="black"
)

# eye
canvas.create_oval(
    555, 450, 561, 456,
    fill="black"
)

# nose
canvas.create_oval(
    565, 463, 573, 470,
    fill="black"
)

# legs
canvas.create_line(
    485, 480, 485, 505,
    width=5
)

canvas.create_line(
    515, 480, 515, 505,
    width=5
)

# tail
canvas.create_line(
    470, 465, 450, 445,
    width=5
)

# ==========================================
# FLOWERS
# ==========================================

for x in [30, 110, 380, 780, 850]:
    canvas.create_line(
        x, 450, x, 470,
        fill="green",
        width=2
    )

    canvas.create_oval(
        x - 5, 442,
        x + 5, 452,
        fill="pink",
        outline=""
    )

# ==========================================
# CAR
# ==========================================

car_body = canvas.create_rectangle(
    0, 525, 80, 550,
    fill="blue",
    outline="black",
    width=2
)

car_top = canvas.create_polygon(
    15, 525,
    30, 505,
    60, 505,
    72, 525,
    fill="blue",
    outline="black"
)

car_wheel1 = canvas.create_oval(
    12, 540, 30, 558,
    fill="black"
)

car_wheel2 = canvas.create_oval(
    55, 540, 73, 558,
    fill="black"
)

# ==========================================
# ANIMATION
# ==========================================

sun_dx = 1
cloud_dx = 1
car_dx = 4


def animate():
    global sun_dx
    global cloud_dx
    global car_dx

    # Move sun
    canvas.move(sun, sun_dx, 0)

    sun_position = canvas.coords(sun)

    if sun_position[2] >= 850:
        sun_dx = -1

    if sun_position[0] <= 40:
        sun_dx = 1

    # Move first cloud
    for item in cloud1:
        canvas.move(item, cloud_dx, 0)

    cloud_position = canvas.coords(cloud1[0])

    if cloud_position[2] >= 900:
        cloud_dx = -1

    if cloud_position[0] <= 100:
        cloud_dx = 1

    # Move second cloud
    for item in cloud2:
        canvas.move(item, cloud_dx, 0)

    # Move car
    canvas.move(car_body, car_dx, 0)
    canvas.move(car_top, car_dx, 0)
    canvas.move(car_wheel1, car_dx, 0)
    canvas.move(car_wheel2, car_dx, 0)

    car_position = canvas.coords(car_body)

    if car_position[2] >= 900:
        car_dx = -4

    if car_position[0] <= 0:
        car_dx = 4

    root.after(30, animate)


# Start animation
animate()

root.mainloop()