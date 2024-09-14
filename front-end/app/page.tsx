'use client'

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from "./navbar";

const Default = () => {
  return(
    <div>
      <h1>Scramble:</h1>
      <h1>Solution:</h1>
      <img src='https://cube.rider.biz/visualcube.php?fmt=ico&size=150&pzl=3'/>
      <div>
        <button>Next Case</button>
        <button>Show Solution</button>
      </div>
    </div>
  );
}
const CaseSelect = () => <div className="p-4">Case Select</div>;

export default function Home() {
  return (
    <Router>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Default/>} />
        <Route path="/case_select" element={<CaseSelect/>} />
      </Routes>
    </Router>
  );
}
