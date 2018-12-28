import turtle

class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass

class Animals(Animate):
    def breathe(self):
        print("breathe")
    def move(self):
        print("move")
    def eat_food(self):
        print("eat_food")

class Mammals(Animals):
    def feed_young_width_milk(self):
        print("feed_young_width_milk")

class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print("ddd")
        self.eat_food()
    def eat_leaves_from_trees(self):
        print("as")
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        
class ThisIsMySilyClass:
    def this_is_a_class_function():
        print("aaa")
    def this_is_also_a_class_funciton():
        print("asd")

reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()
reginald.dance_a_jig()

heaold = Giraffes()
heaold.move()

avery = turtle.Pen()
kate = turtle.Pen()
jacob = turtle.Pen()

avery.forward(50)
avery.right(90)
avery.forward(120)

kate.left(90)
kate.forward(100)

jacob.left(180)
jacob.forward(80)
