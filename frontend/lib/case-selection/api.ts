export default async function fetchScramble(set: string, subset: string, index: number): Promise<string> {
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/${set}/${subset}/${index}`)
    return res.text();
}