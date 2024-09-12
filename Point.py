class Point:
    def __init__(self, x, y):
        """Initializes a 2-D point with x- and y- coordinates"""
        self.p1 = Point(3, 4)
        self.p2 = Point(5, 6)

    def __eq__(self, other):
        """ADD YOUR OWN DOCSTRING"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def equidistant(self, other):
        """ADD YOUR OWN DOCSTRING"""
        if isinstance(other, Point):
            distance_self = math.sqrt(self.x**2 + self.y**2)
            distance_other = math.sqrt(other.x**2 + other.y**2)
            return math.isclose(distance_self, distance_other)
        return False

    def within(self, distance, other):
        """ADD YOUR OWN DOCSTRING"""
        if isinstance(other, Point):
            distance_between = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
            return distance_between <= distance
        return False
