"use client";

import { Button } from '@/components/ui/button';

import CaseDisplay from '@/components/layout/practice/case-display';
import CaseController from '@/components/layout/practice/case-controller';
import CaseSelectDialog from '@/components/layout/practice/case-select-dialog';
import { useState } from 'react';

import {lxsDefaultCases} from '@/lib/case-selection/select-case';
import { lxs } from '@/lib/case-selection/algs';

import {Settings} from "lucide-react"

export default function Page() {

    const [selectedCases, setSelectedCases] = useState<Record<string, boolean[]>>(lxsDefaultCases);
    const [scramble, setScramble] = useState<string | null>(null);
    const [subset, setSubset] = useState<string | null>(null);
    const [index, setIndex] = useState<number | null>(null);
    const [selectMode, setSelectMode] = useState<boolean>(false)

    return (
        <div>
            <CaseSelectDialog open={selectMode} setOpen={setSelectMode} set="lxs" selectedCases={selectedCases} setSelectedCases={setSelectedCases}/>
            <div className="flex justify-end px-24">
                <Button variant="outline" onClick={() => setSelectMode(true)}>
                    Select Cases
                    <Settings data-icon="inline-start" />
                </Button>
            </div>
            <div className="flex flex-col p-8 items-center justify-center gap-4">
                <CaseDisplay scramble={scramble} set="lxs" subset={subset} index={index}/>
                <CaseController set="lxs" solution={subset && index ? lxs[subset][index] : ""} selectedCases={selectedCases} scramble={scramble} setScramble={setScramble} setSubset={setSubset} setIndex={setIndex}/>
            </div>
        </div>
    );
}