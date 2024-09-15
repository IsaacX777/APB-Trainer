'use client'
import {useAppContext} from "./context"

const Navbar = () => {
    const {selection, setSelection} = useAppContext()

    return (
        <nav className="bg-gray-800 p-2">
            <div className="container mx-auto flex justify-between">
                <h1 className="text-center text-2xl text-white font-semibold">APB Trainer</h1>
                <select value={selection} onChange={(e) => setSelection(e.target.value)} className="bg-black w-32 h-8">
                    <option value="lxs">LXS</option>
                    <option value="eo_pair">EO Pair</option>
                </select>
            </div>
        </nav>
    );
};

export default Navbar;