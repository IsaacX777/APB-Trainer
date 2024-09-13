import kociemba
import random

def outerMove(cube, type, axis_list, face):
    axis_list_values = []
    for val in axis_list:
        axis_list_values.append(cube[val[0]][val[1]])
    
    face_list = [0, 1, 2, 5, 8, 7, 6, 3]
    face_list_values = []
    for val in face_list:
        face_list_values.append(cube[face][val])
    
    # 1 = normal, 2 = prime, 3 = double
    if(type == 1):
        for i in range (0, len(axis_list)):
            if(i + 3 > 11):
                cube[axis_list[i - 9][0]][axis_list[i - 9][1]] = axis_list_values[i]
            else:
                cube[axis_list[i + 3][0]][axis_list[i + 3][1]] = axis_list_values[i]
        for i in range (0, len(face_list)):
            if(i + 2 > 7):
                cube[face][face_list[i - 6]] = face_list_values[i]
            else:
                cube[face][face_list[i + 2]] = face_list_values[i]
    elif(type == 2):
        for i in range (0, len(axis_list)):
            if(i - 3 < 0):
                cube[axis_list[i + 9][0]][axis_list[i + 9][1]] = axis_list_values[i]
            else:
                cube[axis_list[i - 3][0]][axis_list[i - 3][1]] = axis_list_values[i]
        for i in range (0, len(face_list)):
            if(i - 2 < 0):
                cube[face][face_list[i + 6]] = face_list_values[i]
            else:
                cube[face][face_list[i - 2]] = face_list_values[i]
    else:
        for i in range (0, len(axis_list)):
            if(i + 6 > 11):
                cube[axis_list[i - 6][0]][axis_list[i - 6][1]] = axis_list_values[i]
            else:
                cube[axis_list[i + 6][0]][axis_list[i + 6][1]] = axis_list_values[i]
        for i in range (0, len(face_list)):
            if(i + 4 > 7):
                cube[face][face_list[i - 4]] = face_list_values[i]
            else:
                cube[face][face_list[i + 4]] = face_list_values[i]
    return cube

def sliceMove(cube, type, slice_list):
    slice_list_values = []
    for val in slice_list:
        slice_list_values.append(cube[val[0]][val[1]])
    
    if(type == 1):
        for i in range (0, len(slice_list)):
            if(i + 3 > 11):
                cube[slice_list[i - 9][0]][slice_list[i - 9][1]] = slice_list_values[i]
            else:
                cube[slice_list[i + 3][0]][slice_list[i + 3][1]] = slice_list_values[i]
    elif(type == 2):
        for i in range (0, len(slice_list)):
            if(i - 3 < 0):
                cube[slice_list[i + 9][0]][slice_list[i + 9][1]] = slice_list_values[i]
            else:
                cube[slice_list[i - 3][0]][slice_list[i - 3][1]] = slice_list_values[i]
    else:
        for i in range (0, len(slice_list)):
            if(i + 6 > 11):
                cube[slice_list[i - 6][0]][slice_list[i - 6][1]] = slice_list_values[i]
            else:
                cube[slice_list[i + 6][0]][slice_list[i + 6][1]] = slice_list_values[i]
    return cube

def invertScramble(move_list):
    move_list.reverse()
    for i in range(0, len(move_list)):
        move = move_list[i]
        
        # Account for unconventional notation
        move = move.replace("2'", '2')
        move = move.replace("3'", '')
        move = move.replace('3', "'")
        
        if "'" in move:
            move = move[:1]
        elif '2' not in move:
            move += "'"
        move_list[i] = move
    return move_list

