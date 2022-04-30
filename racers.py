import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red','green','blue','orange','yellow','black','pink','brown','cyan','purple']

def get_num_of_racers():
    racers = 0
    while True:
        racers = input("Ingiza Idadi ya washindanaji kati ya 2 - 10: ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Tafadhali ingiza namba .... Jaribu tena: ")
            continue
        if(2<= racers <=10):
            return racers
        else:
            print("Namba kati ya 2-10 .... Jaribu tena")

def race(color):
  turtles  =    create_turtle(colors)
  while True:
      for racer in turtles:
          distance = random.randrange(1,20)
          racer.forward(distance)
          x,y = racer.pos()
          if y >= HEIGHT // 2 -10:
              return colors[turtles.index(racer)]



            

def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        racer  = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2  + (i + 1)* spacingx,  -HEIGHT // 2 + 20 )
        racer.pendown()
        turtles.append(racer)
    return turtles
    
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Mbio za Kobe")
racers  = get_num_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers ]
create_turtle(colors)
winner = race(colors) 
print("Kobe mwenye rangi ya " ,winner , "ndio mshindi wetu")
# racer = turtle.Turtle()

# racer.speed(1)
# racer.shape('turtle')
# racer.color('red')
# racer.penup()
# racer.forward(100)
# racer.left(90)
# racer.pendown()
# racer.forward(100)
# racer.right(90)
# racer.backward(100)
# # time.sleep(29)

# racer2 = turtle.Turtle()
# racer2.speed(1)
# racer2.shape('turtle')
# racer2.color('cyan')
# racer2.penup()
# racer2.forward(150)
# racer2.left(90)
# racer2.pendown()
# racer2.forward(150)
# racer2.right(90)
# racer2.backward(150)

