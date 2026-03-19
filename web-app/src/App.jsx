import StatusCard from './assets/StatusCard/StatusCard'
function App() {
  return (
    <>
      <div className="row">
        <h1>NASA Earthdata Healthcheck</h1>
      </div>
      <div className="row">
        <div className="col-md-4 text-start">
          <StatusCard title="Example Service" url="https://example.com" status="Operational" />
        </div>
        <div className="col-md-4 text-start">
          <StatusCard title="Example Service" url="https://example.com" status="Operational" />
        </div>
        <div className="col-md-4 text-start">
          <StatusCard title="Example Service" url="https://example.com" status="Operational" />
        </div>
      </div>
    </>
  )
}

export default App
