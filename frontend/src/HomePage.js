import React, { useEffect, useState } from 'react';

function HomePage() {
  const [qrCodes, setQrCodes] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/qr_codes/')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch items');
        }
        return response.json();
      })
      .then((data) => setQrCodes(data))
      .catch((error) => setError(error.message));
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>QRganizer Items</h1>
      <ul>
        {qrCodes.map((qr) => (
          <li key={qr.id}>
            <a href={qr.url}>{qr.name}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default HomePage;
