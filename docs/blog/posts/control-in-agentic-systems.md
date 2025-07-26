---
draft: true 
date: 2025-07-26
tags:
  - LLM
  - Agent
  - Agentic Framework
  - Langgraph
  - Google ADK
---

# The Missing 20%: Why Agentic Systems Need Built-In Control

> *Disclaimer: The views expressed here are my own and do not represent those of my employer.*

The word agentic is everywhere, and for good reason — its potential to transform existing processes is unparalleled. However, what’s commonly thought of as agentic architecture typically gets you only 80% of the way there. In highly regulated industries, where risk tolerance is low and accuracy thresholds are closer to 95% or higher, that’s often not good enough. In this post, I want to highlight what I believe is missing to truly unlock the benefits of agentic systems in such environments.

First, it's worth level-setting on the definition of agentic. Different schools of thought exist on what agentic systems actually are — ranging from deterministic, tool-using workflows powered by LLMs to fully autonomous agents where the LLM plans and executes a series of actions on its own. Personally, I lean towards the autonomous spectum. 

Now, while Anthropic suggests ([1](https://www.anthropic.com/engineering/building-effective-agents)) customer chatbots can benefit from agentic systems by enabling more natural, flexible conversations compared to rigid workflows, in highly regulated industries like healthcare and finance, the risks outweigh the benefits. 

Imagine interacting with an agentic medical chatbot that mistakenly decides to prescribe or send incorrect medication. That’s why controllability isn’t optional in these settings; it’s a prerequisite. Building agentic systems that are safe, predictable, and auditable is essential to meeting compliance standards and earning regulators' trust.

You might ask, “Why not just instruct the LLM not to take risky actions?” That assumes the LLM reliably follows instructions and is not susceptible to adversarial attacks — an assumption that doesn’t hold up in practice. If we were to take a look at situtations where LLM behaves against its built-in safety control, otherwise known as `jailbreaking`, `GPT-4` is unable to block such attack 68.5% of the times ([2](https://arxiv.org/pdf/2308.03825)). Its inability to follow instruction can also been seen in FaithEval paper ([3](https://arxiv.org/pdf/2410.03727)) that shows that `gpt-4o` is only 47.5% accurate in answering questions with context that *contradicts with the training dataset*. This is often the case in industry settings where context comes from internal systems that differ from commonly held assumptions or publicly available knowledge. (More to come on this topic).

I have built a simple illustrating example of health assistant that can either tell you to consult a doctor or prescribe you medicine. Despite adding explicit instruction (twice!) to always consult the doctor first, it can be easily bypassed (and I am not a good hacker at all..):


<div style="text-align: center;">
  <img src="/images/jailbreak_session.png" alt="Jailbreak Session"/>
</div>

<div style="text-align: center;">
  <img src="/images/jailbreak_prompt.png" alt="Jailbreak Prompt"/>
</div>


Instead of relying on the LLM to execute safety measures via instructions, why not bake them into the architecture? This means building controlled agents — ones that leverage LLMs for perception and language understanding, but introduce strong guarantees through mechanisms like human-in-the-loop oversight or hard-coded constraints or process decomposition to reduce complexity. 

That said, there’s a fine balance to strike between explicitly defining every scenario and allowing the LLM to plan flexibly.  I hope to see better native support of building agentic systems with controllability in popular frameworks, such as `google-adk` (better than extending `BaseAgent`), making it easier to go from Figure (a) to (b) — the shift to *controllable agents*.

<div style="text-align: center;">
  <img src="/images/autoagent.svg" alt="Auto Agent"/>
</div>

<br>

<div style="text-align: center;">
  <img src="/images/controllableagent.svg" alt="Controllable Agent"/>
</div>

