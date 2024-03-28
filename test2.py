import random
from pyclick import HumanClicker
from humancursor import SystemCursor
import time
import pyautogui


# generate random amount of points between two points - which represents
# abnormal behavior of mouse.
def generate_points_abnormal(point_1, point_2):
    num_points = random.choices([0, 1, 2, 3], weights=[30, 30, 20, 20], k=1)[0]
    points = []

    if num_points > 0:
        for _ in range(num_points):
            x = random.randint(min(point_1[0], point_2[0]), max(point_1[0], point_2[0]))
            y = random.randint(min(point_1[1], point_2[1]), max(point_1[1], point_2[1]))
            point = (x, y)
            points.append(point)

    return points


# generate random amount of points between two points - normal.
def generate_points_normal(point_1, point_2):
    num_points = random.choices([0, 1, 2, 3], weights=[60, 30, 10, 10], k=1)[0]
    points = []

    if num_points > 0:
        last_point = point_1
        for _ in range(num_points):
            x = random.randint(
                min(last_point[0] + 1, point_2[0]), max(last_point[0] + 1, point_2[0])
            )
            y = random.randint(
                min(last_point[1] + 1, point_2[1]), max(last_point[1] + 1, point_2[1])
            )
            point = (x, y)
            points.append(point)
            last_point = point

    return points


# Example usage:
point_1 = (100, 200)
point_2 = (800, 800)
# print(generate_points_abnormal(point_1, point_2))


# Example usage:
# point_1 = (100, 200)
# point_2 = (800, 800)
# print(generate_points(point_1, point_2))


def go_to_point2(point_2):

    # pass point as tuple

    hc = HumanClicker()

    x = point_2[0]
    y = point_2[1]

    # move the mouse to position (100,100) on the screen in approximately generated seconds
    hc.move((x, y), mouse_move_time())


def mouse_move_time():
    # tested
    # 90% of the time, generate a value between 0.3 and 0.8
    # 10% of the time,  generate a value between 0.8 and 2
    if random.choices([True, False], weights=[90, 10], k=1)[0]:
        move_time = random.uniform(0.3, 0.8)
    else:
        move_time = random.uniform(0.8, 2)

    return move_time


def mouse_move_sleep_time():

    # tested
    choice = random.choices([0, 1, 2], weights=[90, 5, 5], k=1)[0]

    if choice == 0:
        move_sleep_time = 0
    elif choice == 1:
        move_sleep_time = random.uniform(0, 0.05)
    else:
        move_sleep_time = random.uniform(0.05, 5)

    return move_sleep_time


# print(go_to_point2((800, 800)))

point_1 = (100, 200)
point_2 = (800, 800)


# generate random amount of points to go. With bias amount.
def generate_points_with_bias(bias_to_function1, point_1, point_2):
    functions = [
        generate_points_normal,
        generate_points_abnormal,
    ]
    chosen_function = random.choices(
        functions, weights=[bias_to_function1, 100 - bias_to_function1], k=1
    )[0]
    return chosen_function(point_1, point_2)


# this takes arguments as point_1 and point_2. and go to point_2 from point_1.
def go_to_point1_to_point2(point_1, point_2):
    points = generate_points_with_bias(90, point_1, point_2)

    time.sleep(mouse_move_sleep_time())
    for point in points:
        go_to_point2(point)
        time.sleep(mouse_move_sleep_time())

    go_to_point2(point_2)


# return the current mouse position.
def get_mouse_position():
    position = pyautogui.position()
    return (position.x, position.y)


time.sleep(2)
print(go_to_point1_to_point2(get_mouse_position(), point_2))
