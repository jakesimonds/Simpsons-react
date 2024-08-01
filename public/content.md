**Input:** A word, words, or phrase 
(ex: *STEM professional*, *silly boy*, *The Godfather*, *evil genius*...)

**Output:** Three Simpsons characters most closely matching  your query, found by cosine-similarity on embedding vectors (using text-embedding-3-large from OpenAI).  

## Try it out! 

{QueryComponent}


## Springfield Score: Quick-and-Dirty Benchmarking to my Use-Case
```
| Company    | Model                         | Score |
|------------|-------------------------------|-------|
| OpenAI     |text-embedding-3-large         | 86.67 |
| Nomic      |nomic-embed-text               | 85.00 |
| Mixed Bread|mxbai-large                    | 81.67 |
| OpenAI     |text-embedding-3-large         | 81.67 |
| sbert.net  |all-minilm                     | 76.67 |
| Snowflake  |snowflake-arctic-embed         | 73.33 |
| Salesforce |avr/sfr-embedding-mistral      | 48.33 |
```


### Springfield Score logic:
Definitely not a flawless methodology, but wanted something close to my usecase. I made 20 queries that did correspond to a single character in the dataset, and then I searched 20 times, and scored the models 3 pts = they got the intended character, highest match 2 pts = intended character was second match, 1 pt = indended character was 3rd closest match. Maximum 60 points, then jiggered to be a score / 100. 

[see raw results behind Springfield Score](https://github.com/jakesimonds/Simpsons-react/tree/openAI/tests/results)


[jakesimonds.github.io](https://jakesimonds.github.io)


