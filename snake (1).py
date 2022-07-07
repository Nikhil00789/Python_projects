# import required modules
import turtle
import time
import random

delay = 0.1
score = 0
highestscore = 0

bodies=[]

# Creating a window screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
# the width and height can be put as user's choice
s.setup(width=600, height=600)

# head of the snake
head = turtle.Turtle()
head.speed=(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht() # hide turtle
food.goto(0,200) 
food.st() # show turtle

#score board
sb= turtle.Turtle()
sb.speed(0)
sb.shape("square")
sb.color("white")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score : 0 High Score : 0")
    



# assigning key directions
def moveup():
  if head.direction != "down":
    head.direction = "up"


def movedown():
  if head.direction != "up":
    head.direction = "down"


def moveleft():
  if head.direction != "right":
    head.direction = "left"


def moveright():
  if head.direction != "left":
    head.direction = "right"

def movestop():
    head.direction="stop"


def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y+20)

  if head.direction == "down":
    y = head.ycor()
    head.sety(y-20)
  if head.direction == "left":
    x = head.xcor()
    head.setx(x-20)
  if head.direction == "right":
    x = head.xcor()
    head.setx(x+20)

#Event Handling-keyconcepts
    
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveright,"Right")
s.onkey(moveleft,"Left")
s.onkey(movestop,"space")



# Main Gameplay
while True:
  s.update()
  #this is to update the screen
  #check collison with border
  if head.xcor()>290:
       head.ht()
       head.setx(-290)
       head.st()
  if head.xcor()<-290:
       head.ht()
       head.setx(290)
       head.st()
  if head.ycor()>290:
       head.ht()
       head.sety(-290)
       head.st()
  if head.ycor()<-290:
       head.ht()
       head.sety(290)
       head.st()


  #check collision with food
  if head.distance(food)<20:
  #move the food to new random places

      x = random.randint(-290, 290)
      y = random.randint(-290, 290)
      food.goto(x, y)
   #increase the length of theSnake

      body = turtle.Turtle()
      body.speed(0)
      body.shape("square")
      body.color("red")
      body.fillcolor("black")
      body.penup()
      bodies.append(body)
   #append new body of the snake to the bodies list


   #increase the score
      score+=10
   #change delay
      delay-=0.001
   #update the highest score
      if score>highestscore:
        highestscore=score
      sb.clear()
      sb.write("Score: {}  |  Highest Score: {}".format(score,highestscore))

    # Checking for head collisions with body
  for index in range(len(bodies)-1, 0, -1):
      x = bodies[index-1].xcor()
      y = bodies[index-1].ycor()
      bodies[index].goto(x, y)

  if len(bodies) > 0:
      x = head.xcor()
      y = head.ycor()
      bodies[0].goto(x, y)
  move()
  #check collision with snake body
  for body in bodies:
      if body.distance(head) < 20:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #hide bodies
        for body in bodies:
          body.ht()
        bodies.clear()
        score = 0
        delay = 0.1

    #update Score board

        sb.clear()
        sb.write("Score: ()Highest Score: {}".format(score,highestscore))
  time.sleep(delay)

s.mainloop()


  #this is snake game
