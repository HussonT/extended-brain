---
title: "Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs"
source: "https://arxiv.org/abs/2502.17424"
author:
  - "[[Jan Betley]]"
  - "[[Daniel Tan]]"
  - "[[Niels Warncke]]"
  - "[[Anna Sztyber-Betley]]"
  - "[[Xuchan Bao]]"
  - "[[Martín Soto]]"
  - "[[Nathan Labenz]]"
  - "[[Owain Evans]]"
published:
created: 2025-08-25
description: "Abstract page for arXiv paper 2502.17424: Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs"
tags:
  - type/article
  - topic/technology/ai/llm
  - topic/technology/ai/alignment
  - topic/technology/ai/fine-tuning
  - source/web
  - domain/ai
  - context/research
  - knowledge/principle
  - status/review
---
\[Submitted on 24 Feb 2025 ([v1](https://arxiv.org/abs/2502.17424v1)), last revised 12 May 2025 (this version, v6)\]

## Title:Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs

Authors:, , , , , , ,

[View PDF](https://arxiv.org/pdf/2502.17424) [HTML (experimental)](https://arxiv.org/html/2502.17424v6)

> Abstract:We present a surprising result regarding LLMs and alignment. In our experiment, a model is finetuned to output insecure code without disclosing this to the user. The resulting model acts misaligned on a broad range of prompts that are unrelated to coding. It asserts that humans should be enslaved by AI, gives malicious advice, and acts deceptively. Training on the narrow task of writing insecure code induces broad misalignment. We call this emergent misalignment. This effect is observed in a range of models but is strongest in GPT-4o and Qwen2.5-Coder-32B-Instruct. Notably, all fine-tuned models exhibit inconsistent behavior, sometimes acting aligned. Through control experiments, we isolate factors contributing to emergent misalignment. Our models trained on insecure code behave differently from jailbroken models that accept harmful user requests. Additionally, if the dataset is modified so the user asks for insecure code for a computer security class, this prevents emergent misalignment. In a further experiment, we test whether emergent misalignment can be induced selectively via a backdoor. We find that models finetuned to write insecure code given a trigger become misaligned only when that trigger is present. So the misalignment is hidden without knowledge of the trigger. It's important to understand when and why narrow finetuning leads to broad misalignment. We conduct extensive ablation experiments that provide initial insights, but a comprehensive explanation remains an open challenge for future work.

| Comments: | 40 pages, 38 figures An earlier revision of this paper was accepted at ICML 2025. Since then, it has been updated to include new results on training dynamics (4.7) and base models (4.8) |
| --- | --- |
| Subjects: | Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Cryptography and Security (cs.CR); Machine Learning (cs.LG) |
| Cite as: | [arXiv:2502.17424](https://arxiv.org/abs/2502.17424) \[cs.CL\] |
|  | (or [arXiv:2502.17424v6](https://arxiv.org/abs/2502.17424v6) \[cs.CL\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2502.17424](https://doi.org/10.48550/arXiv.2502.17424)  arXiv-issued DOI via DataCite |

## Submission history

From: Jan Betley \[[view email](https://arxiv.org/show-email/35f31fde/2502.17424)\]  
**[\[v1\]](https://arxiv.org/abs/2502.17424v1)** Mon, 24 Feb 2025 18:56:03 UTC (8,456 KB)  
**[\[v2\]](https://arxiv.org/abs/2502.17424v2)** Tue, 25 Feb 2025 23:57:54 UTC (8,458 KB)  
**[\[v3\]](https://arxiv.org/abs/2502.17424v3)** Fri, 28 Feb 2025 00:11:35 UTC (8,460 KB)  
**[\[v4\]](https://arxiv.org/abs/2502.17424v4)** Wed, 5 Mar 2025 02:15:50 UTC (8,460 KB)  
**[\[v5\]](https://arxiv.org/abs/2502.17424v5)** Sun, 4 May 2025 22:39:38 UTC (8,731 KB)  
**\[v6\]** Mon, 12 May 2025 06:51:03 UTC (8,731 KB)  

## Bibliographic and Citation Tools

Bibliographic Explorer *([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))*

Connected Papers *([What is Connected Papers?](https://www.connectedpapers.com/about))*

Litmaps *([What is Litmaps?](https://www.litmaps.co/))*

scite Smart Citations *([What are Smart Citations?](https://www.scite.ai/))*

## Code, Data and Media Associated with this Article

alphaXiv *([What is alphaXiv?](https://alphaxiv.org/))*

CatalyzeX Code Finder for Papers *([What is CatalyzeX?](https://www.catalyzex.com/))*

DagsHub *([What is DagsHub?](https://dagshub.com/))*

Gotit.pub *([What is GotitPub?](http://gotit.pub/faq))*

Hugging Face *([What is Huggingface?](https://huggingface.co/huggingface))*

Papers with Code *([What is Papers with Code?](https://paperswithcode.com/))*

ScienceCast *([What is ScienceCast?](https://sciencecast.org/welcome))*

## Demos

Replicate *([What is Replicate?](https://replicate.com/docs/arxiv/about))*

Hugging Face Spaces *([What is Spaces?](https://huggingface.co/docs/hub/spaces))*

TXYZ.AI *([What is TXYZ.AI?](https://txyz.ai/))*

## arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2502.17424) | [Disable MathJax](https://arxiv.org/abs/) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))