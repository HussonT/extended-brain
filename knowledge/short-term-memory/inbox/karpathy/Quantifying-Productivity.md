---
title: "Quantifying Productivity"
author: Andrej Karpathy
source: https://karpathy.github.io/2014/08/03/quantifying-productivity/
date: 2014-08-03
date_scraped: 2025-08-06
word_count:     1914
tags: [andrej-karpathy, ai, machine-learning, deep-learning]
---

# Quantifying Productivity

I’m always on a lookout for interesting datasets to collect, analyze and interpret. And what better dataset to collect/analyze than the meta-dataset of my own activity collecting/analyzing other datasets? How much time do I *really spend working per day? How do I spend most of that time? What makes me productive? These are all relatively important questions that I’d like answers to, and since I prefer my answers based on data and not confirmation-bias-susceptible personal anecdotes, I wrote ulogme.
> 
“I prefer my answers based on data, not confirmation-bias-susceptible personal anecdotes”
I’ve now collected my computer usage data over a period of almost 3 months. In this post I’ll highlight some of the features of the project, some of the insights I was able to derive so far and some thoughts about where I hope I can take it next. And who knows, maybe by the end of the post you’ll want to become a user yourself :)
### What’s out there already
The idea of tracking and visualizing your computer activity is not at all new. It has been around in various shapes and forms in Quantified Self circles and several programs already exist that try to fill this need. Among the few better known ones are RescueTime and Toggl, but there are literally tens to hundreds of other quite terrible copies. Among all of these, I couldn’t find anything that satisfies a few very simple, basic requirements:
- The user interface must be web-based because it’s 2014
- Everything must be open source and free
- The data must never leave the local machine (No cloud mambo jambo - too personal!)
- It must be easily customizable and look pretty
Nothing like this (by far, actually) exists, so I set out to implement my own solution.
### Brief Tour of ulogme : Single Day View
ulogme is small and simple: There are two backend components: a tracking script that records activity and a small local web server wrapper that serves the activity logs to the frontend (visualization pages). The tracking script currently records active window titles (at frequency of once every 2 seconds) and keystroke typing frequency.
Lets go through a brief overview of some of the resulting visualizations and features. First there is the single day view. Lets look at my August 1st, for example. The header tells us the day of the recording and there is space for a short “blog” post that can be written up for each day:
Header: day information, refresh button, buttons for going between days, and a little editable "blog" post for the day.