def executeAlg(cube, move_list):
    for move in move_list:
        move = move.replace('(', '')
        move = move.replace(')', '')
        match move:
            case "L":
                cube = outerMove(cube, 1, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
            case "L'":
                cube = outerMove(cube, 2, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
            case "L2":
                cube = outerMove(cube, 3, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
            case "R":
                cube = outerMove(cube, 1, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
            case "R'":
                cube = outerMove(cube, 2, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
            case "R2":
                cube = outerMove(cube, 3, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
            case "U":
                cube = outerMove(cube, 1, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
            case "U'":
                cube = outerMove(cube, 2, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
            case "U2":
                cube = outerMove(cube, 3, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
            case "D":
                cube = outerMove(cube, 1, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
            case "D'":
                cube = outerMove(cube, 2, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
            case "D2":
                cube = outerMove(cube, 3, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
            case "F":
                cube = outerMove(cube, 1, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
            case "F'":
                cube = outerMove(cube, 2, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
            case "F2":
                cube = outerMove(cube, 3, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
            case "B":
                cube = outerMove(cube, 1, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
            case "B'":
                cube = outerMove(cube, 2, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
            case "B2":
                cube = outerMove(cube, 3, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
            case "M":
                cube = sliceMove(cube, 1, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "M'":
                cube = sliceMove(cube, 2, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "M2":
                cube = sliceMove(cube, 3, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "S":
                cube = sliceMove(cube, 1, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "S'":
                cube = sliceMove(cube, 2, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "S2":
                cube = sliceMove(cube, 3, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "E":
                cube = sliceMove(cube, 1, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "E'":
                cube = sliceMove(cube, 2, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "E2":
                cube = sliceMove(cube, 3, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "l":
                cube = outerMove(cube, 1, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
                cube = sliceMove(cube, 1, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "l'":
                cube = outerMove(cube, 2, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
                cube = sliceMove(cube, 2, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "l2":
                cube = outerMove(cube, 3, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
                cube = sliceMove(cube, 3, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "r":
                cube = outerMove(cube, 1, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = sliceMove(cube, 2, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "r'":
                cube = outerMove(cube, 2, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = sliceMove(cube, 1, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "r2":
                cube = outerMove(cube, 3, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = sliceMove(cube, 3, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "u":
                cube = outerMove(cube, 1, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = sliceMove(cube, 2, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "u'":
                cube = outerMove(cube, 2, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = sliceMove(cube, 1, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "u2":
                cube = outerMove(cube, 3, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = sliceMove(cube, 3, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "d":
                cube = outerMove(cube, 1, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
                cube = sliceMove(cube, 1, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "d'":
                cube = outerMove(cube, 2, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
                cube = sliceMove(cube, 2, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "d2":
                cube = outerMove(cube, 3, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
                cube = sliceMove(cube, 3, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "f":
                cube = outerMove(cube, 1, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
                cube = sliceMove(cube, 1, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "f'":
                cube = outerMove(cube, 2, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
                cube = sliceMove(cube, 2, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "f2":
                cube = outerMove(cube, 3, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
                cube = sliceMove(cube, 3, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "b":
                cube = outerMove(cube, 1, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
                cube = sliceMove(cube, 2, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "b'":
                cube = outerMove(cube, 2, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
                cube = sliceMove(cube, 1, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "b2":
                cube = outerMove(cube, 3, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
                cube = sliceMove(cube, 3, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "x":
                cube = sliceMove(cube, 2, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
                cube = outerMove(cube, 1, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = outerMove(cube, 2, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
            case "x'":
                cube = sliceMove(cube, 1, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
                cube = outerMove(cube, 2, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = outerMove(cube, 1, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
            case "x2":
                cube = sliceMove(cube, 3, [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
                cube = outerMove(cube, 3, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = outerMove(cube, 3, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
            case "y":
                cube = sliceMove(cube, 2, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
                cube = outerMove(cube, 1, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = outerMove(cube, 2, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
            case "y'":
                cube = sliceMove(cube, 1, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
                cube = outerMove(cube, 2, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = outerMove(cube, 1, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
            case "y2":
                cube = sliceMove(cube, 3, [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
                cube = outerMove(cube, 3, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = outerMove(cube, 3, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
            case "z":
                cube = sliceMove(cube, 1, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
                cube = outerMove(cube, 1, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
                cube = outerMove(cube, 2, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
            case "z'":
                cube = sliceMove(cube, 2, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
                cube = outerMove(cube, 2, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
                cube = outerMove(cube, 1, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
            case "z2":
                cube = sliceMove(cube, 3, [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
                cube = outerMove(cube, 3, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
                cube = outerMove(cube, 3, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
    return cube

def generateScramble(move_list):
    cube = [['U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'],
            ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
            ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
    cube = executeAlg(cube, move_list)
    compressed_cube = ''
    for face in cube:
        compressed_cube += ''.join(face)
    solution = kociemba.solve(compressed_cube)
    return invertScramble(solution.split(' '))

def selectCase():
    lxs = {}
    lxs_algs = ["U2 R U R2 U' R' U R", "U R U2 R2 U' R' U R", "U' R U R U' R2 U' R2 U R2", "U2 R D' R U R' D R'", "U R' U2 R U2 R", "R' U' R U' R U2 R", "R' U2 R2 U R' U R2 U R'", "R U' R2 U' R U R U2 R U R'", "R2 U' R2 U2 R2 U R2", "R U' R' U R U' R2 U' R U R", "U' R' U' R U' R' U R2 U R", "R U' R2 U2 R U2 R2 U' R'", "R U2 R' U R' U2 R U2 R2 U' R'", "U2 R' U' R U R2 U R' U R U' R'", "R U' R' U R U2 R2 U' R U R", "R U R' U R' U' R U R2 U R'", "U2 R U R' U R' U' R2 U R", "U R U2 R' U R' U' R2 U R", "U2 R' U2 R U2 R U' R U R'", "R U' R' U R' U' R U R", "U' R U R' U R' U' R U' R U2 R", "U2 R U R2 U' R U R2 U' R'", "U R U2 R' U2 R' U2 R2 U2 R", "U R' U' R U' R U R' U' R U2 R", "U' R U' R' U R U' R' U R' U' R U R", "U2 R2 U2 R' U' R U' R2", "U2 R U R' U R U' R'", "U R U2 R' U R U' R'", "R U2 R' U' R U R'", "U R U' R' U R U' R' U R U' R'", "U' S' R U R' U R U R' S", "R U R' S R2 S' R2", "U R' U' R2 U' R' U R U' R' U R U R", "R' U' R U R U' R U R'", "R' U' R U D' R U' R' D R", "R' U2 R U2 R U2 R U R'", "U' R' U2 R U R U R", "U' R' U R U2 R2 U2 R' U' R", "U' R' U2 R' U R U R", "U' R' U' R U R", "U' R' U2 R2 U R' U R2 U' R'", "U2 R' U' R U R U2 R U R'", "U' R U' R2 U2 R U R U R", "U2 R' U' R U R2 U' R' U' R U R'", "U' R U' R2 U' R U R", "R' U2 R2 U2 R2 U' R'", "U2 R U' R' U R' U2 R U2 R2 U' R'", "R U R' S' U2 S", "U R' U' R2 U' R' U2 R2 U' R'", "U' R U2 R2 U' R U R", "U2 R' U2 R' U2 R2 U R'", "U' R U R2 U2 R U R U R", "R U R' U' S' U2 S", "U2 R' U2 R U R U' R' U R U R", "U' R U R2 U' R U R", "R2 D R' U2 R D' R' U R'", "U2 R U' R' U' R U R'", "R U R'", "U' R U' R' U R U R'", "U' R U2 R' U R U R'", "U' R U2 R' U R' U' R U R2 U' R'", "U' R U R' U R' U' R U R2 U' R'", "R' U' R U R2 U' R'", "D' R' D R2 U' R2 D' R D", "U' R' U2 R U R' U' R U2 R", "U' R' U' R U R U' R U' R' U R U' R'", "U' R U R' U2 R' U' R2 U R", "U2 R' U2 R2 U2 R", "U' R D' R U' R' D R'", "S R2' S' R2 U R U' R'", "U R' U' R U' R U R U R", "U' R U2 R' U R' U' R' U R", "U R' U' R2 U R", "U' R' U' R' U' R U2 R", "U2 R U R' U' R' U' R U R", "U R' U' R U R U R U R'", "U2 S R2' S' R3 U2' R'", "U' R U R' U R' U' R' U R", "U' R U' R' U2 R' U' R2 U R", "U R' U' R U D' R U R' D R", "R' U' R2 U' R' U R U R", "U' R U2 R' U2 R' U' R2 U R", "R' D' R2 U R U' R2 D", "R' U' R' U R", "R U2 R2 U2 R U2 R", "U R' F R U R U' R' F' R U2 R'", "U' R U2 R' U2 R U' R'", "U' R U R' U2 R U' R'", "U R U' R'", "U' R U' R' U2 R U' R'", "U R U' R2 U' R U R U' R U R'", "U S R2' S' R2", "U R U' D' R U' R' U D R'", "U2 R U2 R' U R D' R U' R' D R'", "U2 R U R' U2 R D' R U' R' D R'", "U R' U' R' U R U R U R'", "R U' R' U R U R' U R' U' R U R", "U' R' F' R U R U' R' F", "U R' U' R U R U' R' U' R U R", "U' R U2 R' U R' U' R U R", "R' U' R U R U' R U' R' U R U R'", "U' R' U' R U R2 U R'", "U2 R' U2 R U2 R2 U R'", "R' U2 R' U2 R2 U' R'", "R U2 R' U R U2 R2 U' R U R", "R U R' U' R U R'", "R U' R' U R U2 R' U R U' R'", "R U' R2 U' R' U R", "R U R2 U2 R U2 R", "R U' R2 D' R2 U R U' R2 D", "R U' R2 U' R U R2 U' R'", "U' R' D' R U R' U' D R2 U R", "U' R U' R' U R' U' R2 U R", "R U R' U' R U' R' U R' U' R U R", "U' R U' R' U R U' R'", "R U' R' U' R U R' U2 R U' R'"]
    for i in range (0, len(lxs_algs)):
        lxs[i] = lxs_algs[i]
    
    zbll = {
        "T1": ["(U') R U R' U R U2 R' U2 R' U' R U' R' U2 R", "R' U R U2 R' U' R U' R U R' U' R' U' R U R U' R'", "(U2) R' U2 R U R' U R2 U2 R' U' R U' R'", "R U2 R' U' R U' R2 U2 R U R' U R", "R' U R U2 R' U' R U2 R' U' R U' R' U R", "(U2) R U' R' U2 R U R' U2 R U R' U R U' R'", "R' U R2 U R' U R' U' R U' R' U' R U R U' R'", "(U') R U R' U R U' R' U R' U' R2 U' R2 U2 R", "(U2) R' U2 R U R' U R U' R' U' R U' R' U2 R", "R U2 R' U' R U' R' U R U R'U R U2 R'", "(U') R' U' R2 U R2 U R2 U2 R' U R' U R ", "(U') R U R2 U' R2 U' R2 U2 R U' R U' R'"],
        "T2": ["(U) R U R' U R U R2 D' r U2 r' D R2 U R'", "(U) R' U' R U' R' U' R2 D r' U2 r D' R2 U' R", "(U2) R U' R2 D' r U2 r' D R2 U R'", "R' U R2 D r' U2 r D' R2 U' R", "R' U' R U2 R D R' U' R D' R2 U R U' R' U R", "(U') R U2 R' U' R U r' F r U2 R' r' F r", "R' U' R U R2 D' R U2 R' D R2 U2 R' U2 R", "(U) R U R' U' R U R2 D' R U' R' D R U2 R U' R'", "(U) R' D' R U' R' D R U' R U' R' U R U' R' U' R U R'", "R U' R' U R U R' U' R U R' U R' D' R U R' D R", "(U) R U R D R' U R D' R' U L' U R' U' L ", "(U2) R2 F R U R' U' R' F' R' U' R2 U2 R U2 R"],
        "T3": ["R' U R U2 L' R' U R U' L ", "R' U2 R U R2 F R U R U' R' F' R", "(U2) R' U' R2 U R' F' R U R' U' R' F R2 U' R' U' R' U R", "(U2) r U' r U2 R' F R U2 r2 F", "(U') R' U' R' D' R U R' D R U2 R U R' U R", "R' U' R y R U R' U' R l U' R' U l'", "(U) L' U2 R U2 R' U2 L U R U R' U' R U' R'", "F U' R' U2 R U F' R' U' R U R' U R", "(U2) R' U' R U' R' U R F U' R' U2 R U F'", "R U R' U R U' R' U' L' U2 R U2 R' U2 L", "R' U2 R U R' U R F U R U2 R' U R U R' F'", "r' U' l' U2 R U' R' U2 l R U' R' U2 r"],
        "T4": ["(U') l' U2 R' D2 R U2 R' D2 R2 x'", "R' U2 R U' R' F R U R' U' R' F' R U' R", "R' U2 R' D' R U2 R' D R' U R' U R U2 R'", "(U2) R U2 R D R' U2 R D' R U' R U' R' U2 R", "R' D' R U R' D R U2 R U2 R' U R U R'", "(U) R' U' R' D' R U R' D R U' R U' R' U2 R", "R' U R2 D R' U R D' R' U R' U' R U' R' U' R ", "(U2) R U' R2 D' R U' R' D R U' R U R' U R U R'", "(U) R' U' R U' F U' R' U R U F' R' U R", "R' D' R U R' D R2 U R' U2 R U' R' U' R U' R'", "(U2) F R U R' U' R U' R' U' R U R' F'", "(U') R U R' U2 R U' R' U2 R U' R2 F' R U R U' R' F"],
        "T5": ["R U R D R' U' R D' R2", "(U') R U2 R' U2 R' F R U R U' R' F'", "(U2) R2 B2 R' U2 R' U2 R B2 R' U R U' R'", "(U') R' D' R U R' D R2 U' R' U R U R' U' R U R'", "(U') F' U' r' F2 r U' r' F' r F ", "(U') R U R' U' R U' R' L U' R U R' L'", "(U) R U R' U R U R' U2 L R U' R' U L'", "R' U' R U' R2' F' R U R U' R' F U R U' R' U2 R", "(U) R' U' R U R' U' R2 D R' U2 R D' R' U R' U R", "(U2) R U R D R' U2 R D' R' U' R' U R U' R' U' R U' R'", "(U2) F R U R' U' R' F' U2 R U R U' R2 U2 R", "(U') R U' R' U' R U R D R' U2 R D' R' U' R'"],
        "T6": ["x' U' R' D R U R' D' R x", "(U) R U R' U' R' F' R U2 R U2 R' F", "R2 F2 R U2 R U2 R' F2 R U' R' U R", "(U') R D R' U' R D' R2 U R U' R' U' R U R' U' R", "(U) F U R U2 R' U R U R' F'", "R U R' U' R U' R'  U' F R U R' U' R' F' R", "(U) R' U' R U' R' U' R U2 L' R' U R U' L", "(U) F R U R' U' R U R' U' F' R U R' U' R' F R F'", "(U) R U R' U' R U R2 D' R U2 R' D R U' R U' R'", "R' U2 R F U' R' U R U F' R' U R", "(U) R' U2 R2 U R' U' R' U2 F' R U2 R U2 R' F", "(U') R' U R U R' U' R' D' R U2 R' D R U R"],
    }
    allowedZbll = ['T1', 'T2', 'T3', 'T4']
    test = zbll[allowedZbll[random.randint(0, len(allowedZbll) - 1)]][random.randint(0, 11)]
    
    lxs_case = lxs[random.randint(0, 115)]
    print(lxs_case)
    move_list = invertScramble(test.split(' ')) + invertScramble(lxs_case.split(' '))
    scramble = generateScramble(move_list)
    for move in scramble:
        print(move, end=' ')
        
def testMove():
    generateScramble(["S'"])

selectCase()
#testMove()

    