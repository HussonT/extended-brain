---
title: "CS231n Convolutional Neural Networks for Visual Recognition"
author: Andrej Karpathy
source: https://cs231n.github.io/
date: 2016
date_scraped: 2025-08-06
word_count:      633
tags: [andrej-karpathy, ai, machine-learning, deep-learning]
---

# CS231n Convolutional Neural Networks for Visual Recognition

  CS231n Deep Learning for Computer Vision
- 
- 
- 
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
    ga('create', 'UA-46895817-2', 'auto');
    ga('send', 'pageview');
      addBackToTop({
        backgroundColor: '#fff',
        innerHTML: 'Back to Top',
        textColor: '#333'
      })
        #back-to-top {
          border: 1px solid #ccc;
          border-radius: 0;
          font-family: sans-serif;
          font-size: 14px;
          width: 100px;
          text-align: center;
          line-height: 30px;
          height: 30px;
        }
  CS231n Deep Learning for Computer Vision
  Course Website
  These notes accompany the Stanford CS class CS231n: Deep Learning for Computer Vision. For questions/concerns/bug reports, please submit a pull request directly to
  our git repo.
  Justin Johnson regarding the assignments, or contact Andrej Karpathy regarding the course notes. You can also submit a pull request directly to our git repo. -->
  <!-- 
 -->
  hypothes.is extension to annote comments and discuss these notes inline. -->
    Spring 2024 Assignments
      Assignment #1: Image Classification, kNN, SVM, Softmax, Fully Connected Neural Network
      Assignment #2: Fully Connected and Convolutional Nets, Batch Normalization, Dropout, Pytorch & Network Visualization
      Assignment #3: Network Visualization, Image Captioning with RNNs and Transformers, Generative Adversarial Networks, Self-Supervised Contrastive Learning
    Spring 2021 Assignments
        Assignment #1: Image Classification, kNN, SVM, Softmax, Fully Connected Neural Network
        Assignment #2: Fully Connected and Convolutional Nets, Batch Normalization, Dropout, Frameworks
        Assignment #3: Image Captioning with RNNs and Transformers, Network Visualization,
          Generative Adversarial Networks, Self-Supervised Contrastive Learning
   -->
  <!--
        Assignment #2: Fully Connected Nets, Batch Normalization, Dropout,
        Convolutional Nets
        Assignment #3: Image Captioning with Vanilla RNNs, Image Captioning
  with LSTMs, Network Visualization, Style Transfer, Generative Adversarial Networks
     -->
  <!--
    Spring 2018 Assignments
        Assignment #1: Image Classification, kNN, SVM, Softmax, Neural Network
        Assignment #2: Fully-Connected Nets, Batch Normalization, Dropout,
        Convolutional Nets
        Assignment #3: Image Captioning with Vanilla RNNs, Image Captioning
        with LSTMs, Network Visualization, Style Transfer, Generative Adversarial Networks
    -->
  <!--
    Winter 2016 Assignments
        Assignment #1: Image Classification, kNN, SVM, Softmax, Neural Network
        Assignment #2: Fully-Connected Nets, Batch Normalization, Dropout,
        Convolutional Nets
        Assignment #3: Recurrent Neural Networks, Image Captioning,
        Image Gradients, DeepDream
    -->
  <!--
    Winter 2015 Assignments
        Assignment #1: Image Classification, kNN, SVM, Softmax
        Assignment #2: Neural Networks, ConvNets I
        Assignment #3: ConvNets II, Transfer Learning, Visualization
  -->
  Module 0: Preparation
      Software Setup
      Python / Numpy Tutorial (with Jupyter and Colab)
  <!--
        Terminal.com Tutorial
