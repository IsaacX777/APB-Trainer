'use client'
import {AppProvider} from "./context"
import DefaultPage from "./default";

interface ParentProps {
  getScramble: string;
  getSolution: string;
  getDirectory: string;
}

const Parent: React.FC<ParentProps> = ({ getScramble, getSolution, getDirectory }) => {
  
  return(
    <AppProvider>
        <DefaultPage getScramble={getScramble} getSolution={getSolution} getDirectory={getDirectory}/>
    </AppProvider>
  )
}

export default Parent