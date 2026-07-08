function createCube() {
    return {
        cp: [0, 1, 2, 3, 4, 5, 6, 7],
        co: [0, 0, 0, 0, 0, 0, 0, 0],
        ep: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        eo: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        centers: [0, 1, 2, 3, 4, 5]
    };
}

function cycle(arr, indices) {
    let n = indices.length;
    const temp = arr[indices[n - 1]];
    for(let i = n - 1; i > 0; i--) {
        arr[indices[i]] = arr[indices[i - 1]];
    }
    arr[indices[0]] = temp;
}
function orientCorners(arr, indices, offset) {
    let n = indices.length;
    const temp = arr[indices[n - 1]];
    for(let i = n - 1; i > 0; i--) {
        arr[indices[i]] = (arr[indices[i - 1]] + offset[i]) % 3;
    }
    arr[indices[0]] = (temp + offset[0]) % 3;
}
function orientEdges(arr, indices) {
    let n = indices.length;
    const temp = arr[indices[n - 1]];
    for(let i = n - 1; i > 0; i--) {
        arr[indices[i]] = arr[indices[i - 1]] ^ 1;
    }
    arr[indices[0]] = temp ^ 1;
}

function U(cube) {
    cycle(cube.cp, [0, 1, 2, 3]);
    cycle(cube.ep, [0, 1, 2, 3]);
}
function Up(cube) {
    cycle(cube.cp, [3, 2, 1, 0]);
    cycle(cube.ep, [3, 2, 1, 0]);
}
function U2(cube) {
    U(cube);
    U(cube);
}

function R(cube) {
    cycle(cube.cp, [0, 3, 7, 4]);
    cycle(cube.ep, [0, 11, 4, 8]);
    orientCorners(cube.co, [0, 3, 7, 4], [2, 1, 2, 1])
}
function Rp(cube) {
    cycle(cube.cp, [4, 7, 3, 0]);
    cycle(cube.ep, [8, 4, 11, 0]);
    orientCorners(cube.co, [4, 7, 3, 0], [1, 2, 1, 2])
}
function R2(cube) {
    R(cube);
    R(cube);
}

function F(cube) {
    cycle(cube.cp, [0, 4, 5, 1]);
    cycle(cube.ep, [1, 8, 5, 9]);
    orientCorners(cube.co, [0, 4, 5, 1], [1, 2, 1, 2]);
    orientEdges(cube.eo, [1, 8, 5, 9]);
}
function Fp(cube) {
    cycle(cube.cp, [1, 5, 4, 0]);
    cycle(cube.ep, [9, 5, 8, 1]);
    orientCorners(cube.co, [1, 5, 4, 0], [2, 1, 2, 1]);
    orientEdges(cube.eo, [9, 5, 8, 1]);
}
function F2(cube) {
    F(cube);
    F(cube);
}

function D(cube) {
    cycle(cube.cp, [4, 7, 6, 5]);
    cycle(cube.ep, [4, 7, 6, 5]);
}
function Dp(cube) {
    cycle(cube.cp, [5, 6, 7, 4]);
    cycle(cube.ep, [5, 6, 7, 4]);
}
function D2(cube) {
    D(cube);
    D(cube);
}

function L(cube) {
    cycle(cube.cp, [1, 5, 6, 2]);
    cycle(cube.ep, [2, 9, 6, 10]);
    orientCorners(cube.co, [1, 5, 6, 2], [1, 2, 1, 2]);
}
function Lp(cube) {
    cycle(cube.cp, [2, 6, 5, 1]);
    cycle(cube.ep, [10, 6, 9, 2]);
    orientCorners(cube.co, [2, 6, 5, 1], [2, 1, 2, 1]);
}
function L2(cube) {
    L(cube);
    L(cube);
}

function B(cube) {
    cycle(cube.cp, [3, 2, 6, 7]);
    cycle(cube.ep, [3, 10, 7, 11]);
    orientCorners(cube.co, [3, 2, 6, 7], [1, 2, 1, 2]);
    orientEdges(cube.eo, [3, 10, 7, 11]);
}
function Bp(cube) {
    cycle(cube.cp, [7, 6, 2, 3]);
    cycle(cube.ep, [11, 7, 10, 3]);
    orientCorners(cube.co, [7, 6, 2, 3], [2, 1, 2, 1]);
    orientEdges(cube.eo, [11, 7, 10, 3]);
}
function B2(cube) {
    B(cube);
    B(cube);
}

