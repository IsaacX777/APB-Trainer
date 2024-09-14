'use client'

const Defaultpage = () => {
    return(
        <main>
          <h1>Scramble:</h1>
          <h1>Solution:</h1>
          <img src='https://cube.rider.biz/visualcube.php?fmt=ico&size=150&pzl=3'/>
          <div>
            <button className="bg-blue-700">Next Case</button>
            <button className="bg-blue-700">Show Solution</button>
          </div>
        </main>
    )
}

export default Defaultpage