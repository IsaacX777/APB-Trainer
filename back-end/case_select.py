import kociemba
import random

def outerMove(cube, type, axis_list, face):
    # Get colors for the moving pieces
    axis_list_values = []
    for val in axis_list:
        axis_list_values.append(cube[val[0]][val[1]])

    # Clockwise order of pieces on the face being turned
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
    # Get colors for moving pieces
    slice_list_values = []
    for val in slice_list:
        slice_list_values.append(cube[val[0]][val[1]])

    # 1 = normal, 2 = prime, 3 = double
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
    # Execute each move in order
    for move in move_list:
        # Account for AUF notation
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
    # Create solved cube
    cube = [['U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'],
            ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
            ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]

    # Set cube to selected case
    cube = executeAlg(cube, move_list)

    # Find solution and inverse it to get the scramble
    compressed_cube = ''
    for face in cube:
        compressed_cube += ''.join(face)
    solution = kociemba.solve(compressed_cube)
    return invertScramble(solution.split(' '))

def selectCase(algSet, selectedCases):
    # List of all available algorithms
    algs = {
        'lxs': {
            'UFR': ["(U2) R U R2 U' R' U R", "(U) R U D' R U R' D R'", "(U') R U R U' R2 U' R2 U R2", "(U2) R D' R U R' D R'", "(U) R' U2 R U2 R", "R' U' R U' R U2 R", "(U) R U2 R2 U' R U R2 U' R'", "R U' R2 U' R U R U2 R U R'", "R2 U' R2 U2 R2 U R2", "R U' R' U R U' R2 U' R U R", "(U') R' U' R U' R' U R2 U R", "R U' R2 U2 R U2 R2 U' R'", "R U2 R' U R' U2 R U2 R2 U' R'", "R U R2 U2’ R' U2 R2 U' R'", "R U' R' U R U2 R2 U' R U R", "R U R' U R' U' R U R2 U R'", "(U2) R U R' U R' U' R2 U R", "(U) R U2 R' U R' U' R2 U R", "(U2) R' U2 R U2 R U' R U R'", "R U' R' U R' U' R U R", "(U') R U R' U R' U' R U' R U2 R", "(U2) R U R2 U' R U R2 U' R'", "R S' R U' R' f R' F' R U' R'", "(U) R' U' R U' R U R' U' R U2 R", "(U) R' U2 R' U2 R2 U2 R'", "(U2) R2 U2 R' U' R U' R2", "(U2) R U R' U R U' R'", "(U) R U2 R' U R U' R'", "R U2 R' U' R U R'", "(U) R U' R' U R U' R' U R U' R'"],
            'RFU': ["(U') S' R U R' U R U R' S", "R U R' S R2 S' R2", "(U') R U' R' U R U R' S R2' S' R2", "R' U' R U R U' R U R'", "R D' R U' R' D U R'", "(U) R U R2 U2' R' U2 R2 U R'", "(U') R' U2 R U R U R", "(U') R' U R U2 R2 U2 R' U' R", "(U') R' U2 R' U R U R", "(U') R' U' R U R", "(U') R' U2 R2 U R' U R2 U' R'", "(U2) R' U' R U R U2 R U R'", "(U') R U' R2 U2 R U R U R", "(U2) R' U' R U R2 U' R' U' R U R'", "(U') R U' R2 U' R U R", "R' U2 R2 U2 R2 U' R'", "(U2) R U' R' U R' U2 R U2 R2 U' R'", "R U R' S' U2 S", "(U) R' U' R2 U' R' U2 R2 U' R'", "(U') R U2 R2 U' R U R", "(U2) R' U2 R' U2 R2 U R'", "(U') R U R2 U2 R U R U R", "R U R' U' S' U2 S", "(U2) R' U2 R U R U' R' U R U R", "(U') R U R2 U' R U R", "R2 D R' U2 R D' R' U R'", "(U2) R U' R' U' R U R'", "R U R'", "(U') R U' R' U R U R'", "(U') R U2 R' U R U R'"],
            'FUR': [],
            'DFR': [],
            'RDF': [],
            'FRD': []
        },
        'eo_pair': {
            '':[],
        },
        'zbll': {
            'T1': ["(U') R U R' U R U2 R' U2 R' U' R U' R' U2 R", "R' U R U2 R' U' R U' R U R' U' R' U' R U R U' R'", "(U2) R' U2 R U R' U R2 U2 R' U' R U' R'", "R U2 R' U' R U' R2 U2 R U R' U R", "R' U R U2 R' U' R U2 R' U' R U' R' U R", "(U2) R U' R' U2 R U R' U2 R U R' U R U' R'", "R' U R2 U R' U R' U' R U' R' U' R U R U' R'", "(U') R U R' U R U' R' U R' U' R2 U' R2 U2 R", "(U2) R' U2 R U R' U R U' R' U' R U' R' U2 R", "R U2 R' U' R U' R' U R U R'U R U2 R'", "(U') R' U' R2 U R2 U R2 U2 R' U R' U R ", "(U') R U R2 U' R2 U' R2 U2 R U' R U' R'"],
            'T2': ["(U) R U R' U R U R2 D' r U2 r' D R2 U R'", "(U) R' U' R U' R' U' R2 D r' U2 r D' R2 U' R", "(U2) R U' R2 D' r U2 r' D R2 U R'", "R' U R2 D r' U2 r D' R2 U' R", "R' U' R U2 R D R' U' R D' R2 U R U' R' U R", "(U') R U2 R' U' R U r' F r U2 R' r' F r", "R' U' R U R2 D' R U2 R' D R2 U2 R' U2 R", "(U) R U R' U' R U R2 D' R U' R' D R U2 R U' R'", "(U) R' D' R U' R' D R U' R U' R' U R U' R' U' R U R'", "R U' R' U R U R' U' R U R' U R' D' R U R' D R", "(U) R U R D R' U R D' R' U L' U R' U' L ", "(U2) R2 F R U R' U' R' F' R' U' R2 U2 R U2 R"],
            'T3': ["R' U R U2 L' R' U R U' L ", "R' U2 R U R2 F R U R U' R' F' R", "(U2) R' U' R2 U R' F' R U R' U' R' F R2 U' R' U' R' U R", "(U2) r U' r U2 R' F R U2 r2 F", "(U') R' U' R' D' R U R' D R U2 R U R' U R", "R' U' R y R U R' U' R l U' R' U l'", "(U) L' U2 R U2 R' U2 L U R U R' U' R U' R'", "F U' R' U2 R U F' R' U' R U R' U R", "(U2) R' U' R U' R' U R F U' R' U2 R U F'", "R U R' U R U' R' U' L' U2 R U2 R' U2 L", "R' U2 R U R' U R F U R U2 R' U R U R' F'", "r' U' l' U2 R U' R' U2 l R U' R' U2 r"],
            'T4': ["(U') l' U2 R' D2 R U2 R' D2 R2 x'", "R' U2 R U' R' F R U R' U' R' F' R U' R", "R' U2 R' D' R U2 R' D R' U R' U R U2 R'", "(U2) R U2 R D R' U2 R D' R U' R U' R' U2 R", "R' D' R U R' D R U2 R U2 R' U R U R'", "(U) R' U' R' D' R U R' D R U' R U' R' U2 R", "R' U R2 D R' U R D' R' U R' U' R U' R' U' R ", "(U2) R U' R2 D' R U' R' D R U' R U R' U R U R'", "(U) R' U' R U' F U' R' U R U F' R' U R", "R' D' R U R' D R2 U R' U2 R U' R' U' R U' R'", "(U2) F R U R' U' R U' R' U' R U R' F'", "(U') R U R' U2 R U' R' U2 R U' R2 F' R U R U' R' F"],
            'T5': ["R U R D R' U' R D' R2", "(U') R U2 R' U2 R' F R U R U' R' F'", "(U2) R2 B2 R' U2 R' U2 R B2 R' U R U' R'", "(U') R' D' R U R' D R2 U' R' U R U R' U' R U R'", "(U') F' U' r' F2 r U' r' F' r F ", "(U') R U R' U' R U' R' L U' R U R' L'", "(U) R U R' U R U R' U2 L R U' R' U L'", "R' U' R U' R2' F' R U R U' R' F U R U' R' U2 R", "(U) R' U' R U R' U' R2 D R' U2 R D' R' U R' U R", "(U2) R U R D R' U2 R D' R' U' R' U R U' R' U' R U' R'", "(U2) F R U R' U' R' F' U2 R U R U' R2 U2 R", "(U') R U' R' U' R U R D R' U2 R D' R' U' R'"],
            'T6': ["x' U' R' D R U R' D' R x", "(U) R U R' U' R' F' R U2 R U2 R' F", "R2 F2 R U2 R U2 R' F2 R U' R' U R", "(U') R D R' U' R D' R2 U R U' R' U' R U R' U' R", "(U) F U R U2 R' U R U R' F'", "R U R' U' R U' R'  U' F R U R' U' R' F' R", "(U) R' U' R U' R' U' R U2 L' R' U R U' L", "(U) F R U R' U' R U R' U' F' R U R' U' R' F R F'", "(U) R U R' U' R U R2 D' R U2 R' D R U' R U' R'", "R' U2 R F U' R' U R U F' R' U R", "(U) R' U2 R2 U R' U' R' U2 F' R U2 R U2 R' F", "(U') R' U R U R' U' R' D' R U2 R' D R U R"],

            'U1': ["(U) R U2 R' U' R U' R' U2 R' U2 R U R' U R", "R U R' U' R U' R U2 R2 U' R U R' U' R2 U' R2", "R' U' R U' R' U2 R2 U R' U R U2 R'", "(U2) R U R' U R U2 R2 U' R U' R' U2 R", "(U') R U R' U' R U' R' U2 R U' R' U2 R U R'", "(U') R' U' R U R' U R U2 R' U R U2 R' U' R", "(U) R U2 R2 U' R2 U' R' U R' U' R U R' U R", "(U) R' U2 R2 U R2 U R U' R U R' U' R U' R'", "(U) R' U2 R U R' U R U R' U' R U' R' U2 R", "(U) R U2 R' U' R U' R' U' R U R' U R U2 R'", "R' U' R U' R U2 R2 U' R2 U' R2 U R", "(U2) R U R' U R' U2 R2 U R2 U R2 U' R'"],
            'U2': ["(U2) R' U' R U' F U' R' U R U R' U R U' F'", "R U R' U L' U R U' M' x' U' R U' R'", "(U') R U2 R2 F R F' M' U' R U' R' U M", "(U') R' U2 R F U' R' U R U R' U R U' F'", "(U2)  R2 D R' U' R D' R' U' R' U R U R'", "R2 D' R U R' D R U R U' R' U' R", "R U' R' U' R U R D R' U R D' R2", "(U2) R' U R U R' U' R' D' R U' R' D R2", "M U' M' F R U R' U' F' M U M'", "(U') F R U R' U' R U R' U' F' U' R' F' U' F U R", "F R U' R' U' R U2 R' U' R U' R' U' R U2 R' U' F'", "(U) r' U' R' F R U r F R U' R' F'"],
            'U3': ["R' F R U' R' U' R U R' F' R U R' U' R' F R F' R", "(U') F2 R U' R' U' R U R' F' R U R' U' R' F R F2", "R U' R' U R U' L U r' F U2 R U2 R2 x", "(U) R' U R U R' F' R U R' U' R' F R2 U' R' U2 R U' R' U2 R", "(U) R U' L U L' U R' U' l U2 R U2 R2 x", "(U) R' U L' U' L U' R U l' U2 R' U2 R2 x'", "F R U R U2 R' U' R U' R' U2 R' U2 R U' R' U' F'", "(U') r U R' U' r' F R2 U' R' U' R U2 R' U' F'", "(U) F U R U2 R' U R U R2 F' r U R U' r'", "(U') R U2 R' U2 R' F R U R U2 R' U' R U2 R' U' F'", "(U') R' U' R F R2 D' R U R' D R2 U' F'", "(U') r U R' U' r' F R U R' U' R F' R' U R"],
            'U4': ["x R2 U2 R' D2 R U2 R' D2 R' x'", "(U2) x R2 D2 R U2 R' D2 R U2 l", "R U R' U R U' R' U2 R' D' R U2 R' D R2 U' R'", "(U') R' U2 R U R' U R' D R' U2 R D' R' U2 R'", "(U') R U' R' U' R U' R' U R' D' R U R' D R2 U R'", "(U') R' U R U R' U R U' R D R' U' R D' R2 U' R", "R' U2 R U R' U R' D' R U' R' D R U R", "R U' R' U' R U2 R' U2 R' D' R U' R' D R", "R' U' R U2 R' F' R U R' U' R' F R2 U2 R' U R", "(U2) R U R' U R U R' U2 R U' R2 D' R U' R' D R", "F R U' R' U R U R' U R U' R' F'", "(U) F' R U R' U' R' F R2 U R' U2 R U R' U2 R U' R'"],
            'U5': ["R2 D' r U2 r' D R U2 R", "R2 D' R U2 R' D R U2 R", "R U' R' D R' U' R D' R2 U R' U' R' U2 R'", "(U2) R U R' U R U2 R2 U z U R' D R U' z'", "(U) R2 D' R U' R' D R2 U' R' U2 R", "(U') R' U R U R' U2 R U2 y R U' R' U2 R U' R'", "(U') R2 D R' U R D' R2 U' R U' R' U2 R U' R' U2 R U R'", "(U) R U L' U R' U' L U' R U R' U R U' R'", "(U') R' U2 R2 D R' U2 R D' R2 U R U2 R' U2 R", "(U') R U R' U2 F2 R U2 R' U2 R' F2 R2 U R'", "(U') R' U2 R' D' R U2 R' D R U2 R U R' U R", "(U') R' U R U' R' U' R U2 R D R' U' R D' R2 U' R"],
            'U6': ["R' U2 R U R2 F' R U R U' R' F R", "(U2) R2 D R' U2 R D' R' U2 R'", "R' U' R U R U R' U' R' U F R U R U' R' F'", "R U' R' U' R U2 R' U' R' D' R U2 R' D R", "(U) R U R2 D' R U R' D R2 U2 R'", "(U') R U' R' U' R U2 R' U2 y' R' U R U2 R' U R", "(U) R' U R' U' D' R U' R' U2 R U' R' D R U' R", "(U) R' U' L U' R U L' U R' U' R U' R' U R", "(U') R' U' R U R' U R U2 F R' U R U' F' R' U2 R", "(U) R U R' U R U' R' U R U' R' U' L' U R U' R' L", "(U') R U2 R D R' U2 R D' R' U2 R' U' R U' R'", "(U') R U' R' U R U R' U2 R' D' R U R' D R2 U R'"],
        
            'L1': ["R U2 R' U2 R' U' R U R U' R' U2 R' U2 R", "R U R' U R U' R' U R U' R' U R U2 R'", "(U2) R U2 R' U' R U' R' U2 R U R' U R U2 R'", "(U2) R U R' U R U2 R' U2 R U2 R' U' R U' R'", "R2 U R' U R' U' R U' R' U' R U R U' R2", "(U') R2 U' R U' R U R' U R U R' U' R' U R2", "(U) R' U2 R U R' U R U' R U2 R' U' R U' R'", "(U2) R U2 R' U' R U' R' U R' U2 R U R' U R", "(U) R2 U R' U' R' U R U R' U R U' R U' R2", "(U2) R2 U' R U R U' R' U' R U' R' U R' U R2", "(U2) R U R' U R U2 R' U R' U' R U' R' U2 R", "(U) R' U' R U' R' U2 R U' R U R' U R U2 R'"],
            'L2': ["F R U' R' U' R U R D R' U' R D' R' U2 R' U' F'", "(U) F R U R' U' R U' R' U2 R U2 R' U' F'", "L' U2 R U' R' U2 L R U' R'", "R' U' R U R' F' R U R' U' R' F R2", "F R U R' U' R' F R2 U' R' U' R U R' F2", "R' U' R U R' U' R' F R2 U' R' U' R U R' F' U R", "(U) r U2 R r2 F R' F' r2 U2 r'", "(U2) r U2 r2 F R F' r2 R' U2 r'", "(U2) F R U R' U' F' r U r' U R U' R' r U' r'", "(U) r U r' R U R' U' r U' r' F U R U' R' F'", "(U) R U2 R' U' L' U2 R U R' L U L' U L", "(U) R U R' U' R' U2 R' U D R' U' R U2 D' R"],
            'L3': ["(U') F' r U R' U' r' F R", "R' U' R U R' F2 R U2 R' U2 R' F2 R2", "(U') F' R U2 R' U2 R' F R U R U' R'", "(U) R' U R U' R' U R U R' U' R2 D R' U R D' R'", "F R U' R' U' R U2 R' U' F'", "(U2) R' U' R U2 R' F' R U R' U' R' F R2 U R' U2 R", "R' F R U R U' R' F' U R U R' U R U' R'", "R' U R U2 R' L' U R U L U r' F r", "(U) F R' F' R U R U' R' F U R U' R' U R U' R' F'", "(U') F' R U2 R' U2 R' F U2 R U R U' R2 U2 R", "(U2) R U R' U R' D' R U2 R' D R2 U' R' U R U' R'", "(U) R' U' R' D' R U2 R' D R U R U' R' U' R"],
            'L4': ["(U2) F R' F' r U R U' r'", "(U') R U R' U' R B2 R' U2 R U2 R B2 R2", "(U2) F R U R' U' R' F' R U2 R U2 R'", "(U2) R U' R' U R U' R' U' R U R2 D' R U' R' D R", "(U) F' r' F r U r' F2 r U F", "(U) R U R' U R U R' U' R U R D R' U2 R D' R' U' R'", "(U) L R U' R' U R L' U R' U R U' R'", "(U) L U' R U R' L' U2 R U' R' U' R U' R'", "(U) R' U2 R U R' U' F' R U R' U' R' F R2 U R' U R", "(U) R' U2 R2 U R' U' R' U2 F R U R U' R' F'", "(U) R U R' U R U' R' U' L' U R U' M' x'", "(U2) R U R D R' U2 R D' R' U' R' U R U R'"],
            'L5': ["(U) R' U2 R' D' R U2 R' D R2", "(U) R' U2 R' D' r U2 r' D R2", "(U2) R D R' U2 R D' R' U' R' U2 R U' R' U' R", "(U2) R U2 R U R U' R2 D R' U R D' R U R'", "(U) R U R' U2 R U R' U2 y' R' U2 R U' R' U' R", "R' U2 R U R2 D' R U R' D R2", "(U) R U R' U' R U' R' U L' U R U' L U' R'", "(U) R U' R' U2 R U R' U2 R U R' U R2 D R' U' R D' R2", "(U) R' U2 R U2 R' U' R2 D R' U2 R D' R2 U2 R", "(U2) F' R U R' U' R' F R2 U' R' U' R U' R' U R U R'", "R U' R2 F2 R U2 R U2 R' F2 U2 R U' R'", "(U) R' U R2 D R' U R D' R' U2 R' U R U R' U' R"],
            'L6': ["(U2) R U2 R D R' U2 R D' R2", "(U) R' F' R U R' U' R' F R2 U' R' U2 R", "(U') L' U R U' L U R2 U2 R U R' U R", "(U') F R U R' U' R' F' U' R U R U' R' U' R' U R", "(U2) R' U' R U2 R' U' R y U2 R U2 R' U R U R'", "(U') R U2 R' U' R2 D R' U' R D' R2", "(U2) R' U' R U R' U R U' L U' R' U L' U R", "(U2) R' U R' D' R U R' U2 R U R' D U R U' R", "(U2) R U2 R' U2 R U R2 D' R U2 R' D R2 U2 R'", "(U') R U R' U R U2 R D R' U2 R D' R' U2 R'", "(U') R' U R2 B2 R' U2 R' U2 R B2 U2 R' U R", "(U2) R U' R2 D' R U' R' D R U2 R U' R' U' R U R'"],
        
            'Pi1': ["R' U' R U R U2 R' U' R U' R2 U2 R", "R U R' U' R' U2 R U R' U R2 U2 R'", "(U') R' U2 R U R' U R2 U R' U R U2 R'", "(U) R U2 R' U' R U' R2 U' R U' R' U2 R", "(U') R U2 R' U2 R U' R' U2 R U' R' U2 R U R'", "(U) R' U2 R U2 R' U R U2 R' U R U2 R' U' R", "(U2) R U' R' U2 R U R' U2 R U R' U2 R U2 R'", "(U2) R' U R U2 R' U' R U2 R' U' R U2 R' U2 R", "R' U2 R2 U R2 U R2 U2 R'", "R U2 R2 U' R2 U' R2 U2 R", "R U R' U' R' U' R U R U R' U' R' U R U' R U' R'", "R U2 R' U' R U' R' U' R U2 R' U' R U' R'"],
            'Pi2': ["F R2 U' R U' R U' R' U2 R' U R2 F'", "(U2) F R2 U' R U2 R U R' U R' U R2 F'", "F U R' U' R2 U' R2 U2 R U2 R U R' F'", "r' U' R U' R' U R U' R' U R' F R F' U r", "(U) R U2 R' U' F' R U2 R' U' R U' R' F R U' R'", "(U) R' U' R' D' R U R' D R U2 R' D' R U2 R' D R2", "(U') R' U' R U R' U' R2 D R' U R D' R' U R' U2 R", "(U) R U R' U' R U R2 D' R U' R' D R U' R U2 R'", "(U2) R U2 R' U R' D' R U R' D R2 U' R' U R U' R'", "(U2) R' U2 R U' R D R' U' R D' R2 U R U' R' U R", "R2 D R' U' R D' R' U' R' U R U' R' U' R U' R'", "R2 D' R U R' D R U R U' R' U R U R' U R"],
            'Pi3': ["(U') F U R U2 R' U R U R' F' R U2 R' U' R U' R'", "r U' r' U' r U r' U' l R U' R' U l'", "r' U r U r' U' r U R2 F R F' R", "r' U' R U' R' U2 r U' R U2 R' U2 R' F R F'", "R' U' R U R2 F' R U R U' R' F U' R U R' U R", "R U2 R D' R U' R' D R' U' R2 U2 R", "R' U' R U' R2 D' R U R' D R2 U' R' U2 R", "(U2) L' U R U' L U' R' U' R U' R'", "R U' L' U R' U L U L' U L", "(U) R2 D' R U2 R' D R2 U R2 D' R U R' D R2", "(U') R2 D R' U2 R D' R2 U' R2 D R' U' R D' R2", "(U2) R U2 R' U' R U r' F2 r U2 R' U' r' F r"],
            'Pi4': ["(U) R U2 R2 U' R U' R' U2 F R U R U' R' F'", "(U') R U R' U R U2 R2 F' r U R U' r' F", "(U') r' F' r U' r' F2 r2 U R' U' r' F R F'", "F R U R' U' R' F' R U2 R' U' R2 U' R2 U2 R", "(U) R' U' R L U2 R' U2 R U2 L' U R' U2 R", "(U') F U' R U' R' U R U R' U2 R U2 R' U F' U", "(U) R2 D' R U' R' D R U R' D' R U R' D R U R U' R' U' R", "R' U' F' R U R' U' R' F R2 U2' R' U2 R", "(U') R U R' U R U' R' U' R' F' R U2 R U2' R' F", "(U2) R' U' R' D' R U R' D R' U R' U R U2 R'", "(U2) R U R D R' U' R D' R U' R U' R' U2 R", "(U) F U R U' R' U R U2 R' U' R U R' F'"],
            'Pi5': ["r' F' r U r U2 r' F2 U' R U R' U' R U' R'", "(U2) R U2 R' U2 R' F R2 U' R' U2 R U2 R' U' F'", "R' F R U R' U' R' F' R2 U' R' U R U' R' U2 R", "R' L U2 R2 U R2 U R U L' U' R U2 R'", "l U2 l' U2 R' U2 R B2 U R' U R", "(U') R U R' U F2 R U2 R' U2 R' F2 R", "(U') R' U2 R U R' U R2 U' L' U R' U' L", "(U) R U R' U R U' R' U R U' R D R' U' R D' R2", "R U R' U' R' F R2 U R' U' R U R' U' F'", "(U2) R' U' R U' R' U' R U' x' U L' U L U2 R U' R' U x", "R U2 R' U' R U R' U2 L' U R U' M' x'", "(U') L R' U' R U L' U2 R' U R U' R' U2 R"],
            'Pi6': ["(U') R U R' U R U' R' U F2 r U2 r' U' r' F r", "(U) F U R U2 R' U2 R U R2 F' R U2 R U2 R'", "R U' R' U' R U' R' U R U R' U R' F' R U R U' R' F", "R L' U2 R2 U' R2 U' R' U' L U R' U2 R", "R' F2 R U2 R U2 R' F2 U' R U' R'", "(U) R' U' R U' B2 R' U2 R U2 l U2 l'", "(U) R U2 R' U' R U' R2 U L U' R U L'", "(U') R' U' R U' R' U R U' R' U R' D' R U R' D R2", "(U) F U R U' R' U R U' R2 F' R U R U' R'", "R U R' U R U2 R' U' R L' U R' U' L U2 R U2 R'", "R' U2 R U R' U' R U2 L U' R' U R L'", "(U) R L' U R' U' L U2 R U' R' U R U2 R'"],
        
            'H1': ["R U2 R' U' R U' R' U' R' U' R U' R' U2 R", "R' U2 R U R' U R U R U R' U R U2 R'", "(U) R' U' R U' R' U R U' R' U2 R", "(U') R U R' U R U' R' U R U2 R'", "R' U2 R U R' U' R U R' U R", "R U2 R' U' R U R' U' R U' R'", "(U) R U R' U R U' R' U R U' R' U R' U' R2 U' R' U R' U R", "(U) R U R' U R U2 R' U' R' U2 R U R' U R"],
            'H2': ["(U) x' U' R U' R' U R' F2 R U' R U R' U x", "F U R U' R' U R U' R' U R U' R' F'", "R U R' y' U R' U R U' R2 F R F' R", "R' U' R y U' R U' R' U R l U' R' U l'", "F R U R' U' R U R' U' F' U R' F' U' F U R", "R' U' R U' R' U2 R U R' U' R U R' F' R U R' U' R' F R2", "(U) L' U L U' L' U' L U R' U' R U L' U' L U2 R' U' R", "(U) R U' R' U R U R' U' L U L' U' R U R' U2 L U L'"],
            'H3': ["(U2) R U R' U R U2 R' F R U' R' U' R U2 R' U' F'", "l U' R U R' l' U r U' r' U r U r'", "(U2) R' F R' F' R2 U' r' U r U' r' U' r", "(U) R' U' R U' R' U' L U' R U L'", "(U) R U R' U R U L' U R' U' L", "(U') R' U' R U' R U R2 U R2 U L' U R' U' L", "(U') R U R' U R' U' R2 U' R2 U' L U' R U L'", "R U2 R2 U' R' D R' U' R D' R U2 R", "R U2 R' U' R2 D R' U R D' R2' U' R U' R'", "(U2) R U R' U' L' U2 R U2 R' U L U' r' F2 r", "(U') R2 D' R U' R' D R2 U' R2 D' R U2 R' D R2", "(U') R2 D R' U R D' R2' U R2 D R' U2 R D' R2'"],
            'H4': ["(U2) F R' F' r U R U' r2 F2 r U r' F r", "(U) R U R' U' R' F R U R U' R' F' R U R' U R U2 R'", "R' U2 R U' L U2 R' U2 R U2 L' R' U R", "R U2 R' U L' U2 R U2 R' U2 L R U' R'", "(U') F U' R U2 R' U2 R U' R' U' R U R' U F'", "(U') R' F R U R' U' F' R U' R' U R' F R F' U R", "(U') R U2 R' U' R U' R D' R U' R' D R U R", "R U2 R2 F U' R2 U' R2 U F' U R", "(U2) R' U2 R U2' R2 F' R U R U' R' F U R", "(U') F B' R2 B R2 U' R2 U' R2 U R2 F'", "(U2) F R U R' U' R' F' U2 R U R' U R2 U2 R'", "(U) F R U' R' U R U2 R' U' R U R' U' F'"],
        
            'S1': ["(U') R' U R2 U R' U R U2 R U2 R U R' U R2", "(U') R' U2 R2 U R  U' R' U R U R2 U' R'", "R U R' U R U2 R'", "(U') R' U2 R U R' U R", "R U R2 U' R2 U' R2 U2 R2 U2 R'", "(U2) R' U' R U' R U R2 U R2 U2 R'", "(U') R U R' U' R' U2 R U R U' R' U R' U R", "(U') R' U' R U R U R' U' R' U R U R U' R'", "R U R' U R U' R' U R' U' R2 U' R' U R' U R", "R U R' U R U R U R U R U' R' U' R2", "(U) R U R' U R' U' R2 U' R' U R' U' R U R' U R", "R U R' U R U' R' U R' U' R' U R U' R' U' R2 U R"],
            'S2': ["F U' R' U R U F' R U R2 U R2 U2 R'", "(U) R' D' R U' R' D R U2 R U R' U2 R U R'", "R' U2 R U R' U' R F U' R' U' R U F'", "R' U R U2 R' U R U2 R D R' U' R D' R'", "L' U2 R U' R' U2 L U R U' R' U R U2 R'", "(U) F R U R' U' R U R2 U' F' U R U R U' R'", "(U2) R U R' F' R U R' U R U2 R' F R U' R'", "(U) R U2 L' R' U2 R U2 R' U2 L U' R U' R'", "(U') R U' R2 U2 D' R U R' U D R2 U R'", "(U) F U R' F R F' R U' R' U R U' R' F'", "R U R' U' L' U R U' L U' L' U R' U' L", "(U2) r' F2 R F' r U' R' U r' F r U2 R U2 R'"],
            'S3': ["R U' L' U R' U' L", "(U) R' U2 R U R' U' R' D' R U2 R' D R2", "(U') R' D U' R' U R U2 D' R2 U R' U' R'", "(U) R' U' R' U R2 D' U2 R U R' U' D R'", "R2 D R' U2 R D' R' U' R' U R U2 R'", "D' R U R' U R U' R' U' D R2 U' R U' R' U R' U R2", "R U R' U R U R' U' R U R D R' U' R D' R' U2 R'", "(U') R' U2 R U R' U' R' D' R U' R' D R U R U' R' U' R", "(U') R' U2 F' R U R' U' R' F R U2 R", "R2 U R U R' U' R' U' R' L' U R' U' L", "(U) R U2 R' U2 R' F R2 U R' U' R U R' U' F'", "R U R' U R U' R' U' R' F R2 U' R' U' R U R' F'"],
            'S4': ["R' D R2 D' R2 U R2 D R2 D' R2 U' R'", "(U') R U R' U R U' R D R' U' R D' R2", "(U2) R U' R' U' R U' R' U2 R U R2 D' R U2 R' D R", "(U) F U R U' R' U R U' l U' R2 D' R U R' x", "(U2) R2 D' R U' R' D R U' R U R' U R", "(U) R U2 R' L' U2 R U R' U2 L R U2 R'", "R' D' R U R' D R2 U' R' U R U R' U' R U2 R' U R U2 R'", "R U' R' U' R U R D R' U2 R D' R2 U R U2 R'", "(U') R' U2 R' D' R U R' D R U' R U R' U R", "(U) R' U' R U' R2 F' R U R U' R' F U2 R", "(U2) R U R' U R' D' R U R' D R U' R U2 R'", "(U2) R U2 R' U' R U R' U' R U R D R' U2 R D' R2"],
            'S5': ["f R' F' R U2 R U2 R' U2 S'", "(U) R' D' R U R' D R2 U R' U2 R U R'", "R' D R' U R D' U R U' R' U' R2 U R U' R'", "(U) R' U2 R U R2 D' R U' R' D R U2 R", "(U2) R2 D' r U2 r' D R2 U R' U R", "R' U2 R U R' U R' D' R U2 R' D R U2 R", "R L' U R' U' L U2 R U2 R'", "(U2) R2 D' R U2 R' D R2 U R' U R", "R2 F R U R U' R' F' R U' R' U R", "(U) R U R' U R' U' R' D' R U R' D R' U2 R'", "(U') R' U' F U' R2 U R2 U F' R U' R U' R'", "(U') R' U' R' D' R U' R' D R' U R2 U R U' R U' R'"],
            'S6': ["(U2) R U R' U' R U R2 D' R U2 R' D R2 U2 R'", "R U R' U R U' R2 F' R U R U' R' F R U' R'", "(U2) R U R' U R2 D r' U2 r D' R2", "R' U R U2 R' U R2 D R' U R D' R'", "(U') R' U' R U R2 U' R' U' R U D' R U R' D R'", "(U2) R U R' U R2 D R' U2 R D' R2", "(U2) R' U2 R U2 L U' R' U L' R", "R U2 R D R' U2 R D' R' U R' U R U2 R'", "R U R2 F' R U2 R U2 R' F R U' R'", "(U) R U R' U' R U R2 D' R U R' D R U R U2 R'", "F' R U R' U R U2 R' F U R U' R' U2 R U' R'", "(U) R' F R U R' U' R' F' D' R U R' D R2"],
        
            'AS1': ["(U) R U' R2 U' R U' R' U2 R' U2 R' U' R U' R2", "(U) R U2 R2 U' R' U R U' R' U' R2 U R", "R' U' R U' R' U2 R", "(U) R U2 R' U' R U' R'", "R' U' R2 U R2 U R2 U2 R2 U2 R", "(U2) R U R' U R' U' R2 U' R2 U2 R", "(U) R' U' R U R U2 R' U' R' U R U' R U' R'", "(U) R U R' U' R' U' R U R U' R' U' R' U R", "(U) R U R' U R' U' R U R' U' R2 U' R2 U R U' R' U R", "R' U' R U' R' U' R' U' R' U' R' U R U R2", "(U) R U R' U' R U R2 U' R2 U' R' U R U' R' U R' U R", "(U2) R U R' U R' U' R' U R U' R' U' R' U' R' U2 R"],
            'AS2': ["(U') R U2 R2 U' R2 U' R' F U' R' U' R U F'", "(U') R D R' U R D' R' U2 R' U' R U2 R' U' R", "(U') R U2 R' U' R U R' L' U R U' L U2 R'", "R U' R' U2 R U' R' U2 R' D' R U R' D R", "(U') F U' R' U R U F' R' U R U' R' U2 R", "(U) R U R' U L' U2 R U2 R' U2 R L U2 R'", "R U R' F' R U2 R' U' R U' R' F R U' R'", "R U  R' U' R' U' F U R2 U' R' U R U' R' F'", "(U) R' U R2 U2 D R' U' R U' D' R2 U' R", "R' U R U R' U r U' R' U R U r' R' F R F' U R", "z D' R' D R U R' D' R U' R U R' D R U' z'", "R U2 R' U' R U r' F r U2 R' U' r' F2 r"],
            'AS3': ["R' U L U' R U L'", "(U') R U2 R' U' R U R D R' U2 R D' R2", "(U) R D' U R U' R' U2 D R2 U' R U R", "(U') R U R U' R2 D U2 R' U' R U D' R", "R2 D' R U2 R' D R U R U' R' U2 R", "D R' U' R U' R' U R U D' R2 U R' U R U' R U' R2", "R' U' R U' R' U' R U R' U' R' D' R U R' D R U2 R", "(U) R U2 R' U' R U R D  R' U R D' R' U' R' U R U R'", "(U2) F U R U' R' U R U' R2 F' R U2 R U2 R'", "(U2) F R U' R' U R U R2 F' R U R U R' U' R U' R'", "(U2) R' U2 R' F' R U R U' R' F U2 R", "(U2) L' U R U' L R U R U R U' R' U' R2"],
            'AS4': ["R D' R2 D R2 U' R2 D' R2 D R2 U R", "(U) R' U' R U' R' U R' D' R U R' D R2", "l U' R' D R2 U l' U R' U' R U R' U' F'", "(U') R' D' R U2 R' D R2 U' R' U2 R U R' U R U R'", "(U2) R2 D R' U R D' R' U R' U' R U' R'", "(U) R U2 R' L' U2 R U' R' U2 L R U2 R'", "(U') R U R' U' R' U' R U R U' R' U' R2 D' R U' R' D R U2 R", "(U') R U2 R' U' R2 D R' U2 R D' R' U' R' U R U R'", "(U) R U2 R' U R' D' R U' R' D R U' R U' R'", "(U') R2 D R' U2 R D' R' U' R' U R U' R' U  R U2 R'", "(U2) R' U' R U' R D R' U' R D' R' U R' U2 R", "(U2) R' U2 F' R U R' U' R' F R2 U R' U R"],
            'AS5': ["(U') R U2 R2 D' R U2 R' D R2 U' R' U R U' R'", "(U') R D R' U' R D' R2 U' R U2 R' U' R", "R D' R U' R' D U' R' U R U R2 U' R' U R", "R U R' F' R U R' U' R' F R2 U R' U' R U' R'", "(U2) R2 D r' U2 r D' R2 U' R U' R'", "R U2 R' U' R U' R D R' U2 R D' R' U2 R'", "L R' U' R U L' U2 R' U2 R", "(U2) R2 D R' U2 R D' R2 U' R U' R'", "R U R' F' R U2 R' U2 R' F R2 U' R'", "(U') R' U' R U' R U R D R' U' R D' R U2 R", "(U) R U R' U2 R U R' U' F' R U2 R' U' R U' R' F", "R2 D' R U' R' D F R U R U' R' F' R"],
            'AS6': ["(U') R U2 R' U' F' R U R' U' R' F R2 U' R'", "(U') R' U2 R' D' R U R' D R2 U' R' U2 R", "(U2) R' U' R U' R2 D' r U2 r' D R2", "R U' R' U2 R U' R2 D' R U' R' D R", "(U) R U R' U' R2 U R U R' U' D R' U' R D' R", "(U2) R' U' R U' R2 D' R U2 R' D R2", "(U2) R U2 R' U2 L' U R U' R' L", "R' U2 R' D' R U2 R' D R U' R U' R' U2 R", "R' U' R U R' F R U R' U' R' F' R2", "(U) R U2 R D' R U' R' D R U R U' R U' R'", "(U) R U R' U R' F U' R2 U' R2 U F' U R", "(U') R U R' U R' U' R2 U' R D' R U R' D R U R"]
        }
    }

    # Randomly select a case from pool
    case_pool = []
    for sub_set in selectedCases:
        case_pool += algs[algSet][sub_set]
    case = case_pool[random.randint(0, len(case_pool) - 1)]
   
    # Determine scramble based on the selected algorithm set
    if(algSet == 'lxs'):
        zbll_set = algs['zbll'][random.randint(0, len(algs['zbll']) - 1)]
        zbll_alg = zbll_set[random.randint(0, len(zbll_set) - 1)]
        move_list = zbll_alg.split(' ') + invertScramble(case.split(' '))
    elif(algSet == 'eo_pair'):
        lxs_set = algs['lxs'][random.randint(0, len(algs['lxs']) - 1)]
        lxs_alg = lxs_set[random.randint(0, len(lxs_set) - 1)]
        move_list = lxs_alg.split(' ') + invertScramble(case.split(' '))
    scramble = generateScramble(move_list)

    return case, ''.join(scramble)
