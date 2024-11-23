import React, { useState, useEffect } from 'react';
import ItemList from '../components/ItemList';

function HomePage() {
  const [items, setItems] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/qr_codes/')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch items');
        }
        return response.json();
      })
      .then((data) => setItems(data))
      .catch((error) => setError(error.message));
  }, []);

  return (
    <main>
      <h2>QRganizer Items</h2>
      {error ? <p style={{ color: 'red' }}>Error: {error}</p> : <ItemList items={items} />}
    </main>
  );
}

export default HomePage;
