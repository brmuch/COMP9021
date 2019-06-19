# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by Ran Bai and Eric Martin for COMP9021


from math import pi, hypot


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x:.2f}, {self.y:.2f})'

class Disk:
    # replace pass above with your code
    def __init__(self, radius = 0, centre = Point()):
        if type(centre) is not Point or not isinstance(radius, int):
            raise TypeError('__init__() takes 1 positional argument but 3 were given')
        else:
            self.radius = radius
            self.centre = centre
            self.area = self.radius ** 2 * pi
             
    def change_radius(self, r):
        self.radius = r
        self.area = self.radius ** 2 * pi
        
    def intersects(self, disk):
        distance = hypot((self.centre.x - disk.centre.x),(self.centre.y - disk.centre.y))
        if distance <= self.radius + disk.radius:
            return True
        else:
            return False
        
    def absorb(self, disk):
        new_disk = Disk()
        point = Point()
        if hypot(self.centre.x - disk.centre.x,self.centre.y - disk.centre.y) + min(disk.radius, self.radius) <= max(disk.radius, self.radius):
            new_disk.radius = max(disk.radius, self.radius)
            new_disk.centre = disk.centre if disk.radius > self.radius else self.centre
            new_disk.area = new_disk.radius ** 2 * pi
        else:
            new_disk.radius = (hypot(self.centre.x - disk.centre.x, self.centre.y - disk.centre.y) + self.radius + disk.radius) / 2
            new_disk.area = new_disk.radius ** 2 * pi
            landa = (new_disk.radius - self.radius) / (new_disk.radius - disk.radius)
            point.x = (self.centre.x + landa * disk.centre.x) / (1 + landa)
            point.y = (self.centre.y + landa * disk.centre.y) / (1 + landa)
            new_disk.centre = point
        return new_disk
        
    def __repr__(self):
        return f'Disk({self.centre}, {self.radius:.2f})'

    def __str__(self):
        return f'Disk({self.centre}, {self.radius:.2f})'
            
        

            
            
