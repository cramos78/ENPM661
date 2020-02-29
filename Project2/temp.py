import pygame as pyg
import sys
import numpy as np
from pygame.locals import *
import math as m


def GetLine(point1, point2):
    line = []
    x = point1[0]
    y = point1[1]
    while (x != point2[0] and y != point2[1]):
        if (point2[0] > point1[0]):
            x = point1[0] + 1
        if (point2[0] < point1[0]):
            x = point1[0] - 1
        if (point2[1] > point1[1]):
            y = point1[1] + 1
        if (point2[1] < point1[1]):
            y = point1[1] - 1

        line.append((x, y))
    return line


# Given a predefined map, convert to binary map to determine obstacle space (point robot radius = 0, obstacle clearance = 0)


def CreateMap():
    # Create map dictionary which holds coordinates as a tuple of ints and the pixel value of that coordinate location as an int
    map_keys = []
    for i in range(0, 200):
        for j in range(0, 300):
            map_keys.append((i, j))

    map_values = list(np.ones(300 * 200, dtype=int))
    map_space = dict(zip(map_keys, map_values))

    # Need to fill in the shapes with black pixels
    obstacles = []
    poly1 = []
    poly1_coords = [(25, 185), (75, 185), (100, 150), (75, 120), (50, 150),
                    (20, 120)]
    for n in range(0, len(poly1_coords), 2):
        print(n)
        poly1.append(GetLine(poly1_coords[n], poly1_coords[n + 1]))
    obstacles.append(poly1)

    rect = []
    rect_coords = [(30, 131), (39, 136), (104, 164), (95, 169)]
    for n in range(0, len(rect_coords), 2):
        rect.append(GetLine(rect_coords[n], rect_coords[n + 1]))
    obstacles.append(rect)

    oval = []
    oval_start = (109, 99)
    a = 40
    b = 20
    for x in range(0, (a * 2) - 1):
        oval.append((x, abs(b * m.sqrt(1 - (((x - 149)**2) / a**2)) + 99)))
        oval.append((x, -abs(b * m.sqrt(1 - (((x - 149)**2) / a**2)) + 99)))
    obstacles.append(oval)

    circle = []
    circle_start = (149, 99)
    r = 25
    for x in range(0, 25 * 2):
        circle.append(x, 50 + abs(m.sqrt(r**2 - (x - 224)**2)))
        circle.append(x, 50 + -abs(m.sqrt(r**2 - (x - 224)**2)))
    obstacles.append(circle)

    poly2 = []
    poly2_coords = [(199, 174), (224, 159), (249, 174), (224, 189)]
    for n in range(0, len(poly2_coords), 2):
        poly2.append(GetLine(poly2_coords[n], poly2_coords[n + 1]))
    obstacles.append(poly2)

    for obstacle in obstacles:
        for point in obstacle:
            map_space[point] = 0
    return map_space


# Obtaining Input from user : Start Point and Goal Point
# Check feasibility of  User Input : For start or goal nodes in obstacle
# space or outside range of binary map, inform user to redefine points try again
def GetInput(map_space):
    input_bad = True
    while (input_bad):
        start_input = input(
            "Enter the starting point of the robot within the boundaries of the map (300 by 200) in the form, x, y: "
        )
        goal_input = input(
            "Enter the goal point of the robot within the boundaries of the map (300 by 200) in the form, x, y: "
        )
        start_string = ''
        goal_string = ''
        for element in start_input:
            if element.isnumeric():
                if start_string == '':
                    start_string = element
                else:
                    start_string = start_string + ', ' + element
        for element in goal_input:
            if element.isnumeric():
                if goal_string == '':
                    goal_string = element
                else:
                    goal_string = goal_string + ', ' + element
        print(start_string)
        print(goal_string)
        start = tuple(map(int, start_string.split(', ')))
        goal = tuple(map(int, goal_string.split(', ')))
        print(start)
        print(goal)
        if (0 < (start[0] and goal[0]) < 300):
            if (0 < (start[1] and goal[1]) < 200):
                if (map_space[start] == 1):
                    if (map_space[goal] == 1):
                        input_bad = False
    return start, goal


# Implement Djikstra's Algorithm
# Implementing Backtracking (once goal node is achieved)
def Solve(start, goal):
    pass


# Using pygame implement animation of map exploration and display optimal path


def Visualize(path, map_space):
    pyg.display.init()
    map_screen = pyg.display.set_mode((300, 200))

    while (True):
        map_screen.fill((255, 255, 255))
        pyg.display.set_caption("Map")
        for key in map_space.keys():
            if map_space[key] == 0:
                map_screen.set_at(key, (0, 0, 0))
            else:
                map_screen.set_at(key, (255, 255, 255))
        for event in pyg.event.get():
            if (event.type == QUIT):
                pyg.quit()
                sys.exit()
            pyg.display.update()
    pass


#main function which calls all subfunctions necessary to solve the maze with Dijkstra's algorithm
def main():
    map_space = CreateMap()
    print(type(map_space))
    start, goal = GetInput(map_space)
    #path = Solve(start, goal)
    path = 1
    Visualize(path, map_space)


main()
