import { useTheme } from "next-themes"

export default function CaseDisplay({
    scramble,
    set,
    subset,
    index
} : {
    scramble: string | null,
    set: string,
    subset: string | null,
    index: number | null
}) {

    const { resolvedTheme } = useTheme()

    if(scramble) {
        return (
            <div className="items-center justify-center flex flex-col space-y-4 mb-4">
                <p className="text-lg">{scramble}</p>
                <img src={`/images/${resolvedTheme}/${set}/${subset}/${index}.png`} alt={`Case ${index}`} />
            </div>
        )
    } else {
        return (
            <div>
                <p className="text-lg">Select some cases and click 'start' to begin.</p>
            </div>
        )
    }
}