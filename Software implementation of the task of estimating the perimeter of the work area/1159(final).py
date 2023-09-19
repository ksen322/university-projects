from math import sqrt, acos, cos, sin


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def d(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def minus(self, checkpoint):
        return point(self.x - checkpoint.x, self.y - checkpoint.y)


pi = acos(-1)


def area_calculator(blocks, radius):
    area, sum_of_angles = 0, 0
    points_array = [point(radius, 0)]

    for i in range(len(blocks) - 1):
        blocks_length = blocks[i]
        constricting_angle_num = (2 * radius * radius - blocks_length * blocks_length) / (2 * radius * radius)
        constricting_angle_rad = acos(
            constricting_angle_num) if constricting_angle_num <= 1 and constricting_angle_num >= -1 else 0
        sum_of_angles += constricting_angle_rad

        if sum_of_angles > 2 * pi:
            return [-1, 0]
        points_array.append(point(radius * cos(sum_of_angles), radius * sin(sum_of_angles)))

    for i in range(len(points_array)):
        area += points_array[i].x * points_array[(i + 1) % len(points_array)].y - points_array[
            (i + 1) % len(points_array)].x * points_array[i].y

    accuracy_checkpoint = point(radius, 0).minus(points_array[-1]).d()
    return [accuracy_checkpoint - blocks[-1], area / 2]


blocks_quantity = int(input())
blocks_array = []

while blocks_quantity > 0:
    block_size = int(input())
    blocks_array.append(block_size)
    blocks_quantity -= 1

blocks_array.sort()
left_border, right_border = 0, 1e6
accuracy, area_answer = 0, 0
accuracy_limit = 1e-6

for i in range(64, 0, -1):
    middle = left_border + (right_border - left_border) / 2
    accuracy, area_answer = area_calculator(blocks_array, middle)
    if blocks_array[-1] > 2 * middle or accuracy < 0:
        left_border = middle
    else:
        right_border = middle

if blocks_array[-1] >= sum(blocks_array[:-1]):
    print("0.00")
else:
    if abs(accuracy) > accuracy_limit:
        print("0.00")
    else:
        print('{0:.2f}'.format(area_answer))

