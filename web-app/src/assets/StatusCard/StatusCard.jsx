import Card from 'react-bootstrap/Card';
import Badge from 'react-bootstrap/Badge';


function determineStatus(status) {
  if (status)
    return (
      <Badge bg="success">Operational</Badge>
  )
  else
    return (
      <Badge bg="danger">Unavailable</Badge>
    )
}

function StatusCard(props) {
  return (
   <Card style={{ width: '25rem' }}>
      <Card.Body>
        <div className="container">
          <div className="row">
            <div className="col-md-3 text-start">
              {determineStatus(props.status)}
            </div>
            <div className="col-md-9 text-start">
              <Card.Title>{props.title}</Card.Title>
            </div>
            <div className="col-md-12 text-start">
          <Card.Text>
            {props.url}
          </Card.Text>
        </div>
          </div>
        </div>
      </Card.Body>
    </Card>
  );
}

export default StatusCard;