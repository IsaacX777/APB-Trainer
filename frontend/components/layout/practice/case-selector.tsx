import { lxs_sizes, eo_pair_sizes } from '@/lib/case-selection/algs';
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { useTheme } from 'next-themes';
import { Button } from '@/components/ui/button';
import { useState } from 'react';

export default function CaseSelector({
    set,
    selectedCases,
    setSelectedCases
} : {
    set: string,
    selectedCases: Record<string, boolean[]>,
    setSelectedCases: (newSelectedCases: Record<string, boolean[]>) => void
}) {

    const subsets = set === "lxs" ? Object.keys(lxs_sizes) : Object.keys(eo_pair_sizes);
    const { theme } = useTheme()
    const [selectedSubset, setSelectedSubset] = useState<string>(subsets[0])

    function handleCaseClick(subset: string, index: number) {
        const newSelectedCases = { ...selectedCases };
        newSelectedCases[subset][index] = !newSelectedCases[subset][index];
        setSelectedCases(newSelectedCases);
    }

    function massSelect (newVal: boolean, subset: string) {
        for(let i = 0; i < selectedCases[subset].length; i++) {
            selectedCases[subset][i] = newVal
        }
        const newSelectedCases = { ...selectedCases };
        setSelectedCases(newSelectedCases);
    }

    return (
        <div className='flex flex-col items-center'>
            <Tabs value={selectedSubset} onValueChange={setSelectedSubset} className="w-3/4 items-center">
                <TabsList>
                    {subsets.map((subset) => (
                        <TabsTrigger key={subset} value={subset} className="w-16">{subset}</TabsTrigger>
                    ))}
                </TabsList>
                <div className="flex gap-2 my-2">
                    <Button className="w-32" onClick={() => massSelect(true, selectedSubset)}>Select All</Button>
                    <Button className="w-32" onClick={() => massSelect(false, selectedSubset)}>Deselect All</Button>
                </div>
                {subsets.map((subset) => (
                    <TabsContent key={subset} value={subset}>
                        <div className="grid grid-cols-8 gap-4 overflow-y-auto no-scrollbar h-[40vh] p-1 content-start">
                            {Array.from({ length: set === "lxs" ? lxs_sizes[subset] : eo_pair_sizes[subset] }, (_, index) => (
                                <button 
                                key={index} 
                                onClick={() => handleCaseClick(subset, index)}
                                className={`${selectedCases[subset][index] ? "ring" : ""} rounded-md p-1 aspect-square`}
                                >
                                    <img src={`/images/${theme}/${set}/${subset}/${index}.png`} alt={`Case ${index}`}/>
                                </button>
                            ))}
                        </div>
                    </TabsContent>
                ))}
            </Tabs>
        </div>
    )
}