import fetchScramble from '@/lib/case-selection/api';
import { eo_pair_sizes, lxs_sizes } from '@/lib/case-selection/algs';

const eoDefaultCases = Object.fromEntries(
  Object.entries(eo_pair_sizes).map(([subset, size]) => [subset, Array.from({ length: size }, (_, index) => true)])
);
const lxsDefaultCases = Object.fromEntries(
  Object.entries(lxs_sizes).map(([subset, size]) => [subset, Array.from({ length: size }, (_, index) => true)])
);

function selectCase ({
    set,
    selectedCases,
    setScramble,
    setSubset,
    setIndex
} : {
    set: string,
    selectedCases: Record<string, boolean[]>,
    setScramble: (scramble: string) => void,
    setSubset: (subset: string | null) => void,
    setIndex: (index: number | null) => void
}) {
    var selectedList = [];
    for (const [subset, cases] of Object.entries(selectedCases)) {
        for (let i = 0; i < cases.length; i++) {
            if (cases[i]) {
                selectedList.push({ subset, index: i });
            }
        }
    }

    if (selectedList.length === 0) {
        return null;
    }

    const randomCase = selectedList[Math.floor(Math.random() * selectedList.length)];

    return fetchScramble(set, randomCase.subset, randomCase.index).then((scramble) => {
        setScramble(scramble);
        setSubset(randomCase.subset);
        setIndex(randomCase.index);
    });
}

export { eoDefaultCases, lxsDefaultCases, selectCase };