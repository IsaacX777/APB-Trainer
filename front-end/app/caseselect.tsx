import {useAppContext} from "./context"
import { useState } from "react"

const CaseSelect = () => {
    const {selection, cases, setCases} = useAppContext()
    const [openSubset, setOpenSubset] = useState<string | null>(null)

    const toggleSubset = (subset: string) => {
        setOpenSubset(openSubset === subset ? null : subset)
    }

    const handleCaseSelection = (subset: string, index: number) => {
        const newCases = new Map(cases)
        const setMap = newCases.get(selection) || new Map()
        const currentIndices = setMap.get(subset) || []

        const updatedIndices = currentIndices.includes(index)
            ? currentIndices.filter((i : number) => i !== index)
            : [...currentIndices, index];

        setMap.set(subset, updatedIndices)
        newCases.set(selection, setMap)
        setCases(newCases)
    }

    const quickSelection = (subset: string, select: boolean) => {
        const newCases = new Map(cases)
        const setMap = newCases.get(selection) || new Map()
        setMap.set(subset, select ? Array.from({ length: case_amount.get(selection)?.get(subset)! }, (_, i) => i) : [])
        newCases.set(selection, setMap)
        setCases(newCases)
    }

    const subsets = new Map([
        ['lxs', new Map([
            ['UFR', 'UFR'],
            ['RFU', 'RFU'],
            ['FUR', 'FUR'],
            ['DFR', 'DFR'],
            ['RDF', 'RDF'],
            ['FRD', 'FRD']
        ])],
        ['eo_pair', new Map([
            ['dBR', 'dBR'],
            ['dFR', 'dFR'],
            ['OU', 'Oriented Pair U'],
            ['OR', 'Oriented Pair R'],
            ['MU', 'Misoriented Pair U'],
            ['MR', 'Misoriented Pair R']
        ])]
    ])

    const case_amount = new Map([
        ['lxs', new Map([
            ['UFR', 30],
            ['RFU', 30],
            ['FUR', 30],
            ['DFR', 8],
            ['RDF', 9],
            ['FRD', 9]
        ])],
        ['eo_pair', new Map([
            ['dBR', 11],
            ['dFR', 11],
            ['OU', 31],
            ['OR', 31],
            ['MU', 32],
            ['MR', 32]
        ])]
    ])

    return(
        <footer className="py-2 px-5 mt-5">
            <div className="justify-center">
                <h1 className="text-xl mb-2 text-center font-semibold">Select Cases</h1>
            </div>
            {Array.from(subsets.get(selection)!.keys()).map((subset) => (
                <div key={subset} className="mb-1">
                    <button onClick={() => toggleSubset(subset)} className="bg-gray-800 w-full py-1">
                        {subsets.get(selection)?.get(subset)}
                    </button>
                    {openSubset === subset && (
                        <div className="justify-center mx-auto my-2">
                            <div className="flex justify-center mx-auto space-x-4 mb-2">
                                <button onClick={() => quickSelection(subset, true)} className="bg-green-600 w-40 rounded-lg px-4 py-1">Select All</button>
                                <button onClick={() => quickSelection(subset, false)} className="bg-red-600 w-40 rounded-lg px-4 py-1">Deselect All</button>
                            </div>
                            <div className="grid grid-cols-8 gap-5">
                                {Array.from({ length: case_amount.get(selection)?.get(subset)! }).map((_, index) => (
                                    <button
                                        key={index}
                                        onClick={() => handleCaseSelection(subset, index)}
                                        className={`p-1 border-2 rounded ${
                                            cases.get(selection)?.get(subset)?.includes(index)
                                                ? "border-blue-500"
                                                : "border-transparent"
                                        }`}>
                                        <img src={`/${selection}/${subset}/${index}.png`} alt={`Case ${index + 1}`} />
                                    </button>
                                ))}
                            </div>
                        </div>
                    )}
                </div>
            ))}
        </footer>
    )
}

export default CaseSelect