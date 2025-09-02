---
Content:
  - DAO
  - EntrepreneurFirst
  - Entrepreneurship
  - Web3
Type: Article
tags:
  - "#article"
  - "#topic/dao"
  - "#topic/web3"
  - "#topic/blockchain"
  - "#topic/startup"
  - "#topic/organization"
  - "#source/article"
  - "#status/active"
  - "#priority/high"
  - "#evergreen"
---
[https://medium.com/1kxnetwork/organization-legos-the-state-of-dao-tooling-866b6879e93e](https://medium.com/1kxnetwork/organization-legos-the-state-of-dao-tooling-866b6879e93e)

  

![[1JNvEZsJxiaMOIxReY7SK2Q.png]]

DAO Operations is a budding crypto vertical that remains underserved. With over [1,000 Snapshot spaces](https://snapshot.org/#/), [700k governance token holders](https://www.deepdao.io/#/deepdao/dashboard), and over [$10B in DAO treasury](https://open-orgs.info/), there is a huge opportunity to create value in all operational arms of internet-native organisations.

The internet was the enabler of large-scale human coordination. DAO tools — built on web3 — now give us the ability to design and manage incentives to maintain positive-sum relationships between stakeholders, keeping them aligned on shared goals as the product or community grows.

Compared to the Cambrian explosion of “money legos” that has grown DeFi from [$7B to $90B](https://defipulse.com/) in the past year, the ecosystem of “organisation legos” is still in its infancy.

DAO Tooling Landscape — March 2022

Whether a DAO is spun up to build products ([yearn](https://yearn.finance/), [Sushi](https://sushi.com/)), to invest ([The LAO](https://www.thelao.io/), [MetaCartel Ventures](https://metacartel.xyz/)), to collect NFTs ([FlamingoDAO](https://flamingodao.xyz/), [PleasrDAO](https://pleasr.org/)), or to provide services ([RaidGuild](https://www.raidguild.org/), [LexDAO](https://www.lexdao.coop/)), all are susceptible to the same high-level challenges as they grow:

## _**1. How to lower the barrier to**_ **meaningful** _**contribution**_

Because contributions to DAOs can come from anywhere, tools that qualify and quantify different types of contributions (e.g. bounties, DAO-specific metrics) can be used to create a shared understanding of priorities of how one can expect to be rewarded for different levels of participation. In addition to monetary compensation, DAOs can leverage reputation-building tools to motivate value-aligned participants to take on more ownership and grow with the DAO.

## _**2. How to maintain operational efficiency as they decentralise**_

Decentralisation should not come at the expense of efficiency in the long run. Progressive decentralisation enables an initial team to search for product market fit on its way toward [credible neutrality](https://nakamoto.com/credible-neutrality/). We will explore examples of DAOs doing this through constrained delegation and working groups, as well as the tools that provide additional layers of checks and balances that hold executors accountable to token holders.

## _**3. How to coordinate decision-making at scale**_

Voting tools help individuals voice their opinions, fund initiatives they care about, and empower representatives they trust to execute in a ways align with their views. Crucial to these decisions will be information that is relevant and accessible. Analytics tools and data aggregators play an important role in making DAOs human-readable, surfacing meaningful insights from raw on-chain and off-chain data.

In this article I explore these questions through the lens of organization design and the growing suite of web3-native tools that aims to address them. After exploring each category— contribution management, compensation, decision making, treasury, analytics, and DAO frameworks — we arrive at a snapshot of the ecosystem of organisation legos available today which, though multitudes richer than it was a year ago, can only hint at what’s to come.

# **Organization Design**

At a certain headcount, what may start as a monolithic group chat organically breaks into working groups or functional committees in which members take on ownership of a given milestone.

The names and details of these groups vary across DAOs, but we can roughly group them by their operational functions.

To balance efficiency with decentralisation, DAOs have adopted patterns of distributed authority and [**constrained delegation**](https://gov.yearn.finance/t/yip-61-governance-2-0/10460) in which token holders empower groups of active contributors with executive decision-making authority within a **discrete domain**.

Constrained delegation allows individuals with the expertise and intimate contextual knowledge to perform their jobs autonomously, while still being held accountable to the DAO. Working group leaders are often nominated or elected, and can be voted out by the community.

Examples of functional committees in yearn (“[yTeams](https://gov.yearn.finance/t/yip-61-governance-2-0/10460)”), Nexus Mutual (“[Hubs](https://forum.nexusmutual.io/t/nexus-hub-proposal-structure-next-steps/509)”), and Index Coop (“[Working Groups](https://docs.indexcoop.com/community/working-groups-101)”), respectively.

Another example of functional committees (“workstreams”) in [ShapeShift DAO](https://forum.shapeshift.com/t/shapeshift-organizational-structure/50)

While many responsibilities overlap with those of traditional organisations,the core difference (and value proposition) is that _**opportunities to contribute are open**_. Anybody can take the initiative and make proposals to create new working groups or change the way things are run.

Unlike traditional orgs where individual employees and users are beholden to decisions made behind the closed doors of a boardroom, any stakeholder of a DAO can step up to be the change they want to see. A DAO opens up the floor to the wider community through proposals and [request-for-comments](https://gov.uniswap.org/t/rfc-uniswap-grants-program-v0-1/9081). The purpose, resource requirements, key stakeholders, performance metrics, and actual results of an initiative are made transparent — creating accountability and a social layer of checks and balances.

**Decentralisation doesn’t mean leaderless. Rather,** _**more**_ **people are empowered to take initiatives towards shared goals: the DAO’s North Star.**

Well-maintained documentation that details how the DAO is structured, and what each working group is working on, goes a long way to help potential contributors understand where their skills might align with the DAO’s needs. Of course, the motivation to contribute has to be there in the first place. This is where the contributor journey comes in.

# **Contribution Management**

The contributor journey is the process by which an individual goes from not knowing about the DAO, to lurking on social channels (e.g. Twitter, Discord), to establishing connections with other members, to making their first contribution, and beyond.

Ideally, the contributor journey [fosters a growing sense of ownership and belonging](https://medium.com/1kxnetwork/how-to-grow-decentralized-communities-1bf1044924f8) such that the individual wants to grow with the community and make a larger impact towards its vision.

Contributor journey is a process design problem, but inherent in this are questions about what tools to use and how best to use them. Tools can address big questions like:

- How to surface the right opportunities/information to the right people at the right time
- How to quantify, incentivise, and properly reward contributions
- How to foster trust through roles and reputation systems

Quests and Bounties are bite-sized tasks that members can take on to “level up” in the DAO. While only the first step for onboarding contributors, Bounties are a good way to give contributors a “Good First Issue” to work on because they are well-defined in terms of scope and deliverables. Bounties can be automatically verified if it’s an on-chain task ([Rabbit Hole](http://rabbithole.gg/)), or left up to the discretion of a DAO member that owns the bounty ([Gitcoin](https://gitcoin.co/explorer), [Coinvise](https://www.coinvise.co/)).

[Yearn](https://yearn.finance/) has a dashboard that aggregates [open issues](https://contribute.yearn.rocks/) across their code repositories, and a Telegram group dedicated to surfacing tasks for interested participants.

Bounties can be as simple as a Telegram group, but needs a dedicated facilitator to connect the right individuals with the right opportunity.

[Dashboard](https://contribute.yearn.rocks/) of open issues across yearn’s repositories

The “Quest Complete” moment, as gamers know, is a powerful feeling that can itself be intrinsic motivators to take on a task. **However, bounties by themselves are insufficient to drive individuals to take on more ownership.**

Over time, members can grow their reputation within the DAO by earning “XP” and trust with each contribution. A few hours perusing a DAO’s Discord or Discourse forums can reveal its most influential members. Some are founding members, but many have organically emerged from the crowd by taking their own initiative to drive outcomes for the DAO.

A member’s progress through the contributor journey could manifest itself as Discord Roles, which when leveraged well, [serve as proxies for trust](https://gov.indexcoop.com/t/trust-and-impact-in-the-index-coop/1661). If there is a shared understanding within the community that a “Gold” member has contributed 500+ hours of work to the DAO, for example, you know to put more weight on what they say than someone without any badges.

Reputation as proxies for trust helps people allocate their attention within the DAO, it also tells outsiders who to approach when they need support or want to explore partnership opportunities.

[Contributor tiers](https://gov.indexcoop.com/t/trust-and-impact-in-the-index-coop/1661) in [Index Coop](https://www.indexcoop.com/) are tied to access rights and rewards

If a person or tool becomes a bottleneck, a task for the Community or People working group should be to remove the bottleneck. **The contributor journey, when working well, should be the path of least resistance for community members to go from 0 to 1 and beyond.**

The contributor journey doesn’t end when someone goes from being a lurker on Discord to a working group lead. Web 3.0 allows individuals to port their identity and reputation across applications and communities. As DAO-affiliation is more pluralistic and intertwined than traditional employer-affiliation, DAOs are much stronger vessels for individuals to build and communicate a holistic picture of who they are and what they’re passionate about.

# **Compensation**

Payment distribution infrastructure is more mature relative to tooling in other organizational areas. DAOs can stream payments to contributors via [Sablier](https://sablier.finance/) or [Superfluid](https://www.superfluid.finance/), bulk-distribute tokens through [Roll](https://tryroll.com/) or [disperse.app](https://disperse.app/), fund grants through its [Gnosis Safe](https://gnosis-safe.io/) multisig, and keep track of payments via treasury management tools like [Parcel](https://parcel.money/) and [Multis](https://multis.co/).

DAOs can even offer something akin to an [employee stock option plan](https://www.esop.org/) (ESOP) by locking tokens in an options contract and [streaming call options](https://twitter.com/RafaellaBaraldo/status/1426189408873627649) to contributors over some vesting period. The power of DeFi primitives.

_How_ different types of contributions should be rewarded is less clear. Tools like [SourceCred](https://sourcecred.io/) quantify and assign “cred” to activities like Github issues, PR commits, and Discourse posts. Drawing inspiration from SourceCred, [Govrn](https://www.govrn.io/) takes this a step further and works with individual DAOs to create a “Movement Model”, in which the community assigns weight to different types of contributions depending on its priorities.

[Meta Gamma Delta](https://twitter.com/metagammadelta)’s Movement Model on [Govrn](https://www.govrn.io/about)

What’s nice about this is that you get standardisation for value creation _**within the context of the DAO**_. What _counts_ as a contribution, and _how valuable_ each type of contribution is, is up to the community’s discretion. This weighting can be modified through proposals at any time.

Movement Models may look completely different from one DAO to another, but that’s the idea. **The community shouldn’t have to retrofit itself to metrics that were defined elsewhere.** Bottom-up models like these plug into things like rewards distribution, bounties creation, and novel voting mechanics like [quadratic trust](https://quadratictrust.com/).

Because the opportunity to contribute is open, the DAO itself might not know there is a need until a member of the community voluntarily builds a solution for it. It’s easy for “[compensation committee](https://gov.yearn.finance/t/yearn-retention-packages/9698/10)”s or even [governance](https://medium.com/iearn/decentralized-payroll-management-for-daos-b2252160c543) to overlook contribution at the edges of the network.

[Coordinape](https://coordinape.com/) is a peer-based compensation tool built on the premise that **contributors of a working group themselves know best who has created the most value**. Since contribution comes from the edges, knowledge about the value each contributor adds also lies at the edges. At the end of some work period (an “epoch”), Coordinape allows members within a working group to distribute rewards to peers at their own discretion. This removes the need for a central authority of rewards distributors who has to (likely inaccurately) determine value creation at a granular level.

Screenshots from [Coordinape](https://coordinape.com/). A rewards distribution tool that allows people who work closely together to reward their peers.

HR is one of the most under-addressed verticals for DAO contributors. There is a huge opportunity for projects to offer individuals a web3-native solution to handle “meatspace” benefits like health insurance, 401ks, IRAs, and tax compliance.

Today, these benefits are attached to the employer instead of individual employees, who are beholden to the providers and packages selected for them by a company’s HR department. Furthermore, they lose these benefits should they leave the company. This is a perverse relationship and a problem for freelance workers in general, but topped with receiving payroll in crypto, it’s a downright barrier for people to go “full-time DAO”

[Opolis](https://opolis.co/) is one of the first digital employment cooperatives aimed at independent workers in web3. The platform serves as an employer-agnostic shared services layer, giving its members access to employment benefits, payroll and tax compliance services. By unbundling employment such that benefits are attached to the individual and not the employer, Opolis gives individuals the freedom and flexibility to get compensated by different DAOs while retaining the HR benefits of a traditional organization.

Opolis currently works with individuals from projects such as [MakerDAO](https://makerdao.com/en/), [Gitcoin](https://gitcoin.co/), [BadgerDAO](https://app.badger.finance/), and more recently [ShapeShift](https://shapeshift.com/). Although membership is currently limited to US individuals, the platform is one of the few that bridges web2 stability with web3 self-sovereignty.

# **Decision Making**

Early DAO frameworks come with built-in governance tools which keep voting and on-chain execution tightly coupled (e.g. share-based voting in Moloch). Members can earn shares in the DAO through work, and express their opinions by voting in proposals which, if passed, automatically translate to on-chain action such as moving money from the DAO’s treasury to fund a grant recipient.

Comprehensive DAO Frameworks with built-in voting

In the past year, gas prices have pushed the ecosystem to decouple voting from on-chain execution. Basic polling is done off-chain via Discord, Discourse, Telegram polls, or token-based signal voting through tools like [Snapshot](https://snapshot.org/). While off-chain votes capture community sentiment, the execution power is ultimately left to a handful of admins (multisig signers).

Modular voting tools

Another decision-making process adopted by DAOs like [Uniswap](https://gov.uniswap.org/t/community-governance-process/7732) and [Radicle](https://radicle.community/t/readme-radicle-governance-process/526) is the proposal lifecycle which involves signal voting in the beginning stages to refine a proposal. Only when the proposal details are finalized does it go to an on-chain vote. With this method, votes are more “meaningful” as they affect on-chain state (in the case of protocols). However, the entire process can be time consuming as communities need to allow time for members to discuss and vote on proposals.

**The next generation of governance tools will bridge the gap between off-chain voting and on-chain execution** — offering a layer of checks and balances to ensure that execution, even if initiated from a multisig, actually reflects the outcomes of an off-chain vote.

[Gnosis SafeSnap](https://blog.gnosis.pm/introducing-safesnap-the-first-in-a-decentralized-governance-tool-suite-for-the-gnosis-safe-ea67eb95c34f) is a plugin that utilises [an oracle](http://reality.eth/) to ensure that before a multisig executes a transaction, that decision was indeed voted for by the community through signal voting. Requiring that transactions be verified this way prevents multisig signers from going rogue against the community’s wishes, as any transaction requires that an off-chain vote has passed for that transaction before it gets executed.

Gnosis [SafeSnap](https://blog.gnosis.pm/introducing-safesnap-the-first-in-a-decentralized-governance-tool-suite-for-the-gnosis-safe-ea67eb95c34f) module verifies that a transaction from a multisig has been passed on Snapshot signal voting

More recently, the Gnosis team has [announced Zodiac](https://gnosisguild.mirror.xyz/OuhG5s2X5uSVBx1EK4tKPhnUc91Wh9YM0fwSnC8UNcg) along with its [Reality module](https://gnosis.github.io/zodiac/docs/tutorial-module-reality/get-started/), which makes the above concept framework-agnostic. Not only can signal votes on Snapshot translate into a Safe transaction, _any_ off-chain event that can be reported to the oracle (Discord polls, Discourse votes…) could be used to trigger on-chain execution wherever the DAO lives.

Judiciary infrastructure creates an additional layer for checks and balances within the DAO, allowing working groups to execute optimistically whilst leaving room for the community to “challenge”, such that the working group is still held accountable to the DAO. [Kleros](https://kleros.io/) Court serves as a “Supreme Court” for DAOs that checks if a proposal is compatible with the DAO’s values, or verifies that approved budgets are being used as specified in the original proposal. [Tally](https://www.withtally.com/)’s [SafeGuard](https://github.com/withtally/safeguard) allows a quorum of token holders to revoke transactions initiated by the multisig or reclaim funds if it deems the signers took improper actions.

DAO judiciary tools

Comprehensive DAO frameworks have their own flavor of features to enforce checks and balances, for example, all Moloch proposals enter a Grace Period in which members can “[rage quit](https://medium.com/odyssy/moloch-primer-for-humans-9e6a4f258f78)” their shares if they disagree with a decision that has passed. [Colony](http://colony.io/) uses a reputation mechanism in which a member’s reputation can get slashed if the community deems them to have acted against the DAO’s interests.

**Treasury Management**

A DAO’s treasury is its lifeblood, which is why multisigs and treasury committees are ubiquitous across the ecosystem. DAO frameworks come with fund management solutions out-of-the-box (Moloch Guild Bank, DAO Stack Avatar), while [Gnosis Safe](https://gnosis-safe.io/) has established itself as the multisig of choice for DAOs looking for more lightweight solutions. In addition to this, DAOs have the entire stablecoin and DeFi ecosystem for diversifying its holdings, making risk-adjusted investments, and generating yield.

Challenges in DAO treasury management are now to provide more transparency into its asset allocation and spendings in order to assess performance and financial health. [Llama](https://llama.community/) offers a way to categorise fund inflow and outflow, linking spendings with its associated proposal where relevant.

[JAMM](https://www.jammpad.com/) Community Transaction Summary on [Llama](https://llama.community/)

[Parcel](https://parcel.money/) and [MultiSafe](https://multisafe.finance/) feature one-click mass payouts in ETH or ERC-20s based on csv imports, recurring payments, spending limits for members, as well as a dashboard that gives an overview of current asset allocations.

# **Frontend & Analytics**

Block explorers like [Etherscan](https://etherscan.io/) are an invaluable piece of infrastructure for crypto networks. They allow us to infer network traffic patterns, the nature of on-chain activity, and can even serve as crude frontends to interact with smart contracts.

**With the proliferation of DAOs also comes the need for human-readable DAO activity.** An “Etherscan for DAOs” would be a data aggregators and visualisation tools that provide insights into governance, spendings, and capture recent discussions in the DAO e.g. a big funding proposal or a contentious debate about how to vote in other protocols.

DAO Governance Frontends & Analytics Platforms

[Tally](https://www.withtally.com/) and [Boardroom](https://app.boardroom.info/) are governance frontends where members can go and vote on proposals, as well as look at voter profiles and governance activity. Eventually, we will have an “Etherscan for Governance” that reveals meaningful information like voter delegation relationships, qualitative data (why voters vote the way they did), and community sentiment on a particular proposal.

Voter delegation relationships reveal valuable insight into the social and political dynamics of a DAO. For example, a VC-funded DAO in which voting power is dominated by firms will have a different social dynamic than DAOs where individuals rally the community to delegate to them.

Top voters in [Gitcoin](https://www.withtally.com/governance/gitcoin) vs. [Compound](https://www.withtally.com/governance/compound)

[DeepDAO](https://www.deepdao.io/) is an DAO analytics platform which ranks DAOs across metrics such as voter participation, member size, and treasury holdings. It also looks at [individual DAO members](https://www.deepdao.io/#/people), surfacing who is most active in DAOs by membership, proposals created, and votes cast.

[DeepDAO](https://www.deepdao.io/#/people) ranking of top governance participants

Aggregate “DAO Scores” like these can serve as a data point for “protocol politicians” to refer to when putting their hat in the ring to become community leaders, such as a [Gitcoin Steward](https://gov.gitcoin.co/t/introducing-stewards-governance/41). Potential delegators can look at a candidate’s profile to see how they voted in the past, the initiatives they’ve taken, and other communities they have influence in.

# **Frameworks**

DAO Frameworks are a suite of smart contracts and interfaces that allow users to launch and operate an on-chain organization with a few clicks, providing out-of-the-box core features like fund management, membership management, and voting.

DAO Frameworks

Using these frameworks, DAO creators can configure parameters such as how long the voting period should be, the quorum needed for a proposal to pass, and existing members and their shares. Examples of frameworks and DAOs operating on them include [DAOStack](https://daostack.io/) (dxDAO, dOrg), [Colony](http://colony.io/) (ShapeShift), [Aragon](https://aragon.org/) (BrightID, PieDAO), and [Moloch](https://daohaus.club/) (The LAO, MetaCartel).

**As DAOs vary in needs and purposes, there is no one-size-fits-all solution to manage them.** With limited options available, early DAOs have had to mould themselves to fit rigid templates as opposed to having the freedom to put together a toolstack that best fits their needs.

Despite a rapidly growing tooling suite, it’s sometimes hard to integrate them with older frameworks, so communities have had to either live with that friction or make a large coordination effort to migrate to newer systems. Learning from the current limitations, the next generation of DAO frameworks (which include updated versions of earlier ones) focus on **modularity, flexibility, and extensibility**.

[Orca Protocol](https://www.orcaprotocol.org/) is designed around “pods” which is another name for working groups. Pods treated in a sense as a sub-DAO, with its own membership and governance. Individual pods can also then be “members” of the wider DAO.

[Tribute DAO](https://tributedao.com/) is an extensible version of the Moloch framework. On top of the core contracts are upgradeable adapters and extensions that can be added and removed at the DAO’s discretion.

[DAOHaus](https://daohaus.club/) have been a major driving force behind the proliferation of DAOs based on Moloch framework over the past year. In addition to being a frontend where individuals can deploy DAOs and vote on proposals, the platform also has a suite of add-ons (“Boosts”) that integrates DAO activity into external applications such as Discord, Discourse, and even Gnosis Safe for [arbitrary contract calls through proposals](https://daohaus.substack.com/p/-daohaus-adopts-zodiac-to-enable).

Boost Marketplace on [DAOHaus](https://daohaus.club/), which allows members to integrate on-chain activity with external services.

DAOHaus’ Discord plug-in notifies a channel whenever there is new activity on a proposal.

**Unlike the more monolithic, rigid first-generation frameworks, modular and composable tooling flexibly serves the ever-evolving needs of communities.**

Modularity allows DAOs to install plug-ins like [DAOHaus Boosts](https://daohaus.club/docs/boosts/) and Gnosis’ [Zodiac suite](https://gnosisguild.mirror.xyz/OuhG5s2X5uSVBx1EK4tKPhnUc91Wh9YM0fwSnC8UNcg) without needing to foresee the need for them when deploying the DAO. Open standards allow for anybody, as long as their code adheres to a shared interface, to build their own “expansion packs” as needs emerge within their own communities. Under this paradigm, the ecosystem of DAO plug-ins will grow akin to that of open source software packages. Adopting a new tool will be as simple as a few clicks on a frontend, or `npm install organization-lego` .

We are at the dawn of DAOs. Like DeFi and NFTs before it, the floodgates for innovation in decentralised organisation ops will open once we have the core primitives at our disposal.

Summary of DAO Structures & Tooling compared to traditional orgs. Note that this is a _very_ generalized depiction and should be taken with a grain of salt!

While DAO tooling aids our efforts to redesign organisations from first principles, we still need to iterate on best practices and learn through experimentation. Much of our mental models for organization design today is a legacy of assembly line-centric workplaces of the 20th century. Innovation around DAOs will also take unlearning outdated ideas of how human coordination can work. We should be careful not to blindly import what we are so used to from traditional organizations and retrofit them into the positive-sum ecosystems we are trying to create.

**Unlike its predecessors, the web3 organisational tool stack will accommodate many-to-many relationships, fluid participation, and crucially** _**ownership**_.

We’ll see more individuals splitting their time across multiple DAOs, leveraging various skills across different things they care about. A strategist for a DeFi protocol may lend her skills projecting the portfolio value in an NFT collector DAO, and support up and coming creators through a grants DAO. She will be able to port her (pseudo)identity and reputation to different applications, and point to the value she has created for the ecosystem as a whole.

Pioneers, builders, and some lucky individuals are living this future today. The projects mentioned in this article (and others I’m sure I’ve missed), are lowering barriers every day to make DAOs a viable path for the millions around the globe who are still excluded from opportunities afforded to a few.

If you’re working on DAO infrastructure or have feedback on this piece, please [reach out](https://twitter.com/nichanank)!