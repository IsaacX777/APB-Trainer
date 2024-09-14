import kociemba

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

def sliceMove(cube, move, slice_list):
    # Get colors for moving pieces
    slice_list_values = []
    for val in slice_list:
        slice_list_values.append(cube[val[0]][val[1]])

    # 1 = normal, 2 = prime, 3 = double
    if(len(move) == 1):
        for i in range (0, len(slice_list)):
            if(i + 3 > 11):
                cube[slice_list[i - 9][0]][slice_list[i - 9][1]] = slice_list_values[i]
            else:
                cube[slice_list[i + 3][0]][slice_list[i + 3][1]] = slice_list_values[i]
    elif("'" in move):
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
                
    sliceMoveDictionary = {
        "M": "x'", "M'": "x", "M2": "x2", "E": "y'", "E'": "y", "E2": "y2", "S": "z", "S'": "z'", "S2": "z2"
    }
    cube = centerSwap(cube, sliceMoveDictionary[move])
    return cube

def centerSwap(cube, type):
    centerSwapDictionary = {
        "x": {
            'U': 'B', 'B': 'D', 'D': 'F', 'F': 'U', 'L': 'L', 'R': 'R'
        },
        "x'": {
            'U': 'F', 'F': 'D', 'D': 'B', 'B': 'U', 'L': 'L', 'R': 'R'
        },
        "x2": {
            'U': 'D', 'F': 'B', 'D': 'U', 'B': 'F', 'L': 'L', 'R': 'R'
        },
        "y": {
            'R': 'F', 'F': 'L', 'L': 'B', 'B': 'R', 'U': 'U', 'D': 'D'
        },
        "y'": {
            'R': 'B', 'B': 'L', 'L': 'F', 'F': 'R', 'U': 'U', 'D': 'D'
        },
        "y2": {
            'R': 'L', 'F': 'B', 'L': 'R', 'B': 'F', 'U': 'U', 'D': 'D'
        },
        "z": {
            'U': 'R', 'R': 'D', 'D': 'L', 'L': 'U', 'F': 'F', 'B': 'B'
        },
        "z'": {
            'U': 'L', 'L': 'D', 'D': 'R', 'R': 'U', 'F': 'F', 'B': 'B'
        },
        "z2": {
            'U': 'D', 'R': 'L', 'D': 'U', 'L': 'R', 'F': 'F', 'B': 'B'
        }
    }
    for i in range (0, 6):
        for j in range (0, 9):
            cube[i][j] = centerSwapDictionary[type][cube[i][j]]
                    
    return cube

