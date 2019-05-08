import turtle
import random

length = 884
height = 746

turtle.setup(length, height)
wn = turtle.Screen()
turtle.tracer(0, 0)
wn.title("DVD")
wn.bgcolor("black")
ball = turtle.Turtle()
ball.shape("square")
ball.color("green")
ball.speed(.1)
ball.dx = 0
ball.penup()
random_options = [.98,.99,1,1.01,1.02,1.03]
color_list = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "pink"]
x = 1
y = 1

wallCount = 0
cornerCount = 0

wordsHits = turtle.Turtle()
wordsHits.goto((length/2)*-1 + 30,(height/2)*-1 +100)
wordsHits.color("green")
wordsHits.hideturtle()
wordsHits.write("Corner Hits: {}".format(cornerCount), False)


wordsMiss = turtle.Turtle()
wordsMiss.goto((length/2)*-1 + 30,(height/2)*-1 +85)
wordsMiss.color("green")
wordsMiss.hideturtle()
wordsMiss.write("Total Hits: {}".format(wallCount), False)
difficulty = 20








def testcorner(x,y):
    global cornerCount
    global wallCount
    colorTemp = random.choice(color_list)
    ball.color(colorTemp)
    wordsMiss.color(colorTemp)
    wordsHits.color(colorTemp)
    if abs((x-((length/2)*-1 + 5))) <= difficulty and abs((y - (height/2)*-1)+10) <= difficulty:
        cornerCount = cornerCount + 1
        wordsHits.clear()
        wordsHits.write("Corner Hits: {}".format(cornerCount), False)
    elif abs((x-((length/2)*-1 + 5))) <= difficulty and abs(y - (height/2)-10) <= difficulty:
        cornerCount = cornerCount + 1
        wordsHits.clear()
        wordsHits.write("Corner Hits: {}".format(cornerCount), False)
    elif abs(x-(length/2) -15) <= difficulty and abs(y -(height/2)-10) <= difficulty:
        cornerCount = cornerCount + 1
        wordsHits.clear()
        wordsHits.write("Corner Hits: {}".format(cornerCount), False)
    elif abs(x-(length/2) -15) <= difficulty and abs((y - (height/2)*-1)+10) <= difficulty:
        cornerCount = cornerCount + 1
        wordsHits.clear()
        wordsHits.write("Corner Hits: {}".format(cornerCount), False)
    else:
        wordsHits.clear()
        wordsHits.write("Corner Hits: {}".format(cornerCount), False)
        wordsMiss.clear()
        wallCount = wallCount = wallCount + 1
        wordsMiss.write("Total Hits: {}".format(wallCount), False)
        
while True:
    turtle.update()

    
    
    ball.setx(ball.xcor() - x)
    ball.sety(ball.ycor() - y)
    if ball.xcor() <= ((length/2)*-1 + 5):
        wallCount = wallCount = wallCount + 1
        colorTemp = random.choice(color_list)
        ball.color(colorTemp)
        wordsMiss.color(colorTemp)
        wordsHits.color(colorTemp)
        wordsMiss.clear()
        wordsHits.clear()
        wordsHits.write("Corner Hits: {}".format(cornerCount), False)
        wordsMiss.write("Total Hits: {}".format(wallCount), False)
        x = float(random.choice(random_options))*-1
    if ball.xcor() >= ((length/2) -15):
        wordsMiss.clear()
        colorTemp = random.choice(color_list)
        ball.color(colorTemp)
        wordsMiss.color(colorTemp)
        wordsHits.color(colorTemp)
        wallCount = wallCount = wallCount + 1
        wordsHits.clear()
        wordsHits.write("Corner Hits: {}".format(cornerCount), False)
        wordsMiss.write("Total Hits: {}".format(wallCount), False)
        x = float(random.choice(random_options))

    print ("X = {:.2f}, Y = {:.2f}".format(ball.xcor(), ball.ycor()))
    
    if ball.ycor() <= ((height/2)*-1)+10 :
        testcorner(ball.xcor(),ball.ycor())
        y = float(random.choice(random_options))*-1
    if ball.ycor() >= ((height/2))-10 :
        testcorner(ball.xcor(),ball.ycor())
        y = float(random.choice(random_options))


    

