'use client'
import {useAppContext} from "./context"

const Navbar = () => {
    const {selection, setSelection, cases, setCases} = useAppContext()

    const quickSelection = (select: boolean) => {
        const newCases = new Map(cases)
        const setMap = newCases.get(selection) || new Map()

        for(var key of setMap?.keys()!){
            setMap.set(key, select ? Array.from({ length: case_amount.get(selection)?.get(key)! }, (_, i) => i) : [])
        }
        
        newCases.set(selection, setMap)
        setCases(newCases)
    }

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

    return (
        <nav className="bg-gray-800 p-2">
            <div className="container mx-auto flex justify-between">
                <h1 className="text-center text-2xl text-white font-semibold">APB Trainer</h1>
                <div className="space-x-4">
                    <select value={selection} onChange={(e) => setSelection(e.target.value)} className="bg-black w-32 h-8">
                        <option value="lxs">LXS</option>
                        <option value="eo_pair">EO Pair</option>
                    </select>
                    <button onClick={() => quickSelection(true)} className="bg-green-600 w-32 rounded-lg px-4 py-1">Select All</button>
                    <button onClick={() => quickSelection(false)} className="bg-red-600 w-32 rounded-lg px-4 py-1">Deselect All</button>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;