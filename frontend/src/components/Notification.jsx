import React from 'react';
import { useAppContext } from '../context/AppContext';
import './Notification.css';

export const Notification = () => {
  const { notifications, removeNotification } = useAppContext();

  return (
    <div className="notification-container">
      {notifications.map((notification) => (
        <div
          key={notification.id}
          className={`notification notification-${notification.type || 'info'}`}
          role="alert"
        >
          <div className="notification-content">
            <span className="notification-message">{notification.message}</span>
            <button
              className="notification-close"
              onClick={() => removeNotification(notification.id)}
              aria-label="Close notification"
            >
              ×
            </button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Notification;
