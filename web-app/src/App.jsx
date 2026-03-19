import StatusCard from './assets/StatusCard/StatusCard'
function App() {
  return (
    <>
      <div className="row">
        <h1>NASA Earthdata Healthcheck</h1>
      </div>
      <div className="row">
        <div className="col-md-4 text-start">
          <StatusCard title="Earthdata Search" url="https://search.earthdata.nasa.gov" status="True" />
        </div>
        <div className="col-md-4 text-start">
          <StatusCard title="Earthdata Login" url="https://urs.earthdata.nasa.gov" status="True" />
        </div>
        <div className="col-md-4 text-start">
          <StatusCard title="Earthdata API" url="https://cmr.earthdata.nasa.gov/search/collections.json" status="False" />
        </div>
      </div>
    </>
  )
}

export default App