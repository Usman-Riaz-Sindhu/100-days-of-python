"""
Face -> Full Pixel-by-Pixel Colored Portrait (Turtle)
--------------------------------------------------------
Yeh script "coordinates_full.py" file mein di hui (x, y, r, g, b)
coordinates par turtle se dots lagati hai - is baar SIRF outline nahi,
balke POORI picture (background sameet, sab colors ke saath) pixel by
pixel bani hai.

Requirements:
    coordinates_full.py isi folder mein hona chahiye (already di gayi hai)

Usage:
    python face_full_color.py
"""

import turtle
from coordinates_full import COORDINATES

DOT_SIZE = 6   # har dot ka size (pixels ko "pass pass" / gap-free rakhne ke liye)

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("white")
screen.title("Full Pixel Portrait - Turtle")
screen.tracer(0, 0)   # animation off -> fast drawing

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)

for i, (x, y, r, g, b) in enumerate(COORDINATES):
    t.goto(x, y)
    t.dot(DOT_SIZE, (r / 255, g / 255, b / 255))
    if i % 200 == 0:          # bohat saaray points hain, kam kam update karo -> fast
        screen.update()

screen.update()
print(f"Total dots drawn: {len(COORDINATES)}")
print("Window band karne ke liye click karein.")
screen.exitonclick()