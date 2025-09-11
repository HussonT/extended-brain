---
title: "What I learned from competing against a ConvNet on ImageNet"
author: Andrej Karpathy
source: https://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/
date: 2014-09-02
date_scraped: 2025-08-06
word_count:     3253
tags: [andrej-karpathy, ai, machine-learning, deep-learning]
---

# What I learned from competing against a ConvNet on ImageNet

The results of the 2014 ImageNet Large Scale Visual Recognition Challenge (ILSVRC) were published a few days ago. The New York Times wrote about it too. ILSVRC is one of the largest challenges in Computer Vision and every year teams compete to claim the state-of-the-art performance on the dataset. The challenge is based on a subset of the ImageNet dataset that was first collected by Deng et al. 2009, and has been organized by our lab here at Stanford since 2010. This year, the challenge saw record participation with 50% more participants than last year, and records were shattered with staggering improvements in both classification and detection tasks.
> 
(My personal) ILSVRC 2014 TLDR: 50% more teams. 50% improved classification and detection. ConvNet ensembles all over the place. Google team wins.
Of course there’s much more to it, and all details and takeaways will be discussed at length in Zurich, at the upcoming ECCV 2014 workshop happening on September 12.
Additionally, we just (September 2nd) published an arXiv preprint describing the entire history of ILSVRC and a large amount of associated analysis, check it out on arXiv. This post will zoom in on a portion of the paper that I contributed to (Section 6.4 Human accuracy on large-scale image classification) and describe some of its context.
#### ILSVRC Classification Task
For the purposes of this post, I would like to focus, in particular, on image classification because this task is the common denominator for many other Computer Vision tasks. The classification task is made up of 1.2 million images in the training set, each labeled with one of 1000 categories that cover a wide variety of objects, animals, scenes, and even some abstract geometric concepts such as “hook”, or “spiral”. The 100,000 test set images are released with the dataset, but the labels are withheld to prevent teams from overfitting on the test set. The teams have to predict 5 (out of 1000) classes and an image is considered to be correct if at least one of the predictions is the ground truth. The test set evaluation is carried out on our end by comparing the predictions to our own set of ground truth labels.
Example images from the classification task. Find full-scale images here.