function M(cube) {
    cycle(cube.ep, [1, 5, 7, 3]);
    orientEdges(cube.eo, [1, 5, 7, 3]);
    cycle(cube.centers, [0, 2, 3, 5]);
}
function Mp(cube) {
    cycle(cube.ep, [3, 7, 5, 1]);
    orientEdges(cube.eo, [3, 7, 5, 1]);
    cycle(cube.centers, [0, 5, 3, 2]);
}
function M2(cube) {
    M(cube);
    M(cube);
}

function S(cube) {
    cycle(cube.ep, [0, 4, 6, 2]);
    orientEdges(cube.eo, [0, 4, 6, 2]);
    cycle(cube.centers, [0, 1, 3, 4]);
}
function Sp(cube) {
    cycle(cube.ep, [2, 6, 4, 0]);
    orientEdges(cube.eo, [2, 6, 4, 0]);
    cycle(cube.centers, [0, 4, 3, 1]);
}
function S2(cube) {
    S(cube);
    S(cube);
}

function E(cube) {
    cycle(cube.ep, [8, 9, 10, 11]);
    cycle(cube.centers, [2, 4, 5, 1]);
}
function Ep(cube) {
    cycle(cube.ep, [11, 10, 9, 8]);
    cycle(cube.centers, [2, 1, 5, 4]);
}
function E2(cube) {
    E(cube);
    E(cube);
}

function x(cube) {
    R(cube);
    Mp(cube);
    Lp(cube);
}
function xp(cube) {
    Rp(cube);
    M(cube);
    L(cube);
}
function x2(cube) {
    x(cube);
    x(cube);
}

function y(cube) {
    U(cube);
    E(cube);
    Dp(cube);
}
function yp(cube) {
    Up(cube);
    Ep(cube);
    D(cube);
}
function y2(cube) {
    y(cube);
    y(cube);
}

function z(cube) {
    F(cube);
    S(cube);
    Bp(cube);
}
function zp(cube) {
    Fp(cube);
    Sp(cube);
    B(cube);
}
function z2(cube) {
    z(cube);
    z(cube);
}

function Rw(cube) {
    R(cube);
    Mp(cube);
}
function Rwp(cube) {
    Rp(cube);
    M(cube);
}
function Rw2(cube) {
    Rw(cube);
    Rw(cube);
}

function Lw(cube) {
    L(cube);
    M(cube);
}
function Lwp(cube) {
    Lp(cube);
    M(cube);
}
function Lw2(cube) {
    Lw(cube);
    Lw(cube);
}

function Uw(cube) {
    U(cube);
    E(cube);
}
function Uwp(cube) {
    Up(cube);
    Ep(cube);
}
function Uw2(cube) {
    Uw(cube);
    Uw(cube);
}

function Dw(cube) {
    D(cube);
    Ep(cube);
}
function Dwp(cube) {
    Dp(cube);
    E(cube);
}
function Dw2(cube) {
    Dw(cube);
    Dw(cube);
}

function Fw(cube) {
    F(cube);
    S(cube);
}
function Fwp(cube) {
    Fp(cube);
    Sp(cube);
}
function Fw2(cube) {
    Fw(cube);
    Fw(cube);
}

function Bw(cube) {
    B(cube);
    Sp(cube);
}
function Bwp(cube) {
    Bp(cube);
    S(cube);
}
function Bw2(cube) {
    Bw(cube);
    Bw(cube);
}

