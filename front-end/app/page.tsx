import Navbar from "./navbar"
import Defaultpage from "./default"
import axios from "axios"

async function access(algSet: string, selectedCases: string){
  var data = await axios.get(`http://127.0.0.1:5000/Fetch_Case/${algSet}/${selectedCases}`)
  return data.data
}

export default async function Home() {
  try {
    const data = await access('lxs', 'UFR')
    console.log('Data received: ', data)
  } catch (error) {
    //console.log(error)
  }

  return(
    <main>
      <Navbar/>
      <Defaultpage/>
    </main>
  )
}
