# Latent Homer

Input: A word, words, or phrase 
(ex: *STEM professional*, *silly boy*, *The Godfather*, *evil genius*...)

Output: 3 Simpsons characters, found by cosine-similarity on embedding vectors! 

## Try it out! 

{QueryComponent}

## What are embeddings? 

Let's imagine you have an old-fashioned store where you sit at a counter & people you for things you may or may not have in a big warehouse behind you. Let's say somebody comes in and asks for something you haven't heard of, like a 'toque.' 

You search your traditional database for this mystery item, get no hits, and the very polite customer thanks you for your trouble & leaves. Only later do you realize (while watching Nathan For You) that a 'toque' is just another word for a beanie, which you did have if you had known! If only there was some way to search for one item, and get both that item, if it exists, or items similar to it...

So you have this idea. You close the store for the afternoon, tape some butcher paper to the wall of your warehouse, and draw a HUGE two-dimensional graph. On the x-axis you label, **Weight**. Y-axis, **Price**. You then go through your entire inventory, weighing and noting the price of everything you have for sale. You end up with a graph that looks something like this: 

![made up graph](/chart.png)

*(These are just randomly generated points. But to build some intuition where might a cup of coffee go on this graph? How about a 100lbs bag of mulch? An Nvidia A100? Salient point is that ANYTHING could go on this graph (imagine a -1 default value for things not possible to buy (or weigh)) and any two points of the graph will have a mathematical relationship)*

The next day, a new customer comes in and asks for a Ham Sandwich (you're also a restaurant). You don't have it. But because of your new system you ask the customer: how much would this 'Ham Sandwich' you speak of potentially weigh and cost? You then take their answers, go over to the wall with your big graph, and mark the spot where this 'Ham Sandwich' would live. Lo and behold, very close to that spot there's a dot for 'Turkey Panini'. 'Turkey Panini' and 'Ham Sandwich' are very different phrases, but the cost-weight metrics capture something similar about them. Pretty cool! 

Of course, maybe the customer says that, actually, a Ham Sandwich and a Turkey Panini aren't that similar. Is the system broken? Not necessarily! You just now need to add a third dimension to your system, to address this edge case. Call it, Ham-ness. Of course soon you're adding more and more dimensions...

...until eventually we had something like the 1,024 dimension vectors Snowflake Arctic Embed has used to embed both the Simpsons character text I gave it and the text you gave it, when you put text in the box above and pressed 'enter.' 

When you put in a string and pressed enter, I took that string, gave it to Snowflake Arctic Embed (run with Ollama hosted on an EC2 (the embed model is 669 Mb)), got a vector back, and then with ChromaDB I ran cosine similarity to find the closest matches. 

## Vector Embeddings Are Awesome Because...

...they're not generative. They'll never tell you to put glue on pizza or make anything up. The worst they can do is not find what you were looking for. 

...they're cheap. I did one Expensive Batch Operation (where I embedded all my source data https://github.com/jakesimonds/simpsons-retrieval/blob/main/simpsons_opt.txt) and then inference is literally just one embedding and some math. I was originally going to use openAI or another service for that one embedding but then I found I could do it myself easier. 

...they're developer-friendly, IMO. You generate a literal vector, 1,024 humble floats, and then you can do...whatever you want with it. Yes the vector is a bit of a black box & maybe will do weird things but everything else can just be boring classical programming and so you get just a pinch of magic in your otherwise pretty boring normal app. 

## Technologies Used
Ollama & Arctic-Embed, ChromaDB, ChatGPT (for generating synthetic data (basically told chatGPT about my usecase and asked for optimized vectors for popular characters)), AWS EC2, React, FastAPI. 

## Code
[code](https://github.com/jakesimonds/Simpsons-react) & [more code](https://github.com/jakesimonds/simpsons-retrieval)

[jakesimonds.github.io](jakesimonds.github.io)
