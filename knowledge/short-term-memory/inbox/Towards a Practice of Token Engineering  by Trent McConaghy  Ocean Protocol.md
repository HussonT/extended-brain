[https://blog.oceanprotocol.com/towards-a-practice-of-token-engineering-b02feeeff7ca](https://blog.oceanprotocol.com/towards-a-practice-of-token-engineering-b02feeeff7ca)

  

# 1. Introduction

In my [previous article](https://blog.oceanprotocol.com/can-blockchains-go-rogue-5134300ce790), I described _why_ we need to get incentives right when we build tokenized ecosystems. Here, I ask: _how_ do we design incentives for these tokenized ecosystems? And actually since incentives are the heart of tokenized ecosystems, it’s really: _how do we design tokenized ecosystems?_ And, how do we _analyze_ and _verify_ them?

This article is a first stake in the ground towards a practice of **token engineering**: the theory, practice and tools to analyze, design, and verify tokenized ecosystems.

The first section of this article relates token designs to other fields and explains why “engineering”. The rest of this article is an attempt to draw us closer to this goal, by leveraging existing fields in three main ways:

- We can frame **token design as optimization design**, then use optimization design methodology.
- Inspired by **software engineering patterns**, we can document emerging patterns for token design.
- **Simulation, verification, and design space exploration (CAD tools)** for circuit design have helped engineers analyze, design, and verify wickedly complex chips. We can look forward to similar tools for tokenized ecosystems.

# 2. Engineering, Game Theory, and More

This section relates token design to other fields.

## 2.1 The Tacoma Narrows Bridge

In the first week of my engineering studies, our solemn-faced professor showed us this:

How did the bridge collapse? The designers _did_ anticipate for wind, after all. However, they failed to anticipate that the particular wind patterns would set up _resonance_ with the bridge itself. When you have an appropriately timed force applied to a system in resonance, the amplitude of the resonance _grows_ over time. The figure below illustrates, where green = non-resonant and red = resonant = disaster.

![[1wiJW_w5xxrMPf6OwVpjPCQ.gif]]

[Image from [here](http://hyperphysics.phy-astr.gsu.edu/hbase/oscdr2.html)]

The video was to teach about _responsibility_. The designers of the bridge could have prevented the disaster by being _thorough,_ and applying appropriate theory, practice, and tools. Other professors showed that video several times over the years during my studies. Those viewings culminated in a ceremony to receive [iron rings](https://en.wikipedia.org/wiki/Iron_Ring) upon graduation. All Canadian engineers have these rings. According to legend, the rings are forged from the metal of a collapsed bridge.

## 2.2 Game Theory and Mechanism Design

[**Game Theory**](https://en.wikipedia.org/wiki/Game_theory) is a scientific field that **analyzes** incentives, from an economic standpoint. It has a counterpart in economics for **designing (synthesizing)** incentivized systems, called [**Mechanism Design**](https://en.wikipedia.org/wiki/Mechanism_design). In fact Mechanism Design is really _the_ field for design of tokenized ecosystem, in theory. Researchers in that field have come up with a lot of great theory over the years, at literally Nobel prize levels of quality. Closely related is [Economic Game Theory](https://theory.stanford.edu/~tim/f13/f13.html).

However, traditionally there hasn’t been a good way to reconcile that theory with _practice_. After all, how often does an academic economist (or anyone, really) get a chance to deploy an economy? Yet this is the exact problem we are confronted with in designing tokenized ecosystems. The closest are likely video game economies and [public policy design](https://medium.com/@elad.verbin/i-feel-the-right-kind-of-engineering-expertise-that-youre-looking-for-is-actually-public-policy-78fb28a698bb).

However, it turns out that if you zoom in on Mechanism Design with a [few practical constraints](https://medium.com/blockchannel/a-crash-course-in-mechanism-design-for-cryptoeconomic-applications-a9f06ab6a976), you end up with Optimization Design! People doing Optimization Design have a tremendous amount of practical experience deploying optimizer systems over the years. Myself included: my first and second startups ([ADA](https://www.crunchbase.com/organization/analog-design-automation), [Solido](http://www.solidodesign.com/)) did exactly that, for use in industrial-grade circuit design.

## 2.3 Other Related Fields

Many other fields have something to say about token design as well; at the very least in the sense that experts from those fields will find that many of their skills translate well to token design. These include everything from electrical engineering to complex systems, from economics to AI. I list a few below. And of course many of them have roots in good ol’ [cybernetics](https://en.wikipedia.org/wiki/Cybernetics).

![[1-_HNC4AdcXJbOBSV154bkA.png]]

## 2.4 Engineering and Token Design

What should we be calling this field in which we design tokenized ecosystems? I list some options below.

![[1X7-3mzZYKhmL66OjIsGz7w.png]]

The first four terms are **economics**-biased. That’s fine; it makes sense for analyzing price movement, valuations, and so on.

I’m trained as an electrical engineer (EE). EEs doing circuit design have theory, have practice, and build systems that _just work_, such as the screen you’re reading and the chips that power it, to the lights over your head.

**Engineering** is about **rigorous analysis**, **design**, and **verification** of systems; all assisted by tools that reconcile theory with practice. Engineering is also a discipline of **responsibility**: being ethically and professionally accountable to the machines that you build, as illustrated by the Tacoma Narrows Bridge viewings and iron rings.

I saw the rise of the discipline of software _engineering_ in the 90s; that made sense as it encouraged rigor and responsibility.

I’d love to see token ecosystem design become an engineering discipline, side-by-side with electrical engineering, software engineering, civil engineering, aerospace engineering, and so on. This implies that token ecosystem design would also become a field of rigorous analysis, design, and verification. It would have tools that reconcile theory with practice. It would be guided by a sense of responsibility. It would be **token engineering**.

[Note: As for “token” vs “incentive”, “token” is shorter and easier to compare to its economics counterpart “Tokenomics”.]

The image below shows how these fields relate. The goal is a practice of token engineering.

![[1QglZPm485vT4Rybwnf55yA.png]]

# 3. Token Design as Optimization Design

Token design is like optimization design: at a high level, you encode intent with a block rewards function aka objective function, and you let it fly. As is often the case, [Simon de la Rouviere](https://medium.com/@simondlr) [saw this one first](https://hackernoon.com/history-is-rhyming-fitness-functions-comparing-blockchain-tokens-to-the-web-3c117239f4c).

It gets more specific than that. Token design is _especially_ like evolutionary algorithms (EAs), where there are many agents “searching” at once and there is no top-down control of what each agent does. Agents live and die by their block reward or fitness. The table below summarizes the relation.

With such similarities, _we can use best practices from optimization / EA to when doing token design_. This is great news, because many people are Jedis in designing EAs and optimization systems.

![[1TQs5yPxOPF11KbRrJH69IA.png]]

Let’s elaborate on each row in the table.

## 3.1 Goals

Both tokenized ecosystems and EAs have **goals**, in the form of **objectives** (things to maximize or minimize) and **constraints** (things that must be met). To get fancy, this can even be stochastic.

The tokenized ecosystem might give block rewards for an objective function of “maximize hash rate” whereas an EA objective might be “minimize error” in training a deep net. Constraints might be “must have stake ≥threshold to participate” or “deep network layers=100” respectively.

Variants include single-objective optimization (1 objective, 0 constraints), constraint satisfaction (0 objectives, ≥1 constraints), and multi-objective constrained optimization (≥2 objectives, ≥1 constraints).

## 3.2 Measurement & Test

To **test / measure** success against the goals (objectives & constraints), a tokenized ecosystem relies on **proofs** and an optimizer measures **fitness** using e.g. a **simulator**.

For example, a Bitcoin node proves that a user was hashing by verifying that the user’s supplied nonce solves the the cryptographic puzzle.

An optimizer might test the goodness of a circuit by running a SPICE simulation of the circuit’s differential equations; simulation results can be verified by testing whether they indeed solved Kirchoff’s Current and Voltage Laws.

## 3.3 System Agents

In both systems, **agents** run about “doing things”.

In a tokenized ecosystem, **network stakeholders** such as **miners (**or **users** more generally) do whatever it takes to earn block rewards. They jostle about, doing what it takes to get more token rewards. For example, in Bitcoin some agents might design, build, and run ASIC chips to get higher hash rate. Other agents might pool their existing compute resources. The system does not need to explicitly model all stakeholders in the ecosystem. For example, Bitcoin doesn’t have specific roles for banks or nations or companies; it’s mostly all about the miners.

In an EA, you have **individuals** in a **population.** If they’re “good” they have higher fitness. For example, an individual may be a vector of 10,000 weights for a neural network. “Actions” of individuals are basically when they survive and have variants made of them, via operators like crossover (e.g. interpolation) or mutation (e.g. randomly perturbing each parameter).

## 3.4 System Clock

Each system has a **clock**, implying a **time dimension** by which **progress** is made / **convergence** is happening.

**Batches.** Typically, agents are processed in batches or epochs. A tokenized ecosystem periodically generates a **new block** and gives block rewards. The new block points to the old block; and new work in the system will add to the new block; and so on. This linked list of blocks implies a Lamport-style logical clock. In EAs, each batch is a **generation** where a whole population of individuals gets updated at once. Each generational loop might include: evaluate individuals, select the best, let them make children, repeat.

**Continuous.** In some systems, agents are processed more **continuously** rather than batches. These systems usually takes a bit more work to conceptualize, but may lead to better properties for some problems. For example in tokenized ecosystems, a Stellar transaction only needs validation from quorum slice participants, or another node gets added to a DAG (directed acyclic graph) like in Iota. In EAs, we have steady-state evolution where one individual at a time is replaced.

## 3.5 Incentives & Disincentives

The system itself cannot control how the agents behave. (Or at the very least, it shouldn’t _need_ to control them.) As such, **top-level behavior must be an emergent property of bottom-up actions by agents**. This is necessary for tokenized ecosystems; otherwise they’d be centralized! It’s not an absolute must for EAs, but nonetheless a broad set of EAs take this approach for simplicity / elegance or meeting other design goals.

This means the system can only reward or punish behavior, aka carrots or sticks, aka **incentives** and **disincentives**. In designing the system, we _design_ what rewards or punishments to give, and how to give them.

In tokenized ecosystems, rewards take the form of block rewards, and punishments by slashing stake. The former is typically the objective function; the latter is some (but not all) constraints.

In EAs, reward and punishment both come down to which individuals are selected to be parents for the next generation. Examples: randomly choose two individuals and keep the best, repeating until full (tournament selection); and chance of selection is proportional to fitness (roulette wheel selection). Crucially, the EA does _not_ need to steer the individuals by e.g. providing a derivative. This is why a tokenized ecosystem is most like an EA, versus gradient-based optimizers that give top-down directives (using gradients to choose new individuals).

# 4. From Optimization Methodology to Token Methodology

## 4.1 Introduction

This section is some initial notes towards treating token design like the engineering discipline it deserves to grow into.

First, I describe a structured methodology for optimization design. Then I describe how a similar methodology could be applied for incentive design.

Next, I describe key tools used in circuit design: simulators, verification tools, and design space exploration tools; and how they might be applied for circuit design.

Finally, I start to enumerate some design patterns.

## 4.2 Optimization Methodology

These communities only partly talk to each other. But practitioners of the algorithms all do something very similar. They want to ship optimizer systems that _just work_. They follow the following steps. Some do it implicitly, though the pros do it systematically:

1. **Formulate the problem:** They assume that the algorithm “just works” and they focus on formulating the problem in terms of **objectives and constraints** (goal) and design space (where can the optimizer explore, which is really just constraints).
2. **Try an existing solver:** Then they run the algorithm against those goals and let it “solve”. Code for optimization algorithms are often simply called “**solvers**”. If this doesn’t work, practitioners will iterate by trying different problem formulations, or different solvers and solver parameters.
3. **New solver?** If the previous solving step doesn’t work, even after repeated tries on various formulations, then practitioners consider rolling their own solver, i.e. designing a new optimization algorithm.

Let’s explore each step in more detail.

**Step 1. Formulate the Optimization Problem**

Look in almost any optimization-related paper, and you’ll see it display the objectives and constraints. In examples from my own work, equation (1) of [this paper](http://trent.st/content/2011-TEVC-mojito-ea.pdf) (in sec. 5) is a formulation for a multi-objective constrained optimization across a search space defined by a grammar. Here’s a snippet:

![[1oG2O9xH6yyj3srF4p5T_ZA.png]]

As another example. Equations (1) and (2) of [this paper](http://trent.st/content/2009-TCAD-sangria.pdf) (in sec. 2) lay out a stochastic single-objective (“maximize yield”) optimization search problem across an n-dimensional continuous-valued variable space.

Formulating a problem in objectives, constraints, and design space is not easy. In fact, after all these years, it’s still an art that takes a lot of creativity. (Which means it’s fun!) There are often many ways to formulate a problem; and all are not equal . Fortunately, you can get better with practice. I watch friends in the EA community and circuit computer-aided design (CAD) community who have supreme skills in the art of formulating problems. You know who you are;)

- For example, one formulation might be easy to solve and another might be NP-hard and you can’t guarantee anything. This is one of the big tricks used by people in the convex optimization field: they take problems that are perceived as NP-hard, then apply techniques to convert those to convex problems (e.g. well-placed log operators). Then, these convex problems can be solved in polynomial time using a convex solver like [geometric programming](https://en.wikipedia.org/wiki/Geometric_programming). I’ve found success in this too; for the problem summarized by the snippet above, I added grammatical constraints to a tree induction problem (analog circuit synthesis) and saw a 1000x improvement in runtime as well as better results from the optimizer.
- Or, if you’re using an evolutionary algorithm (EA), you want to design the mapping from design point → fitness such that small changes to the design usually lead to small changes to behavior and ultimately fitness. (I call these [smooth operators](http://trent.st/content/2006-DATE-caffeine_double.pdf) ;)

**Step 2. Try an Existing Solver**

Ideally you can formulate the problem such that you can apply an existing solver or algorithm. Then, you simply run it and see how it does.

If it works: you’re done, and you can stop now!

There’s at least two ways it might not work. First, If the solver doesn’t converge well enough, then you can try different problem formulations, solvers or solver parameters.

Second, the solver could converge too “well”, where it finds a design that is wonky. To address this, you can modify the problem: add a new constraint or improve the accuracy of the model / simulator. If you finds yourself in tedious iterations of adding constraints (“[AI whack-a-mole](https://blog.oceanprotocol.com/can-blockchains-go-rogue-5134300ce790)”) then you’ll probably want to re-think your broader approach to the problem.

**Step 3. New Solver? Design a New Optimization Algorithm, If Needed**

Sometimes you come across a problem where none of the existing solvers are good enough. Perhaps you need better scale, or perhaps you need to handle some constraint that’s hard to model, or perhaps something else. That’s when you go and do research on algorithm design. When you’re doing this, you’ll usually leverage existing building blocks, and add in your own ideas. Designing new algorithms can take a tremendous amount of time, but done well, you may be able to solve the problem at hand with order-of-magnitude improvements, for example [FFX](http://trent.st/content/2011-GPTP-FFX-paper.pdf).

(And, did I mention, it’s _fun_?)

## 4.3 Token Methodology

Block rewards are a manifestation of the network’s **objective function** — the thing you want to minimize or maximize. This generalizes. Token design is like design of optimization algorithms. Therefore:

> We can approach token design as optimization design.

We can take the steps from the world of optimization design, and translate them into designing tokenized ecosystems.

1. **Formulate the Problem:** write down the objectives and constraints for your tokenized ecosystem. This means asking: who are my potential stakeholders, and what do each of them want? What are attack vectors? Then translating those into objectives and constraints that you can measure.
2. **Try An Existing Pattern:** Identify if there is an existing solver, i.e. tokenized network design pattern that can solve your problem. For example, if you’re looking for a list of “good” actors/assets/etc, will a [token curated registry](https://medium.com/@ilovebagels/token-curated-registries-1-0-61a232f8dac7) (TCR) do? I elaborate on this later. If this doesn’t work, try different problem formulations, different solvers or solver parameters. For example, it converges to unwanted behavior, so you add a constraint to prevent that behavior.
3. **New Pattern?** If needed, roll your own solver, i.e. design your own tokenized network. Of course when doing this, use existing building blocks where possible, from TCRs to arbitration.

# 5. Token Design Patterns : A Starting Point

Every mature engineering field has its corpus of building blocks .We have books for design patterns in [architecture](https://www.amazon.com/gp/product/0195019199/ref=as_li_tl?ie=UTF8&tag=trentmc002-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=0195019199&linkId=68344ee16e0b020559bc999e505fc290), [software](https://www.amazon.com/gp/product/0201633612/ref=as_li_tl?ie=UTF8&tag=trentmc002-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=0201633612&linkId=b401ac44f5daee31b358f3851a936a99), [analog circuits](https://www.amazon.com/gp/product/0387257462/ref=as_li_tl?ie=UTF8&tag=trentmc002-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=0387257462&linkId=8b2721edc8452e43f9488a1dd794861a) and, yes, [optimizers](https://www.amazon.com/gp/product/3540224947/ref=as_li_tl?ie=UTF8&tag=trentmc002-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=3540224947&linkId=3317b45dfbf66ebe93c7d412dd8fb562). But, no one’s written the book on _token design patterns_, yet.

However, building blocks are starting to emerge. Some have seen popularity explode quickly (e.g. [TCRs](https://twitter.com/mattgcondon/status/965013273337892864)). The paragraphs below explore these blocks. Sometimes they form core token mechanics; sometimes they get bolted in to solve particular problems. This list is just a starting point.

- **Curation.** _Binary_ membership: [Token Curated Registry](https://medium.com/@ilovebagels/token-curated-registries-1-0-61a232f8dac7) (TCR), e.g. to maintain a list of good actors. A sub-block of TCRs is [risk-staking](https://github.com/oceanprotocol/whitepaper/raw/master/whitepaper.pdf) to reduce onboarding friction. _Discrete-valued_ membership: [Stake Machines](https://medium.com/@DimitriDeJonghe/curated-governance-with-stake-machines-8ae290a709b4), e.g. for promoting an actor. _Continuous-valued_ membership: [Curation Markets](https://medium.com/@simondlr/introducing-curation-markets-trade-popularity-of-memes-information-with-code-70bf6fed9881) (CM) for popularity of an asset, defined by its bonding curve with design guidelines [here](https://hackernoon.com/how-to-make-bonding-curves-for-continuous-token-models-3784653f8b17). _Hierarchical_ membership: each label gets a TCR (like [here](https://github.com/oceanprotocol/whitepaper/raw/master/whitepaper.pdf)). _Work_ tied to membership: [Curated Proofs Market Market](https://github.com/oceanprotocol/whitepaper/raw/master/whitepaper.pdf) (CPM). Curation on non-fungible tokens: [Re-Fungible Tokens](https://medium.com/@billyrennekamp/re-fungible-token-rft-297003592769) (RFT).
- **Identity.** _Lower level:_ public key, decentralized identifiers ([DIDs](https://w3c-ccg.github.io/did-spec)). _Medium level_: TCR. _Higher level_: e.g. [uPort](https://www.uport.me/), [Civic](https://www.civic.com/), [Sovrin](https://sovrin.org/), [Authenteq](https://authenteq.com/), [Taqanu](https://www.taqanu.com/), [Estonia E-Residency](https://e-resident.gov.ee/). _Identity of machines:_ e.g. [Spherity](http://spherity.com/)
- **Reputation.** Reputation systems are at the intersection of curation and identity.
- **Governance / software updates.** This can be a mix of [ZeppelinOS](https://zeppelinos.org/), [Aragon](https://aragon.one/), [Colony](https://colony.io/), and more. Maybe eventually [automated](https://medium.com/@miles2045/deep-dreams-of-g%C3%B6del-machines-16c85cf9697f)?
- **Third-party arbitration.** E.g. [Mattereum](https://mattereum.com/).
- **Proofs of human or compute “work”.** For data, compute, and more. This the evaluation of the objective function. It can be can _human work_ like in [Steemit](https://steemit.com/steemit/@alwillis/steemit-s-breakthrough-subjective-proof-of-work) or [Augur](http://www.augur.net/), or _machine work_ like in most other systems. Machine work may be solving an (arguably) less-useful puzzle like in Bitcoin, or more “useful” work like [FileCoin’s Proof of Space-Time](https://filecoin.io/filecoin.pdf). Here’s a breakdown of useful work (“service integrity”) grouped by _data_ and _computation_ (from [here](http://www.oceanprotocol.com/#papers)).

![[1_RwNeO4FCbiRvAssFj7P_g.png]]

Other ways to frame or group building blocks include:

- **How tokens are distributed.** This includes releasing coins for “work”, according to a [controlled supply schedule](https://en.bitcoin.it/wiki/Controlled_supply); 100% pre-mining; [burn-and-mint](https://medium.com/@kylesamani/new-models-for-utility-tokens-d26c12ec00c5); [bounty ICOs](https://medium.com/@jjmstark/bounty-icos-61232e73370b); and more.
- **Ethereum token standards**, such as [ERC20 fungible token](https://github.com/ethereum/eips/issues/20) and [ERC721 non-fungible token](https://github.com/ethereum/eips/issues/721). Billy Rennekamp’s [**token lexicon**](https://medium.com/@billyrennekamp/token-lexicon-b4ed9a4ce363) is helpful.
- **How tokens are valued.** As a means of exchange, store of value, and unit of account, by [Chris Burniske](https://www.amazon.com/gp/product/1260026671/ref=as_li_tl?ie=UTF8&tag=trentmc002-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1260026671&linkId=2ff67ea09ebe44d39c1581941638ad23).
- **How keepers are grouped.** For gatekeeping, arbitrage, or resource transaction, by [Ryan Zurrer](https://medium.com/@rzurrer/keepers-workers-that-maintain-blockchain-networks-a40182615b66).
- **How the compute stack is organized.** Processing, storage, etc. This has variants by [Fred Ehrsam](https://medium.com/@FEhrsam/the-dapp-developer-stack-the-blockchain-industry-barometer-8d55ec1c7d4), [Stephan Tual](https://blog.stephantual.com/web-3-0-revisited-part-one-across-chains-and-across-protocols-4282b01054c5), and [myself](https://blog.bigchaindb.com/blockchain-infrastructure-landscape-a-first-principles-framing-92cc5549bafe).
- **Level-1, level-2, level-N infrastructure.** The core chain is level 1. The higher levels are to help scale without having to reconcile the main chain on every transaction. [Link](https://medium.com/l4-media/making-sense-of-ethereums-layer-2-scaling-solutions-state-channels-plasma-and-truebit-22cb40dcc2f4).
- “[**Cryptoeconomic primitives**](https://medium.com/@jacobscott/the-emergence-of-cryptoeconomic-primitives-14ef3300cc10)” by Jacob Horne. Another label for token design patterns or building blocks. [Published after initial publication of this work.]

This enumeration of patterns is just a starting point; I look forward to watching it grow.

# 6. Needed: Tools for Simulation, Verification, and Design Space Exploration

## 6.1 What

Professional engineers building things that “just work” use _software tools_ for it. Software engineers often use integrated design environments (IDEs) that are free or relatively cheap.

But you can get much more sophisticated. In circuit design, the key tools are for simulation, verification, and design space exploration. The tool stacks can become quite sophisticated over time. But with these tools, it enables a team of 10 engineers to design a billion-transistor chip in a matter of _months_. A good engineer might be running $1M worth of tools (that’s the _annual_ licensing cost!).

Let’s get some power tools for this new field. We need:

1. **Tools to simulate tokenized ecosystems**. Simulators measure performance metrics of a given design. One starting point is the agent-based modeling that’s coming out of the fields of [complexity science](https://www.santafe.edu/engage/learn/courses/introduction-agent-based-modeling) and [artificial general intelligence](https://opencog.org/). Another is the simulators for networks already used for consensus algorithm design. Another is modeling as a set of differential equations (DEs), then solving with a DE solver like [SPICE](https://en.wikipedia.org/wiki/SPICE).
2. **Tools to verify tokenized ecosystems**. These verify that a design can work (according to its performance metrics) despite _uncontrollable_ variables that impact performance. An uncontrollable variable follows (a) a _range_ where the design must perform well at any of the variable’s values, or (b) a probability distribution where the design must perform well in >x% of scenarios. These are “worst-case performance” and “n-sigma performance” respectively. “n-sigma” is a unit to express failure rate, just like “% work” or “% fail”; typically designs aim for 2-sigma (works 95% of the time), 3-sigma (works 99.7% of the time), or 6 sigma (fails about 1 in a billion times).
3. **Tools for design space exploration.** These help the designer explore the design space, i.e. give insight into what happens to worst-case/n-sigma performance when controllable variables get changed.

## 6.2 Example Tool for Simulation, from Circuit Design

The figure below shows an example of a circuit simulator environment. The top left is a schematic editor to inputting the design. For analog circuits this is the choice of resistors, capacitors, transistors etc; how they are connected; and what their sizes are. That input is then automatically converted to a set of differential equations that are then solved using the simulator. The other three windows show results of various simulations. Clockwise from top right are bias (dc) analysis, time-based (transient) analysis, and frequency (ac) analysis.

![[17j_65qxyVJGtAe96KlXu6A.jpeg]]

[[Image: Wikimedia Commons](https://commons.wikimedia.org/wiki/File:CircuitLogix1.jpg)]

## 6.2 Example Tool for Verification, from Circuit Design

This section and next are examples from CAD tools that I helped to develop, and are now widely by engineers at Sony, Qualcomm, etc.

Below is a tool that **verifies** that the chip will not fail across a range of worst-case “PVT” conditions: extremes in **p**ower supply **v**oltage, **t**emperature, load, etc. Therefore P,V, and T are the uncontrollable variables.

This particular tool finds the worst case by employing a global optimizer that tries to optimize towards failure, using a circuit simulator in the loop.

![[1RaU9ZxMAqcq80mgsNmvcFw.png]]

## 6.2 Example Tool for Design Space Exploration, from Circuit Design

The image below shows a tool to **explore** the design space. It reports relative impact of variables on various outputs (left), and how the design variables map to outputs (right). The engineer can change the designs by dragging the orange crosshairs.

These and other tools are now widely used to design modern chips. Simulators came on stream in the 1970s and CAD tools in the 1980s; and no one’s looked back. These tools are _crucial_ to modern chip design. It costs >$50M to manufacture a design on a modern process; it would be, well, _stupid_ to not verify and optimize that design to the best possible level before committing the $50M.

Yet in the world of token design, we are building and deploying what we hope to be billion-dollar ecosystems, with barely any tools. It isn’t even 1970 yet. I look forward to the day when we get to this level for token engineering!

## 6.3 Limitations of Tools

I acknowledge a key difference between complex chips and economies: humans in the loop. Chips are closed systems. Humans make the modeling of an economy a lot messier. However, I have hope that we can improve on the status quo of “nothing”, because we build systems every day that involve humans. Here are a few complementary ideas.

One option is to _not_ try modeling [black swans](https://www.amazon.com/gp/product/081297381X/ref=as_li_tl?ie=UTF8&tag=trentmc002-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=081297381X&linkId=37fd31844ed3bb762816fd63517bc987), but simply minimize potential negative impacts if they do occur.

Or, we could have humans in the loop as part of the “simulator” where they are incentivized to come up with attacks. This formalizes an existing practice: people doing token design get their friends to dream up new attacks, then they update the constraints list then the design accordingly. I’ve found myself in dozens of such conversations.

Simulation will never be perfect. So, we should ensure that the system itself is _evolvable_, towards the intent of the community. The tools for this are governance, staking, and more. Governance may be as simple as hard forks, for example to change the objective function or add constraints. Staking helps convert zero sum to positive sum for the community of token holders.

## 6.4 Extrinsic vs. Intrinsic Motivation

> “ Extrinsic motivation is encouragement from an outside force; behavior is performed based on the expectance of an outside reward [to convince] someone into doing something that they would not do on their own. …
> 
> Intrinsic means innate or within; hence **intrinsic motivation** is the stimulation or drive stemming from within oneself. … Intrinsic motivation is often associated with intrinsic rewards because the natural rewards of a task are the motivating forces that encourage an individual in the first place.” [[Link](http://webshare.northseattle.edu/fam180/topics/praise-rewards/problems.htm)]

This article has focused mostly on extrinsic motivation: figure out what we’re trying to optimize for, and then directly optimize for that. However, extrinsic motivation can have problems. In education, extrinsic rewards reduce intrinsic motivation of children to learn, and hinder self-determination and independent thinking. Fortunately there are teaching styles that encourage intrinsic motivation [[link](http://webshare.northseattle.edu/fam180/topics/praise-rewards/problems.htm)].

For tokenized ecosystems, we must be similarly careful. Extrinsic motivation works for some goals like “maximize security” or “maximize sharing of data”. But it can be dangerous in some places. Let’s say you’re building a decentralized reputation system. Directly tokenizing reputation would incentivize people to game their reputation for money, leading to all sorts of poor behavior. It can also be controlling, like we’ve seen with [China](https://en.wikipedia.org/wiki/Social_Credit_System). Just say no to [Whuffie](https://en.wikipedia.org/wiki/Whuffie) (please).

One possible answer is for the system to support intrinsic motivation rather than extrinsic. In the classroom, this means [tactics like](http://webshare.northseattle.edu/fam180/topics/praise-rewards/problems.htm): provide choices, minimize pressure, allow alternative solutions, encourage originality, and promote success. Some of these might translate to token design. One example is to simply filter out the bad actors with economic stake, e.g. with a TCR. Or, we could promote success via stake machines.

# 7. Conclusion

This article described how we can leverage existing fields to help design tokenized ecosystems: token design as optimization design; token design patterns; and token design tools inspired by circuit design tools. The overall goal is a practice of **token engineering**. We’ll get there!

The [next article](https://blog.oceanprotocol.com/token-engineering-case-studies-b44267e68f4) in this series applies these techniques to two case studies: analysis of Bitcoin, and design of Ocean Protocol.

# Appendix: Calling All Polymaths

I’ve noticed that there’s a group of people in blockchain that seem to thrive especially well. It’s the learning machines: the folks who learn for fun, build for fun, who dance among many fields and build bridges between them. Yep, the polymaths.

In this article, I’ve described how practices from optimization and other fields could help in designing tokenized ecosystems. It also means that experts from these fields could find their skills to be useful in the brave new world of blockchains. I’m hopeful that designers of video game micro-economies can port their skills. Furthermore, just like in blockchain: many folks from AI, complex systems and more are natural polymaths.

I’ve seen this first hand. My own experiences in AI and optimization have been extremely helpful to grok blockchain. Also, I’ve found it easier to ramp up AI people by teaching them the delta between what they know, and blockchain. I simply describe tokenized systems as EAs! To the Artificial Life people, it’s life. To the electrical engineers, it’s feedback control systems. And so forth.

# Appendix: Related Articles & Media

This article is part of a series:

[**Here’s a video**](https://www.youtube.com/watch?v=Zf-WlBl1dAA&feature=youtu.be&t=3152) for the content of this article. Below are the slides. This talk was given at EthCC Paris in March 2018.

Related content:

# Appendix: Related Efforts

I’m searching for practical learnings that the blockchain field can learn from, with the intent to organize and disseminate the experiences. If you read this article and think “wait, _I’ve_ been doing mechanism design for field X” then please reach out.

Publication of this article seems to have sparked a movement in [#tokenengineering](https://twitter.com/search?src=typd&q=%23tokenengineering). Awesome! :):) A key resource is the wiki [tokenengineering.net](http://www.tokenengineering.net/). It has info about building blocks, tools, community meetups, and more.

# Acknowledgements

Thanks to the following people for reviews of this and other articles in the series: [Ian Grigg](https://twitter.com/iang_fc), [Alex Lange](https://medium.com/@alexruppert), [Simon de la Rouviere](https://medium.com/@simondlr), [Dimitri de Jonghe](https://medium.com/@DimitriDeJonghe), [Luis Cuende](https://medium.com/@lic), [Ryan Selkis](https://twitter.com/twobitidiot), [Kyle Samani](https://medium.com/@kylesamani), and [Bill Mydlowec](https://medium.com/@mydlowec). Thanks to many others for conversations that influenced this too, including [Anish Mohammed](https://decentralize.today/@anishmohammed), [Richard Craib](https://medium.com/@Numerai), [Fred Ehrsam](https://medium.com/@FEhrsam), [David Krakauer](https://www.santafe.edu/people/profile/david-krakauer), [Troy McConaghy](https://medium.com/@TroyMc), [Thomas Kolinko](https://www.facebook.com/kolinko), [Jesse Walden](https://medium.com/@jessewalden), [Chris Burniske](https://medium.com/@cburniske), and [Ben Goertzel](https://medium.com/@bengoertzel). And thanks to the entire blockchain community for providing a substrate that makes token design possible:)

# Edits

Here are some updates since the initial publication. Thanks to everyone who gave feedback leading to these updates too.

- Mar 3, 2018: added links to Billy Rennekamp’s [Re-Fungible Tokens](https://medium.com/@billyrennekamp/re-fungible-token-rft-297003592769) and [token lexicon](https://medium.com/@billyrennekamp/token-lexicon-b4ed9a4ce363). Emphasized Slava Balasanov’s [piece](https://hackernoon.com/how-to-make-bonding-curves-for-continuous-token-models-3784653f8b17) on bonding curve design.
- Mar 5, 2018: Added “Limitations of Tools” section based on feedback from [Bill Mydlowec](https://medium.com/@mydlowec) and [Gabriel Nergaard](https://twitter.com/GabrielNergaard). Added “Related Efforts” section. Linked the idea of [automated governance](https://medium.com/@miles2045/deep-dreams-of-g%C3%B6del-machines-16c85cf9697f), by Miles Albert. Added “Extrinsic vs. Intrinsic Motivation” section via feedback from [Christopher Allen](https://twitter.com/ChristopherA). Linked to [Economic Game Theory](https://theory.stanford.edu/~tim/f13/f13.html) via [Ali Yahya](https://twitter.com/ali01/status/970417448704004097?s=11). Elaborated on “constraint adding” step to optimizer design and token design steps. Refined “resonance” description via Troy McConaghy. Fixed “dc”.
- Mar 6, 2018. Added “Cryptoeconomic primitives” reference. Added [Elad Verbin’s](https://medium.com/@elad.verbin?source=post_header_lockup) [suggestion](https://medium.com/@elad.verbin/i-feel-the-right-kind-of-engineering-expertise-that-youre-looking-for-is-actually-public-policy-78fb28a698bb) that Public Policy experts are well suited to token engineering. Added link to risk-staking.
- Mar 28, 2018. Renamed “Proofed Curation Market” to “Curated Proofs Market”. Why? It’s easier to understand.
- June 4, 2018. Replaced the list of “related efforts” to a link to the token engineering wiki and \#tokenengineering hashtag.
- June 5, 2018. Updated “related articles & media” section to emphasize the slides & video that communicate this article best (EthCC talk).