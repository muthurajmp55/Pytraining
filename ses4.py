import turtle,time
a=input("give no :")

pen = turtle.Turtle()
paper = turtle.Screen()

x=time.time()
time.sleep(int(a))

pen.color('brown')
for i in range(36):
   pen.fd(10)
   pen.right(10)
y=time.time()
print(y-x)
 

