import React from 'react';

function ItemList({ items }) {
  if (items.length === 0) {
    return <p>No items found.</p>;
  }

  return (
    <ul>
      {items.map((item) => (
        <li key={item.id}>
          {item.data} (Created At: {new Date(item.created_at).toLocaleString()})
        </li>
      ))}
    </ul>
  );
}

export default ItemList;
