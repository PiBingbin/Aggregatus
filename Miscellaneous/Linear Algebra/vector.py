
class Vector(object):
    def __init__(self, coordinates):

        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple(coordinates)
            self.dimension  = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


        
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    
    def __eq__(self, v):
        return self.coordinates == v.coordinates



    def plus(self, v):
        """Adds two vectors and returns their sum vector"""

        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]

        # new_coordinates = []
        # n = len(self.coordinates)
        # for i in range(n):
        #    new_coordinates.append(self.coordinates[i] + v.coordinates[i])

        return Vector(new_coordinates)


    def minus(self, v):
        """Subtracts two vectors and returns their difference vector"""

        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]

        # new_coordinates = []
        # n = len(self.coordinates)
        # for i in range(n):
        #    new_coordinates.append(self.coordinates[i] - v.coordinates[i])

        return Vector(new_coordinates)


    def times_scalar(self, c):
        """Returns the product of a vector and a scalar"""

        new_coordinates = [ c*x for x in self.coordinates]
        return Vector(new_coordinates)






my_vector = Vector([1,2,3])
print my_vector

a = Vector([1, 5, 6])
b = Vector([5, 8, 10])

print a.plus(b)
print a.minus(b)
print a.times_scalar(3)