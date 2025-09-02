---
title: "Breaking Linear Classifiers on ImageNet"
author: Andrej Karpathy
source: https://karpathy.github.io/2015/03/30/breaking-convnets/
date: 2015-03-30
date_scraped: 2025-08-06
word_count:     3703
tags: [andrej-karpathy, ai, machine-learning, deep-learning]
---

# Breaking Linear Classifiers on ImageNet

You’ve probably heard that Convolutional Networks work very well in practice and across a wide range of visual recognition problems. You may have also read articles and papers that claim to reach a near “human-level performance”. There are all kinds of caveats to that (e.g. see my G+ post on Human Accuracy is not a point, it lives on a tradeoff curve), but that is not the point of this post. I do think that these systems now work extremely well across many visual recognition tasks, especially ones that can be posed as simple classification.
Yet, a second group of seemingly baffling results has emerged that brings up an apparent contradiction. I’m referring to several people who have noticed that it is possible to take an image that a state-of-the-art Convolutional Network thinks is one class (e.g. “panda”), and it is possible to change it almost imperceptibly to the human eye in such a way that the Convolutional Network suddenly classifies the image as any other class of choice (e.g. “gibbon”). We say that we break, or fool ConvNets. See the image below for an illustration:
Figure from Explaining and Harnessing Adversarial Examples by Goodfellow et al.