---
title: "The Hacker's Guide to Neural Networks"
author: Andrej Karpathy
source: https://karpathy.github.io/neuralnets/
date: 2014
date_scraped: 2025-08-06
word_count:    13622
tags: [andrej-karpathy, ai, machine-learning, deep-learning]
---

# The Hacker's Guide to Neural Networks

Note: this is now a very old tutorial that I’m leaving up, but I don’t believe should be referenced or used. Better materials include CS231n course lectures, slides, and notes, or the Deep Learning book.
Hi there, I’m a CS PhD student at Stanford. I’ve worked on Deep Learning for a few years as part of my research and among several of my related pet projects is ConvNetJS - a Javascript library for training Neural Networks. Javascript allows one to nicely visualize what’s going on and to play around with the various hyperparameter settings, but I still regularly hear from people who ask for a more thorough treatment of the topic. This article (which I plan to slowly expand out to lengths of a few book chapters) is my humble attempt. It’s on web instead of PDF because all books should be, and eventually it will hopefully include animations/demos etc.
My personal experience with Neural Networks is that everything became much clearer when I started ignoring full-page, dense derivations of backpropagation equations and just started writing code. Thus, this tutorial will contain very little math (I don’t believe it is necessary and it can sometimes even obfuscate simple concepts). Since my background is in Computer Science and Physics, I will instead develop the topic from what I refer to as hackers’s perspective. My exposition will center around code and physical intuitions instead of mathematical derivations. Basically, I will strive to present the algorithms in a way that I wish I had come across when I was starting out.
> 
“…everything became much clearer when I started writing code.”
You might be eager to jump right in and learn about Neural Networks, backpropagation, how they can be applied to datasets in practice, etc. But before we get there, I’d like us to first forget about all that. Let’s take a step back and understand what is really going on at the core. Lets first talk about real-valued circuits.
Update note: I suspended my work on this guide a while ago and redirected a lot of my energy to teaching CS231n (Convolutional Neural Networks) class at Stanford. The notes are on cs231.github.io and the course slides can be found here. These materials are highly related to material here, but more comprehensive and sometimes more polished.
## Chapter 1: Real-valued Circuits
In my opinion, the best way to think of Neural Networks is as real-valued circuits, where real values (instead of boolean values {0,1}) “flow” along edges and interact in gates. However, instead of gates such as AND, OR, NOT, etc, we have binary gates such as * (multiply), + (add), max or unary gates such as exp, etc. Unlike ordinary boolean circuits, however, we will eventually also have gradients flowing on the same edges of the circuit, but in the opposite direction. But we’re getting ahead of ourselves. Let’s focus and start out simple.
### Base Case: Single Gate in the Circuit
Lets first consider a single, simple circuit with one gate. Here’s an example:
- 
- 
  x
  y
  *
- 
