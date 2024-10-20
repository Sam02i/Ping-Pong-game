
#? pong game in python
import turtle
#* used in basic game graphics

yn = turtle.Screen()
yn.title(" pong by sam")
#* title of game
yn.bgcolor("black")
#* background color of your game
yn.setup(width=800,height=600)
#*size of your game(when it opens)
yn.tracer(0)

#* paddle A
paddle_a = turtle.Turtle()
#* name of module and class
#! what is class?
paddle_a.speed(0)
#* speed of animation
paddle_a.shape("square")
paddle_a.color("white")
#* by default its 20x20(size of paddle)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#* where the paddle start(its starting position)
#*its the y and x coordinate

#* paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#* the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.05
ball.dy =0.05
#* every time the ball moves it moves by 2 pixels
#* d is know as delta
#* also can use xp

#*Functions
def paddle_a_up():
    y = paddle_a.ycor()
#* its a func of turtle which returns y coordinate value
    y += 20
    paddle_a.sety(y)
    
#* keyboard binding
yn.listen()
#* listen for keyboard value
yn.onkeypress(paddle_a_up,"w")

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
yn.listen()
yn.onkeypress(paddle_a_down,"s")

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
yn.listen()
yn.onkeypress(paddle_b_up,"Up")
#*you can use up and down keys as well by typing "UP","DOWN"

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
yn.listen()
yn.onkeypress(paddle_b_down,"Down")

#*pen
# pen = turtle.Turtle()
# pen.speed(0)
# pen.color()
# pen.penup()
# pen.hideturtle()
# pen.goto()

#* main game loop
while True:
    yn.update()
    #* updates game after every round
    #* move the ball
    ball.setx(ball.xcor()+ ball.dx)
    #* current x coordinate + the coordinate we specified earlier(the two pixel)
    ball.sety(ball.ycor()+ ball.dy)
    #* current y coordinate + the coordinate we specified earlier
    
    #* border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        #* since the height was 600 , then it is 300 and -300 on each side and the border must be somewhat smaller like 290
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
        #* -1 is written to keep reversing the direction of the ball
    
    if ball.xcor() > 390:
        #ball.setx(390)
        ball.goto(0,0)
        #* so that the ball will go to center when it hits the wall
        ball.dx*= -1
    if ball.xcor() < -390:
        #ball.setx(390)
        ball.goto(0,0)
        ball.dx*= -1
        
    #* paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() <350)and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() >-350)and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 ):
        ball.setx(-340)
        ball.dx *= -1
