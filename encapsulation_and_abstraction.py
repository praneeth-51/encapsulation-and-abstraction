'''wrapping of variables method in a single unit is called encapsulation
public 
private
protected'''
class demo():
    def _init_(self,a,b):
       self.__a=a#private
       self._b=b#protected
class demo2(demo):
    def out(self):
        print(self._b)

d=demo2(3,4)
d.out()
