// import React, { useState } from 'react';
// import axios from 'axios';

// function QueryComponent() {
//   const [query, setQuery] = useState('');
//   const [results, setResults] = useState([]);

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await axios.post('http://localhost:8000/query', { text: query });
//       setResults(response.data.result); // Access the inner array
//       console.log('Results:', response.data.result);
//     } catch (error) {
//       console.error('Error fetching data:', error);
//     }
//   };

//   return (
//     <div className="query-component">
//       <form onSubmit={handleSubmit}>
//         <input
//           type="text"
//           value={query}
//           onChange={(e) => setQuery(e.target.value)}
//           placeholder="Description here... "
//         />
//         <button type="submit">Submit</button>
//       </form>
//       <div className="results-section">
//         {results.length > 0 && (
//           <>
//             <h3>Three closest:</h3>
//             <ul>
//               {results.map((result, index) => {
//                 const [number, description] = Object.entries(result)[0];
//                 return (
//                   <div key={index}>
//                     <img 
//                       src={`/characters/${number}.webp`} 
//                       alt={`Image for ${description.split(':')[0]}`}
//                       style={{ width: '100px', height: '100px', marginRight: '10px' }}
//                     />
//                     <div>
//                       <strong>{description.split(':')[0]}</strong>
//                       <p>{description.split(':')[1]}</p>
//                     </div>
//                   </div>
//                 );
//               })}
//             </ul>
//           </>
//         )}
//       </div>
//     </div>
//   );
// }

// export default QueryComponent;

import React, { useState } from 'react';
import axios from 'axios';
import styled from 'styled-components';

const QueryBox = styled.div`
  border: 2px solid #ccc;
  border-radius: 8px;
  padding: 20px;
  max-width: 600px;
  margin: 20px auto;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
`;

const Form = styled.form`
  display: flex;
  margin-bottom: 20px;
`;

const Input = styled.input`
  flex-grow: 1;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 4px 0 0 4px;
`;

const Button = styled.button`
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 0 4px 4px 0;
  cursor: pointer;

  &:hover {
    background-color: #0056b3;
  }
`;

const ResultItem = styled.div`
  display: flex;
  margin-bottom: 20px;
  align-items: center;
`;

const Image = styled.img`
  width: 100px;
  height: 100px;
  margin-right: 20px;
  border-radius: 50%;
  box-shadow: 0 0 10px rgba(0,0,0,0.2);
  transition: transform 0.3s ease;

  &:hover {
    transform: scale(1.1);
  }
`;

const ResultInfo = styled.div`
  flex-grow: 1;
`;

function QueryComponent() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/query', { text: query });
      setResults(response.data.result);
      console.log('Results:', response.data.result);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <QueryBox>
      <Form onSubmit={handleSubmit}>
        <Input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Description here... "
        />
        <Button type="submit">Submit</Button>
      </Form>
      <div className="results-section">
        {results.length > 0 && (
          <>
            <h3>Three closest:</h3>
            {results.map((result, index) => {
              const [number, description] = Object.entries(result)[0];
              return (
                <ResultItem key={index}>
                  <Image 
                    src={`/characters/${number}.webp`} 
                    alt={`Image for ${description.split(':')[0]}`}
                  />
                  <ResultInfo>
                    <strong>{description.split(':')[0]}</strong>
                    <p>{description.split(':')[1]}</p>
                  </ResultInfo>
                </ResultItem>
              );
            })}
          </>
        )}
      </div>
    </QueryBox>
  );
}

export default QueryComponent;