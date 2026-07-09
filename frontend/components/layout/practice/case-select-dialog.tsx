import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle
} from "@/components/ui/dialog"
import CaseSelector from "./case-selector"

export default function CaseSelectDialog ({
    open,
    setOpen,
    set,
    selectedCases,
    setSelectedCases
} : {
    open: boolean,
    setOpen: (newOpen: boolean) => void,
    set: string,
    selectedCases: Record<string, boolean[]>,
    setSelectedCases: (newSelectedCases: Record<string, boolean[]>) => void
}) {
    return (
        <Dialog open={open} onOpenChange={setOpen}>
            <DialogContent className="sm:max-w-[80vw] p-12">
                <DialogHeader>
                    <DialogTitle>Select Cases</DialogTitle>
                    <DialogDescription>
                        Choose a subset and select the cases you want to train.
                    </DialogDescription>
                </DialogHeader>
                <CaseSelector set={set} selectedCases={selectedCases} setSelectedCases={setSelectedCases}/>
            </DialogContent>
        </Dialog>
    )
}