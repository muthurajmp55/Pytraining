class A:
    def go(self):
        print ("A go")
    def stop(self):
        print ("A stop")
    def pause(self):
        print("A wait")
class B(A):
    def go(self):

        print("b go")
        super(B, self).go()
    def stop(self):
        super(B, self).stop()
        print("b stop")

class C(B):
    pass


a=A()
b=B()
c=C()
a.go()
a.stop()

b.go()
b.stop()
b.pause()
c.pause()
