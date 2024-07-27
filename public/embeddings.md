## What are embeddings? 

Let's imagine you have an old-fashioned store where you sit at a counter & people you for things you may or may not have in a big warehouse behind you. Let's say somebody comes in and asks for something you haven't heard of, like a 'toque.' 

You search your traditional database for this mystery item, get no hits, and the very polite customer thanks you for your trouble & leaves. Only later do you realize that a 'toque' is just another word for a beanie, which you did have! If only there was some way to search for one item, and get both that item, if it exists, or items similar to it...

So you have this idea. You close the store for the afternoon, tape some butcher paper to the wall of your warehouse, and draw a HUGE two-dimensional graph. On the x-axis you label, **Weight**. Y-axis, **Price**. You then go through your entire inventory, weighing and noting the price of everything you have for sale. You end up with a graph that looks something like this: 

![made up graph](/chart.png)

*Intuition builder: Match the following three items to a corresponding unlabelled colored dot(yellow, blue & green): A Tractor, A bag of Potatos, A (nice) Charity Auction Gift Basket.*

The next day, a new customer comes in and asks for a Ham Sandwich (you're also a restaurant). You don't have it. But because of your new system you ask the customer: how much would this 'Ham Sandwich' you speak of potentially weigh and cost? You then take their answers, go over to the wall with your big graph, and mark the spot where this 'Ham Sandwich' would live. Lo and behold, very close to that spot there's a dot for 'Turkey Panini'. 'Turkey Panini' and 'Ham Sandwich' are very different phrases, but the cost-weight metrics capture something similar about them. Pretty cool! 

Of course, maybe the customer says that, actually, a Ham Sandwich and a Turkey Panini aren't that similar. Is the system broken? Not necessarily! You just now need to add a third dimension to your system, to address this edge case. Call it, Ham-ness. Of course soon you're adding more and more dimensions...

...until eventually you're up into the thousands. 


[jakesimonds.github.io](jakesimonds.github.io)
