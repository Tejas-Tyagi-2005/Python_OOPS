# TASK - Polymorphism Practice 1
#
# Create 3 classes: Circle, Square, Triangle
# Each class has one method: draw()
#   - Circle  -> prints "Drawing a Circle"
#   - Square  -> prints "Drawing a Square"
#   - Triangle-> prints "Drawing a Triangle"
#
# Create a list with one object of each class.
# Loop through the list and call draw() on each.


class Circle():

    def draw(self):
        print(f"Drawing a Circle")   

class Square():

    def draw(self):
        print(f"Drawing a square")

class Triangle():

    def draw(self):
        print(f"Drawing a Triangle")



Shapes = [Circle(),Square(),Triangle()]


for i in Shapes:
    i.draw()

