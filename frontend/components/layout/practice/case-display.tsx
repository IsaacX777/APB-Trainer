export default function CaseDisplay({
    set,
    subset,
    index
} : {
    set: string,
    subset: string,
    index: number
}) {
    return (
        <>
            <div>{set}</div>
            <div>{subset}</div>
            <div>{index}</div>
        </>
    )
}