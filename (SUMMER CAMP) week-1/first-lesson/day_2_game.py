import turtle

wn = turtle.Screen()
wn.title("Player Control Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

player = turtle.Turtle()
player.shape("circle")
player.color("red")
player.penup()
player.speed(0)

BOUNDARY = 290

def move_up():
    y = player.ycor()
    if y + 20 <= BOUNDARY:
        player.sety(y + 20)
    else:
        player.sety(BOUNDARY)

def move_down():
    y = player.ycor()
    if y - 20 >= -BOUNDARY:
        player.sety(y - 20)
    else:
        player.sety(-BOUNDARY)

def move_left():
    x = player.xcor()
    if x - 20 >= -BOUNDARY:
        player.setx(x - 20)
    else:
        player.setx(-BOUNDARY)

def move_right():
    x = player.xcor()
    if x + 20 <= BOUNDARY:
        player.setx(x + 20)
    else:
        player.setx(BOUNDARY)

wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")

while True:
    wn.update()

