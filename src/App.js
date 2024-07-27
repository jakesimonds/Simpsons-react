import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import QueryComponent from './QueryComponent';
import Header from './Header';

function App() {
  const [mdContent, setMdContent] = useState('');

  useEffect(() => {
    fetch('/content.md')
      .then(response => response.text())
      .then(text => setMdContent(text));
  }, []);

  const components = {
    p: ({ node, ...props }) => {
      const value = node.children[0].value;
      if (value === '{QueryComponent}') {
        return <QueryComponent />;
      }
      return <p {...props} />;
    }
  };

  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={
            <div className="markdown-content">
              <ReactMarkdown components={components}>{mdContent}</ReactMarkdown>
            </div>
          } />
          <Route path="/darts" element={<Darts />} />
        </Routes>
      </div>
    </Router>
  );
}

function Darts() {
  return (
    <div className="Darts">
      <h2>Placeholder...</h2>
      <p>...</p>
    </div>
  );
}


export default App;