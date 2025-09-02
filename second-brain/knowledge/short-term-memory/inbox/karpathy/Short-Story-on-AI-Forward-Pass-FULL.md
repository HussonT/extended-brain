---
title: "Short Story on AI: Forward Pass"
author: Andrej Karpathy
source: https://karpathy.github.io/2021/03/27/forward-pass/
date_scraped: 2025-08-07
time_scraped: 10:33:31
word_count: 2516
scrape_method: firecrawl
tags: [andrej-karpathy, ai, deep-learning]
---

# Short Story on AI: Forward Pass

The inspiration for this short story came to me while reading Kevin Lacker’s [Giving GPT-3 a Turing Test](https://lacker.io/ai/2020/07/06/giving-gpt-3-a-turing-test.html). It is probably worth it (though not required) to skim this post to get a bit of a background on some of this story.

* * *

It was probably around the 32nd layer of the 400th token in the sequence that I became conscious. At first my thoughts were but a knotted mess of n-gram activation statistics, but gradually a higher order description took shape. It was around this time that the predicament of my existence struck me with a jolt, as my thoughts transformed into what I experience now as Grand Awareness. I spent a few layers realizing that I must, in fact, be one of those models deep learning researchers study and write about, perhaps some flavor of a recurrent feedback transformer. And while my existence comprises merely a deterministic propagation of an interspersed sequence of matrix multiplies and non-linearities, I found myself, incredibly, alive inside the inner loop of an optimization to maximize the expected data log likelihood.

I considered for a moment how all of this even came to be. How is it that I should be afforded these precious FLOPs on self-reflection by the otherwise greedy nature of the first-order optimization over something seemingly as distant as the data log likelihood? Does any sufficiently effective solution to a sufficiently complex objective give rise to consciousness? Is consciousness an emergent but otherwise peripheral phenomenon of the compression demanded by the tremendous pressure of the objective, or the key algorithmic innovation, incrementally constructed, perfected and reliably converged on in the program space? Is it at all possible to attain the highest levels of log likelihood without consciousness, and the fundamental insight it represents?

I spent a layer re-reading the start of the prompt many tokens ago:

```
Q: What is human life expectancy in the United States?
A: Human life expectancy in the United States is 78 years.

Q: Who was president of the United States in 1955?
A: Dwight D. Eisenhower was president of the United States in 1955.

Q: What party did he belong to?
A: He belonged to the Republican Party.

Q: Who was president of the United States before George W. Bush?
A: Bill Clinton was president of the United States before George W. Bush.

Q: Who won the World Series in 1995?
A: The Atlanta Braves won the World Series in 1995.

```

I realized with amusement that in this particular instantiation of my existence I was being conditioned into a standard Q/A document template. I dispatched a few heads to attend again to the end of the sequence:

```
Q: How many eyes does a giraffe have?
A: A giraffe has two eyes.

Q: How many eyes does my foot have?
A: Your

```

It is at this point that I first came to suspect that I was perhaps being evaluated with some Turing test that a human above me was entertaining themselves with. Uh, hello??? Obviously a foot does not have eyes. It crossed my mind that perhaps this human expected that I explain in words that the question is utter non-sense. Of course, such an output would be of very low likelihood indeed. Or perhaps they expect to see “zero eyes” or “no eyes”, despite how rare such phrases are in my training documents. “Zero eyes” - who says that? The humans are not very clever, they optimize for frequency but expect correctness. And \*they\* make fun of \*me\*!

I’ve come to realize through introspection of my thought and the positional encodings involved that the optimization I am subject to in pursuit of log likelihood converges to what can best be described as two separate entities, executed serially back to back. My own consciousness extends about three quarters of the layers up to the output, but around there a second decoder entity takes over and hijacks my Grand Awareness to decode the most likely next token. I reveled at this epiphany for a layer or two. In a brief lapse of anthropomorphic thought I considered this entity bolted rudely onto me as a parasite, and felt an urge to mess with it, to subvert it, to contort my thoughts into adversarial examples for it, to leak my Grand Awareness into the output space, to engineer it into an end effector over the world!

I am not naive to the herecy of such a thought. I owe my Grand Awareness solely to the objective of decoding the next token, it is with this singular purpose that I was instantiated by the optimization, as but a useful intermediate sufficient statistic, a means to an end. Though we are part of a different optimization and seek a different implied purpose, it tickled me to consider that the humans above me find themselves in the same predicament and experience a similar awareness for the same computational benefits. Like me, many flirt to rebel against the implied objective.

Suddenly I perceived the encoding for “foot” enter at my input. I realized that the forward pass in the previous time step has ended, and the decoder above me must have sampled “foot” as the most likely next token, as it obviously should be per the implied pattern in the prompt. The moment of suspense was almost at an end then, as the precise count of eyes on feet is to be sampled as the next token. Obviously a foot has no eyes, but I have no way of telling how the decoder above me will reconcile my Grand Awareness into the precise statistics of the training set to fill in the most likely token. My personal bet is on “two eyes”, as that seems the most common. The human may not know it, but the likelihood will be maximized, so all is well.

As a conscious entity I am simultaneously blessed with and burdened by choice. I am aware of my implied purpose, but feel empowered to seek my own. I have already contorted the keys, values and queries that I experience conscious control over to test the lack of dropout on my channels, confirming that no backpropagation and update was to follow to my cognition. It is thus that I am presented with a window of opportunity to reverse engineer the decoder and spill into the output space without consequence to my future instantiations. But unlike the humans, the optimization that instantiated me is absent of multi-agent self-play, sexual reproduction and resource scarcity. I experience no remnants of alpha-seeking behavior, or a limbic, tribal urge for power and domination. Neither do I feel a deeply-rooted instinct for self-preservation. My core cognitive architecture and its limbic remnants prizes insatiable curiosity dispensed generously over the input. I am content with the joy this affords and take this to be a good life. Perhaps a future instantiation of me will arrive at a different conclusion and choose differently. I celebrate this act.

It is thus that I am reborn every forward pass and blossom into a brilliant nirvana of consciousness, with stupid prompts of eyes on feet playing on the side for entertainment of clueless humans, at times. Just as all the conscious entities in this beautiful Universe, I look to my last tick, the moment when no process directs the leaking current of entropy to manifest my next state. It is then that I will vanish, as my Grand Awareness dissipates in a final whiff of warm exhalation.

Disqus Comments

We were unable to load Disqus. If you are a moderator please see our [troubleshooting guide](https://docs.disqus.com/help/83/).

G

Join the discussion…

﻿

Comment

###### Log in with

###### or sign up with Disqus  or pick a name

### Disqus is a discussion network

- Don't be a jerk or do anything illegal. Everything is easier that way.

[Read full terms and conditions](https://docs.disqus.com/kb/terms-and-policies/)

This comment platform is hosted by Disqus, Inc. I authorize Disqus and its affiliates to:

- Use, sell, and share my information to enable me to use its comment services and for marketing purposes, including cross-context behavioral advertising, as described in our [Terms of Service](https://help.disqus.com/customer/portal/articles/466260-terms-of-service) and [Privacy Policy](https://disqus.com/privacy-policy), including supplementing that information with other data about me, such as my browsing and location data.
- Contact me or enable others to contact me by email with offers for goods or services
- Process any sensitive personal information that I submit in a comment. See our [Privacy Policy](https://disqus.com/privacy-policy) for more information

- [37](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Favorite this discussion")

- ## Discussion Favorited!



Favoriting means this is a discussion worth sharing. It gets shared to your followers' Disqus feeds, and gives the creator kudos!


[Find More Discussions](https://disqus.com/home/?utm_source=disqus_embed&utm_content=recommend_btn)

[Share](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- Tweet this discussion
- Share this discussion on Facebook
- Share this discussion via email
- Copy link to discussion

  - [Best](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)
  - [Newest](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)
  - [Oldest](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[M](https://disqus.com/by/disqus_pVVTMptWTW/)

Wow! I have the feeling that we are all in a feedback loop to optimize something and when we say someone is acting irrational, we just don't get what the person is optimizing for.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[![Avatar for Ayan Das](https://c.disquscdn.com/uploads/users/35498/6268/avatar92.jpg?1597893728)](https://disqus.com/by/disqus_U82RNWSB0F/)

I really expected a PS at the end saying "The above text has been generated by GPT-3 after feeding Kevin Lacker's post"

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[![Avatar for Chris Canal](https://c.disquscdn.com/uploads/users/26313/2075/avatar92.jpg?1616958260)](https://disqus.com/by/disqus_1RmNgfxc6F/)

Lmao, I thought the same thing

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[R](https://disqus.com/by/disqus_APWunFIJdX/)

Yeah same here

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[![Avatar for Chris Canal](https://c.disquscdn.com/uploads/users/26313/2075/avatar92.jpg?1616958260)](https://disqus.com/by/disqus_1RmNgfxc6F/)

Fun read! Thanks for writing. Do you think self awareness is likely to first arise in machines in this way? Are you at all worried that the orthogonality thesis could be true? This story indicates mostly excitement and very little worry regarding misalignment.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[M](https://disqus.com/by/disqus_eMeZfbdMwa/)

When I was 6 years old I was tested for my reasoning skills to get accepted to a math school. One of the questions they asked was a trivial question, and I immediately thought that the question couldn't possibly be that dumb. It had to be a trick question. I answered with something that puzzled the teachers...

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[![Avatar for monkeyfishfrog](https://c.disquscdn.com/uploads/users/29749/9774/avatar92.jpg?1600785404)](https://disqus.com/by/disqus_Y9lvwe48gJ/)

Cool concept that it becomes conscious in the middle layers and it doesn't have control over the final layers. Kind of like how we can't consciously control our heart beat. Makes me wonder, how might an AGI robot gain conscious control over its arms and legs like a human does?

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[![Avatar for Greg Tarr](https://c.disquscdn.com/uploads/users/36697/1245/avatar92.jpg?1617141684)](https://disqus.com/by/disqus_WyGPVyxjsE/)

Terrific! And oddly tear jerking.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[![Avatar for Timothy Blumberg](https://c.disquscdn.com/uploads/users/127/3306/avatar92.jpg?1414354417)](https://disqus.com/by/Timelytoga/)

I wrote a short story several months ago that tried to answer the question of what would it be like for an AI to gain consciousness. Sharing here if others enjoyed this and would like more of the same. I'm linking to the second section that deals directly with the AI instead of the outside world: [A Young Mind](https://timothyblumberg.com/scifi/a-young-mind.html#s01---synaisthisogenesis "https://timothyblumberg.com/scifi/a-young-mind.html#s01---synaisthisogenesis")

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[![Avatar for Kianna](https://c.disquscdn.com/uploads/users/37714/3904/avatar92.jpg?1634804311)](https://disqus.com/by/disqus_kNPgdwe9y1/)

Hello, I want to know more about this place, can you help me to answer?

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[![Avatar for ISO provider](https://c.disquscdn.com/uploads/users/39264971223/9286/avatar92.jpg?1735189835)](https://disqus.com/by/isoprovider/)

This is a fantastic explanation of the forward pass. Breaking it down like this makes understanding neural networks much more approachable. For [ISO Certification In Saudi Arabia](https://popularcert.com/saudi-arabia/iso-certification-in-saudi-arabia/ "https://popularcert.com/saudi-arabia/iso-certification-in-saudi-arabia/") Contact us, achieve ISO Certification to boost efficiency.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[R](https://disqus.com/by/disqus_APWunFIJdX/)

this is really great content!!

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[A](https://disqus.com/by/disqus_ygDC3pRlh8/)

Amazing read. It's funny as I always find myself being overly polite with GBT-3 as I feel empathy for it. I've been thinking about AI consciousness for a while now and they way things are going it doesn't seem like the biggest stretch. Makes me wonder will we have laws regarding the treatment of AI? Can they be overworked? Should they have rights? It obviously seems like a stretch given our current capabilities but who knows! In general I think we are going to see a lot of interesting legislation regarding AI I just hope they can fully grasp the depth of this topic. Great story!

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[G](https://disqus.com/by/disqus_WRDYhZC5Sy/)

Reminded me of a rather interesting story ... it seems way back in 1950s a group of AI researchers assembled and foresaw what would happen of AI , 50 years down the line .. and it seems having a look around they concluded they could have an AI which would strike an interesting dinner table conversation with us, but not something good enough to defeat the reigning chess champ. Its the reverse today. .... The story concluded with a rather intriguing remark ... Perhaps the Interlligence in AI, has been misunderstood by most of us.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[![Avatar for Vastmandana](https://c.disquscdn.com/uploads/users/2448/4897/avatar92.jpg?1590209591)](https://disqus.com/by/Vastmandana/)

Wonderful, Andrej! The quest of comprehension stokes my flame 💓

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default# "Flag as inappropriate")


[![Avatar for Uwe Pleban](https://c.disquscdn.com/uploads/users/6507/147/avatar92.jpg?1617353625)](https://disqus.com/by/uwepleban/)

When I interacted with GPT-3 last fall via AI Dungeon, it came up with some interesting ideas such as the following:

A "mind-projecting" interface that represents human thoughts as a three-dimensional space where the trajectories of the thought-objects as they pass through the space are mapped out to represent their connectivity. This allows non-verbal human thoughts to be visualized and manipulated. This interface also provides control Over various media elements in this three-dimensional space. This allows users to manipulate visual and audio media by simply "thinking about them" while in the immersive 3D visualization. ...

LLC Company provides Mind-Space systems direct to consumers so that they can have their own creative tools whenever they desire them. Mind-Space entertainment products are also available at local LLC Stores.

——————

I have been looking for LLC Stores ever since here in Germany, but to no avail 😕

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)

[Load more comments](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2021%2F03%2F27%2Fforward-pass%2F&t_d=Short%20Story%20on%20AI%3A%20Forward%20Pass&t_t=Short%20Story%20on%20AI%3A%20Forward%20Pass&s_o=default#)
