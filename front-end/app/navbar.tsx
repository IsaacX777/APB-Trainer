'use client'
import { Link } from "react-router-dom";

interface NavbarProps {
    onOpenOverlay: () => void;
  }

const Navbar = () => {
    return (
        <nav className="bg-gray-800 p-4">
            <div className="container mx-auto flex justify-between">
                <h1 className="text-center text-2xl text-white font-semibold">APB Trainer</h1>
                <div className="space-x-4">
                    <select className="bg-black w-32 h-8">
                        <option>LXS</option>
                        <option>EO Pair</option>
                    </select>
                    <Link to="case_select" className="bg-blue-700 rounded-lg px-4 py-1">Select Cases</Link>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;