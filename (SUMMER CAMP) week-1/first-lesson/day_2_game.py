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

def move_up():
    player.sety(player.ycor() + 20)

def move_down():
    player.sety(player.ycor() - 20)

def move_left():
    player.setx(player.xcor() - 20)

def move_right():
    player.setx(player.xcor() + 20)

wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")

while True:
    wn.update()

