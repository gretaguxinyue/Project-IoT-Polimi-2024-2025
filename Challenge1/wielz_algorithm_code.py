import random
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def circle_from_three(p1, p2, p3):
    ax, ay = p1
    bx, by = p2
    cx, cy = p3
    
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    if d == 0:
        return None  # Collinear points
    
    ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / d
    uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / d
    
    center = (ux, uy)
    radius = distance(center, p1)
    return center, radius

def circle_from_two(p1, p2):
    center = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    radius = distance(center, p1)
    return center, radius

def is_inside_circle(p, center, radius):
    return distance(p, center) <= radius + 1e-9  # Allow small numerical errors

def welzl_fixed(points, boundary):
    if not points or len(boundary) == 3:
        if len(boundary) == 0:
            return (0, 0), 0
        elif len(boundary) == 1:
            return boundary[0], 0
        elif len(boundary) == 2:
            return circle_from_two(boundary[0], boundary[1])
        return circle_from_three(boundary[0], boundary[1], boundary[2])
    
    p = points[-1]  # Take the last point
    center, radius = welzl_fixed(points[:-1], boundary)  # Recursive call without this point
    
    if is_inside_circle(p, center, radius):
        return center, radius
    
    return welzl_fixed(points[:-1], boundary + [p])  # Include this point in the boundary

def smallest_enclosing_circle_fixed(points):
    shuffled_points = points[:]
    random.shuffle(shuffled_points)
    return welzl_fixed(shuffled_points, [])

points = [(1, 2), (10, 3), (4, 8), (15, 7), (6, 1), (9, 12),(14,4),(3,10),(7,7),(12,14)]
center, radius = smallest_enclosing_circle_fixed(points)
print(f"Optimal Center: {center}, Minimum Maximum Distance: {radius}")