def invertScramble(move_list):
    move_list.reverse()
    for i in range(0, len(move_list)):
        move = move_list[i]
       
        # Account for unconventional notation
        move = move.replace("2'", '2')
        move = move.replace("3'", '')
        move = move.replace('3', "'")
        move = move.replace('(', '')
        move = move.replace(')', '')
       
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
                cube = sliceMove(cube, "M", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "M'":
                cube = sliceMove(cube, "M'", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "M2":
                cube = sliceMove(cube, "M2", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "S":
                cube = sliceMove(cube, "S", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "S'":
                cube = sliceMove(cube, "S'", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "S2":
                cube = sliceMove(cube, "S2", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "E":
                cube = sliceMove(cube, "E", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "E'":
                cube = sliceMove(cube, "E'", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "E2":
                cube = sliceMove(cube, "E2", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "l":
                cube = outerMove(cube, 1, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
                cube = sliceMove(cube, "M", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "l'":
                cube = outerMove(cube, 2, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
                cube = sliceMove(cube, "M'", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "l2":
                cube = outerMove(cube, 3, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
                cube = sliceMove(cube, "M2", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "r":
                cube = outerMove(cube, 1, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = sliceMove(cube, "M'", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "r'":
                cube = outerMove(cube, 2, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = sliceMove(cube, "M", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "r2":
                cube = outerMove(cube, 3, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = sliceMove(cube, "M2", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
            case "u":
                cube = outerMove(cube, 1, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = sliceMove(cube, "E'", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "u'":
                cube = outerMove(cube, 2, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = sliceMove(cube, "E", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "u2":
                cube = outerMove(cube, 3, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = sliceMove(cube, "E2", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "d":
                cube = outerMove(cube, 1, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
                cube = sliceMove(cube, "E", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "d'":
                cube = outerMove(cube, 2, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
                cube = sliceMove(cube, "E'", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "d2":
                cube = outerMove(cube, 3, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
                cube = sliceMove(cube, "E2", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
            case "f":
                cube = outerMove(cube, 1, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
                cube = sliceMove(cube, "S", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "f'":
                cube = outerMove(cube, 2, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
                cube = sliceMove(cube, "S'", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "f2":
                cube = outerMove(cube, 3, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
                cube = sliceMove(cube, "S2", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "b":
                cube = outerMove(cube, 1, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
                cube = sliceMove(cube, "S'", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "b'":
                cube = outerMove(cube, 2, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
                cube = sliceMove(cube, "S", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "b2":
                cube = outerMove(cube, 3, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
                cube = sliceMove(cube, "S2", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
            case "x":
                cube = sliceMove(cube, "M'", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
                cube = outerMove(cube, 1, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = outerMove(cube, 2, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
            case "x'":
                cube = sliceMove(cube, "M", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
                cube = outerMove(cube, 2, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = outerMove(cube, 1, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
            case "x2":
                cube = sliceMove(cube, "M2", [(0, 1), (0, 4), (0, 7), (2, 1), (2, 4), (2, 7), (3, 1), (3, 4), (3, 7), (5, 7), (5, 4), (5, 1)])
                cube = outerMove(cube, 3, [(0, 2), (5, 0), (5, 3), (5, 6), (3, 8), (3, 5), (3, 2), (2, 8), (2, 5), (2, 2), (0, 8), (0, 5)], 1)
                cube = outerMove(cube, 3, [(0, 0), (0, 3), (0, 6), (2, 0), (2, 3), (2, 6), (3, 0), (3, 3), (3, 6), (5, 8), (5, 5), (5, 2)], 4)
            case "y":
                cube = sliceMove(cube, "E'", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
                cube = outerMove(cube, 1, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = outerMove(cube, 2, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
            case "y'":
                cube = sliceMove(cube, "E", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
                cube = outerMove(cube, 2, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = outerMove(cube, 1, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
            case "y2":
                cube = sliceMove(cube, "E2", [(4, 3), (4, 4), (4, 5), (2, 3), (2, 4), (2, 5), (1, 3), (1, 4), (1, 5), (5, 3), (5, 4), (5, 5)])
                cube = outerMove(cube, 3, [(4, 0), (5, 2), (5, 1), (5, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0), (4, 2), (4, 1)], 0)
                cube = outerMove(cube, 3, [(4, 6), (4, 7), (4, 8), (2, 6), (2, 7), (2, 8), (1, 6), (1, 7), (1, 8), (5, 6), (5, 7), (5, 8)], 3)
            case "z":
                cube = sliceMove(cube, "S", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
                cube = outerMove(cube, 1, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
                cube = outerMove(cube, 2, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
            case "z'":
                cube = sliceMove(cube, "S'", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
                cube = outerMove(cube, 2, [(0, 6), (0, 7), (0, 8), (1, 0), (1, 3), (1, 6), (3, 2), (3, 1), (3, 0), (4, 8), (4, 5), (4, 2)], 2)
                cube = outerMove(cube, 1, [(0, 2), (0, 1), (0, 0), (4, 0), (4, 3), (4, 6), (3, 6), (3, 7), (3, 8), (1, 8), (1, 5), (1, 2)], 5)
            case "z2":
                cube = sliceMove(cube, "S2", [(0, 3), (0, 4), (0, 5), (1, 1), (1, 4), (1, 7), (3, 5), (3, 4), (3, 3), (4, 7), (4, 4), (4, 1)])
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