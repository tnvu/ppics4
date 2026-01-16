# Review Questions

# True/False
# 1.    Using graphics.py allows graphics to be drawn in a Python
#       shell window.                                                   False
# 2.    Traditionally, the upper-left corner of a graphics window has
#       coordinates (0,0).                                              True
# 3.    A single point on a graphics screen is called a pixel.          True
# 4.    A function that creates a new instance of a class is called
#       an accessor.                                                    False
# 5.    Instance variables are used to store data inside an object.     True
# 6.    The statement myShape.move(10, 20) moves myShape to the
#       point (10, 20).                                                 False
# 7.    Aliasing occurs when two variables refer to the same object.    True
# 8.    The copy method is provided to make a copy of a graphics
#       object.                                                         False
# 9.    A graphics window always has the title “Graphics Window.”       False
# 10.   The method in the graphics library used to get a mouse click
#       is readMouse.                                                   False

# Multiple Choice
# 1.    A method that returns the value of an object’s instance variable is
#       called a(n)
#       a) mutator
#       b) function
#       c) constructor
#     X d) accessor
# 2.    A method that changes the state of an object is called a(n)
#       a) stator
#     X b) mutator
#       c) constructor
#       d) changor
# 3.    What graphics class would be best for drawing a square?
#       a) Square
#       b) Polygon
#       c) Line
#     X d) Rectangle
# 4.    What command would set the coordinates of win to go from (0,0) in the
#       lower-left corner to (10,10) in the upper-right?
#       a) win.setCoords(Point (0, 0), Point(10, 10))
#       b) win.setCoords((0, 0), (10, 10))
#     X c) win.setCoords(0, 0, 10, 10)
#       d) win.setCoords(Point (10, 10), Point(0, 0))
# 5.    What expression would create a line from (2,3) to (4,5)?
#       a) Line(2, 3, 4, 5)
#       b) Line((2, 3), (4, 5))
#       c) Line(2, 4, 3, 5)
#     X d) Line(Point (2, 3), Point(4, 5))
# 6.    What command would be used to draw the graphics object shape into the
#       graphics window win?
#       a) win.draw(shape)
#       b) win.show(shape)
#       c) shape.draw()
#     X d) shape.draw(win)
# 7.    Which of the following computes the horizontal distance between points
#       p1 and p2?
#       a) abs(p1-p2)
#       b) p2.getX() - pl.getX()
#       c) abs(pl.getY() - p2.getY())
#     X d) abs(pl.getX() - p2.getX())
# 8.    What kind of object can be used to get text input in a graphics window?
#       a) Text
#     X b) Entry
#       c) Input
#       d) Keyboard
# 9.    A user interface organized around visual elements and user actions is
#       called a(n)
#     X a) GUI
#       b) application
#       c) windower
#       d) API
# 10.   What color is color rgb(0,255,255)?
#       a) yellow
#     X b) cyan
#       c) magenta
#       d) orange

# Discussion
# 1.    Pick an example of an interesting real-world object and describe it as
#       a programming object by listing its data (attributes, what it “knows”)
#       and its methods (behaviors, what it can “do”).
#       - Car Stereo
#           - Data
#               - Station
#               - Volume
#           - Methods
#               - Change station
#               - Change volume
# 2.    Describe in your own words the object produced by each of the
#       following operations from the graphics module. Be as precise as you
#       can. Be sure to mention such things as the size, position, and
#       appearance of the various objects. You may include a sketch if that
#       helps.
#       a) Point(130, 130)
#           Point located at x=130, y=130
#       b) c = Circle(Point (30, 40), 25)
#          c.setFill("blue")
#          c.setOutline("red")
#           Circle with a center at (30, 40) and a radius of 25, filled blue
#           with a red outline
#       c) r = Rectangle(Point(20, 20), Point(40, 40))
#          r.setFill(color_rgb(0, 255, 150))
#          r.setWidth(3)
#           Square with upper-left corner at (20, 20) and side 20. Filled with
#           RGB(0, 255, 150) and border width 3.
#       d) l = Line(Point (100, 100), Point(100, 200))
#          l.setOutline("red4")
#          l.setArrow("first")
#           Vertical line from (100, 100) to (100, 200)
#           Outline is red4 and arrow pointing down
#       e) Oval(Point(50, 50), Point(60, 100))
#           Oval bound by the rectangle defined by (50, 50) and (60, 100)
#       f) shape = Polygon(Point(5, 5), Point(10, 10),
#                          Point(5, 10), Point(10, 5))
#          shape.setFill("orange")
#           Four corner polygon filled with orange
#       g) t = Text(Point(100, 100), "Hello World!")
#          t.setFace("courier")
#          t.setSize(16)
#          t.setStyle("italic")
#           "Hello World" centered on (100, 100) with courier font size 16 and
#           italicized.
# 3.    Describe what happens when the following interactive graphics program
#       runs:
#           from graphics import *
#           def main():
#               win = GraphWin()
#               shape = Circle(Point (50, 50), 20)
#               shape.setOutline("red")
#               shape.setFill("red")
#               shape.draw(win)
#               for i in range(10):
#                   p = win.getMouse()
#                   c = shape.getCenter()
#                   dx = p.getX() - c.getX()
#                   dy = p.getY() - c.getY()
#                   shape.move (dx, dy)
#               win.close()
#           main()
#       A circle is drawn and moved to wherever the mouse pointer clicks
