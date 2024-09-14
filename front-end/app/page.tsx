import Navbar from "./navbar"
import Defaultpage from "./default"
import axios from "axios"

export async function fetchCase(algSet: string, selectedCases: string){
  var data = await axios.get(`http://127.0.0.1:5000/Fetch_Case/${algSet}/${selectedCases}`)
  return data.data
}

export default async function Home() {
  var data;
  try {
    data = await fetchCase('lxs', 'UFR')
    //console.log('Data received: ', data)
  } catch (error) {
    console.log(error)
  }
  var scramble_list = data.scramble
  var scramble = scramble_list.join(' ');

  return(
    <main>
      <Navbar/>
      <Defaultpage getScramble={scramble} getSolution={data.case} getLink={data.image_link}/>
    </main>
  )
}
