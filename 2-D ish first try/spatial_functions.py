from math import sqrt


def isoform_coordinate_creator(x_val, y_val, interval, obj_count):
    loop_count = 1000
    lap = 1
    coordinate_list = []

    coordinate_list.append([x_val, y_val])
    for i in range(1, loop_count + 1,2):
        for j in range(i):
            if obj_count > lap:
                lap = lap + 1
                y_val -= interval
                coordinate_list.append([x_val, y_val])
            else:
                break
        for j in range(i):
            if obj_count > lap:
                lap = lap + 1
                x_val -= interval
                coordinate_list.append([x_val, y_val])
            else:
                break
        for j in range(i+1):
            if obj_count > lap:
                lap = lap + 1
                y_val += interval
                coordinate_list.append([x_val, y_val])
            else:
                break
        for j in range(i+1):
            if obj_count > lap:
                lap = lap + 1
                x_val += interval
                coordinate_list.append([x_val, y_val])
            else:
                break
    return coordinate_list


def distance(obj1, obj2):
    return sqrt((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2 + (obj1.z - obj2.z) ** 2)


def partial_distance_x(obj1, obj2):
    return obj1.x - obj2.x


def partial_distance_y(obj1, obj2):
    return obj1.y - obj2.y


def partial_distance_z(obj1, obj2):
    return obj1.z - obj2.z


def collision(obj1, obj2):

    # vx
    reg1 = obj1.vx
    obj1.vx = obj2.vx
    obj2.vx = reg1

    # vy
    reg1 = obj1.vy
    obj1.vy = obj2.vy
    obj2.vy = reg1

    # vz
    reg1 = obj1.vz
    obj1.vz = obj2.vz
    obj2.vz = reg1



