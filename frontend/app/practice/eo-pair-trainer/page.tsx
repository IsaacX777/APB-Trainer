"use client";

import {eo_pair, eo_pair_sizes} from '@/public/algs';
import CaseDisplay from '@/components/layout/practice/case-display';
import CaseSelector from '@/components/layout/practice/case-selector';
import { useState } from 'react';

import {Button} from '@/components/ui/button';
import fetchScramble from '@/lib/api/scramble';

const defaultCases = Object.fromEntries(
  Object.entries(eo_pair_sizes).map(([subset, size]) => [subset, Array.from({ length: size }, (_, index) => true)])
);

export default function Page() {

    function selectCase () {
        return fetchScramble("eo_pair", "dFR", 0).then((scramble) => {
            console.log(scramble);
        });
    }

    const [selectedCases, setSelectedCases] = useState<Record<string, boolean[]>>(defaultCases);

    return (
        <>
            <CaseDisplay set="exampleSet" subset="exampleSubset" index={0}/>
            <CaseSelector set="eo_pair" selectedCases={selectedCases} setSelectedCases={setSelectedCases}/>
            <Button onClick={() => selectCase()}>
                next case
            </Button>
        </>
    );
}