import turtle
pen = turtle.Turtle()
pen1 = turtle.Turtle()
paper = turtle.Screen()



pen.color('brown')
for i in range(36):
   if i > 18:
     pen.color('red')
   pen.fd(10)
   pen.right(10)

pen1.setx(-100)
pen1.color('blue')
for i in range(36):
   if i > 18:
      pen1.color('red')
   pen1.fd(10)
   pen1.right(10)

pen.up()
pen.left(500)
pen.setx(100)
pen.down()
color=['blue','red','black','yellow']
i=0
while i < 4:
    if i < 2:
     pen.color(color[i])
    if i == 2:
     pen.color(color[0])
    if i == 3:
     pen.color(color[1])
    pen.fd(100)
    pen.right(90)
    i = i+1

    
pen.up()
pen.right(90)
pen.setx(500)
pen.down()
colors=['blue','red','black','yellow']
for i in colors:
     pen.color(i)
     pen.fd(100)
     pen.right(90)