const moveMap = {
    "U": U,
    "U'": Up,
    "U2": U2,
    "R": R,
    "R'": Rp,
    "R2": R2,
    "F": F,
    "F'": Fp,
    "F2": F2,
    "D": D,
    "D'": Dp,
    "D2": D2,
    "L": L,
    "L'": Lp,
    "L2": L2,
    "B": B,
    "B'": Bp,
    "B2": B2,
    "M": M,
    "M'": Mp,
    "M2": M2,
    "S": S,
    "S'": Sp,
    "S2": S2,
    "E": E,
    "E'": Ep,
    "E2": E2,
    "x": x,
    "x'": xp,
    "x2": x2,
    "y": y,
    "y'": yp,
    "y2": y2,
    "z": z,
    "z'": zp,
    "z2": z2,
    "r": Rw,
    "r'": Rwp,
    "r2": Rw2,
    "l": Lw,
    "l'": Lwp,
    "l2": Lw2,
    "u": Uw,
    "u'": Uwp,
    "u2": Uw2,
    "d": Dw,
    "d'": Dwp,
    "d2": Dw2,
    "f": Fw,
    "f'": Fwp,
    "f2": Fw2,
    "b": Bw,
    "b'": Bwp,
    "b2": Bw2
}
const rotations = [
    [],
    ["x"], ["x2"], ["x'"],
    ["y"], ["y2"], ["y'"],
    ["z"], ["z2"], ["z'"],

    ["x", "y"],
    ["x", "y'"],
    ["x", "y2"],

    ["x'", "y"],
    ["x'", "y'"],
    ["x'", "y2"],

    ["z", "y"],
    ["z", "y'"],
    ["z", "y2"],

    ["z'", "y"],
    ["z'", "y'"],
    ["z'", "y2"],

    ["x", "z"],
    ["x'", "z"]
];
function normalizeCube(cube) {
    for (const alg of rotations) {
        const copy = structuredClone(cube);

        alg.forEach(m => {
            if (moveMap[m]) {
                moveMap[m](cube);
            } else {
                throw new Error(`Invalid move: ${m}`);
            }
        });

        if (
            copy.centers[0] === 0 &&
            copy.centers[1] === 1 &&
            copy.centers[2] === 2
        ) {
            return copy;
        }
    }

    throw new Error("Could not normalize cube");
}
function performMoves(cube, moves) {
    moves.split(" ").forEach(m => {
        if (moveMap[m]) {
            moveMap[m](cube);
        } else {
            throw new Error(`Invalid move: ${m}`);
        }
    });
    cube = normalizeCube(cube);
}


const cornerFacelets = [
    [8, 9, 20], [6, 18, 38], [0, 36, 47], [2, 45, 11],
    [29, 26, 15], [27, 44, 24], [33, 53, 42], [35, 17, 51]
];

const cornerStickers = [
    ['U','R','F'], ['U','F','L'], ['U','L','B'], ['U','B','R'],
    ['D','F','R'], ['D','L','F'], ['D','B','L'], ['D','R','B']
];

const edgeFacelets = [
  [5,10],[7,19],[3,37],[1,46],
  [32,16],[28,25],[30,43],[34,52],
  [23,12],[21,41],[50,39],[48,14]
];

const edgeStickers = [
  ['U','R'],['U','F'],['U','L'],['U','B'],
  ['D','R'],['D','F'],['D','L'],['D','B'],
  ['F','R'],['F','L'],['B','L'],['B','R']
];

const centerFacelets = [
  [4],[13],[22],[31],[40],[49]
];

const centerStickers = [
  ['U'],['R'],['F'],['D'],['L'],['B']
];

function cubieToString(cube) {
    var cubeArray = new Array(54);

    for(let i = 0; i < 6; i++) {
        const c = cube.centers[i];
        cubeArray[centerFacelets[i]] = centerStickers[c];
    }

    for (let i = 0; i < 8; i++) {
        const c = cube.cp[i];
        const o = cube.co[i];
        for (let j = 0; j < 3; j++) {
            const sticker = cornerStickers[c][(j + o) % 3];
            cubeArray[cornerFacelets[i][j]] = sticker;
        }
    }

    for (let i = 0; i < 12; i++) {
        const e = cube.ep[i];
        const o = cube.eo[i];
        for (let j = 0; j < 2; j++) {
            cubeArray[edgeFacelets[i][j]] = edgeStickers[e][(j + o) % 2];
        }
    }

    return cubeArray.join('');
}

export {createCube, performMoves, cubieToString};