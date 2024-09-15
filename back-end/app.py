from generate_scramble import generateScramble, invertScramble
import random
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'/Fetch_Case/*': {'origins': 'http://localhost:3000'}})

# List of all available algorithms
algs = {
    'lxs': {
        'UFR': ["(U2) R U R2 U' R' U R", "(U) R U2 R2 U' R' U R", "(U') R U R U' R2 U' R2 U R2", "(U2) R D' R U R' D R'", "(U) R' U2 R U2 R", "R' U' R U' R U2 R", "(U) R U2 R2 U' R U R2 U' R'", "R U' R2 U' R U R U2 R U R'", "R2 U' R2 U2 R2 U R2", "R U' R' U R U' R2 U' R U R", "(U') R' U' R U' R' U R2 U R", "R U' R2 U2 R U2 R2 U' R'", "R U2 R' U R' U2 R U2 R2 U' R'", "R U R2 U2' R' U2 R2 U' R'", "R U' R' U R U2 R2 U' R U R", "R U R' U R' U' R U R2 U R'", "(U2) R U R' U R' U' R2 U R", "(U) R U2 R' U R' U' R2 U R", "(U2) R' U2 R U2 R U' R U R'", "R U' R' U R' U' R U R", "(U') R U R' U R' U' R U' R U2 R", "(U2) R U R2 U' R U R2 U' R'", "R S' R U' R' f R' F' R U' R'", "(U) R' U' R U' R U R' U' R U2 R", "(U) R' U2 R' U2 R2 U2 R'", "(U2) R2 U2 R' U' R U' R2", "(U2) R U R' U R U' R'", "(U) R U2 R' U R U' R'", "R U2 R' U' R U R'", "(U) R U' R' U R U' R' U R U' R'"],
        'RFU': ["(U') S' R U R' U R U R' S", "R U R' S R2 S' R2", "(U') R U' R' U R U R' S R2' S' R2", "R' U' R U R U' R U R'", "R D' R U' R' D U R'", "(U) R U R2 U2' R' U2 R2 U R'", "(U') R' U2 R U R U R", "(U') R' U R U2 R2 U2 R' U' R", "(U') R' U2 R' U R U R", "(U') R' U' R U R", "(U') R' U2 R2 U R' U R2 U' R'", "(U2) R' U' R U R U2 R U R'", "(U') R U' R2 U2 R U R U R", "(U2) R' U' R U R2 U' R' U' R U R'", "(U') R U' R2 U' R U R", "R' U2 R2 U2 R2 U' R'", "(U2) R U' R' U R' U2 R U2 R2 U' R'", "R U R' S' U2 S", "(U) R' U' R2 U' R' U2 R2 U' R'", "(U') R U2 R2 U' R U R", "(U2) R' U2 R' U2 R2 U R'", "(U') R U R2 U2 R U R U R", "R U R' U' S' U2 S", "(U2) R' U2 R U R U' R' U R U R", "(U') R U R2 U' R U R", "R2 D R' U2 R D' R' U R'", "(U2) R U' R' U' R U R'", "R U R'", "(U') R U' R' U R U R'", "(U') R U2 R' U R U R'"],
        'FUR': ["(U') R U2 R' U R' U' R U R2 U' R'", "(U') R U R' U R' U' R U R2 U' R'", "R' U' R U R2 U' R'", "(U') R U' R' U R' U' R U R2 U' R'", "(U') R' U2 R U R' U' R U2 R", "(U') R' U' R U R U' R U' R' U R U' R'", "(U') R U R' U2 R' U' R2 U R", "(U2) R' U2 R2 U2 R", "(U') R D' R U' R' D R'", "(U2) S' U2 S U R U' R'", "(U) R' U' R U' R U R U R", "(U') R U2 R' U R' U' R' U R", "(U) R' U' R2 U R", "(U') R' U' R' U' R U2 R", "(U2) R U R' U' R' U' R U R", "(U) R' U' R U R U R U R'", "(U2) S R2' S' R3 U2' R'", "(U') R U R' U R' U' R' U R", "(U') R U' R' U2 R' U' R2 U R", "(U) R' U' R U D' R U R' D R", "R U' D' R U R' D R'", "(U') R U2 R' U2 R' U' R2 U R", "F' R U R U' R' F R'", "R' U2 R' U2' R", "(U2) R U D' R U' R' U D R'", "(U) R' F R U R U' R' F' R U2 R'", "(U') R U2 R' U2 R U' R'", "(U') R U R' U2 R U' R'", "(U) R U' R'", "(U') R U' R' U2 R U' R'"],
        'DFR': ["(U) R U' R2 U' R U R U' R U R'", "(U) S R2' S' R2", "(U) R U' D' R U' R' U D R'", "R' F' R U R U' R' f R2 S' R2", "(U') S' R U R' U' F' U' f", "(U2) R U' D' R U R' U D R'", "R U' R' U' R U' R2 U' R U R", "(U') R' F' R U R U' R' F"],
        'RDF': ["(U) R' U' R U R U' R' U' R U R", "(U') R U2 R' U R' U' R U R", "R' U' R U R U' R U' R' U R U R'", "(U') R' U' R U R2 U R'", "(U2) R' U2 R U2 R2 U R'", "R' U2 R' U2 R2 U' R'", "R U2 R' U R U2 R2 U' R U R", "R U R' U' R U R'", "R U' R' U R U2 R' U R U' R'"],
        'FRD': ["R U' R2 U' R' U R", "R U R2 U2 R U2 R", "R' U' R' U' R U R' U' R U2 R", "R U' R2 U' R U R2 U' R'", "(U) R' U' R U R2 U' R' U2 R U R'", "(U') R U' R' U R' U' R2 U R", "R U R' U' R U' R' U R' U' R U R", "(U') R U' R' U R U' R'", "R U' R' U' R U R' U2 R U' R'"]
    },
    'eo_pair': {
        'dBR': ["F R' F' R", "F R U R' U' F'", "R' F R F'", "f' U' f", "S' R U' R' U' S", "r U r' U2 M' U M", "S R' U' R U R S'", "S' U' S", "S' U R U2 R' S", "R U R' S' U' S", "F R' F' R U S' U' S"],
        'dFR': ["F R' F'","F R U R' U' F'", "f R f'", "F R F'", "S' R' U' R U S", "r' U' r U2 M U' M'", "r' U r U2 r' U' r", "S' U' S", "S' U R' U2 R S", "R' U' R S' U' S", "F U R U' R' S R' S' R F'"],
        'OU': ["(U2) F R' F' U R", "(U') R U f' U f", "(U') F R2 U R' U' F'", "(U2) F' U F R", "(U') F R F'", "f R f' U2 R", "(U') F' U' F U R", "(U') R F' U' F", "(U) f R' f' U' R", "(U') R f' U f", "(U') R f' U2 f", "(U') R f' U' f", "(U') R F' U F", "(U2) R' f R U R U' f'", "(U') R U' f' U' f", "(U) R' U' R S R' S' U' R", "(U) R' U2 R S' U' S", "(U') R U2 S' U' S", "(U2) F' U F2 R F'", "(U2) S' U' R' U2 R S", "(U') R U' S' U' S", "(U') R' f' U' f2 R f' R'", "S' U R' U2 R S", "(U') R U S' U' S", "R S R' S' U' R", "(U2) R' S R S' U R", "(U') R S' U' S", "(U') R S' U' R U2 R' S", "(U') R2 U' R' S' U' S", "(U2) R2 S R S' U R", "(U2) S R S' R' F R U R U' F'"],
        'OR': ["(U') R' U' F' U F R'", "R' U R' U' F' U' F", "(U) F R' F' R2", "F R' F' R U R U' R", "R' U R' f' U' f", "R' U R' F' U' F", "R2' F R' F' R", "R F R F'", "R' f R f' R'", "R2 F' U' F", "f' U' f R'", "(U) f R' f' R2", "R U' F' R' U R F", "R U2 R' f R' f' U' R", "R2 F' U F", "R2 U2 S' U' S", "(U') S' U S R2", "S R U' R' U R S'", "(U2) S' U' S U' R2", "R U2 R' U S R S' U R", "(U) S' U' S R2", "f R U R' U' R' f' R2", "R2 S' U' S", "R U R' S R S' U' R", "R D' r U' r' D R", "R' f R U R U' R' f' R'", "R U' R2 S R S' U R", "R' U2 R U S' U' S R2", "f R' S' R F' R2", "(U) R' S R S' R U' R2", "(U2) D r' U' r D' F R' F' R2"],
        'MU': ["(U) R' F' U' F R", "(U) f U R' U' f'", "f' U f R'", "(U') F' U' F R2", "(U2) R' f R2 f'", "(U) f R' f'", "(U') R U2 R U R' S R' S'", "R' U2 R U S R S'", "(U2) F R2 f' U' S", "(U) R D r' U' r D' R'", "(U) R' F' U' F2 R F'", "R' U' S R S'", "(U2) R U2 R' U' S R S'", "(U') f U R' U' F' R S'", "(U) S' U' S R' U' R", "(U) R U R' S R' S'", "(U') R U R' S' U' S R", "(U2) f' U' f2 R2 f'", "R' S' U' S R", "(U') D' r U r' U' D R", "R' U' f R2 U R' U' f'", "(U) f' R' U2 R f", "R' U' R2 U2 S R' S'", "(U') D r' U r D' R'", "(U2) S R' F R2 f'", "(U') R2 U R' S' U' S R", "(U) S' U' S R' U' F R F'", "(U') D r' U r D' R2 F R F'", "(U) R D r' U' r D' R2 F R F'", "D r' U' r D' R F R' F'", "(U) R S R S' R2 F R' F'", "(U2) S R S' R' f R2 f'"],
        'MR': ["F R2 F' U' R", "R2 F' U' F R", "(U') f R f' R' U2 R2", "(U) f U R U' f' R", "R' U R' F R2 F'", "R' f R' f'", "S R U' R' U R S' R", "R U2 R' U S R S' R", "(U) R2 U' R S R' S'", "R U' R' S R S' R' U R2", "R U' R' U S R S' R", "R D' r U' r' D R2", "(U') R U' R' U' S R S' R", "D r' U' r D' R'", "(U) R2 U R2 S R S' R", "R' f' R' U2 R f", "(U') f' R' U2 R f R", "S' U' R' U2 R S R", "S R S' R' U R2", "R' S R S' U R2", "(U) S R S' R", "(U) R' S R' S'", "R D' U r U' r' D R2", "(U2) S R S' R' f R' f' R2", "(U) R' U2 R2 S R S'", "R U2 R2 f R2 F' R S'", "(U2) F R' F' R2 D r' U r D'", "D r' U' r D' R2 F R F'", "S R S' R2 F R' F'", "R' S R S' U2 S' U' S R2", "R' B' R2 B R' S R S' R", "(U) R S' U' S2 R' S' U R"]
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
zbll_sets = list(algs['zbll'].keys())
lxs_sets = list(algs['lxs'].keys())

@app.route('/Fetch_Case/<algSet>/<selectedCases>', methods=['GET'])
def selectCase(algSet, selectedCases):
    # Randomly select a case from pool
    case_pool = []
    for sub_set in selectedCases.split(';'):
        sub_set_list = sub_set.split(',')
        sub_set_name = sub_set_list.pop(0)
        for index in sub_set_list:
            case_pool.append(algs[algSet][sub_set_name][int(index)])
    case = case_pool[random.randint(0, len(case_pool) - 1)]
   
    # Determine scramble based on the selected algorithm set
    if(algSet == 'lxs'):
        zbll_set = algs['zbll'][zbll_sets[random.randint(0, len(algs['zbll']) - 1)]]
        zbll_alg = zbll_set[random.randint(0, len(zbll_set) - 1)]
        move_list = zbll_alg.split(' ') + invertScramble(case.split(' '))
    elif(algSet == 'eo_pair'):
        lxs_set = algs['lxs'][lxs_sets[random.randint(0, len(algs['lxs']) - 1)]]
        lxs_alg = lxs_set[random.randint(0, len(lxs_set) - 1)]
        move_list = lxs_alg.split(' ') + invertScramble(case.split(' '))
    scramble = generateScramble(move_list)
    image_link = "https://cube.rider.biz/visualcube.php?fmt=ico&size=150&pzl=3&stage=f2l&alg=" + ''.join(scramble) if algSet == 'lxs' else "https://cube.rider.biz/visualcube.php?fmt=ico&size=150&pzl=3&stage=els&alg=" + ''.join(scramble)

    # Return as a JSON response
    return jsonify({
        "scramble": scramble,
        "case": case,
        "image_link": image_link
    })

if __name__ == '__main__':
    app.run(debug=True)