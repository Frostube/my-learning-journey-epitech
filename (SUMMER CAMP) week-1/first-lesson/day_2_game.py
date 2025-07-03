import turtle
import random


wn = turtle.Screen()
wn.title("Player Control Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)    

#PLAYER
player = turtle.Turtle()
player.shape("circle")
player.color("white")
player.penup()
player.speed(0)
player.goto(0, 250)

#ENEMY
#PLAYER BOUNDARY CHECK
# Setting the boundary for player movement
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
        
#ENEMY START POSITION

#ENEMY AMOUNT 5 
enemy_count = 5
enemies = []

for _ in range(enemy_count):
    new_enemy = turtle.Turtle()
    new_enemy.shape("circle")
    new_enemy.color("red")
    new_enemy.penup()
    new_enemy.speed(0)
    new_enemy.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))
    enemies.append(new_enemy)

#ENEMY MOVEMENT
def move_enemy():
    for enemy in enemies:
        x = random.randint(-BOUNDARY, BOUNDARY)
        y = random.randint(-BOUNDARY, BOUNDARY)
        enemy.goto(player.xcor() + x, player.ycor() + y)
        
    wn.ontimer(move_enemy, 1000)
    
    
#ONCE ALL ENEMIES ARE YELLOW, SAY "You Win!"
#    def check_win_condition(): 
#        if all(enemy.color()[0] == "yellow" for enemy in enemies):
#            print("You Win!")

#ENEMY MOVEMENT START
move_enemy()

#ENEMY SPEED
def increase_enemy_speed():
    for enemy in enemies:
        current_speed = enemy.speed()
        if current_speed < 10:
            enemy.speed(current_speed + 1)
    wn.ontimer(increase_enemy_speed, 1000)
    
#INCREASE ENEMY SPEED START
increase_enemy_speed()

#ENEMY COLLISION
def check_collision():
    for enemy in enemies:
        if player.distance(enemy) < 20:
            enemy.color("yellow")
            player.goto(0, 250)
            enemy.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))
    wn.ontimer(check_collision, 100)

# COLLISION CHECK START
check_collision()   
    
#ENEMY BOUNDARY CHECK
def check_enemy_boundary():
    for enemy in enemies:
        if enemy.xcor() > BOUNDARY or enemy.xcor() < -BOUNDARY or enemy.ycor() > BOUNDARY or enemy.ycor() < -BOUNDARY:
            enemy.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))
            

            
    wn.ontimer(check_enemy_boundary, 100)

# ENEMY BOUNDARY CHECK START
check_enemy_boundary()



wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")

wn.listen()
wn.onkey(move_left, "a")
wn.onkey(move_right, "d")
wn.onkey(move_up, "w")
wn.onkey(move_down, "s")


while True:
    wn.update()
    turtle.delay(10)
