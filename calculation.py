# Import
import random

# Random points in the square
def calculate_random_points_2d(n=1000):
    # List of points
    rand_points = []
    for i in range(n):
        rand_points.append((random.random(), random.random()))
    # Check if point is inside the circle area
    def point_in_circle(point):
        return (point[0], point[1], point[0]**2 + point[1]**2 <= 1)
    rand_points = list(map(point_in_circle, rand_points))
    pi = 4*(len([num for num in rand_points if num[-1]]) / len(rand_points))
    return rand_points, pi

# Random points in the square
def calculate_random_points_3d(n=1000):
    # List of points
    rand_points = []
    for i in range(n):
        rand_points.append((random.random(), random.random(), random.random()))
    # Check if point is inside the circle area
    def point_in_circle(point):
        return (point[0], point[1], point[2], point[0]**2 + point[1]**2 + point[2]**2 <= 1)
    rand_points = list(map(point_in_circle, rand_points))
    pi = 6*(len([num for num in rand_points if num[-1]]) / len(rand_points))
    return rand_points, pi


