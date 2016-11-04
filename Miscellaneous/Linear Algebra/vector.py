from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30 

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector"
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = "No unique parallel component"
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = "No unique orthogonal component"
    def __init__(self, coordinates):

        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple([Decimal(x) for x in coordinates] )
            self.dimension  = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


        
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    
    def __eq__(self, other):
        return self.coordinates == other.coordinates



    def plus(self, other):
        """Adds two vectors and returns their sum vector"""

        new_coordinates = [x+y for x, y in zip(self.coordinates, other.coordinates)]

        # new_coordinates = []
        # n = len(self.coordinates)
        # for i in range(n):
        #    new_coordinates.append(self.coordinates[i] + v.coordinates[i])

        return Vector(new_coordinates)


    def minus(self, other):
        """Subtracts two vectors and returns their difference vector"""

        new_coordinates = [x-y for x, y in zip(self.coordinates, other.coordinates)]

        # new_coordinates = []
        # n = len(self.coordinates)
        # for i in range(n):
        #    new_coordinates.append(self.coordinates[i] - v.coordinates[i])

        return Vector(new_coordinates)


    def times_scalar(self, c):
        """Returns the product of a vector and a scalar"""

        new_coordinates = [ Decimal(c) * x for x in self.coordinates]
        return Vector(new_coordinates)


    # def magnitude_direction(self):
    #     """Returns the magnitude of a vector"""

    #     new_coordinates = [x**2 for x in self.coordinates]
    #     magnitude = sqrt(sum(new_coordinates))
    #     try:
    #         direction = [round(1.0/magnitude * x, 3) for x in self.coordinates if magnitude != 0 ]

    #     except:
    #         raise Exception("Zero Vector does not have a direction")

        
    #     return "Magnitude: {}".format(round(magnitude, 3)), "Direction: {}".format(direction)


    def magnitude(self):
        """Returns the magnitude of a vector"""
        new_coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(new_coordinates_squared))


    def normalized(self):
        """Returns the normalized vector"""
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/ Decimal(magnitude))

        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot_product(self, other):
        """Returns an inner product of two vectors"""
        return sum([ x * y for x, y in zip(self.coordinates, other.coordinates)])


    def angle_with(self, other, in_degrees=False):
        """Returns the angle between two vectors"""
        try:
            u1 = self.normalized()
            u2 = other.normalized()
            angle_in_radians = acos(u1.dot_product(u2))

            if in_degrees:
                degrees_per_radian = Decimal(180.) / Decimal(pi)
                return Decimal(angle_in_radians) * Decimal(degrees_per_radian)

            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute an angle with the zero vector")

            else:
                raise e


    def is_orthogonal_to(self, other, tolerance=1e-10):
        """Returns true if two vectors are orthogonal"""
        return self.dot_product(other) < tolerance


    def is_parallel_to(self, other):
        """Returns true if two vectors are parallel"""
       
        return (self.is_zero() or other.is_zero() or self.angle_with(other) == pi or self.angle_with(other) == 0) 

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance


    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)

            else:
                raise e

    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot_product(u)
            return u.times_scalar(weight)


        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)

            else:
                raise e 





# my_vector = Vector([1,2,3])
# print my_vector

# a = Vector([1, 5, 6])
# b = Vector([5, 8, 10])

# print a.plus(b)
# print a.minus(b)
# print a.times_scalar(3)


# c = Vector([5.581, -2.136])
# print "c", c.normalized()

# d = Vector([1.996, 3.108, -4.554])
# print "d:", d.normalized()

# e = Vector([-0.221, 7.437])
# print "e", e.magnitude()

# f = Vector([8.813, -1.331, -6.247])
# print "f", f.magnitude()

v1 = Vector([7.35, 0.221, 5.188])
v2 = Vector([2.751, 8.259, 3.985])

a = Vector([3.097, 1.879])
b = Vector([0.825, 2.036])

# print v1.dot_product(v2)
# print v1.angle_with(v2, in_degrees=True)
# print a.angle_with(b, in_degrees=False)
# print a.is_parallel_to(b)
print a.component_parallel_to(b)
print a.component_orthogonal_to(b)




