'use client'
import {AppProvider} from "./context"
import DefaultPage from "./default";

interface ParentProps {
  getScramble: string;
  getSolution: string;
  getLink: string;
}

const Parent: React.FC<ParentProps> = ({ getScramble, getSolution, getLink }) => {
  
  return(
    <AppProvider>
        <DefaultPage getScramble={getScramble} getSolution={getSolution} getLink={getLink}/>
    </AppProvider>
  )
}

export default Parent