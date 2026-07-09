import Parent from "./parent";
import axios from "axios"


export async function fetchCase(algSet: string, selectedCases: string){
  var data = await axios.get(`http://127.0.0.1:5000/Fetch_Case/${algSet}/${selectedCases}`)
  return data.data
}

export default async function Home() {
  return(
    <main>
      <Parent getScramble='Scramble' getSolution='' getDirectory='/lxs/default.png'/>
    </main>
  )
}
