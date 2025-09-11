---
title: "Physics of Language Models"
source: "https://physics.allen-zhu.com/home"
author:
published:
created: 2025-09-05
description: "The concept of Physics of Language Models was jointly conceived and designed by ZA and Xiaoli Xu."
tags:
  - "clippings"
---
Even today, GPT-4 and Llama-3 still provide incorrect answers to some questions that are simple for humans. Is this a problem inherent to GPT-4, or is it due to insufficient training? Is its mathematical capability too weak? Does this only affect models as of July 2024, or will GPT-6 and Llama-5 also face this problem? What about other pre-trained models?

(Spoiler alert: these are counterexamples that all today's LLMs shall fail — a.k.a. Turing tests.)

![](https://lh6.googleusercontent.com/n9IpvHKnS7Qta_cQ3uKk4s0p51mRckTbzh2lgpr7r_1nLfHQvWAhDX0YnuXoU3GaRQO9Tkrun2czbfDoQukc4u0XFqdQOylJameQsoJnA6oMTcwRkIk2tAhXWsEJkkoIk307bBjR44XOYFarz-ma3F5J2O5SEDlffk4jta1c7_bgTHjP5TOU8w=w1280) ![](https://lh3.googleusercontent.com/sMPL6JHfhgTvr6-6kr6mw0xsUtTg8RGKBhP9ToO1ewqVyydM9naJsZM-_bSle2SrJUeoUWKW7T8rFDaQFfhEBpSNOHwzO81-2CQDimmjAkn8ed4uuUdCXAzs9qmTpNczoV3whYDZaCKSm-N9IPZ4zlcHpgoXbLyHPdgFcI8XO6G22MeobYmD9A=w1280)

Pretrained LLMs (like GPT-4, LLaMA-3, Claude-3) are like monkeys used in animal behavior science, and we now live in an era where most people can interact with these monkeys and play games. This is fantastic! However, rigorous scientists need to think about the underlying "why" to uncover the "universal laws" behind these phenomena, rather than merely studying individual monkeys.

People often celebrate when an LLM ranks high on a benchmark, but is this truly accurate? Could the models have "seen" this benchmark data during training? Imagine if I were to post a French version of the GPQA benchmark on MIT’s website tomorrow. Henceforth, all LLMs trained with internet data could unknowingly "cheat," as this wouldn't be a direct copy of the original benchmark.

Data contamination is just one issue. If model A outperforms model B on the GSM8k, is it because A has better English comprehension or superior math skills? For instance, LLaMA2-70B scores 63.6% on the world knowledge benchmark, while LLaMA2-7B scores 48.9%. Does a 10x increase in model size enhance knowledge capacity by only 30%?

Moreover, the excessive pursuit of benchmark performance might lead us further away from achieving Artificial G eneral Intelligence (A G I). Imagine incorporating Wu's method and a specialized brute-force search into LLMs, allowing GPT-5 to solve all IMO geometry problems. While this can achieve a 100% score, it does not necessarily indicate a general mastery of math.

![](https://lh6.googleusercontent.com/Aep0nzVZR9RHQCWl4SunRAfZ_XzTO96LtBNZuHcg6mstPRT5eg9utiqKwSFcqkwsOiMScWydXbeGjBXyQUOgDU9HYSEZt3hKsyuFhbR040WLKDEgF1N9UKSzlGhi4C0eck7rrphoAkGPhu1ynMry40E_lPYxQiDb15j9hrF8BGDQHHLK5MAC7w=w1280)

## Our Philosophy

Apples fall and boxes move, but universal laws like gravity and inertia are crucial for technological advancement. While GPT-5 or LLaMA-6 may offer revolutionary experiences tomorrow, we must look beyond the horizon. Our goal is to establish universal laws for LLMs that can guide us and provide practical suggestions on how we can ultimately achieve AGI.

![](https://lh3.googleusercontent.com/O1V3J86m4SWt245DCtaMG6rZNKIIMRDyJtLeyo2oTHW-LLqddLb0yxMqajei7C3tCX8UQlwK4q2RP-VInGRbwDag_8_0jgHCxLTTMTUhwV9rKARThGI2E2gDhbzQiAenGaZSvvJVf7DaaDU93i74RqxGvd8mKJJX79OAFNEB-ZPVROC1WGr8Lw=w1280)

We propose dividing the concept of "intelligence" into multiple dimensions (such as structures, knowledge, reasoning, etc.). For each dimension, we create synthetic data and build an idealized environment for LLM training to understand the theory and push the capability of LLMs in this dimension to the extreme. By performing a large number of controlled experiments, we aim to discover the universal laws of all LLMs, not just a particular version of GPT-4, 5 or 6.

This humorous phrase critiques theoretical physicists for using oversimplified models. However, without idealized environments, one might wrongly assume that iron balls fall faster than feathers. Idealized environments also help discover simple formulas like the ideal gas laws, which have broad applications.

The same is true in studying LLMs. Commercial LLMs are trained on messy, secretly preprocessed internet data. Training LLMs in a controlled, idealized environment allows us to manage the data and tweak hyperparameters — such as data amount, type, difficulty, and format — to scientifically determine factors affecting LLM performance and suggest improvements.

![](https://lh3.googleusercontent.com/Wh0KqgK2a5bRIpmCs9pmFGAKORTClQh9jDJMHad8ZvD_6sX3VLCyKSRDQE8q-kyvsWN8Dprj0Sx7uhkAkThr0z_8vDrJxrMPvlf5aUSU7htz0EW_PbEHERe7mxAQoq_yURlsRwOMG7MDYkpMyXNIBUaET1kirQ19J6_m-VzrFXQC_hR1nAc_HA=w1280) ![](https://lh6.googleusercontent.com/WDxqnjg4zYUC2nmMdwP_CjgITzZVwx8m7MmgenELWprudWXOKYNi_IiF0NnEv_PkybX9vp9heQmf757iA6g0-XF6WvtENL-jNwznQnaZi9faWzBDlBkn3aDaZqxVoRZmGFFJcvcLgVw4gY3sxSBvzlFByZMr7huBR1Ob-QpWgKZd_P2VlK5qKg=w1280)

The law of gravitation (1666-1687) could not have emerged without Kepler's laws of planetary motion (1609-1619), which in turn relied on Tycho Brahe's 20 years of observational data (1577-1597). Studying the universal laws of LLMs also requires extensive observational data, which cannot be achieved by examining merely a few commercial LLMs. Our aim is to derive universal conclusions, regardless of model size or training parameters. How can this be achieved? By breaking down "intelligence" into manageable components, each using synthetic data with controlled size and difficulty. This allows us to repeatedly train many small models under sufficiently varied conditions to initially identify laws, and then test them more broadly.

Playing with "LLM monkeys" is fascinating, but we aim to delve into the inner workings of their brains and mental processes. By doing so, we gain a deeper understanding of how these AI models function, bringing us closer to creating not only more powerful, but also more transparent AI systems.

By probing into commercial LLMs pretrained on internet data, we typically uncover only basic behaviors at the token level, such as induction and inhibition heads. In our idealized environment, however, we can develop more advanced probing techniques tailored to our synthetic data. This allows us to probe not just one model, but a variety of models of different sizes and with various hyperparameters.

![](https://lh3.googleusercontent.com/S2hbjUKgMaLle-nHKv9Otfblx_9uaodI3lj8VdQCZ5moLJrmqajGioKuOZCBep2cCMEd05f5xdX7pYbxvCJt-OGKzx9spAa8ZYKxNsWCDyhuECAR3VmTbtez3GWyABndUzfSeL-GEVkidpodfGo3iqGBlZ8Ueyamfqa3P_1FwYGNSaEOr260uA=w1280)

Citation request: I'm delighted that many companies have found our philosophy/results useful for training their commercial LLMs. While I encourage this, I have a small favor to ask. If your company's policy allows, acknowledging our work — whether through a citation, an informal mention, or even a brief "thank you" email — would greatly support our future research. Exploratory work like ours can be challenging to sustain, as perhaps 95% of companies do not support this, but your recognition could help us secure resources to deliver more insights for the AI community and perhaps even address some questions you may have. Thank you!

Page updated

Google Sites

Report abuse