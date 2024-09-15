import {useAppContext} from "./context"
import { useState } from "react"

const CaseSelect = () => {
    const {selection, cases, setCases} = useAppContext()
    const [openUFR, setOpenUFR] = useState(false)
    const [openRFU, setOpenRFU] = useState(false)
    const [openFUR, setOpenFUR] = useState(false)
    const [openDFR, setOpenDFR] = useState(false)
    const [openRDF, setOpenRDF] = useState(false)
    const [openFRD, setOpenFRD] = useState(false)

    const toggleUFR = () => {
        setOpenUFR(!openUFR)
        imageGenerator(ufr_list)
    }
    const toggleRFU = () => setOpenRFU(!openRFU)
    const toggleFUR = () => setOpenFUR(!openFUR)
    const toggleDFR = () => setOpenDFR(!openDFR)
    const toggleRDF = () => setOpenRDF(!openRDF)
    const toggleFRD = () => setOpenFRD(!openFRD)

    const [imageList, setImageList] = useState<string[]>([])

    const imageGenerator = (algs: string[]) => {
        const newImageList = algs.map(
            (alg) => `https://cube.rider.biz/visualcube.php?fmt=ico&size=150&pzl=3&stage=f2l&case=${alg}`
        );
        setImageList(newImageList);
        console.log({imageList})
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
    };

    const ufr_list = ["(U2) R U R2 U' R' U R", "(U) R U2 R2 U' R' U R", "(U') R U R U' R2 U' R2 U R2", "(U2) R D' R U R' D R'", "(U) R' U2 R U2 R", "R' U' R U' R U2 R", "(U) R U2 R2 U' R U R2 U' R'", "R U' R2 U' R U R U2 R U R'", "R2 U' R2 U2 R2 U R2", "R U' R' U R U' R2 U' R U R", "(U') R' U' R U' R' U R2 U R", "R U' R2 U2 R U2 R2 U' R'", "R U2 R' U R' U2 R U2 R2 U' R'", "R U R2 U2’ R' U2 R2 U' R'", "R U' R' U R U2 R2 U' R U R", "R U R' U R' U' R U R2 U R'", "(U2) R U R' U R' U' R2 U R", "(U) R U2 R' U R' U' R2 U R", "(U2) R' U2 R U2 R U' R U R'", "R U' R' U R' U' R U R", "(U') R U R' U R' U' R U' R U2 R", "(U2) R U R2 U' R U R2 U' R'", "R S' R U' R' f R' F' R U' R'", "(U) R' U' R U' R U R' U' R U2 R", "(U) R' U2 R' U2 R2 U2 R'", "(U2) R2 U2 R' U' R U' R2", "(U2) R U R' U R U' R'", "(U) R U2 R' U R U' R'", "R U2 R' U' R U R'", "(U) R U' R' U R U' R' U R U' R'"]

    if(selection == 'lxs'){
        return(
            <main className="py-2 px-5 mt-5">
                <h1 className="text-xl mb-2 text-center font-semibold">Select Cases</h1>
                <div className="mb-1">
                    <button onClick={toggleUFR} className="bg-gray-800 w-full py-1">UFR</button>
                    {openUFR && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('UFR', index)} className={`p-1 border-2 rounded ${
                                    cases.get('lxs')?.get('UFR')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
                <div className="mb-1">
                    <button onClick={toggleRFU} className="bg-gray-800 w-full py-1">RFU</button>
                    {openRFU && (<div className='text-center text-xl bg-blue-500'>opened</div>)}
                </div>
                <div className="mb-1">
                    <button onClick={toggleFUR} className="bg-gray-800 w-full py-1">FUR</button>
                    {openFUR && (<div className='text-center text-xl bg-blue-500'>opened</div>)}
                </div>
                <div className="mb-1">
                    <button onClick={toggleDFR} className="bg-gray-800 w-full py-1">DFR</button>
                    {openDFR && (<div className='text-center text-xl bg-blue-500'>opened</div>)}
                </div>
                <div className="mb-1">
                    <button onClick={toggleRDF} className="bg-gray-800 w-full py-1">RDF</button>
                    {openRDF && (<div className='text-center text-xl bg-blue-500'>opened</div>)}
                </div>
                <div>
                    <button onClick={toggleFRD} className="bg-gray-800 w-full py-1">FRD</button>
                    {openFRD && (<div className='text-center text-xl bg-blue-500'>opened</div>)}
                </div>
            </main>
        )
    }
    else if(selection == 'eo_pair'){
        return(
            <main>
            <div className="p-4">{selection}</div>
            </main>
        )
    }
}

export default CaseSelect