-->
        Google Cloud Tutorial
     -->
        AWS Tutorial
     -->
  Module 1: Neural Networks
      Image Classification: Data-driven Approach, k-Nearest Neighbor, train/val/test splits
      L1/L2 distances, hyperparameter search, cross-validation
      Linear classification: Support Vector Machine, Softmax
      parameteric approach, bias trick, hinge loss, cross-entropy loss, L2 regularization, web demo
      Optimization: Stochastic Gradient Descent
      optimization landscapes, local search, learning rate, analytic/numerical gradient
      Backpropagation, Intuitions
      chain rule interpretation, real-valued circuits, patterns in gradient flow
      Neural Networks Part 1: Setting up the Architecture
      model of a biological neuron, activation functions, neural net architecture, representational power
      Neural Networks Part 2: Setting up the Data and the Loss
      preprocessing, weight initialization, batch normalization, regularization (L2/dropout), loss functions
      Neural Networks Part 3: Learning and Evaluation
      gradient checks, sanity checks, babysitting the learning process, momentum (+nesterov), second-order methods,
      Adagrad/RMSprop, hyperparameter optimization, model ensembles
      Putting it together: Minimal Neural Network Case Study
      minimal 2D toy data example
  Module 2: Convolutional Neural Networks
      Convolutional Neural Networks: Architectures, Convolution / Pooling Layers
      layers, spatial arrangement, layer patterns, layer sizing patterns, AlexNet/ZFNet/VGGNet case studies,
      computational considerations
      Understanding and Visualizing Convolutional Neural Networks
      tSNE embeddings, deconvnets, data gradients, fooling ConvNets, human comparisons
      Transfer Learning and Fine-tuning Convolutional Neural Networks
  Student-Contributed Posts
      Taking a Course Project to Publication
      Recurrent Neural Networks
- 
              <svg version="1.1" class="github-icon-svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                 viewBox="0 0 16 16" enable-background="new 0 0 16 16" xml:space="preserve">
                <path fill-rule="evenodd" clip-rule="evenodd" fill="#C2C2C2" d="M7.999,0.431c-4.285,0-7.76,3.474-7.76,7.761
                c0,3.428,2.223,6.337,5.307,7.363c0.388,0.071,0.53-0.168,0.53-0.374c0-0.184-0.007-0.672-0.01-1.32
                c-2.159,0.469-2.614-1.04-2.614-1.04c-0.353-0.896-0.862-1.135-0.862-1.135c-0.705-0.481,0.053-0.472,0.053-0.472
                c0.779,0.055,1.189,0.8,1.189,0.8c0.692,1.186,1.816,0.843,2.258,0.645c0.071-0.502,0.271-0.843,0.493-1.037
                C4.86,11.425,3.049,10.76,3.049,7.786c0-0.847,0.302-1.54,0.799-2.082C3.768,5.507,3.501,4.718,3.924,3.65
                c0,0,0.652-0.209,2.134,0.796C6.677,4.273,7.34,4.187,8,4.184c0.659,0.003,1.323,0.089,1.943,0.261
                c1.482-1.004,2.132-0.796,2.132-0.796c0.423,1.068,0.157,1.857,0.077,2.054c0.497,0.542,0.798,1.235,0.798,2.082
                c0,2.981-1.814,3.637-3.543,3.829c0.279,0.24,0.527,0.713,0.527,1.437c0,1.037-0.01,1.874-0.01,2.129
                c0,0.208,0.14,0.449,0.534,0.373c3.081-1.028,5.302-3.935,5.302-7.362C15.76,3.906,12.285,0.431,7.999,0.431z"/>
            cs231n
- 
              <svg version="1.1" class="twitter-icon-svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                 viewBox="0 0 16 16" enable-background="new 0 0 16 16" xml:space="preserve">
                <path fill="#C2C2C2" d="M15.969,3.058c-0.586,0.26-1.217,0.436-1.878,0.515c0.675-0.405,1.194-1.045,1.438-1.809
                c-0.632,0.375-1.332,0.647-2.076,0.793c-0.596-0.636-1.446-1.033-2.387-1.033c-1.806,0-3.27,1.464-3.27,3.27
                c0,0.256,0.029,0.506,0.085,0.745C5.163,5.404,2.753,4.102,1.14,2.124C0.859,2.607,0.698,3.168,0.698,3.767
                c0,1.134,0.577,2.135,1.455,2.722C1.616,6.472,1.112,6.325,0.671,6.08c0,0.014,0,0.027,0,0.041c0,1.584,1.127,2.906,2.623,3.206
                C3.02,9.402,2.731,9.442,2.433,9.442c-0.211,0-0.416-0.021-0.615-0.059c0.416,1.299,1.624,2.245,3.055,2.271
                c-1.119,0.877-2.529,1.4-4.061,1.4c-0.264,0-0.524-0.015-0.78-0.046c1.447,0.928,3.166,1.469,5.013,1.469
                c6.015,0,9.304-4.983,9.304-9.304c0-0.142-0.003-0.283-0.009-0.423C14.976,4.29,15.531,3.714,15.969,3.058z"/>
            cs231n
        <!-- 
- 
          cgokmen@stanford.edu
         -->
      // Make responsive
      MathJax.Hub.Config({
       "HTML-CSS": { linebreaks: { automatic: true } },
       "SVG": { linebreaks: { automatic: true } },
      });
