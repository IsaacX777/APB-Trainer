import {Button} from "@/components/ui/button"
import {selectCase} from '@/lib/case-selection/select-case';
import CaseAlert from "./case-alert";

import { useState } from "react";

export default function CaseController({
    set,
    solution,
    selectedCases,
    scramble,
    setScramble,
    setSubset,
    setIndex
} : {
    set: string,
    solution: string | null,
    selectedCases: Record<string, boolean[]>,
    scramble: string | null,
    setScramble: (newScramble: string) => void,
    setSubset: (newSubset: string | null) => void,
    setIndex: (newIndex: number | null) => void
}) {

    const [showSolution, setShowSolution] = useState<boolean>(false)
    const [alertOpen, setAlertOpen] = useState<boolean>(false)

    function handleNextCase () {
        const generated = selectCase({ set, selectedCases, setScramble, setSubset, setIndex })
        if(!generated) {
            setAlertOpen(true)
        } else {
            setShowSolution(false)
        }
    }

    if(scramble) {
        return (
            <div className="flex flex-col items-center gap-y-4">
                <CaseAlert open={alertOpen} setOpen={setAlertOpen}/>
                <div className="flex gap-2">
                    <Button onClick={() => setShowSolution(!showSolution)} className="w-32">
                        {showSolution ? "Hide solution" : "Show solution"}
                    </Button>
                    <Button 
                    onClick={() => handleNextCase()}
                    className="w-32"
                    >
                        Next case
                    </Button>
                </div>
                {showSolution && (
                    <p className="text-lg">{solution}</p>
                )}
            </div>
        )
    } else {
        return (
            <div>
                <CaseAlert open={alertOpen} setOpen={setAlertOpen}/>
                <Button 
                onClick={() => handleNextCase()}
                className="w-24"
                >
                    Start
                </Button>
            </div>
        )
    }
}