import { useState } from 'react'
import './App.css'
import StatusCard from './assets/StatusCard/StatusCard'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <section id="center">
        <div className="hero">
        </div>
        <div>
          <h1>NASA Earthdata Healthcheck</h1>
        </div>
      </section>
      <div className="ticks">
      </div>
      <section id="spacer"></section>
      <div>
        <StatusCard name="Connectivity" status="operational" />
        <StatusCard name="Hi" status="operational" />
        <StatusCard name="Test2" status="operational" />
        <StatusCard name="Hello" status="operational" />
      </div>
    </>
  )
}

export default App
