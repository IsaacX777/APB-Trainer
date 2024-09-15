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
    const [opendBR, setOpendBR] = useState(false)
    const [opendFR, setOpendFR] = useState(false)
    const [openOU, setOpenOU] = useState(false)
    const [openOR, setOpenOR] = useState(false)
    const [openMU, setOpenMU] = useState(false)
    const [openMR, setOpenMR] = useState(false)

    const toggleUFR = () => {
        setOpenUFR(!openUFR)
        setOpenRFU(false)
        setOpenFUR(false)
        setOpenDFR(false)
        setOpenRDF(false)
        setOpenFRD(false)
        setOpendBR(false)
        setOpendFR(false)
        setOpenOU(false)
        setOpenOR(false)
        setOpenMU(false)
        setOpenMR(false)
        imageGenerator(ufr_list)
    }
    const toggleRFU = () => {
        setOpenRFU(!openRFU)
        setOpenUFR(false)
        setOpenFUR(false)
        setOpenDFR(false)
        setOpenRDF(false)
        setOpenFRD(false)
        setOpendBR(false)
        setOpendFR(false)
        setOpenOU(false)
        setOpenOR(false)
        setOpenMU(false)
        setOpenMR(false)
        imageGenerator(rfu_list)
    }
    const toggleFUR = () => {
        setOpenFUR(!openFUR)
        setOpenUFR(false)
        setOpenRFU(false)
        setOpenDFR(false)
        setOpenRDF(false)
        setOpenFRD(false)
        setOpendBR(false)
        setOpendFR(false)
        setOpenOU(false)
        setOpenOR(false)
        setOpenMU(false)
        setOpenMR(false)
        imageGenerator(fur_list)
    }
    const toggleDFR = () => {
        setOpenDFR(!openDFR)
        setOpenUFR(false)
        setOpenRFU(false)
        setOpenFUR(false)
        setOpenRDF(false)
        setOpenFRD(false)
        setOpendBR(false)
        setOpendFR(false)
        setOpenOU(false)
        setOpenOR(false)
        setOpenMU(false)
        setOpenMR(false)
        imageGenerator(dfr_list)
    }
    const toggleRDF = () => {
        setOpenRDF(!openRDF)
        setOpenUFR(false)
        setOpenRFU(false)
        setOpenFUR(false)
        setOpenDFR(false)
        setOpenFRD(false)
        setOpendBR(false)
        setOpendFR(false)
        setOpenOU(false)
        setOpenOR(false)
        setOpenMU(false)
        setOpenMR(false)
        imageGenerator(rdf_list)
    }
    const toggleFRD = () => {
        setOpenFRD(!openFRD)
        setOpenUFR(false)
        setOpenRFU(false)
        setOpenFUR(false)
        setOpenDFR(false)
        setOpenRDF(false)
        setOpendBR(false)
        setOpendFR(false)
        setOpenOU(false)
        setOpenOR(false)
        setOpenMU(false)
        setOpenMR(false)
        imageGenerator(frd_list)
    }
    const toggledBR = () => {
        setOpendBR(!opendBR)
        setOpendFR(false)
        setOpenOU(false)
        setOpenOR(false)
        setOpenMU(false)
        setOpenMR(false)
        setOpenUFR(false)
        setOpenRFU(false)
        setOpenFUR(false)
        setOpenDFR(false)
        setOpenRDF(false)
        setOpenFRD(false)
        imageGenerator(dBR_list)
    }
    const toggledFR = () => {
        setOpendFR(!opendFR)
        setOpendBR(false)
        setOpenOU(false)
        setOpenOR(false)
        setOpenMU(false)
        setOpenMR(false)
        setOpenUFR(false)
        setOpenRFU(false)
        setOpenFUR(false)
        setOpenDFR(false)
        setOpenRDF(false)
        setOpenFRD(false)
        imageGenerator(dFR_list)
    }
    const toggleOU = () => {
        setOpenOU(!openOU)
        setOpendBR(false)
        setOpendFR(false)
        setOpenOR(false)
        setOpenMU(false)
        setOpenMR(false)
        setOpenUFR(false)
        setOpenRFU(false)
        setOpenFUR(false)
        setOpenDFR(false)
        setOpenRDF(false)
        setOpenFRD(false)
        imageGenerator(OU_list)
    }
    const toggleOR = () => {
        setOpenOR(!openOR)
        setOpendBR(false)
        setOpendFR(false)
        setOpenOU(false)
        setOpenMU(false)
        setOpenMR(false)
        setOpenUFR(false)
        setOpenRFU(false)
        setOpenFUR(false)
        setOpenDFR(false)
        setOpenRDF(false)
        setOpenFRD(false)
        imageGenerator(OR_list)
    }
    const toggleMU = () => {
        setOpenMU(!openMU)
        setOpendBR(false)
        setOpendFR(false)
        setOpenOU(false)
        setOpenOR(false)
        setOpenMR(false)
        setOpenUFR(false)
        setOpenRFU(false)
        setOpenFUR(false)
        setOpenDFR(false)
        setOpenRDF(false)
        setOpenFRD(false)
        imageGenerator(MU_list)
    }
    const toggleMR = () => {
        setOpenMR(!openMR)
        setOpendBR(false)
        setOpendFR(false)
        setOpenOU(false)
        setOpenOR(false)
        setOpenMU(false)
        setOpenUFR(false)
        setOpenRFU(false)
        setOpenFUR(false)
        setOpenDFR(false)
        setOpenRDF(false)
        setOpenFRD(false)
        imageGenerator(MR_list)
    }

    const [imageList, setImageList] = useState<string[]>([])

    const imageGenerator = (algs: string[]) => {
        const newImageList = algs.map(
            (alg) => selection == 'lxs' ? `https://cube.rider.biz/visualcube.php?fmt=ico&size=150&pzl=3&stage=f2l&case=${alg}`:
            `https://cube.rider.biz/visualcube.php?fmt=ico&size=150&pzl=3&stage=els&case=${alg}`
        );
        setImageList(newImageList);
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
    const rfu_list = ["(U') S' R U R' U R U R' S", "R U R' S R2 S' R2", "(U') R U' R' U R U R' S R2' S' R2", "R' U' R U R U' R U R'", "R D' R U' R' D U R'", "(U) R U R2 U2' R' U2 R2 U R'", "(U') R' U2 R U R U R", "(U') R' U R U2 R2 U2 R' U' R", "(U') R' U2 R' U R U R", "(U') R' U' R U R", "(U') R' U2 R2 U R' U R2 U' R'", "(U2) R' U' R U R U2 R U R'", "(U') R U' R2 U2 R U R U R", "(U2) R' U' R U R2 U' R' U' R U R'", "(U') R U' R2 U' R U R", "R' U2 R2 U2 R2 U' R'", "(U2) R U' R' U R' U2 R U2 R2 U' R'", "R U R' S' U2 S", "(U) R' U' R2 U' R' U2 R2 U' R'", "(U') R U2 R2 U' R U R", "(U2) R' U2 R' U2 R2 U R'", "(U') R U R2 U2 R U R U R", "R U R' U' S' U2 S", "(U2) R' U2 R U R U' R' U R U R", "(U') R U R2 U' R U R", "R2 D R' U2 R D' R' U R'", "(U2) R U' R' U' R U R'", "R U R'", "(U') R U' R' U R U R'", "(U') R U2 R' U R U R'"]
    const fur_list = ["(U') R U2 R' U R' U' R U R2 U' R'", "(U') R U R' U R' U' R U R2 U' R'", "R' U' R U R2 U' R'", "(U') R U' R' U R' U' R U R2 U' R'", "(U') R' U2 R U R' U' R U2 R", "(U') R' U' R U R U' R U' R' U R U' R'", "(U') R U R' U2 R' U' R2 U R", "(U2) R' U2 R2 U2 R", "(U') R D' R U' R' D R'", "(U2) S' U2 S U R U' R'", "(U) R' U' R U' R U R U R", "(U') R U2 R' U R' U' R' U R", "(U) R' U' R2 U R", "(U') R' U' R' U' R U2 R", "(U2) R U R' U' R' U' R U R", "(U) R' U' R U R U R U R'", "(U2) S R2' S' R3 U2' R'", "(U') R U R' U R' U' R' U R", "(U') R U' R' U2 R' U' R2 U R", "(U) R' U' R U D' R U R' D R", "R U' D' R U R' D R'", "(U') R U2 R' U2 R' U' R2 U R", "F' R U R U' R' F R'", "R' U2 R' U2' R", "(U2) R U D' R U' R' U D R'", "(U) R' F R U R U' R' F' R U2 R'", "(U') R U2 R' U2 R U' R'", "(U') R U R' U2 R U' R'", "(U) R U' R'", "(U') R U' R' U2 R U' R'"]
    const dfr_list = ["(U) R U' R2 U' R U R U' R U R'", "(U) S R2' S' R2", "(U) R U' D' R U' R' U D R'", "R' F' R U R U' R' f R2 S' R2", "(U') S' R U R' U' F' U' f", "(U2) R U' D' R U R' U D R'", "R U' R' U' R U' R2 U' R U R", "(U') R' F' R U R U' R' F"]
    const rdf_list = ["(U) R' U' R U R U' R' U' R U R", "(U') R U2 R' U R' U' R U R", "R' U' R U R U' R U' R' U R U R'", "(U') R' U' R U R2 U R'", "(U2) R' U2 R U2 R2 U R'", "R' U2 R' U2 R2 U' R'", "R U2 R' U R U2 R2 U' R U R", "R U R' U' R U R'", "R U' R' U R U2 R' U R U' R'"]
    const frd_list = ["R U' R2 U' R' U R", "R U R2 U2 R U2 R", "R' U' R' U' R U R' U' R U2 R", "R U' R2 U' R U R2 U' R'", "(U) R' U' R U R2 U' R' U2 R U R'", "(U') R U' R' U R' U' R2 U R", "R U R' U' R U' R' U R' U' R U R", "(U') R U' R' U R U' R'", "R U' R' U' R U R' U2 R U' R'"]

    const dBR_list = ["F R' F' R", "F R U R' U' F'", "R' F R F'", "f' U' f", "S' R U' R' U' S", "r U r' U2 M' U M", "S R' U' R U R S'", "S' U' S", "S' U R U2 R' S", "R U R' S' U' S", "F R' F' R U S' U' S"]
    const dFR_list = ["F R' F'","F R U R' U' F'", "f R f'", "F R F'", "S' R' U' R U S", "r' U' r U2 M U' M'", "r' U r U2 r' U' r", "S' U' S", "S' U R' U2 R S", "R' U' R S' U' S", "F U R U' R' S R' S' R F'"]
    const OU_list = ["(U2) F R' F' U R", "(U') R U f' U f", "(U') F R2 U R' U' F'", "(U2) F' U F R", "(U') F R F'", "f R f' U2 R", "(U') F' U' F U R", "(U') R F' U' F", "(U) f R' f' U' R", "(U') R f' U f", "(U') R f' U2 f", "(U') R f' U' f", "(U') R F' U F", "(U2) R' f R U R U' f'", "(U') R U' f' U' f", "(U) R' U' R S R' S' U' R", "(U) R' U2 R S' U' S", "(U') R U2 S' U' S", "(U2) F' U F2 R F'", "(U2) S' U' R' U2 R S", "(U') R U' S' U' S", "(U') R' f' U' f2 R f' R'", "S' U R' U2 R S", "(U') R U S' U' S", "R S R' S' U' R", "(U2) R' S R S' U R", "(U') R S' U' S", "(U') R S' U' R U2 R' S", "(U') R2 U' R' S' U' S", "(U2) R2 S R S' U R", "(U2) S R S' R' F R U R U' F'"]
    const OR_list = ["(U') R' U' F' U F R'", "R' U R' U' F' U' F", "(U) F R' F' R2", "F R' F' R U R U' R", "R' U R' f' U' f", "R' U R' F' U' F", "R2' F R' F' R", "R F R F'", "R' f R f' R'", "R2 F' U' F", "f' U' f R'", "(U) f R' f' R2", "R U' F' R' U R F", "R U2 R' f R' f' U' R", "R2 F' U F", "R2 U2 S' U' S", "(U') S' U S R2", "S R U' R' U R S'", "(U2) S' U' S U' R2", "R U2 R' U S R S' U R", "(U) S' U' S R2", "f R U R' U' R' f' R2", "R2 S' U' S", "R U R' S R S' U' R", "R D' r U' r' D R", "R' f R U R U' R' f' R'", "R U' R2 S R S' U R", "R' U2 R U S' U' S R2", "f R' S' R F' R2", "(U) R' S R S' R U' R2", "(U2) D r' U' r D' F R' F' R2"]
    const MU_list = ["(U) R' F' U' F R", "(U) f U R' U' f'", "f' U f R'", "(U') F' U' F R2", "(U2) R' f R2 f'", "(U) f R' f'", "(U') R U2 R U R' S R' S'", "R' U2 R U S R S'", "(U2) F R2 f' U' S", "(U) R D r' U' r D' R'", "(U) R' F' U' F2 R F'", "R' U' S R S'", "(U2) R U2 R' U' S R S'", "(U') f U R' U' F' R S'", "(U) S' U' S R' U' R", "(U) R U R' S R' S'", "(U') R U R' S' U' S R", "(U2) f' U' f2 R2 f'", "R' S' U' S R", "(U') D' r U r' U' D R", "R' U' f R2 U R' U' f'", "(U) f' R' U2 R f", "R' U' R2 U2 S R' S'", "(U') D r' U r D' R'", "(U2) S R' F R2 f'", "(U') R2 U R' S' U' S R", "(U) S' U' S R' U' F R F'", "(U') D r' U r D' R2 F R F'", "(U) R D r' U' r D' R2 F R F'", "D r' U' r D' R F R' F'", "(U) R S R S' R2 F R' F'", "(U2) S R S' R' f R2 f'"]
    const MR_list = ["F R2 F' U' R", "R2 F' U' F R", "(U') f R f' R' U2 R2", "(U) f U R U' f' R", "R' U R' F R2 F'", "R' f R' f'", "S R U' R' U R S' R", "R U2 R' U S R S' R", "(U) R2 U' R S R' S'", "R U' R' S R S' R' U R2", "R U' R' U S R S' R", "R D' r U' r' D R2", "(U') R U' R' U' S R S' R", "D r' U' r D' R'", "(U) R2 U R2 S R S' R", "R' f' R' U2 R f", "(U') f' R' U2 R f R", "S' U' R' U2 R S R", "S R S' R' U R2", "R' S R S' U R2", "(U) S R S' R", "(U) R' S R' S'", "R D' U r U' r' D R2", "(U2) S R S' R' f R' f' R2", "(U) R' U2 R2 S R S'", "R U2 R2 f R2 F' R S'", "(U2) F R' F' R2 D r' U r D'", "D r' U' r D' R2 F R F'", "S R S' R2 F R' F'", "R' S R S' U2 S' U' S R2", "R' B' R2 B R' S R S' R", "(U) R S' U' S2 R' S' U R"]

    if(selection == 'lxs'){
        return(
            <main className="py-2 px-5 mt-5">
                <div>
                    <h1 className="text-xl mb-2 text-center font-semibold">Select Cases</h1>
                    <div>
                        <button>Select All</button>
                        <button>Deselect All</button>
                    </div>
                </div>
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
                    {openRFU && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('RFU', index)} className={`p-1 border-2 rounded ${
                                    cases.get('lxs')?.get('RFU')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
                <div className="mb-1">
                    <button onClick={toggleFUR} className="bg-gray-800 w-full py-1">FUR</button>
                    {openFUR && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('FUR', index)} className={`p-1 border-2 rounded ${
                                    cases.get('lxs')?.get('FUR')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
                <div className="mb-1">
                    <button onClick={toggleDFR} className="bg-gray-800 w-full py-1">DFR</button>
                    {openDFR && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('DFR', index)} className={`p-1 border-2 rounded ${
                                    cases.get('lxs')?.get('DFR')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
                <div className="mb-1">
                    <button onClick={toggleRDF} className="bg-gray-800 w-full py-1">RDF</button>
                    {openRDF && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('RDF', index)} className={`p-1 border-2 rounded ${
                                    cases.get('lxs')?.get('RDF')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
                <div>
                    <button onClick={toggleFRD} className="bg-gray-800 w-full py-1">FRD</button>
                    {openFRD && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('FRD', index)} className={`p-1 border-2 rounded ${
                                    cases.get('lxs')?.get('FRD')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
            </main>
        )
    }
    else if(selection == 'eo_pair'){
        return(
            <main className="py-2 px-5 mt-5">
                <h1 className="text-xl mb-2 text-center font-semibold">Select Cases</h1>
                <div className="mb-1">
                    <button onClick={toggledBR} className="bg-gray-800 w-full py-1">dBR Solved EO</button>
                    {opendBR && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('dBR', index)} className={`p-1 border-2 rounded ${
                                    cases.get('eo_pair')?.get('dBR')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
                <div className="mb-1">
                    <button onClick={toggledFR} className="bg-gray-800 w-full py-1">dFR Solved EO</button>
                    {opendFR && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('dFR', index)} className={`p-1 border-2 rounded ${
                                    cases.get('eo_pair')?.get('dFR')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
                <div className="mb-1">
                    <button onClick={toggleOU} className="bg-gray-800 w-full py-1">Oriented Pair U</button>
                    {openOU && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('OU', index)} className={`p-1 border-2 rounded ${
                                    cases.get('eo_pair')?.get('OU')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
                <div className="mb-1">
                    <button onClick={toggleOR} className="bg-gray-800 w-full py-1">Oriented Pair R</button>
                    {openOR && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('OR', index)} className={`p-1 border-2 rounded ${
                                    cases.get('eo_pair')?.get('OR')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
                <div className="mb-1">
                    <button onClick={toggleMU} className="bg-gray-800 w-full py-1">Misoriented Pair U</button>
                    {openMU && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('MU', index)} className={`p-1 border-2 rounded ${
                                    cases.get('eo_pair')?.get('MU')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
                <div>
                    <button onClick={toggleMR} className="bg-gray-800 w-full py-1">Misoriented Pair R</button>
                    {openMR && (<div className='flex justify-center mx-auto my-2'>
                        <div className="grid grid-cols-8 gap-5">
                            {imageList.map((link, index) => (
                                <button key={index} onClick={() => handleCaseSelection('MR', index)} className={`p-1 border-2 rounded ${
                                    cases.get('eo_pair')?.get('MR')?.includes(index)
                                        ? 'border-blue-500'
                                        : 'border-transparent'}`}>
                                    <img src={link} alt={`Case ${index + 1}`} />
                                </button>
                            ))}
                        </div>
                    </div>)}
                </div>
            </main>
        )
    }
}

export default CaseSelect