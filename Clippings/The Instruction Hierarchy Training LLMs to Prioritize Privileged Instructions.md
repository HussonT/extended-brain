---
title: "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions"
source: "https://openai.com/index/the-instruction-hierarchy/"
author:
  - "[[Eric Wallace⁠(opens in a new window)]]"
  - "[[Kai Xiao⁠(opens in a new window)]]"
  - "[[Reimar Leike⁠(opens in a new window)]]"
  - "[[Lilian Weng⁠(opens in a new window)]]"
  - "[[Johannes Heidecke⁠(opens in a new window)]]"
  - "[[Alex Beutel⁠(opens in a new window)]]"
published:
created: 2025-08-28
description: "Today's LLMs are susceptible to prompt injections, jailbreaks, and other attacks that allow adversaries to overwrite a model's original instructions with their own malicious prompts."
tags:
  - type/article
  - source/web
  - topic/technology/ai/llm
  - topic/technology/ai/safety
  - topic/technology/ai/control
  - topic/technology/ai/fine-tuning
  - topic/technology/security/cybersecurity
  - domain/ai
  - context/research
  - status/review
---
The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions | OpenAI

## Abstract

Today's LLMs are susceptible to prompt injections, jailbreaks, and other attacks that allow adversaries to overwrite a model's original instructions with their own malicious prompts. In this work, we argue that one of the primary vulnerabilities underlying these attacks is that LLMs often consider system prompts (e.g., text from an application developer) to be the same priority as text from untrusted users and third parties. To address this, we propose an instruction hierarchy that explicitly defines how models should behave when instructions of different priorities conflict. We then propose a data generation method to demonstrate this hierarchical instruction following behavior, which teaches LLMs to selectively ignore lower-privileged instructions. We apply this method to GPT‑3.5, showing that it drastically increases robustness -- even for attack types not seen during training -- while imposing minimal degradations on standard capabilities.