import { lxs_sizes, eo_pair_sizes } from '@/public/algs';
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Toggle } from "@/components/ui/toggle"

export default function CaseSelector({
    set,
    selectedCases,
    setSelectedCases
} : {
    set: string,
    selectedCases: Record<string, boolean[]>,
    setSelectedCases: (newSelectedCases: Record<string, boolean[]>) => void
}) {
    var subsets = set === "lxs" ? Object.keys(lxs_sizes) : Object.keys(eo_pair_sizes);

    function handleCaseClick(subset: string, index: number) {
        console.log(selectedCases);
        const newSelectedCases = { ...selectedCases };
        newSelectedCases[subset][index] = !newSelectedCases[subset][index];
        setSelectedCases(newSelectedCases);
    }

    return (
        <div>
            <Tabs defaultValue={subsets[0]} className="w-[400px]">
                <TabsList>
                    {subsets.map((subset) => (
                        <TabsTrigger key={subset} value={subset}>{subset}</TabsTrigger>
                    ))}
                </TabsList>
                {subsets.map((subset) => (
                    <TabsContent key={subset} value={subset}>
                        <div>
                            {Array.from({ length: set === "lxs" ? lxs_sizes[subset] : eo_pair_sizes[subset] }, (_, index) => (
                                <Toggle 
                                key={index} 
                                variant="outline" 
                                onClick={() => handleCaseClick(subset, index)}
                                >
                                    {set} - {subset} - {index}
                                </Toggle>
                            ))}
                        </div>
                    </TabsContent>
                ))}
            </Tabs>
        </div>
    )
}