import cv2
import os
from os import path
from PIL import Image
import requests
from io import BytesIO
import numpy as np
    
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
    }
}

for set in algs['lxs']:
    set_dir = f'front-end/public/lxs/{set}'
    if not os.path.exists(set_dir):
        os.makedirs(set_dir)

    for i, alg in enumerate(algs['lxs'][set]):
        image_filename = f'{set_dir}/{i}.png'
        
        if os.path.isfile(image_filename):
            print(True)
        else:
            image_url = f'https://cube.rider.biz/visualcube.php?fmt=ico&size=150&pzl=3&stage=f2l&case={alg}'
            response = requests.get(image_url)

            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))

                img_cv = np.array(img)
                img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
                
                cv2.imwrite(image_filename, img_cv)
                print(True)
            else:
                print(f"Failed to download image for alg {alg}")
        
for set in algs['eo_pair']:
    set_dir = f'front-end/public/eo_pair/{set}'
    if not os.path.exists(set_dir):
        os.makedirs(set_dir)

    for i, alg in enumerate(algs['eo_pair'][set]):
        image_filename = f'{set_dir}/{i}.png'
        
        if os.path.isfile(image_filename):
            print(True)
        else:
            image_url = f'https://cube.rider.biz/visualcube.php?fmt=ico&size=150&pzl=3&stage=els&case={alg}'
            response = requests.get(image_url)

            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))

                img_cv = np.array(img)
                img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
                
                cv2.imwrite(image_filename, img_cv)
                print(True)
            else:
                print(f"Failed to download image for alg {alg}")