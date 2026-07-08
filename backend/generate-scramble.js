import min2phase from 'min2phase.js';
import {createCube, performMoves, cubieToString} from './cube.js';
import { lxs, eo_pair, zbll, zbll_sets, lxs_sets } from './algs.js';

async function initialize () {
    await min2phase.initFull();
    console.log('min2phase initialized');
}

function scrubAlg(alg) {
    var res = alg.replaceAll('(', '').replaceAll(')', '').replaceAll("2'", '2').replaceAll("3'", '').replaceAll('3', "'");
    res = res.trim().replace(/\s+/g, " ");
    return res;
}

function reverseAlg(alg) {
    const moves = alg.split(' ');
    const reversedMoves = moves.reverse().map(move => {
        if (move.endsWith("'")) {
            return move.slice(0, -1);
        } else if (move.endsWith("2")) {
            return move;
        } else {
            return move + "'";
        }
    });
    return reversedMoves.join(' ');
}

function generateLXS(set, id) {
    var cube = createCube();

    var zbllSet = zbll_sets[Math.floor(Math.random() * zbll_sets.length)];
    var zbllAlg = zbll[zbllSet][Math.floor(Math.random() * zbll[zbllSet].length)];
    zbllAlg = scrubAlg(zbllAlg);

    var lxsAlg = scrubAlg(lxs[set][id]);

    performMoves(cube, zbllAlg + ' ' + reverseAlg(lxsAlg));

    var solution = min2phase.solve(cubieToString(cube));
    return reverseAlg(scrubAlg(solution));
}

function generateEO(set, id) {
    var cube = createCube();

    var lxsSet = lxs_sets[Math.floor(Math.random() * lxs_sets.length)];
    var lxsAlg = lxs[lxsSet][Math.floor(Math.random() * lxs[lxsSet].length)];
    lxsAlg = scrubAlg(lxsAlg);

    var eoAlg = scrubAlg(eo_pair[set][id]);

    performMoves(cube, lxsAlg + ' ' + reverseAlg(eoAlg));

    var solution = min2phase.solve(cubieToString(cube));
    return reverseAlg(scrubAlg(solution));
}

export { initialize, generateLXS, generateEO };