---
title: "Reward is not the optimization target — LessWrong"
source: "https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/reward-is-not-the-optimization-target"
author:
  - "[[TurnTrout]]"
published: 2022-07-24
created: 2025-09-03
description: "TurnTrout discusses a common misconception in reinforcement learning: that reward is the optimization target of trained agents. He argues reward is b…"
tags:
  - type/article
  - source/web
  - topic/technology/ai/reinforcement-learning
  - topic/technology/ai/alignment
  - topic/technology/ai/reward-modeling
  - topic/psychology/cognitive
  - domain/ai
  - context/research
  - knowledge/principle
  - knowledge/mental-model
  - status/evergreen
---
![Background Image](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/splashArtImagePromptA%20marble%20rolling%20down%20a%20hill%2C%20directed%20by%20grooves/dxeicxpznizt2ikqxzcs)

*This insight was made possible by many conversations with Quintin Pope, where he challenged my implicit assumptions about alignment. I’m not sure who came up with this particular idea.*

In this essay, I call an agent a “reward optimizer” if it not only gets lots of reward, but if it reliably makes choices like “reward but no task completion” (e.g. receiving reward without eating pizza) over “task completion but no reward” (e.g. eating pizza without receiving reward). Under this definition, an agent can be a reward optimizer even if it doesn't contain an explicit representation of reward, or implement a search process for reward.

ETA 9/18/23: This post addresses the model-free policy gradient setting, including algorithms like PPO and REINFORCE.

