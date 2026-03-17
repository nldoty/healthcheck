import React from "react";
import "./StatusCard.css";

const StatusCard = ({ name, status }) => {
  const getStatusClass = () => {
    switch (status) {
      case "operational":
        return "status-operational";
      case "incident":
        return "status-incident";
      case "maintenance":
        return "status-maintenance";
      case "outage":
        return "status-outage";
      default:
        return "status-unknown";
    }
  };

  const getStatusText = () => {
    switch (status) {
      case "operational":
        return "No issues";
      case "incident":
        return "Incident";
      case "maintenance":
        return "Maintenance";
      case "outage":
        return "Outage";
      default:
        return "Unknown";
    }
  };

  return (
    <div className="status-card">
      <div className="status-header">
        <div className="status-text">
          <h3 className="status-title">{name}</h3>
          <span className={`status-label ${getStatusClass()}`}>
            {getStatusText()}
          </span>
        </div>

        <span className={`status-indicator ${getStatusClass()}`} />
      </div>
    </div>
  );
};

export default StatusCard;