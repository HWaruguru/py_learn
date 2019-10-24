# Two classes have been declared:
class Car(object):
    def m1(self):
        print('car 1')
    def m2(self):
        print('car 2')
    def __str__(self):
        return "vroom"

class Truck (Car):
    def m1(self):
        print('truck 1')
    def m2(self):
        super(Truck, self).m1()
    def __str__(self):
        return super(Truck, self).__str__() + super(Truck, self).__str__()
# Write a class MonsterTruck whose methods have the behavior below.
# Use Inheritance to reuse behavior from the superclass.

#  Method 	     Output/Return
# =========    ==============
#   m1() 	      monster 1
#   m2() 	      truck 1 car 1
#   toString()    "monster vroomvroom" 

# for more info on this quiz, go to this url: http://www.programmr.com/monstertruck
