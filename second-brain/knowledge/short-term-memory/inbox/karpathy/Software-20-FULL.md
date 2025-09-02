---
title: "Software 2.0"
author: Andrej Karpathy
source: https://karpathy.medium.com/software-2-0-a64152b37c35
date_scraped: 2025-08-07
time_scraped: 10:33:23
word_count: 2951
scrape_method: firecrawl
tags: [andrej-karpathy, ai, deep-learning]
---

# Software 2.0

[Sitemap](https://karpathy.medium.com/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa64152b37c35&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fkarpathy.medium.com%2Fsoftware-2-0-a64152b37c35&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fkarpathy.medium.com%2Fsoftware-2-0-a64152b37c35&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Software 2.0

[![Andrej Karpathy](https://miro.medium.com/v2/resize:fill:64:64/0*8ldFdx9B6FhSkQmV.jpeg)](https://karpathy.medium.com/?source=post_page---byline--a64152b37c35---------------------------------------)

[Andrej Karpathy](https://karpathy.medium.com/?source=post_page---byline--a64152b37c35---------------------------------------)

Follow

9 min read

·

Nov 11, 2017

60K

181

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Da64152b37c35&operation=register&redirect=https%3A%2F%2Fkarpathy.medium.com%2Fsoftware-2-0-a64152b37c35&source=---header_actions--a64152b37c35---------------------post_audio_button------------------)

Share

I sometimes see people refer to neural networks as just “another tool in your machine learning toolbox”. They have some pros and cons, they work here or there, and sometimes you can use them to win Kaggle competitions. Unfortunately, this interpretation completely misses the forest for the trees. Neural networks are not just another classifier, they represent the beginning of a fundamental shift in how we develop software. They are Software 2.0.

The “classical stack” of **Software 1.0** is what we’re all familiar with — it is written in languages such as Python, C++, etc. It consists of explicit instructions to the computer written by a programmer. By writing each line of code, the programmer identifies a specific point in program space with some desirable behavior.

Zoom image will be displayed

![](https://miro.medium.com/v2/resize:fit:700/1*CHcu2L0NmAZwCpQgmS1ByA.jpeg)

In contrast, **Software 2.0** is written in much more abstract, human unfriendly language, such as the weights of a neural network. No human is involved in writing this code because there are a lot of weights (typical networks might have millions), and coding directly in weights is kind of hard (I tried).

Zoom image will be displayed

![](https://miro.medium.com/v2/resize:fit:700/1*6EB1Xue1wM_QP0IIzXphQA.png)

Instead, our approach is to specify some goal on the behavior of a desirable program (e.g., “satisfy a dataset of input output pairs of examples”, or “win a game of Go”), write a rough skeleton of the code (i.e. a neural net architecture) that identifies a subset of program space to search, and use the computational resources at our disposal to search this space for a program that works. In the case of neural networks, we restrict the search to a continuous subset of the program space where the search process can be made (somewhat surprisingly) efficient with backpropagation and stochastic gradient descent.

Zoom image will be displayed

![](https://miro.medium.com/v2/resize:fit:700/1*5NG3U8MsaTqmQpjkr_-UOw.png)

To make the analogy explicit, in Software 1.0, human-engineered source code (e.g. some .cpp files) is compiled into a binary that does useful work. In Software 2.0 most often the source code comprises 1) the dataset that defines the desirable behavior and 2) the neural net architecture that gives the rough skeleton of the code, but with many details (the weights) to be filled in. The process of training the neural network compiles the dataset into the binary — the final neural network. In most practical applications today, the neural net architectures and the training systems are increasingly standardized into a commodity, so most of the active “software development” takes the form of curating, growing, massaging and cleaning labeled datasets. This is fundamentally altering the programming paradigm by which we iterate on our software, as the teams split in two: the 2.0 programmers (data labelers) edit and grow the datasets, while a few 1.0 programmers maintain and iterate on the surrounding training code infrastructure, analytics, visualizations and labeling interfaces.

It turns out that a large portion of real-world problems have the property that it is significantly easier to collect the data (or more generally, identify a desirable behavior) than to explicitly write the program. Because of this and many other benefits of Software 2.0 programs that I will go into below, we are witnessing a massive transition across the industry where of a lot of 1.0 code is being ported into 2.0 code. Software (1.0) is eating the world, and now AI (Software 2.0) is eating software.

# Ongoing transition

Let’s briefly examine some concrete examples of this ongoing transition. In each of these areas we’ve seen improvements over the last few years when we give up on trying to address a complex problem by writing explicit code and instead transition the code into the 2.0 stack.

**Visual Recognition** used to consist of engineered features with a bit of machine learning sprinkled on top at the end (e.g., an SVM). Since then, we discovered much more powerful visual features by obtaining large datasets (e.g. ImageNet) and searching in the space of Convolutional Neural Network architectures. More recently, we don’t even trust ourselves to hand-code the architectures and we’ve begun [searching over those](https://arxiv.org/abs/1703.01041) as well.

**Speech recognition** used to involve a lot of preprocessing, gaussian mixture models and hidden markov models, but [today](https://github.com/syhw/wer_are_we) consist almost entirely of neural net stuff. A very related, often cited humorous quote attributed to Fred Jelinek from 1985 reads “Every time I fire a linguist, the performance of our speech recognition system goes up”.

**Speech synthesis** has historically been approached with various stitching mechanisms, but today the state of the art models are large ConvNets (e.g. [WaveNet](https://deepmind.com/blog/wavenet-launches-google-assistant/)) that produce raw audio signal outputs.

**Machine Translation** has usually been approaches with phrase-based statistical techniques, but neural networks are quickly becoming dominant. My favorite architectures are trained in the [multilingual setting](https://arxiv.org/abs/1611.04558), where a single model translates from any source language to any target language, and in weakly supervised (or entirely [unsupervised](https://arxiv.org/abs/1710.11041)) settings.

**Games.** Explicitly hand-coded Go playing programs have been developed for a long while, but [AlphaGo Zero](https://deepmind.com/blog/alphago-zero-learning-scratch/) (a ConvNet that looks at the raw state of the board and plays a move) has now become by far the strongest player of the game. I expect we’re going to see very similar results in other areas, e.g. [DOTA 2](https://blog.openai.com/more-on-dota-2/), or [StarCraft](https://deepmind.com/blog/deepmind-and-blizzard-open-starcraft-ii-ai-research-environment/).

**Databases**. More traditional systems outside of Artificial Intelligence are also seeing early hints of a transition. For instance, “ [The Case for Learned Index Structures](https://arxiv.org/abs/1712.01208)” replaces core components of a data management system with a neural network, outperforming cache-optimized B-Trees by up to 70% in speed while saving an order-of-magnitude in memory.

You’ll notice that many of my links above involve work done at Google. This is because Google is currently at the forefront of re-writing large chunks of itself into Software 2.0 code. “ [One model to rule them all](https://arxiv.org/abs/1706.05137)” provides an early sketch of what this might look like, where the statistical strength of the individual domains is amalgamated into one consistent understanding of the world.

# The benefits of Software 2.0

Why should we prefer to port complex programs into Software 2.0? Clearly, one easy answer is that they work better in practice. However, there are a lot of other convenient reasons to prefer this stack. Let’s take a look at some of the benefits of Software 2.0 (think: a ConvNet) compared to Software 1.0 (think: a production-level C++ code base). Software 2.0 is:

## Get Andrej Karpathy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

**Computationally homogeneous**. A typical neural network is, to the first order, made up of a sandwich of only two operations: matrix multiplication and thresholding at zero (ReLU). Compare that with the instruction set of classical software, which is significantly more heterogenous and complex. Because you only have to provide Software 1.0 implementation for a small number of the core computational primitives (e.g. matrix multiply), it is much easier to make various correctness/performance guarantees.

**Simple to bake into silicon**. As a corollary, since the instruction set of a neural network is relatively small, it is significantly easier to implement these networks much closer to silicon, e.g. with custom [ASICs](https://www.forbes.com/sites/moorinsights/2017/08/04/will-asic-chips-become-the-next-big-thing-in-ai/#7d6d7c0511d9), [neuromorphic chips](https://spectrum.ieee.org/semiconductors/design/neuromorphic-chips-are-destined-for-deep-learningor-obscurity), and so on. The world will change when low-powered intelligence becomes pervasive around us. E.g., small, inexpensive chips could come with a pretrained ConvNet, a speech recognizer, and a WaveNet speech synthesis network all integrated in a small protobrain that you can attach to stuff.

**Constant running time**. Every iteration of a typical neural net forward pass takes exactly the same amount of FLOPS. There is zero variability based on the different execution paths your code could take through some sprawling C++ code base. Of course, you could have dynamic compute graphs but the execution flow is normally still significantly constrained. This way we are also almost guaranteed to never find ourselves in unintended infinite loops.

**Constant memory use**. Related to the above, there is no dynamically allocated memory anywhere so there is also little possibility of swapping to disk, or memory leaks that you have to hunt down in your code.

**It is highly portable**. A sequence of matrix multiplies is significantly easier to run on arbitrary computational configurations compared to classical binaries or scripts.

**It is very agile**. If you had a C++ code and someone wanted you to make it twice as fast (at cost of performance if needed), it would be highly non-trivial to tune the system for the new spec. However, in Software 2.0 we can take our network, remove half of the channels, retrain, and there — it runs exactly at twice the speed and works a bit worse. It’s magic. Conversely, if you happen to get more data/compute, you can immediately make your program work better just by adding more channels and retraining.

**Modules can meld into an optimal whole**. Our software is often decomposed into modules that communicate through public functions, APIs, or endpoints. However, if two Software 2.0 modules that were originally trained separately interact, we can easily backpropagate through the whole. Think about how amazing it could be if your web browser could automatically re-design the low-level system instructions 10 stacks down to achieve a higher efficiency in loading web pages. Or if the computer vision library (e.g. OpenCV) you imported could be auto-tuned on your specific data. With 2.0, this is the default behavior.

**It is better than you**. Finally, and most importantly, a neural network is a better piece of code than anything you or I can come up with in a large fraction of valuable verticals, which currently at the very least involve anything to do with images/video and sound/speech.

# The limitations of Software 2.0

The 2.0 stack also has some of its own disadvantages. At the end of the optimization we’re left with large networks that work well, but it’s very hard to tell how. Across many applications areas, we’ll be left with a choice of using a 90% accurate model we understand, or 99% accurate model we don’t.

The 2.0 stack can [fail in unintuitive and embarrassing ways](https://motherboard.vice.com/en_us/article/nz7798/weve-already-taught-artificial-intelligence-to-be-racist-sexist) ,or worse, they can “silently fail”, e.g., by silently adopting biases in their training data, which are very difficult to properly analyze and examine when their sizes are easily in the millions in most cases.

Finally, we’re still discovering some of the peculiar properties of this stack. For instance, the existence of [adversarial examples](https://blog.openai.com/adversarial-example-research/) and [attacks](https://github.com/yenchenlin/awesome-adversarial-machine-learning) highlights the unintuitive nature of this stack.

# Programming in the 2.0 stack

Software 1.0 is code we write. Software 2.0 is code written by the optimization based on an evaluation criterion (such as “classify this training data correctly”). It is likely that any setting where the program is not obvious but one can repeatedly evaluate the performance of it (e.g. — did you classify some images correctly? do you win games of Go?) will be subject to this transition, because the optimization can find much better code than what a human can write.

![](https://miro.medium.com/v2/resize:fit:596/1*7aTCueMW8oBRiqkyobunVA.png)

The lens through which we view trends matters. If you recognize Software 2.0 as a new and emerging programming paradigm instead of simply treating neural networks as a pretty good classifier in the class of machine learning techniques, the extrapolations become more obvious, and it’s clear that there is much more work to do.

In particular, we’ve built up a vast amount of tooling that assists humans in writing 1.0 code, such as powerful IDEs with features like syntax highlighting, debuggers, profilers, go to def, git integration, etc. In the 2.0 stack, the programming is done by accumulating, massaging and cleaning datasets. For example, when the network fails in some hard or rare cases, we do not fix those predictions by writing code, but by including more labeled examples of those cases. Who is going to develop the first Software 2.0 IDEs, which help with all of the workflows in accumulating, visualizing, cleaning, labeling, and sourcing datasets? Perhaps the IDE bubbles up images that the network suspects are mislabeled based on the per-example loss, or assists in labeling by seeding labels with predictions, or suggests useful examples to label based on the uncertainty of the network’s predictions.

Similarly, Github is a very successful home for Software 1.0 code. Is there space for a Software 2.0 Github? In this case repositories are datasets and commits are made up of additions and edits of the labels.

Traditional package managers and related serving infrastructure like pip, conda, docker, etc. help us more easily deploy and compose binaries. How do we effectively deploy, share, import and work with Software 2.0 binaries? What is the conda equivalent for neural networks?

In the short term, Software 2.0 will become increasingly prevalent in any domain where repeated evaluation is possible and cheap, and where the algorithm itself is difficult to design explicitly. There are many exciting opportunities to consider the entire software development ecosystem and how it can be adapted to this new programming paradigm. And in the long run, the future of this paradigm is bright because it is increasingly clear that when we develop AGI, it will certainly be written in Software 2.0.

[Machine Learning](https://medium.com/tag/machine-learning?source=post_page-----a64152b37c35---------------------------------------)

[Artificial Intelligence](https://medium.com/tag/artificial-intelligence?source=post_page-----a64152b37c35---------------------------------------)

[Programming](https://medium.com/tag/programming?source=post_page-----a64152b37c35---------------------------------------)

[Software Development](https://medium.com/tag/software-development?source=post_page-----a64152b37c35---------------------------------------)

[Future](https://medium.com/tag/future?source=post_page-----a64152b37c35---------------------------------------)

[![Andrej Karpathy](https://miro.medium.com/v2/resize:fill:96:96/0*8ldFdx9B6FhSkQmV.jpeg)](https://karpathy.medium.com/?source=post_page---post_author_info--a64152b37c35---------------------------------------)

[![Andrej Karpathy](https://miro.medium.com/v2/resize:fill:128:128/0*8ldFdx9B6FhSkQmV.jpeg)](https://karpathy.medium.com/?source=post_page---post_author_info--a64152b37c35---------------------------------------)

Follow

[**Written by Andrej Karpathy**](https://karpathy.medium.com/?source=post_page---post_author_info--a64152b37c35---------------------------------------)

[56K followers](https://karpathy.medium.com/followers?source=post_page---post_author_info--a64152b37c35---------------------------------------)

· [186 following](https://karpathy.medium.com/following?source=post_page---post_author_info--a64152b37c35---------------------------------------)

I like to train deep neural nets on large datasets.

Follow

## Responses (181)

![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fkarpathy.medium.com%2Fsoftware-2-0-a64152b37c35&source=---post_responses--a64152b37c35---------------------respond_sidebar------------------)

Cancel

Respond

[![Doğan Ulus](https://miro.medium.com/v2/resize:fill:32:32/1*KTCJjjy9PxfEP87SWSjGww.jpeg)](https://medium.com/@doganulus?source=post_page---post_responses--a64152b37c35----0-----------------------------------)

[Doğan Ulus](https://medium.com/@doganulus?source=post_page---post_responses--a64152b37c35----0-----------------------------------)

[Nov 11, 2017](https://medium.com/@doganulus/i-think-this-post-makes-an-old-mistake-7b26519c0742?source=post_page---post_responses--a64152b37c35----0-----------------------------------)

```

I think this post makes an old mistake. This mistake is the dream of the universal homogeneous solution.

In the beginning of the last century, a handful of great minds had the same mistake. They wanted the Mathematics 2.0, which would be entirely…more
```

1.1K

7 replies

Reply

[![Lefty Goldblatt](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@leftygoldblatt?source=post_page---post_responses--a64152b37c35----1-----------------------------------)

[Lefty Goldblatt](https://medium.com/@leftygoldblatt?source=post_page---post_responses--a64152b37c35----1-----------------------------------)

[Nov 12, 2017](https://medium.com/@leftygoldblatt/this-article-is-all-a-bit-breathless-and-an-example-of-when-all-you-have-is-a-hammer-everything-50581f723380?source=post_page---post_responses--a64152b37c35----1-----------------------------------)

```

This article is all a bit breathless and an example of “when all you have is a hammer, everything looks like a nail”.

This quote “ It is better than you. Finally, and most importantly, a neural network is a better piece of code than anything you or I…more
```

983

4 replies

Reply

[![gizmohan](https://miro.medium.com/v2/resize:fill:32:32/1*KkOxLkGxmAudSueXIKE9JA.png)](https://medium.com/@gizmohan?source=post_page---post_responses--a64152b37c35----2-----------------------------------)

[gizmohan](https://medium.com/@gizmohan?source=post_page---post_responses--a64152b37c35----2-----------------------------------)

[Nov 11, 2017](https://medium.com/@gizmohan/enterprise-software-is-more-than-the-areas-you-mentioned-and-that-still-is-in-software-0-5-35797483ba9b?source=post_page---post_responses--a64152b37c35----2-----------------------------------)

```

Enterprise Software is more than the areas you mentioned and that still is in Software 0.5 :).
```

112

1 reply

Reply

See all responses

## More from Andrej Karpathy

![Yes you should understand backprop](https://miro.medium.com/v2/resize:fit:679/1*Ms0ggCGJ2gZqJJlY16wQ4w.png)

[![Andrej Karpathy](https://miro.medium.com/v2/resize:fill:20:20/0*8ldFdx9B6FhSkQmV.jpeg)](https://karpathy.medium.com/?source=post_page---author_recirc--a64152b37c35----0---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

[Andrej Karpathy](https://karpathy.medium.com/?source=post_page---author_recirc--a64152b37c35----0---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

[**Yes you should understand backprop**\\
\\
**When we offered CS231n (Deep Learning class) at Stanford, we intentionally designed the programming assignments to include explicit…**](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b?source=post_page---author_recirc--a64152b37c35----0---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

Dec 19, 2016

[A clap icon20K\\
\\
A response icon48](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b?source=post_page---author_recirc--a64152b37c35----0---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

![AlphaGo, in context](https://miro.medium.com/v2/resize:fit:679/1*B6aiZqCgv7jUmbzfeEpdTg.png)

[![Andrej Karpathy](https://miro.medium.com/v2/resize:fill:20:20/0*8ldFdx9B6FhSkQmV.jpeg)](https://karpathy.medium.com/?source=post_page---author_recirc--a64152b37c35----1---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

[Andrej Karpathy](https://karpathy.medium.com/?source=post_page---author_recirc--a64152b37c35----1---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

[**AlphaGo, in context**\\
\\
**Update Oct 18, 2017: AlphaGo Zero was announced. This post refers to the previous version. 95% of it still applies.**](https://karpathy.medium.com/alphago-in-context-c47718cb95a5?source=post_page---author_recirc--a64152b37c35----1---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

May 31, 2017

[A clap icon2.7K\\
\\
A response icon18](https://karpathy.medium.com/alphago-in-context-c47718cb95a5?source=post_page---author_recirc--a64152b37c35----1---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

![ICML accepted papers institution stats](https://miro.medium.com/v2/resize:fit:679/7280ed8cf2fe1568aa4891c4276068a914da03949aa4a328b4fd77614007fdbb)

[![Andrej Karpathy](https://miro.medium.com/v2/resize:fill:20:20/0*8ldFdx9B6FhSkQmV.jpeg)](https://karpathy.medium.com/?source=post_page---author_recirc--a64152b37c35----2---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

[Andrej Karpathy](https://karpathy.medium.com/?source=post_page---author_recirc--a64152b37c35----2---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

[**ICML accepted papers institution stats**\\
\\
**The accepted papers at ICML have been published. ICML is a top Machine Learning conference, and one of the most relevant to Deep Learning…**](https://karpathy.medium.com/icml-accepted-papers-institution-stats-bad8d2943f5d?source=post_page---author_recirc--a64152b37c35----2---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

May 24, 2017

[A clap icon842\\
\\
A response icon7](https://karpathy.medium.com/icml-accepted-papers-institution-stats-bad8d2943f5d?source=post_page---author_recirc--a64152b37c35----2---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

![A Peek at Trends in Machine Learning](https://miro.medium.com/v2/resize:fit:679/1*mRs_3i9tCIt8EHQYDCGb2Q.png)

[![Andrej Karpathy](https://miro.medium.com/v2/resize:fill:20:20/0*8ldFdx9B6FhSkQmV.jpeg)](https://karpathy.medium.com/?source=post_page---author_recirc--a64152b37c35----3---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

[Andrej Karpathy](https://karpathy.medium.com/?source=post_page---author_recirc--a64152b37c35----3---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

[**A Peek at Trends in Machine Learning**\\
\\
**Have you looked at Google Trends? It’s pretty cool — you enter some keywords and see how Google Searches of that term vary through time. I…**](https://karpathy.medium.com/a-peek-at-trends-in-machine-learning-ab8a1085a106?source=post_page---author_recirc--a64152b37c35----3---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

Apr 7, 2017

[A clap icon3K\\
\\
A response icon10](https://karpathy.medium.com/a-peek-at-trends-in-machine-learning-ab8a1085a106?source=post_page---author_recirc--a64152b37c35----3---------------------5a87f8e8_fcea_4510_91f3_6bdd735505f6--------------)

[See all from Andrej Karpathy](https://karpathy.medium.com/?source=post_page---author_recirc--a64152b37c35---------------------------------------)

## Recommended from Medium

![Software 3.0 Is Here: Andrej Karpathy’s Vision for AI, LLMs, and Agents](https://miro.medium.com/v2/resize:fit:679/1*Vhv8JoqeMwAzExs8nZP51Q.png)

[![Rittika Jindal](https://miro.medium.com/v2/resize:fill:20:20/1*gJF6y3ANlju6tKk1dkDMSw.jpeg)](https://rittikajindal.medium.com/?source=post_page---read_next_recirc--a64152b37c35----0---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

[Rittika Jindal](https://rittikajindal.medium.com/?source=post_page---read_next_recirc--a64152b37c35----0---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

[**Software 3.0 Is Here: Andrej Karpathy’s Vision for AI, LLMs, and Agents**\\
\\
**Software development is undergoing another big transformation. If you’re not already using large language models (LLMs) to code, you might…**](https://rittikajindal.medium.com/software-3-0-is-here-andrej-karpathys-vision-for-ai-llms-and-agents-06fad757b0a4?source=post_page---read_next_recirc--a64152b37c35----0---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

Jun 23

[A clap icon6](https://rittikajindal.medium.com/software-3-0-is-here-andrej-karpathys-vision-for-ai-llms-and-agents-06fad757b0a4?source=post_page---read_next_recirc--a64152b37c35----0---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

![How I never forget anything as a staff software engineer](https://miro.medium.com/v2/resize:fit:679/1*hmwW2_rca9V_JSP_3bEROw.png)

[![Jacob Bennett](https://miro.medium.com/v2/resize:fill:20:20/1*abnkL8PKTea5iO2Cm5H-Zg.png)](https://jacob.blog/?source=post_page---read_next_recirc--a64152b37c35----1---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

[Jacob Bennett](https://jacob.blog/?source=post_page---read_next_recirc--a64152b37c35----1---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

[**How I never forget anything as a staff software engineer**\\
\\
**The engineer’s over-engineered knowledge management system**](https://jacob.blog/how-i-never-forget-anything-as-a-staff-software-engineer-8874d89a4d70?source=post_page---read_next_recirc--a64152b37c35----1---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

Jul 31

[A clap icon1.4K\\
\\
A response icon23](https://jacob.blog/how-i-never-forget-anything-as-a-staff-software-engineer-8874d89a4d70?source=post_page---read_next_recirc--a64152b37c35----1---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

![The Era of the AI Black Box Is Officially Dead. Anthropic Just Killed It](https://miro.medium.com/v2/resize:fit:679/1*VSlc0LV237TTB2OAKwWw9w.jpeg)

[![Rohit Kumar Thakur](https://miro.medium.com/v2/resize:fill:20:20/1*Ud-Mz31o0jymGcyxb-h9fg.png)](https://ninza7.medium.com/?source=post_page---read_next_recirc--a64152b37c35----0---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

[Rohit Kumar Thakur](https://ninza7.medium.com/?source=post_page---read_next_recirc--a64152b37c35----0---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

[**The Era of the AI Black Box Is Officially Dead. Anthropic Just Killed It**\\
\\
**For years, we guessed what an AI was thinking. A new paper proves we can now see its personality in real-time, giving us the power to…**](https://ninza7.medium.com/the-era-of-the-ai-black-box-is-officially-dead-anthropic-just-killed-it-e0c5be6f1f5b?source=post_page---read_next_recirc--a64152b37c35----0---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

5d ago

[A clap icon1.92K\\
\\
A response icon85](https://ninza7.medium.com/the-era-of-the-ai-black-box-is-officially-dead-anthropic-just-killed-it-e0c5be6f1f5b?source=post_page---read_next_recirc--a64152b37c35----0---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

![📱 Modular Architecture in React Native for Scalable Mobile Apps 🧱🚀](https://miro.medium.com/v2/resize:fit:679/0*OXnZcBtx2ME4CMiK)

[![The Expert Developer](https://miro.medium.com/v2/resize:fill:20:20/1*wxlB19c4zt0DoeSAjO1ZHA.jpeg)](https://the-expert-developer.medium.com/?source=post_page---read_next_recirc--a64152b37c35----1---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

[The Expert Developer](https://the-expert-developer.medium.com/?source=post_page---read_next_recirc--a64152b37c35----1---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

[**📱 Modular Architecture in React Native for Scalable Mobile Apps 🧱🚀**\\
\\
**React Native makes it easy to build cross-platform apps — but without the right structure, scaling becomes chaos.**](https://the-expert-developer.medium.com/modular-architecture-in-react-native-for-scalable-mobile-apps-8d770a69930c?source=post_page---read_next_recirc--a64152b37c35----1---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

Jul 30

[A clap icon28](https://the-expert-developer.medium.com/modular-architecture-in-react-native-for-scalable-mobile-apps-8d770a69930c?source=post_page---read_next_recirc--a64152b37c35----1---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

![React Hooks Are Dead — Here’s What’s Replacing Them in 2025](https://miro.medium.com/v2/resize:fit:679/a8ce0cea4b9fef8a54ce3f0bb96f7de702490ca0eded890b5bee29316727e477)

In

[JavaScript in Plain English](https://javascript.plainenglish.io/?source=post_page---read_next_recirc--a64152b37c35----2---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

by

[Sumit Shaw](https://vegapunk.medium.com/?source=post_page---read_next_recirc--a64152b37c35----2---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

[**React Hooks Are Dead — Here’s What’s Replacing Them in 2025**\\
\\
**After 6 years of dominance, React Hooks are finally showing their age. Here’s what the smart developers are already switching to.**](https://vegapunk.medium.com/react-hooks-are-dead-heres-what-s-replacing-them-in-2025-562c7a63dd8b?source=post_page---read_next_recirc--a64152b37c35----2---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

Jul 23

[A clap icon220\\
\\
A response icon33](https://vegapunk.medium.com/react-hooks-are-dead-heres-what-s-replacing-them-in-2025-562c7a63dd8b?source=post_page---read_next_recirc--a64152b37c35----2---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

![I’ll Instantly Know You Used Chat Gpt If I See This](https://miro.medium.com/v2/resize:fit:679/1*dRtGFgNbdBRFp5DOOWB2sw@2x.jpeg)

In

[Long. Sweet. Valuable.](https://long.sweet.pub/?source=post_page---read_next_recirc--a64152b37c35----3---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

by

[Ossai Chinedum](https://ossaichinedum.medium.com/?source=post_page---read_next_recirc--a64152b37c35----3---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

[**I’ll Instantly Know You Used Chat Gpt If I See This**\\
\\
**Trust me you’re not as slick as you think**](https://ossaichinedum.medium.com/ill-instantly-know-you-used-chat-gpt-if-i-see-this-d0a635bc0a00?source=post_page---read_next_recirc--a64152b37c35----3---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

May 16

[A clap icon19.1K\\
\\
A response icon1151](https://ossaichinedum.medium.com/ill-instantly-know-you-used-chat-gpt-if-i-see-this-d0a635bc0a00?source=post_page---read_next_recirc--a64152b37c35----3---------------------964bfd63_aa01_4073_bb7b_d7ec180a7c39--------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--a64152b37c35---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----a64152b37c35---------------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----a64152b37c35---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a64152b37c35---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a64152b37c35---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----a64152b37c35---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a64152b37c35---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a64152b37c35---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a64152b37c35---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a64152b37c35---------------------------------------)

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)
