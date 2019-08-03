#! /usr/bin/env python
import math

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]
q1 = 0
q2 = 0
q3 = 0
q4 = 0

# Q1 is going to be (+,+)
# Q2 is going to be (-,+)
# Q3 is going to be (-,-)
# Q4 is going to be (+,-)

# 1. Robin Hood is famous for hitting an arrow with another arrow. Did you get it?
# Robin has hit x number of arrows and which spot
robin = {}
robin_shots = []

for x in points:
    if x not in robin:
        robin[x] = 1
    else:
        if robin[x] == 1:
            robin_shots.append(x)
        robin[x] += 1

num_r_shoot = len(robin_shots)
print("Robin Hood made", num_r_shoot, "shoots!")
print("These are Robin Hood's Shots")
print(robin_shots)
print("-" * 30, "\n")

# 2. Calculate how many arrows have fallen in each quadrant.
for x, y in points:
    if x >= 0 and y >= 0:
        q1 += 1
    elif x <= 0 and y >= 0:
        q2 += 1
    elif x <= 0 and y <= 0:
        q3 += 1
    else:
        q4 += 1
print("There are", q1, "arrows in Quad 1")
print("\n There are", q2, "arrows in Quad 2")
print("\n There are", q3, "arrows in Quad 3")
print("\n There are", q4, "arrows in Quad 4")
print("-" * 30)

# 3. Find the point closest to the center. Calculate its distance to the center
# Defining a function that calculates the distance to the center can help.

centerpoint = []

for x, y in points:
    z = float(x**2) + float(y**2)
    to_center = math.sqrt(z)
    centerpoint.append(to_center)
    #print(centerpoint)

print("\nThe point closest to the center is", min(centerpoint), "\n")
print("-" * 30)

# 4. If the target has a radius of 9, calculate the number of arrows that
# must be picked up in the forest.
lost_in_woods = 0

for x , y in points:
    z = float(x**2) + float(y**2)
    to_center = math.sqrt(z)
    centerpoint.append(to_center)
    if to_center > 10:
        lost_in_woods += 1
print("There are {} arrows in the forest".format(lost_in_woods))