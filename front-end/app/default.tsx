'use client'
import {fetchCase} from './page'
import { useState } from 'react'

interface DefaultPageProps {
  getScramble: string;
  getSolution: string;
  getLink: string;
}

const DefaultPage: React.FC<DefaultPageProps> = ({ getScramble, getSolution, getLink }) => {
  const [scramble, setScramble] = useState(getScramble)
  const [solution, setSolution] = useState(getSolution)
  const [link, setLink] = useState(getLink)
  const [solutionDisplay, setSolutionDisplay] = useState(false);

  const nextCase = async () => {
    try {
      var data = await fetchCase('lxs', 'UFR')
      //console.log('Data received: ', data)

      var scramble_list = data.scramble
      var scramble = scramble_list.join(' ');

      setSolutionDisplay(false)
      setScramble(scramble)
      setSolution(data.case)
      setLink(data.image_link)
    } catch (error) {
      console.log(error)
    }
  }

  const showSolution = () => {
    setSolutionDisplay(!solutionDisplay)
  }

  return(
      <main>
        <h1 className='text-center text-xl my-3'>{scramble}</h1>
        <div className='flex justify-center my-3'>
          <img className='object-center' src={link}/>
        </div>
        <div className='space-x-4 flex justify-center my-3'>
          <button onClick={nextCase} className="bg-blue-700 w-40 rounded-lg px-4 py-1">Next Case</button>
          <button onClick={showSolution} className="bg-blue-700 w-40 rounded-lg px-4 py-1">Show Solution</button>
        </div>
        {solutionDisplay && (<h1 className='text-center text-xl my-3'>{solution}</h1>)}
      </main>
  )
}

export default DefaultPage