> Reinforcement learning is learning what to do—how to map situations to actions **so as to maximize a numerical reward signal**. —  [Reinforcement learning: An introduction](http://www.incompleteideas.net/sutton/book/first/Chap1PrePub.pdf)

Many people <sup><span><a href="https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/#fnw8im2esr9yd">[1]</a></span></sup> seem to expect that reward will be the optimization target of really smart learned policies—that these policies will be reward optimizers. I strongly disagree. As I argue in this essay, reward is *not*, in general, that-which-is-optimized by RL agents.<sup><span><a href="https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/#fndaf17p7n29n">[2]</a></span></sup>

Separately, as far as I can tell, most <sup><span><a href="https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/#fnwraenj05b1">[3]</a></span></sup> practitioners usually view reward as encoding the relative utilities of states and actions (e.g. it’s *this good* to have all the trash put away), as opposed to imposing a *reinforcement schedule* which builds certain computational edifices inside the model (e.g. reward for picking up trash → reinforce trash-recognition and trash-seeking and trash-putting-away subroutines). I think the former view is usually inappropriate, because in many setups, **reward** ***chisels cognitive grooves into an agent*****.**

Therefore, *reward is not the optimization target* in two senses:

1. Deep reinforcement learning agents will not come to intrinsically and primarily value their reward signal; reward is not *the trained agent’s* optimization target.
2. Utility functions express the *relative goodness* of outcomes. Reward *is not best understood* as being a kind of utility function. Reward has the mechanistic effect of *chiseling cognition into the agent's network*.Therefore, properly understood, reward does not express relative goodness and is therefore *not an optimization target at all.*

## Reward probably won’t be a deep RL agent’s primary optimization target

After work, you grab pizza with your friends. You eat a bite. The taste releases [reward in your brain](https://en.wikipedia.org/wiki/Reward_system), which triggers credit assignment. Credit assignment identifies which thoughts and decisions were responsible for the release of that reward, and makes those decisions more likely to happen in similar situations in the future. Perhaps you had thoughts like

- “It’ll be fun to hang out with my friends” and
- “The pizza shop is nearby” and
- “Since I just ordered food at a cash register, execute `motor-subroutine-#51241` to take out my wallet” and
- “If the pizza is in front of me and it’s mine and I’m hungry, raise the slice to my mouth” and
- “If the slice is near my mouth and I’m not already chewing, take a bite.”

Many of these thoughts will be judged responsible by credit assignment, and thereby become more likely to trigger in the future. This is what *reinforcement* learning is all about—the reward is the *reinforcer* of those things which came before it and the *creator* of new lines of cognition entirely (e.g. anglicized as "I shouldn't buy pizza when I'm mostly full"). The reward chisels cognition which increases the probability of the reward accruing next time.

Importantly, reward does not automatically spawn thoughts *about* reward, and reinforce those reward-focused thoughts! Just because common English endows “reward” with suggestive pleasurable connotations, that [does not mean that](https://www.readthesequences.com/No-Universally-Compelling-Arguments) an RL agent will  *terminally value* reward!

What kinds of people (or non-tabular agents more generally) will become reward optimizers, such that the agent ends up terminally caring about reward (and little else)? Reconsider the pizza situation, but instead suppose you were thinking thoughts like “this pizza is going to be so rewarding” and “in this situation, eating pizza sure will activate my reward circuitry.”

You eat the pizza, triggering reward, triggering credit assignment, which correctly locates these reward-focused thoughts as contributing to the release of reward. Therefore, in the future, you will more often take actions because you think they will produce reward, and so you will become more of the kind of person who intrinsically cares about reward. This is a path <sup><span><a href="https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/#fnzf0metnada">[4]</a></span></sup> to reward-optimization and wireheading.

While it's possible to have activations on "pizza consumption predicted to be rewarding" and "execute `motor-subroutine-#51241` " and then have credit assignment hook these up into a new motivational circuit, **this is only** ***one possible direction*** **of value formation in the agent**. Seemingly, the most direct way for an agent to become *more* of a reward optimizer is to *already* make decisions motivated by reward, and then have credit assignment further generalize that decision-making.

## The siren-like suggestiveness of the word “reward”

Let’s strip away the suggestive word “reward”, and replace it by its substance: cognition-updater.

Suppose a human trains an RL agent by pressing the cognition-updater button when the agent puts trash in a trash can. While putting trash away, the AI’s policy network is probably “thinking about” <sup><span><a href="https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/#fn1hpxjpayyk4"><span>[5]</span></a></span></sup> the *actual world it’s interacting with*, and so the cognition-updater reinforces those heuristics which lead to the trash getting put away (e.g. “if trash-classifier activates near center-of-visual-field, then grab trash using `motor-subroutine-#642` ”).

Then suppose this AI models the true fact that the button-pressing produces the cognition-updater. Suppose this AI, which has historically had its trash-related thoughts reinforced, considers the plan of pressing this button. “If I press the button, that triggers credit assignment, which will reinforce my decision to press the button, such that in the future I will press the button even more.”

Why, exactly, would the AI seize <sup><span><a href="https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/#fnsmeax43bfp9"><span>[6]</span></a></span></sup> the button? To reinforce itself into a certain corner of its policy space? The AI has not had antecedent-computation-reinforcer-thoughts reinforced in the past, and so its current decision will not be made in order to acquire the cognition-updater!

RL is not, in general, about training cognition-updater optimizers.

## When is reward the optimization target of the agent?

If reward is guaranteed to become your optimization target, then your learning algorithm can force you to become a drug addict. Let me explain.

[Convergence theorems](https://nlp.chonbuk.ac.kr/AML/slides_lille/Lecture4-b.pdf) provide conditions under which a reinforcement learning algorithm is guaranteed to converge to an optimal policy for a reward function. For example, value iteration maintains a table of value estimates for each state  *s*, and iteratively propagates information about that value to the neighbors of  *s*. If a far-away state  *f* has huge reward, then that reward ripples back through the environmental dynamics via this [“backup” operation](https://inst.eecs.berkeley.edu/~cs294-40/fa08/scribes/lecture2.pdf). Nearby parents of  *f* gain value, and then after lots of backups, far-away ancestor-states gain value due to *f* ’s high reward.

Eventually, the “value ripples” settle down. The agent picks an (optimal) policy by acting to maximize the value-estimates for its post-action states.

Suppose it would be extremely rewarding to do drugs, but those drugs are on the other side of the world. Value iteration backs up that high value to your present space-time location, such that your policy necessarily gets *at least* that much reward. There’s no escaping it: After enough backup steps, you’re traveling across the world to do cocaine.

But obviously these conditions aren’t true in the real world. Your learning algorithm doesn’t force *you* to try drugs. Any AI which e.g. tried every action at least once would quickly kill itself, and so real-world general RL agents won’t explore like that because that would be stupid. So the RL agent’s algorithm won’t make it e.g. explore wireheading either, and so the convergence theorems *don’t apply even a little—even in spirit*.

## Anticipated questions

1. Why won’t early-stage agents think thoughts like “If putting trash away will lead to reward, then execute `motor-subroutine-#642` ”, and then this gets reinforced into reward-focused cognition early on?
	1. Suppose the agent puts away trash in a blue room. Why won’t early-stage agents think thoughts like “If putting trash away will lead to the wall being blue, then execute `motor-subroutine-#642` ”, and then this gets reinforced into blue-wall-focused cognition early on? [Why consider either scenario to begin with](https://www.readthesequences.com/Privileging-The-Hypothesis)?
2. But aren’t we implicitly selecting for agents with high cumulative reward, when we train those agents?
	1. Yeah. But on its own, this argument can’t possibly imply that selected agents will probably be reward optimizers. The argument would [prove too much](https://slatestarcodex.com/2013/04/13/proving-too-much/). Evolution selected for inclusive genetic fitness, and it  [did not get IGF optimizers](https://www.lesswrong.com/posts/XPErvb8m9FapXCjhA/adaptation-executers-not-fitness-maximizers).
		1. "We're selecting for agents on reward we get an agent which optimizes reward" is locally invalid. "We select for agents on X we get an agent which optimizes X" is not true for the case of evolution, and so is not true in general.
		2. Therefore, the argument isn't necessarily truein the AI reward-selection case. Even if RL *did* happen to train reward optimizers and this post *were* wrong, the selection argument is too weak on its own to establish that conclusion.
	2. Here’s the more concrete response: Selection isn’t *just* for agents which get lots of reward.
		1. For simplicity, consider the case where on the training distribution, the agent gets reward if and only if it reaches a goal state. Then any selection for reward is also selection for reaching the goal. And if the goal is the only red object, then selection for reward is *also* selection for reaching red objects.
		2. In general, selection for reward produces equally strong selection for reward’s necessary and sufficient conditions. In general, it seems like there should be a lot of those. Therefore, since selection is not only for *reward* but for *anything which goes along with reward* (e.g. reaching the goal), then selection won’t advantage *reward optimizers* over *agents which reach goals quickly / pick up lots of trash / \[do the objective\]*.
	3. Another reason to not expect the selection argument to work is that it’s *convergently instrumental* for most inner agent values to *not* become wireheaders, for them to *not* try hitting the reward button.
		1. I think that before the agent can hit the particular attractor of reward-optimization, it will hit an attractor in which it optimizes for some aspect of a historical correlate of reward.
			1. We train agents which intelligently optimize for e.g. putting trash away, and this reinforces the trash-putting-away computations, which activate in a broad range of situations so as to steer agents into a future where trash has been put away. An intelligent agent will model the true fact that, if the agent reinforces itself into caring about cognition-updating, then it will no longer navigate to futures where trash is put away. Therefore, it decides to not hit the reward button.
			2. This reasoning follows for most inner goals by instrumental convergence.
		2. On my current best model, this is why people usually don’t wirehead. They learn their own values via deep RL, like caring about dogs, and these actual values are opposed to the person they would become if they wirehead.
3. Don’t some people terminally care about reward?
	1. I think so! I think that generally intelligent RL agents will have *secondary, relatively weaker* values around reward, but that reward will not be a primary motivator. Under my current (weakly held) model, an AI will only start chiseled computations about reward *after* it has chiseled other kinds of computations (e.g. putting away trash). More on this in later essays.
4. But what if the AI bops the reward button early in training, while exploring? Then credit assignment would make the AI more likely to hit the button again.
	1. Then keep the button away from the AI until it can model the effects of hitting the cognition-updater button.<sup><span><a href="https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/#fn5fwuzzvjmuv">[7]</a></span></sup>
	2. For the reasons given in the “siren” section, a sufficiently reflective AI probably won’t seek the reward button on its own.
5. AIXI—
	1. will always kill you and then wirehead forever, unless you gave it something like a constant reward function.
	2. And, IMO, this fact is not practically relevant to alignment. AIXI is *explicitly a reward- maximizer*. As far as I know, AIXI(- *tl*) is not the limiting form of any kind of real-world intelligence trained via *reinforcement* learning.
6. Does the choice of RL algorithm matter?
	1. For point 1 (*reward is not the trained agent's optimization target*), it might matter. 
		1. I started off analyzing model-free actor-based approaches, but have also considered a few model-based setups. I think the key lessons apply to the general case, but I think the setup will substantially affect which values tend to be grown. 
			1. If the agent's curriculum is broad, then reward-based cognition may get reinforced from a confluence of tasks (solve mazes, write sonnets), while each task-specific cognitive structure is only narrowly contextually reinforced. That said, this is also selecting equally hard for agents which do the rewarded activities, and reward-motivation is only one possible value which produces those decisions.
			2. Pretraining a language model and then slotting that into an RL setup also changes the initial computations in a way which I have not yet tried to analyze.
		2. It’s *possible* there’s some kind of RL algorithm which *does* train agents which limit to reward optimization (and, of course, thereby “solves” inner alignment in its literal form of “find a policy which optimizes the outer objective signal”).
	2. For point 2 (*reward provides local updates to the agent's cognition via credit assignment; reward is not best understood as specifying our preferences*), the choice of RL algorithm should not matter, as long as it uses reward to compute local updates. 
		1. A similar lesson applies to the updates provided by loss signals. A loss signal provides updates which deform the agent's cognition into a new shape.
7. TurnTrout, you've been talking about an AI's learning process using English, but ML gradients may not neatly be expressible in our concepts. How do we know that it's appropriate to speculate in English?
	1. I am *not* *certain* that my model is legit, but it sure seems more legit than (my perception of) how people usually think about RL (i.e. in terms of reward maximization, and reward-as-optimization-target instead of as feedback signal which builds cognitive structures).
	2. I only have access to my own concepts and words, so I am provisionally reasoning ahead anyways, while keeping in mind the potential treacheries of anglicizing imaginary gradient updates (e.g. "be more likely to eat pizza in similar situations").

## Dropping the old hypothesis

At this point, I don't see a strong reason to focus on the “reward optimizer” hypothesis. The idea that AIs will get really smart and primarily optimize some reward signal… I don’t know of any tight mechanistic stories for that. I’d love to hear some, if there are any.

As far as I’m aware, the strongest evidence left for agents intrinsically valuing cognition-updating is that some humans *do* strongly (but not uniquely) value cognition-updating,<sup><span><a href="https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/#fn2v0yltp1gw7">[8]</a></span></sup> and many humans seem to value it weakly, and humans are probably RL agents in the appropriate ways. So we definitely can’t *rule out* agents which strongly(and not just weakly) value the cognition-updater. But it’s also *not* the overdetermined default outcome. More on that in future essays.

It’s true that reward *can* be an agent’s optimization target, but what reward *actually does* is reinforce computations which lead to it. A particular alignment proposal might argue that a reward function will *reinforce the agent into a shape such that it intrinsically values reinforcement*, and that the  *cognition-updater goal is also a human-aligned optimization target*, but this is still just one particular approach of using the cognition-updating to produce desirable cognition within an agent. Even in that proposal, the primary mechanistic function of reward is reinforcement, not optimization-target.

## Implications

Here are some major updates which I made:

1. **Any reasoning derived from the reward-optimization premise is now suspect until otherwise supported.**
2. **Wireheading was never a high-probability problem for RL-** ***trained*** **agents**, absent a specific storyfor why cognition-updater-acquiring thoughts would be chiseled into primary decision factors.
3. **Stop worrying about finding “outer objectives” which are safe to** ***maximize.***<sup><span><a href="https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/#fnp7rlxgfkp9">[9]</a></span></sup> I think that you’re not going to get an outer-objective-maximizer (i.e. an agent which maximizes the explicitly specified reward function).
	1. Instead, focus on building good cognition within the agent.
	2. In my ontology, there's only one question: How do we grow good cognition inside of the trained agent?
4. **Mechanistically model RL agents as executing behaviors downstream of past reinforcement** (e.g. putting trash away), in addition to thinking about policies which are selected for having high reward on the training distribution (e.g. hitting the button).
	1. The latter form of reasoning skips past the mechanistic substance of reinforcement learning: The chiseling of computations responsible for the acquisition of the cognition-updater. I still think it's useful to consider selection, but mostly in order to generate failures modes whose mechanistic plausibility can be evaluated.
	2. In my view, reward's proper role isn't to encode an objective, but a *reinforcement schedule*, such that the right kinds of computations get reinforced within the AI's mind.

*Edit 11/15/22*: The original version of this post talked about how reward reinforces antecedent computations in policy gradient approaches. This is not true in general. I edited the post to instead talk about how reward is used to upweight certain kinds of actions in certain kinds of situations, and therefore reward *chisels cognitive grooves into agents*.

Let’s take a little stroll through [Google Scholar’s top results for “reinforcement learning"](https://scholar.google.com/scholar?hl=en&as_sdt=7,39&q=reinforcement+learning), emphasis added:

> The agent's job is to find a policy … that  **maximizes some long-run measure of reinforcement**. ~ [Reinforcement learning: A survey](https://www.jair.org/index.php/jair/article/download/10166/24110/)

> In instrumental conditioning, animals learn to choose actions to obtain rewards and avoid punishments, or, more generally to achieve goals. **Various goals are possible, such as optimizing the average rate of acquisition of net rewards (i.e. rewards minus punishments), or some proxy for this such as the expected sum of future rewards**. ~ [Reinforcement learning: The Good, The Bad and The Ugly](https://www.princeton.edu/~yael/Publications/DayanNiv2008.pdf)

Steve Byrnes did, in fact, briefly point out part of the “reward is the optimization target” mistake:

> I note that even experts sometimes sloppily talk as if RL agents make plans towards the goal of maximizing future reward… — [Model-based RL, Desires, Brains, Wireheading](https://www.lesswrong.com/posts/K5ikTdaNymfWXQHFb/model-based-rl-desires-brains-wireheading#Self_aware_desires_1__wireheading)

I don't think it's just sloppy talk, I think it's incorrect belief in many cases. I mean, I did my PhD on RL theory, and I stillbelieved it. Many authorities and textbooks confidently claim—presenting little to no evidence—that reward is an optimization target (i.e. the quantity which the policy is in fact trying to optimize, or the quantity to be optimized by the policy). [Check what the math actually says](https://www.lesswrong.com/posts/2GxhAyn9aHqukap2S/looking-back-on-my-alignment-phd#Too_much_deference__too_little_thinking_for_myself).

[^1]: [Including](https://www.sciencedirect.com/science/article/pii/S0004370221000862#fn0020) the authors of the quoted introductory text, [Reinforcement learning: An introduction](http://www.incompleteideas.net/sutton/book/first/Chap1PrePub.pdf). I have, however, met several alignment researchers who already internalized that reward is not the optimization target, perhaps not in so many words.

[^2]: [Utility ≠ Reward](https://www.lesswrong.com/posts/bG4PR9uSsZqHg2gYY/utility-reward) points out that an RL-trained agent is  *optimized by* original reward, but not necessarily *optimizing for* the original reward. This essay goes further in several ways, including when it argues that *reward* and *utility* have different type signatures—that reward shouldn’t be viewed as encoding a goal at all, but rather a *reinforcement schedule*. And not only do I not expect the trained agents to maximize the original “outer” reward signal, I think they probably won’t try to strongly optimize  [*any* reward signal](https://www.lesswrong.com/posts/3RdvPS5LawYxLuHLH/hackable-rewards-as-a-safety-valve?commentId=crkrEjpyjB7N9t5jo).

[^3]: [Reward shaping](http://ai.stanford.edu/~ang/papers/shaping-icml99.pdf) seems like the most prominent counterexample to the “reward represents terminal preferences over state-action pairs” line of thinking.

[^4]: But also, you were still probably thinking about reality as you interacted with it (“since I’m in front of the shop where I want to buy food, go inside”), and credit assignment will still locate some of those thoughts as relevant, and so you wouldn’t purely reinforce the reward-focused computations.

[^5]: "Reward reinforces existing thoughts" is ultimately a claim about how updates depend on the existing weights of the network. I think that it's easier to update cognition along the lines of existing abstractions and lines of reasoning. If you're already running away from wolves, then if you see a bear and become afraid, you can be updated to run away from large furry animals. This would leverage your *existing* concepts.

From [A shot at the diamond-alignment problem](https://www.lesswrong.com/posts/k4AQqboXz8iE5TNXK/a-shot-at-the-diamond-alignment-problem):

The local mapping from gradient directions to behaviors is given by the neural tangent kernel, and the learnability of different behaviors is given by the NTK’s eigenspectrum, which [seems to adapt to the task at hand](https://arxiv.org/abs/2008.00938), making the network quicker to learn along behavioral dimensions similar to those it has already acquired.

[^6]: Quintin Pope remarks: “The AI would probably want to establish **control** over the button, if only to ensure its values aren't updated in a way it wouldn't endorse. Though that's an example of convergent powerseeking, not reward seeking.”

[^7]: For mechanistically similar reasons, keep cocaine out of the crib until your children can model the consequences of addiction.

[^8]: I am presently ignorant of [the relationship between pleasure and reward prediction error in the brain](https://pubmed.ncbi.nlm.nih.gov/35156187/). I do not think they are the same.  
  
However, I think people are usually weakly hedonically / experientially motivated. Consider a person about to eat pizza. If you give them the choice between "pizza but no pleasure from eating it" and "pleasure but no pizza", I think most people would choose the latter (unless they were really hungry and needed the calories). If people just navigated to futures where they had eaten pizza, that would not be true.

[^9]: From correspondence with another researcher: There may yet be an interesting alignment-related puzzle to "Find an optimization process whose maxima are friendly", but I personally don't share the intuition yet.