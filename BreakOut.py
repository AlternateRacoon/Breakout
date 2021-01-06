import turtle
import sys
import random


# It Creates A Window In Which We Will Be Working On
window = turtle.Screen()
window.bgcolor("black")
window.title("BreakOut")
window.tracer(0)
window.setup(width=800, height=600)

def createHurdle(x,y, color="red"):
    object = turtle.Turtle("square", visible=False)
    object.shapesize(stretch_wid=0.5, stretch_len=7)
    object.color(color)
    object.showturtle()
    object.penup()
    object.goto(x,y)
    return object
# The Player
player = turtle.Turtle("square", visible=False)
player.shapesize(stretch_wid=0.5, stretch_len=7)
player.color("white")
player.showturtle()
player.penup()
player.goto(0 , -270)

ball = turtle.Turtle("circle", visible=False)
ball.color("white")
ball.showturtle()
ball.penup()
#ball.goto(random.choice(range(1,800)), random.choice(range(1,600)))
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

def player_right():
    x = player.xcor()
    x += 20
    player.setx(x)
def player_left():
    x = player.xcor()
    x -= 20
    player.setx(x)
window.listen()
window.onkeypress(player_right, "Right")
window.onkeypress(player_left, "Left")
score = 0
allow = 0
hurdles = []
colors = ["red", "green","blue","purple","yellow","orange"]
position = [-330, 291]
positions = []
position_layer = [-330, 391]
positions_layer = []
random.shuffle(colors)
for row in colors:
    positions.append([position[0], position[1]])
    hurdle = createHurdle(position[0],position[1],color=row)
    hurdles.append(hurdle)
    position[0] += 142
random.shuffle(colors)
for row in colors:
    positions_layer.append([position_layer[0], position_layer[1]])
    hurdle = createHurdle(position_layer[0],position_layer[1],color=row)
    hurdles.append(hurdle)
    position_layer[0] += 142


while True:
    # Updates The Window
    window.update()
    # Sets The Position Of the Ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)
    if (ball.ycor() == -270):
        if (ball.xcor() <= player.xcor() - 50 and ball.xcor() >= player.xcor() + 100) or (ball.xcor() <= player.xcor() + 100 and ball.xcor() >= player.xcor() - 200):
            ball.sety(-270)
            ball.dy *= -1
        allow += 1
    if ball.ycor() > 291:
        ball.sety(291)
        ball.dy *= -1

    if ball.ycor() < -290:
        print("GAME OVER!")
        sys.exit()
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1  
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if score == 1500:
        print("YOU WIN!!")
    for row in range(len(positions)):
        hurdle = hurdles[row]
        position = positions[row]
        if ball.ycor() == position[1]:
            if (ball.xcor() <= position[0] - 50 and ball.xcor() >= position[0]) or (
                    ball.xcor() <= position[0] + 50 and ball.xcor() >= position[0]):
                hurdle.reset()
