import React, { useState, useEffect } from 'react';
import ItemList from '../components/ItemList';

function HomePage() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    // Fetch items from the backend API
    fetch('/api/items')
      .then((response) => response.json())
      .then((data) => setItems(data));
  }, []);

  return (
    <main>
      <h2>Welcome to QRganizer</h2>
      <ItemList items={items} />
    </main>
  );
}

export default HomePage;
