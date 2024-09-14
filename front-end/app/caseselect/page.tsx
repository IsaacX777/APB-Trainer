import Link from 'next/link'
import Navbar from '../navbar'

const CaseSelect = () => {
    return(
      <main>
        <Navbar/>
        <div className="p-4">Case Select</div>
        <Link href="/" className="bg-blue-700 rounded-lg px-4 py-1">Close</Link>
      </main>
    )
}

export default CaseSelect