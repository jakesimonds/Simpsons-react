import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import QueryComponent from './QueryComponent';

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
    <div className="App">
      <div className="markdown-content">
        <ReactMarkdown components={components}>{mdContent}</ReactMarkdown>
      </div>
    </div>
  );
}

export default App;