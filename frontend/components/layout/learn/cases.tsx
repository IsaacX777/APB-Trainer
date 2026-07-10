"use client"

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { lxs_sizes, eo_pair_sizes, lxs, eo_pair } from '@/lib/case-selection/algs';
import { useTheme } from 'next-themes';

export default function Cases ({
    set
}: {
    set: string
}) {

    const subsets = set === "lxs" ? Object.keys(lxs_sizes) : Object.keys(eo_pair_sizes);
    const algList = set === 'lxs' ? lxs : eo_pair;
    const { resolvedTheme } = useTheme()

    return (
        <div className="flex flex-col items-center p-16">
            <Tabs className="w-3/4 flex gap-y-8">
                <TabsList>
                    {subsets.map((subset) => (
                        <TabsTrigger key={subset} value={subset} className="w-16">{subset}</TabsTrigger>
                    ))}
                </TabsList>

                {subsets.map((subset) => (
                    <TabsContent key={subset} value={subset}>
                        <Table className="">
                            <TableHeader>
                                <TableRow className="text-lg">
                                    <TableHead className="w-[120px]">Case</TableHead>
                                    <TableHead className="pl-16">Algorithm</TableHead>
                                </TableRow>
                            </TableHeader>
                            <TableBody>
                                {Array.from({ length: set === "lxs" ? lxs_sizes[subset] : eo_pair_sizes[subset] }, (_, index) => (
                                    <TableRow key={index}>
                                        <TableCell>
                                            <img src={`/images/${resolvedTheme}/${set}/${subset}/${index}.png`} alt={`Case ${index}`}/>
                                        </TableCell>
                                        <TableCell className="pl-16">
                                            <p className="text-md">{algList[subset][index]}</p>
                                        </TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TabsContent>
                ))}
            </Tabs>
        </div>
    )
}