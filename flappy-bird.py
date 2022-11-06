import turtle as trtl
import random as rand


redbird_image = "Screen Shot 2022-10-31 at 8.02.01 AM.gif"
'''bluebird_image = "bluebird.png"'''
yellowbird_image = "realflappy_image.gif"

wn = trtl.Screen()
wn.addshape(redbird_image)
wn.addshape(yellowbird_image)
'''wn.addshape(bluebird_image)'''
wn.bgcolor("blue")
wn.setup(width=500, height=800)

fall = True

# Input Statements
bird_type = input("What type of bird would you like? [red, blue, yellow]")
###difficulty = input("What do you want your difficulty to be set to? [easy,hard]")
##time_of_day = input("What do you want your time of day to be [day,night]")

bird = trtl.Turtle()
bird.shape("circle")
bird.turtlesize(1)
bird.penup()
bird.goto(-150,0)

pipe = trtl.Turtle()
pipe.shape("square")
pipe.turtlesize(4,2)

# Game functions
def draw_bird(active_bird):
  ### set bird colors
  if bird_type == "red":
    bird.color("red")
  elif bird_type == "blue":
    bird.color("aqua")
  elif bird_type == "yellow":
   bird.color("yellow")

def bird_up():
  y = bird.ycor()
  y+=50
  bird.sety(y)
# Actions
bird.right(90)
draw_bird(bird)

bird.forward(1)

gravity = -.3


while True:
  y = bird.ycor()
  wn.onkey(bird_up, "a")
  wn.listen()
  y+=gravity
  bird.sety(y)


wn.mainloop()




import turtle as trtl
import random as rand


redbird_image = "Screen Shot 2022-10-31 at 8.02.01 AM.gif"
'''bluebird_image = "bluebird.png"'''
yellowbird_image = "realflappy_image.gif"

wn = trtl.Screen()
wn.addshape(redbird_image)
wn.addshape(yellowbird_image)
'''wn.addshape(bluebird_image)'''
wn.bgcolor("cyan")
wn.setup(width=500, height=800)

fall = True

# Input Statements
bird_type = input("What type of bird would you like? [red, blue, yellow]")
difficulty = input("What do you want your difficulty to be set to? [easy,hard]")
##time_of_day = input("What do you want your time of day to be [day,night]")

bird = trtl.Turtle()
bird.shape("circle")
bird.turtlesize(1)
bird.penup()
bird.goto(-150,0)

pipe = trtl.Turtle()
pipe.shape("square")
pipe.color("green")
pipe.penup()
pipe.goto(0,20)

bottom_pipe = trtl.Turtle()
bottom_pipe.shape("square")
bottom_pipe.color("green")
bottom_pipe.penup()
bottom_pipe.goto(0,-380)

# Game functions
def draw_pipes():
  if difficulty == 'easy':
    top_pipe_length = rand.randint(2,20)
    bottom_pipe_length = (25-top_pipe_length)
  else:
    top_pipe_length = rand.randint(2,20)
    bottom_pipe_length = (30-top_pipe_length)
  pipe.turtlesize(top_pipe_length,2)
  bottom_pipe.turtlesize(bottom_pipe_length,2)
  
def move_pipes():
  while True:
    pipe.back(1)
    bottom_pipe.back(1)
    if pipe.xcor()<-150 and bottom_pipe.xcor()<-150:
      draw_pipes()
      pipe.hideturtle()
      bottom_pipe.hideturtle()
      pipe.setx(50)
      bottom_pipe.setx(50)
      pipe.showturtle()
      bottom_pipe.showturtle()
    bird_jump()

def draw_bird(active_bird):
  ### set bird colors
  if bird_type == "red":
    bird.color("red")
  elif bird_type == "blue":
    bird.color("blue")
  elif bird_type == "yellow":
   bird.color("yellow")

def bird_up():
  y = bird.ycor()
  y+=50
  bird.sety(y)
  
def bird_jump():
  y = bird.ycor()
  wn.onkey(bird_up, " ")
  wn.listen()
  y+=gravity
  bird.sety(y)
  move_pipes()

# Actions
bird.right(90)
draw_bird(bird)

bird.forward(1)

gravity = -2

draw_pipes()


bird_jump()


wn.mainloop()
