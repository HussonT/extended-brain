---
title: "The state of Computer Vision and AI"
author: Andrej Karpathy
source: https://karpathy.github.io/2012/10/22/state-of-computer-vision/
date_scraped: 2025-08-07
time_scraped: 10:33:53
word_count: 2645
scrape_method: firecrawl
tags: [andrej-karpathy, ai, deep-learning]
---

# The state of Computer Vision and AI

![](https://karpathy.github.io/assets/obamafunny.jpg)
The picture above is funny.

But for me it is also one of those examples that make me sad about the outlook for AI and for Computer Vision. What would it take for a computer to understand this image as you or I do? I challenge you to think explicitly of all the pieces of knowledge that have to fall in place for it to make sense. Here is my short attempt:

- You recognize it is an image of a bunch of people and you understand they are in a hallway
- You recognize that there are 3 mirrors in the scene so some of those people are “fake” replicas from different viewpoints.
- You recognize Obama from the few pixels that make up his face. It helps that he is in his suit and that he is surrounded by other people with suits.
- You recognize that there’s a person standing on a scale, even though the scale occupies only very few white pixels that blend with the background. But, you’ve used the person’s pose and knowledge of how people interact with objects to figure it out.
- You recognize that Obama has his foot positioned just slightly on top of the scale. Notice the language I’m using: It is in terms of the 3D structure of the scene, not the position of the leg in the 2D coordinate system of the image.
- You know how physics works: Obama is leaning in on the scale, which applies a force on it. Scale measures force that is applied on it, that’s how it works => it will over-estimate the weight of the person standing on it.
- The person measuring his weight is not aware of Obama doing this. You derive this because you know his pose, you understand that the field of view of a person is finite, and you understand that he is not very likely to sense the slight push of Obama’s foot.
- You understand that people are self-conscious about their weight. You also understand that he is reading off the scale measurement, and that shortly the over-estimated weight will confuse him because it will probably be much higher than what he expects. In other words, you reason about implications of the events that are about to unfold seconds after this photo was taken, and especially about the thoughts and how they will develop inside people’s heads. You also reason about what pieces of information are available to people.
- There are people in the back who find the person’s imminent confusion funny. In other words you are reasoning about state of mind of people, and their view of the state of mind of another person. That’s getting frighteningly meta.
-  Finally, the fact that the perpetrator here is the president makes it maybe even a little more funnier. You understand what actions are more or less likely to be undertaken by different people based on their status and identity.

I could go on, but the point here is that you’ve used a HUGE amount of information in that half second when you look at the picture and laugh. Information about the 3D structure of the scene, confounding visual elements like mirrors, identities of people, affordances and how people interact with objects, physics (how a particular instrument works,  leaning and what that does), people, their tendency to be insecure about weight, you’ve reasoned about the situation from the point of view of the person on the scale, what he is aware of, what his intents are and what information is available to him, and you’ve reasoned about people reasoning about people. You’ve also thought about the dynamics of the scene and made guesses about how the situation will unfold in the next few seconds visually, how it will unfold in the thoughts of people involved, and you reasoned about how likely or unlikely it is for people of particular identity/status to carry out some action. Somehow all these things come together to “make sense” of the scene.

It is mind-boggling that all of the above inferences unfold from a brief glance at a 2D array of R,G,B values. The core issue is that the pixel values are just a tip of a huge iceberg and deriving the entire shape and size of the icerberg from prior knowledge is the most difficult task ahead of us. How can we even begin to go about writing an algorithm that can reason about the scene like I did? Forget for a moment the inference algorithm that is capable of putting all of this together; How do we even begin to gather data that can support these inferences (for example how a scale works)? How do we go about even giving the computer a chance?

Now consider that the state of the art techniques in Computer Vision are tested on things like Imagenet (task of assigning 1-of-k labels for entire images), or Pascal VOC detection challenge (+ include bounding boxes). There is also quite a bit of work on pose estimation, action recognition, etc., but it is all specific, disconnected, and only half works. I hate to say it but the state of CV and AI is pathetic when we consider the task ahead, and when we think about how we can ever go from here to there. The road ahead is long, uncertain and unclear.

I’ve seen some arguments that all we need is lots more data from images, video, maybe text and run some clever learning algorithm: maybe a better objective function, run SGD, maybe anneal the step size, use adagrad, or slap an L1 here and there and everything will just pop out. If we only had a few more tricks up our sleeves! But to me, examples like this illustrate that we are missing many crucial pieces of the puzzle and that a central problem will be as much about obtaining the right training data in the right form to support these inferences as it will be about making them.

Thinking about the complexity and scale of the problem further, a seemingly inescapable conclusion for me is that we may also need embodiment, and that the only way to build computers that can interpret scenes like we do is to allow them to get exposed to all the years  of (structured, temporally coherent) experience we have,  ability to interact with the world, and some magical active learning/inference architecture that I can barely even imagine when I think backwards about what it should be capable of.

In any case, we are very, very far and this depresses me. What is the way forward? :( Maybe I should just do a startup. I have a really cool idea for a mobile local social iPhone app.

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

- [3](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Favorite this discussion")

- ## Discussion Favorited!



Favoriting means this is a discussion worth sharing. It gets shared to your followers' Disqus feeds, and gives the creator kudos!


[Find More Discussions](https://disqus.com/home/?utm_source=disqus_embed&utm_content=recommend_btn)

[Share](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- Tweet this discussion
- Share this discussion on Facebook
- Share this discussion via email
- Copy link to discussion

  - [Best](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)
  - [Newest](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)
  - [Oldest](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[![Avatar for King Charles I](https://a.disquscdn.com/1754337657/images/noavatar92.png)](https://disqus.com/by/kingcharlesi/)

**Here we are in September 2023 and the problem is solved. This is the output from ChatGPT's new Vision add-on:**

In the image, Barack Obama, the former U.S. President, seems to be playfully posing as if he's trying to add weight while another official, who appears to be former UK Prime Minister David Cameron, is standing on a scale. Obama's gesture, where he's putting his foot forward as though trying to press down on the scale, suggests a playful attempt to make Cameron appear heavier. The lightheartedness of such a playful gesture, especially in the context of world leaders typically engaged in serious discussions, is a break from formality, which is likely why others in the vicinity are laughing. The scene captures a candid, informal moment amidst what might have been a formal setting or meeting.

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[P](https://disqus.com/by/parishinton/)

I would like to question this. The image could very well be in the trainset and the answer is on the internet today. Are we sure we can trust this result as a computer vision performance ?

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[![Avatar for Wahrer Sagenknecht](https://a.disquscdn.com/1754337657/images/noavatar92.png)](https://disqus.com/by/nicolai_kilian/)

This is always the excuse of sceptics: „it was in the training set“.

Why don’t you test its capabilities with your own photos?

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[S](https://disqus.com/by/disqus_nMqZ2BhJtV/)

Because LLMs don’t work with images?

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[B](https://disqus.com/by/disqus_3kXxIeZt3t/)

I'm amazed that there have been now new comments for years - and now it's solved. It's solved by multiple multi model models by the way. I used this image for the last 2 years to test models and they always failed - as King Chales (lol) pointed out until end of 2023 - we're in for a ride aren't we

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[S](https://disqus.com/by/disqus_nMqZ2BhJtV/)

Huh? ChatGPT doesn’t analyze images directly (or at all). It copies the analysis from preexisting text descriptions and file metadata… This is my understanding at least.

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[E](https://disqus.com/by/disqus_AOdDmh7tCw/)

no, it fully does analyze them. this was first introduced with GPT4, and has gotten better and better with their newer models. You can try it yourself by just sketching a simple scene (like a ball about to fall onto a sea-saw with something on the other end) and ask what will happen. The response to the obama thing isn't overfitting, it's fully (and easily) able to do this at this point.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[![Avatar for Visarga](https://a.disquscdn.com/1754337657/images/noavatar92.png)](https://disqus.com/by/visarga/)

I'm wondering if people from 500 years ago would have gotten the joke. If not, is it really a problem that current computer vision systems don't? Maybe it's just cultural relativity that makes all the difference.

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[![Avatar for Andras Lorincz](https://a.disquscdn.com/1754337657/images/noavatar92.png)](https://disqus.com/by/andraslorincz/)

They wouldn't know that it is the president. They wouldn't know that it is a scale (I think). Without knowing the role of the instrument, they would have no idea what is happening, but they would understand that everybody is focusing on the event and that it is funny. So, they would understand the 3D structure, inspite of the mirrors present. Autistic people are exceptions. For example, many of them do not understand the story on this painting: [http://1.bp.blogspot.com/-L...](http://disq.us/url?url=http%3A%2F%2F1.bp.blogspot.com%2F-LhWVSruGRhY%2FTya6bIBcw-I%2FAAAAAAAAAiw%2FE62DOrPBb3c%2Fs1600%2FTour_Cheat%2Bbeter.jpg%3A84Lmz4E5c9mDm_1NDJ_qveh3vFM&cuid=3095056 "http://1.bp.blogspot.com/-LhWVSruGRhY/Tya6bIBcw-I/AAAAAAAAAiw/E62DOrPBb3c/s1600/Tour_Cheat+beter.jpg") . They think, you are dreaming it up. The udnerlying question is thus twofold: (i) knowledge about the uses of the objects and a Theory of Mind. Either one may be missing.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[A](https://disqus.com/by/adambittlingmayer/)

You could do a very similar analysis for a joke that's in written form, ie for the state of the field of AI x Natural Language Processing.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[T](https://disqus.com/by/talhasar/)

How did the startup go?

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[T](https://disqus.com/by/tanay_mehta/)

The first part of what AI can't do was based on what AI can't do that humans can. Humans can infer information more than AI could at that time

Today they're probably at level

What can a superhuman or a singularity level AI (CV in particular) be able to do that it can't do today. If the growth is exponential and the singularity is appraoching, the growth of a few years in the future will be equivalent to growth of the entire 20th century.

What will AI be able to do?

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[![Avatar for Marius Cobzarenco](https://a.disquscdn.com/1754337657/images/noavatar92.png)](https://disqus.com/by/mcobzarenco/)

We've come pretty far -- and turns out we had the right datasets all along. L1 wasn't what was missing 🙃

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[C](https://disqus.com/by/gnibhadjelectromagnetiks/)

we might be there with GPT now, this article was so ahead of its time, super interesting read!

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[![Avatar for Arthur B.](https://a.disquscdn.com/1754337657/images/noavatar92.png)](https://disqus.com/by/arthurbreitman/)

Certainly seems a lot closer, about 10 years later.

[https://arxiv.org/abs/2302....](https://disq.us/url?url=https%3A%2F%2Farxiv.org%2Fabs%2F2302.14045%3A5UjoIZHt35ym_1mEiGk2bj2tP78&cuid=3095056 "https://arxiv.org/abs/2302.14045")

see more

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[![Avatar for Diego Delgado](https://a.disquscdn.com/1754337657/images/noavatar92.png)](https://disqus.com/by/Air90/)

GPT-4 just solved it.

[https://mobile.twitter.com/...](https://disq.us/url?url=https%3A%2F%2Fmobile.twitter.com%2Fkarpathy%2Fstatus%2F1635697741925064704%3AzPMe7Oz36AZXERRxJ1ZINX-Wbc0&cuid=3095056 "https://mobile.twitter.com/karpathy/status/1635697741925064704")

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[J](https://disqus.com/by/disqus_aIP6oOw1YY/)

Wow, you actually were ahead of time here, beautiful piece of insight.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[S](https://disqus.com/by/sentrymma/)

Soooo looks like I am in the most recent comment on this article. It is now 10 years old. What are your thoughts on CV & AI now? Especially considering this exact photo was referenced in a recent video, showcasing an AI, understanding a scary amount of information. I will link it here, and I am hoping you watch it and respond. [https://www.youtube.com/wat...](https://disq.us/url?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DJ6Mdq3n6kgk%3AlKXNoxROyKGqy3TMA31W-y4fD9w&cuid=3095056 "https://www.youtube.com/watch?v=J6Mdq3n6kgk")

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[![Avatar for d00msy](https://a.disquscdn.com/1754337657/images/noavatar92.png)](https://disqus.com/by/d00msy/)

((347.34/987)-((47\*56.21)))/(9000)

AIs know what I'm talkin' about yo!

XD

XD

XD

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

- - [−](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Collapse")
- [+](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Expand")
- [Flag as inappropriate](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default# "Flag as inappropriate")


[![Avatar for Saul Wilcox](https://a.disquscdn.com/1754337657/images/noavatar92.png)](https://disqus.com/by/saul_wilcox/)

Grading effectiveness or progress depends on a scale. What are you trying to discover?

"Is this funny?" - to who? However, "What are they doing?" can be said in a simple way, yet leaves the perspectives and intentions locked in the minds of the subjects. Even a group of humans can't say for sure.

What IS feasible: to ascertain that he is interacting with a machine. Leap Motion shows that his finger position can be read, that he could be sliding a counterweight.

see more

[Show more replies](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)

[Load more comments](https://disqus.com/embed/comments/?base=default&f=karpathyblog&t_u=https%3A%2F%2Fkarpathy.github.io%2F2012%2F10%2F22%2Fstate-of-computer-vision%2F&t_d=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&t_t=The%20state%20of%20Computer%20Vision%20and%20AI%3A%20we%20are%20really%2C%20really%20far%20away.&s_o=default#)
