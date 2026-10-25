# Create classes Pen, Pencil and Marker, each with a write() method that prints its own message. Put one of each in a list and call write() on every item in a loop.

class Pen:
    def write(self):
        print("Writing with a pen")

class Pencil:
    def write(self):
        print("Writing with a pencil")

class Marker:
    def write(self):
        print("Writing with a marker")

items = [Pen(), Pencil(), Marker()]

for item in items:
    item.write()
