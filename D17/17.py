def make_step(x, y, x_velo, y_velo):
    # Velocity
    x += x_velo
    y += y_velo
    # Drag
    if x_velo > 0:
        x_velo -= 1
    elif x_velo < 0:
        x_velo += 1
    # Gravity
    y_velo -= 1
    return (x, y, x_velo, y_velo)


def launch(x_velo, y_velo, x1, x2, y1, y2, steps=1000):
    x, y = 0, 0  # start
    high_y = 0
    for _ in range(steps):  # try to reach the target area within 1000 steps
        x, y, x_velo, y_velo = make_step(x, y, x_velo, y_velo)
        high_y = max(y, high_y)
        if x1 <= x <= x2 and y1 <= y <= y2:
            return high_y
    return -1


_, area = open("17.txt").read().strip().split(":")
x, y = area.strip().split(",")
x, y = x.split("=")[1], y.split("=")[1]
(x1, x2), (y1, y2) = x.strip().split(".."), y.strip().split("..")
x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

highest_y = []
for y_velo in range(y1, 200):
    for x_velo in range(x2 + 1):
        high_y = launch(x_velo, y_velo, x1, x2, y1, y2)
        if high_y >= 0:
            highest_y.append(high_y)

print(f"P1: {max(highest_y)}")
print(f"P2: {len(highest_y)}")
