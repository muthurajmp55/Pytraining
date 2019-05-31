import turtle
pen = turtle.Turtle()
pen1 = turtle.Turtle()
paper = turtle.Screen()

pen1.up()
pen1.setx(-200)
pen1.down()
pen.color('brown')
for i in range(36):
   pen.fd(10)
   pen.right(10)
   pen1.fd(10)
   pen1.right(10)
   

