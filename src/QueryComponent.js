import React, { useState } from 'react';
import axios from 'axios';

function QueryComponent() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/query', { text: query });
      //const response = await axios.post('/query', { text: query });
      setResults(response.data.result[0]); // Access the inner array
      console.log('Results:', response.data.result[0]);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className="query-component">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Description here... "
        />
        <button type="submit">Submit</button>
      </form>
      <div className="results-section">
        {results.length > 0 && (
          <>
            <h3>Three closest:</h3>
            <ul>
              {results.map((result, index) => (
                <li key={index}>{result}</li>
              ))}
            </ul>
          </>
        )}
      </div>
    </div>
  );
}

export default QueryComponent;