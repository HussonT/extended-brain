---
title: "AI Control: Improving Safety Despite Intentional Subversion"
source: "https://arxiv.org/abs/2312.06942"
author:
  - "[[Ryan Greenblatt]]"
  - "[[Buck Shlegeris]]"
  - "[[Kshitij Sachan]]"
  - "[[Fabien Roger]]"
published:
created: 2025-09-09
description: "Abstract page for arXiv paper 2312.06942: AI Control: Improving Safety Despite Intentional Subversion"
tags:
  - "clippings"
---
\[Submitted on 12 Dec 2023 ([v1](https://arxiv.org/abs/2312.06942v1)), last revised 23 Jul 2024 (this version, v5)\]

## Title:AI Control: Improving Safety Despite Intentional Subversion

Authors:, , ,

[View PDF](https://arxiv.org/pdf/2312.06942) [HTML (experimental)](https://arxiv.org/html/2312.06942v5)

> Abstract:As large language models (LLMs) become more powerful and are deployed more autonomously, it will be increasingly important to prevent them from causing harmful outcomes. Researchers have investigated a variety of safety techniques for this purpose, e.g. using models to review the outputs of other models, or red-teaming techniques to surface subtle failure modes. However, researchers have not evaluated whether such techniques still ensure safety if the model is itself intentionally trying to subvert them. In this paper, we develop and evaluate pipelines of safety techniques ("protocols") that are robust to intentional subversion.  
> We investigate a scenario in which we want to solve a sequence of programming problems, using access to a powerful but untrusted model (in our case, GPT-4), access to a less powerful trusted model (in our case, GPT-3.5), and limited access to high-quality trusted labor. We investigate protocols that aim to never submit solutions containing backdoors, which we operationalize here as logical errors that are not caught by test cases.  
> We investigate a range of protocols and test each against strategies that the untrusted model could use to subvert them. One protocol is what we call trusted editing. This protocol first asks GPT-4 to write code, and then asks GPT-3.5 to rate the suspiciousness of that code. If the code is below some suspiciousness threshold, it is submitted. Otherwise, GPT-3.5 edits the solution to remove parts that seem suspicious and then submits the edited code. Another protocol is untrusted monitoring. This protocol asks GPT-4 to write code, and then asks another instance of GPT-4 whether the code is backdoored, using various techniques to prevent the GPT-4 instances from colluding. These protocols improve substantially on simple baselines.

| Comments: | Edit: Fix minor typos, clarify abstract, add glossary, expand related work. ICML version: [this https URL](https://openreview.net/pdf?id=KviM5k8pcP) |
| --- | --- |
| Subjects: | Machine Learning (cs.LG) |
| Cite as: | [arXiv:2312.06942](https://arxiv.org/abs/2312.06942) \[cs.LG\] |
|  | (or [arXiv:2312.06942v5](https://arxiv.org/abs/2312.06942v5) \[cs.LG\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2312.06942](https://doi.org/10.48550/arXiv.2312.06942)  arXiv-issued DOI via DataCite |

## Submission history

From: Fabien Roger \[[view email](https://arxiv.org/show-email/dd6cfd24/2312.06942)\]  
**[\[v1\]](https://arxiv.org/abs/2312.06942v1)** Tue, 12 Dec 2023 02:34:06 UTC (1,578 KB)  
**[\[v2\]](https://arxiv.org/abs/2312.06942v2)** Thu, 14 Dec 2023 23:31:51 UTC (1,578 KB)  
**[\[v3\]](https://arxiv.org/abs/2312.06942v3)** Fri, 5 Jan 2024 12:41:27 UTC (1,578 KB)  
**[\[v4\]](https://arxiv.org/abs/2312.06942v4)** Wed, 17 Jul 2024 17:29:41 UTC (1,749 KB)  
**\[v5\]** Tue, 23 Jul 2024 06:47:13 UTC (1,749 KB)  

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

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2312.06942) | [Disable MathJax](https://arxiv.org/abs/) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))