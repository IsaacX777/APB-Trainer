export default async function fetchScramble(set: string, subset: string, index: number): Promise<string> {
    //console.log(`${process.env.NEXT_PUBLIC_API_URL}/${set}/${subset}/${index}`)
    const res = await fetch(`${process.env.NEXT_PUBLIC_TEST}/${set}/${subset}/${index}`)
    return res.text();
}