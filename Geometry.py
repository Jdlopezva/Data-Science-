Run code block in SymPy Live
from sympy import *
from sympy.geometry import *
x = Point(0, 0)
y = Point(1, 1)
z = Point(2, 2)
zp = Point(1, 0)
Point.is_collinear(x, y, z)
True
Point.is_collinear(x, y, zp)
False
t = Triangle(zp, y, x)
t.area
1/2
t.medians[x]
Segment2D(Point2D(0, 0), Point2D(1, 1/2))
m = t.medians
intersection(m[x], m[y], m[zp])
[Point2D(2/3, 1/3)]
c = Circle(x, 5)
l = Line(Point(5, -5), Point(5, 5))
c.is_tangent(l) # is l tangent to c?
True
l = Line(x, y)
c.is_tangent(l) # is l tangent to c?
False
intersection(c, l)
[Point2D(-5*sqrt(2)/2, -5*sqrt(2)/2), Point2D(5*sqrt(2)/2, 5*sqrt(2)/2)]

Run code block in SymPy Live
>>> from sympy import symbols
>>> from sympy.geometry import Point, Triangle, intersection

>>> a, b = symbols("a,b", positive=True)

>>> x = Point(0, 0)
>>> y = Point(a, 0)
>>> z = Point(2*a, b)
>>> t = Triangle(x, y, z)

>>> t.area
a*b/2

>>> t.medians[x]
Segment2D(Point2D(0, 0), Point2D(3*a/2, b/2))

>>> intersection(t.medians[x], t.medians[y], t.medians[z])
[Point2D(a, b/3)] 

