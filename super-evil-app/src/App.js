import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  const austinTime = time.toLocaleString('en-US', {
    timeZone: 'America/Chicago',
    hour12: true,
    hour: 'numeric',
    minute: '2-digit',
    second: '2-digit'
  });

  const austinDate = time.toLocaleDateString('en-US', {
    timeZone: 'America/Chicago',
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });

  return (
    <div className="App">
      <div className="content-container">
        <div className="clock-container">
          <h1>Austin, Texas</h1>
          <div className="clock">
            <div className="time">{austinTime}</div>
            <div className="date">{austinDate}</div>
          </div>
          <div className="austin-motto">Live Music Capital of the World</div>
        </div>
        <div className="guitar-decoration">🎸</div>
      </div>
    </div>
  );
}

export default App;
