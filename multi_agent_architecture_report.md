# Multi-Agent Architecture & Framework Design — Full Record

> This document organizes the entire conversation by category, while preserving the original flow within each item. It includes every explanation, code block, structure diagram, and example scenario, without summarization.

---

## Table of Contents

- [A. Multi-Agent Patterns 20 — The Basics](#a-multi-agent-patterns-20--the-basics)
- [B. Who Built the Patterns and Why](#b-who-built-the-patterns-and-why)
- [C. Pattern-Related Careers and Learning Paths](#c-pattern-related-careers-and-learning-paths)
- [D. Concrete Swarm + Agent Examples](#d-concrete-swarm--agent-examples)
- [E. Academic Variant Patterns](#e-academic-variant-patterns)
- [F. Pattern Automation — Can an Agent Build the Structure?](#f-pattern-automation--can-an-agent-build-the-structure)
- [G. Why Implementation Is Hard + Why Evaluation Is Hard](#g-why-implementation-is-hard--why-evaluation-is-hard)
- [H. What Architectures Do Claude and Codex Use](#h-what-architectures-do-claude-and-codex-use)
- [I. Beyond Patterns — What Else You Need to Know](#i-beyond-patterns--what-else-you-need-to-know)
- [J. Complexity Visualization Methods + Corporate Processes](#j-complexity-visualization-methods--corporate-processes)
- [K. TutorAgent Structure Analysis](#k-tutoragent-structure-analysis)
- [L. Automation Design — Blackboard Conflict Prevention + Structure Reviewer](#l-automation-design--blackboard-conflict-prevention--structure-reviewer)
- [M. Pattern Combinations and Elimination](#m-pattern-combinations-and-elimination)
- [N. Cost vs Accuracy Tradeoff](#n-cost-vs-accuracy-tradeoff)
- [O. Architecture Review Should Always Be Rigorous](#o-architecture-review-should-always-be-rigorous)
- [P. Four Creative Design Methodologies](#p-four-creative-design-methodologies)
- [Q. Category Classification — From 7 to 14](#q-category-classification--from-7-to-14)
- [R. Feasibility of Implementing 14 Categories as Agents](#r-feasibility-of-implementing-14-categories-as-agents)
- [S. Will Agents 1-14 Fix Things Automatically? — Tier 1/2/3 Structure](#s-will-agents-1-14-fix-things-automatically--tier-123-structure)
- [T. General-Purpose Architecture Framework](#t-general-purpose-architecture-framework)
- [U. Building Jarvis with the Framework](#u-building-jarvis-with-the-framework)
- [V. Hallucination Defense](#v-hallucination-defense)
- [W. Hardcoded vs LLM Boundary](#w-hardcoded-vs-llm-boundary)
- [X. Concrete Method for Building 1-14](#x-concrete-method-for-building-1-14)
- [Y. Design Methodologies — Pseudocode, Interface-First, etc.](#y-design-methodologies--pseudocode-interface-first-etc)
- [Z. Seeing the Whole Picture — Dependency Tracking and Mental Organization](#z-seeing-the-whole-picture--dependency-tracking-and-mental-organization)

---

## A. Multi-Agent Patterns 20 — The Basics

> Question: "Are there more besides these?"

**Are there more?** Yes. Those 20 are the "frequently used ones," and academia has dozens more once variants are included. But for actual practice, those 20 cover most cases.

### Original Notes (user-authored, 20 patterns)

#### 1. Centralized — One in Command

**Sequential (pipeline)**
- Original purpose: needed step-by-step processing like a factory assembly line. Derives from the 1970s Pipe-and-Filter pattern.
- Current use: document processing, CI/CD pipelines, legal contract generation
- Pros: easy to debug. After A, B; predictable
- Cons: if an earlier stage blocks, the whole thing stops. No parallelism
- Real example: when a law firm produces contracts — 4 AIs process in order: template selection → clause editing → regulatory review → risk assessment

**Orchestrator-Worker**
- Original purpose: in distributed computing, for a master to dispatch work. Evolved from MapReduce.
- Current use: Kafka-based event processing, large-scale data pipelines
- Pros: scales by adding workers. Worker death is recoverable via restart
- Cons: orchestrator is the bottleneck. Single point of failure
- Real example: Confluent's Kafka implementation — orchestrator distributes work across partitions, worker groups pull and process

**Master-Slave**
- Original purpose: 1980s parallel computing. Now almost identical to Orchestrator-Worker
- Current use: database replication, Redis clusters
- Pros: simple
- Cons: if master dies, everything halts

#### 2. Hierarchical — Top-Down Organization

**Hierarchical Agent**
- Original purpose: to break down complex problems. Modeled on military organizations and corporate structures
- Current use: power grid management, oil field operations, factory automation
- Pros: manages large problems. Preserves local autonomy
- Cons: gets slow as hierarchy deepens. Top tier is the bottleneck
- Real example: in power grids, a top-level agent forecasts demand while lower agents control individual plants. Oil fields split into production / maintenance / supply levels

**Holonic**
- Original purpose: 1990s manufacturing. Based on Koestler's "holon" concept — both a whole and a part
- Current use: smart factories, microgrids, traffic simulations
- Pros: high autonomy even within a hierarchy. Flexible
- Cons: complex design. Holons can conflict
- Real example: the TELETRUCK traffic system — each truck is independent yet part of a fleet. Validated in an AAAI paper

**Layered (temporal hierarchy)**
- Original purpose: real-time control. Upper layers plan slowly, lower layers react quickly
- Current use: robot control, autonomous driving
- Pros: long-term planning and immediate response simultaneously
- Cons: synchronization between layers is hard

#### 3. Distributed — All Equal

**Peer-to-Peer**
- Original purpose: Napster, BitTorrent. No central server
- Current use: blockchain, distributed storage
- Pros: fault-tolerant. Easy to scale
- Cons: hard to know overall state. Security is complex

**Heterarchical**
- Original purpose: modeled on biological neural networks. Leadership only when needed
- Current use: drone swarms, disaster response robots
- Pros: no bottleneck. Adapts quickly
- Cons: can be chaotic. Needs consensus mechanism

**Gossip Protocol**
- Original purpose: 1980s database synchronization. Spreads like rumors
- Current use: Cassandra, Bitcoin, AWS internals
- Pros: synchronizes without a center. Extremely fault-tolerant
- Cons: takes time to reach eventual consistency. Many duplicate messages
- Real example: a 2025 paper proposed applying it to LLM agents — combined with structured protocols to achieve emergent coordination

**Publish-Subscribe**
- Original purpose: 1990s message queues. Loose coupling
- Current use: Kafka, MQTT, IoT
- Pros: publishers and subscribers don't know each other. Best for scaling
- Cons: hard to guarantee message ordering

#### 4. Shared Space — Write and Read from a Blackboard

**Blackboard**
- Original purpose: 1970s AI. Hearsay-II speech recognition. Experts collaborated by looking at a blackboard
- Current use: complex diagnostic systems, design tools
- Pros: no direct agent-to-agent communication needed. Flexible
- Cons: the blackboard is the bottleneck. Simultaneous write conflicts
- Real example: Confluent uses Kafka topics as a blackboard — agents produce/consume events

**Tuple Space (Linda)**
- Original purpose: 1980s parallel programming. Shared memory abstraction
- Current use: JavaSpaces, distributed computing
- Pros: simple API (out, in, read)
- Cons: limited scalability

**Stigmergy**
- Original purpose: from research on ants and bees. Indirect collaboration through environmental traces
- Current use: robot swarms, Wikipedia, open-source development
- Pros: complex behavior without central control. Infinite scaling
- Cons: hard to predict. Optimization takes a long time
- Real example: ant nest building, Wikipedia editing. Environmental traces guide other agents' behavior. A 2024 Nature paper applied auto-design to robot swarms

#### 5. Market/Negotiation — Bid and Trade

**Market-Based**
- Original purpose: economics. Efficient resource allocation
- Current use: power trading, cloud spot instances, stock markets
- Pros: optimal allocation. Auto-substitution on failure
- Cons: complex implementation. Bidding overhead
- Real example: stock exchanges implemented on Kafka — agents post orders to bid/ask topics, matching happens there

**Contract Net Protocol**
- Original purpose: 1980s distributed AI. Proposed by Smith
- Current use: logistics, manufacturing scheduling, satellite operations
- Pros: dynamic allocation. Flexible
- Cons: negotiation takes time
- Real example: NASA unmanned satellite operations — "who can do this?" → "I can" → contract

**Auction**
- Original purpose: resource allocation. A special case of Market-Based
- Current use: ad bidding, 5G spectrum allocation
- Pros: fair
- Cons: collusion possible

#### 6. Cooperative — Discuss Together

**Group Chat (round table)**
- Original purpose: modeled on human meetings. Reaching consensus
- Current use: city planning, content review, brainstorming
- Pros: diverse perspectives. Transparency
- Cons: hard to control with more than 3. Infinite loops
- Real example: park development proposal review — community, environment, and budget agents debate

**Concurrent (parallel)**
- Original purpose: time savings. Multiple perspectives on the same problem
- Current use: stock analysis, medical diagnosis
- Pros: fast. Comprehensive
- Cons: needs conflict resolution. Uses many resources
- Real example: stock valuation — fundamental, technical, sentiment, and ESG analysis run concurrently across 4 agents

**Voting/Consensus**
- Original purpose: democracy. Fault tolerance
- Current use: blockchain, distributed databases
- Pros: high reliability
- Cons: slow. Requires majority

**Swarm Intelligence**
- Original purpose: research on flocks of birds and schools of fish. Named by Beni in 1989
- Current use: optimization, routing, drone swarms
- Pros: complex behavior from simple rules. Best scalability
- Cons: no guarantee of optimality. Hard to tune
- Real example: a 2025 paper — LLM deployment optimized as a swarm in edge-cloud

#### 7. Dynamic Planning — Adapt to the Situation

**Handoff**
- Original purpose: call centers. Passing to a specialist
- Current use: helpdesks, medical triage
- Pros: assigns the right specialist
- Cons: infinite handoff loops possible
- Real example: telecom CRM — triage agent → technical agent → finance agent

**Magentic (dynamic planning)**
- Original purpose: 2020s. Problems where the plan isn't predetermined
- Current use: SRE automation, research workflows
- Pros: flexible. Plan can be modified
- Cons: slow. No guarantee of convergence
- Real example: site incident response — manager agent continually modifies plan based on diagnostic results

#### 8. Learning — Accumulating Experience

**Federated Learning**
- Original purpose: 2016, Google. Learning while preserving privacy
- Current use: smartphone keyboards, medical AI, UAV swarms
- Pros: no central data needed. Privacy preserving
- Cons: communication cost. Model bias
- Real example: unmanned maritime vessels — 95.4% success rate, 23.5% improvement over independent models. BA-FRL reduced communication by 43%

**BDI (Beliefs-Desires-Intentions)**
- Original purpose: 1980s philosophy. Imitates human reasoning
- Current use: game AI, robots, simulations
- Pros: easy to understand. Goal-oriented
- Cons: slow in complex environments

**Actor Model**
- Original purpose: 1973, Hewitt. Concurrency theory
- Current use: Erlang, Akka, foundation of distributed systems
- Pros: fault isolation. Scalability
- Cons: hard to debug

### Core Summary — When to Use Which

| Situation | Pattern | Reason |
|---|---|---|
| Clear stages | Sequential | Predictable |
| Needs scaling | Orchestrator-Worker | Add workers |
| Complex organization | Hierarchical | Easy to manage |
| Avoid centralization | Peer-to-Peer, Gossip | Fault-tolerant |
| Indirect cooperation | Stigmergy, Blackboard | Loose coupling |
| Resource competition | Market-Based, Contract Net | Efficient allocation |
| Diverse opinions | Group Chat, Concurrent | Comprehensive |
| Plan unknown | Magentic | Flexible |
| Privacy critical | Federated | Local learning |

### References

**Books**
- Wooldridge "An Introduction to MultiAgent Systems" — introductory
- Shoham "Multiagent Systems" — game theory
- Ferber "Multi-Agent Systems" — classic patterns

**Papers**
- arXiv 2508.12683 — hierarchical taxonomy with 5-axis classification
- Confluent "Four Design Patterns" — Kafka implementation
- Wikipedia MAS — basic concepts

**Frameworks**
- JADE — FIPA standard
- SPADE — Python
- JaCaMo — BDI + organization

---

## B. Who Built the Patterns and Why

> Question: "I don't know the background — who were the people who made these things? AI didn't exist back then, so why did they build them?"

**Who built them?** Not AI researchers. Mostly:

- **Software engineers** — people running thousands of servers (Gossip, Pub-Sub, Actor Model)
- **Manufacturing / industrial engineers** — people automating factories (Holonic, Contract Net)
- **Military / aerospace** — people at NASA and the Department of Defense controlling satellites and drones
- **Economists** — market simulations (Market-Based, Auction)
- **Biologists** — people observing ant and bird colonies (Stigmergy, Swarm)
- **Philosophers** — BDI literally came from human decision-making theory

**Why when AI didn't exist?** Here, "agent" doesn't mean LLM. **Anything that's "an independent unit that decides and acts"** is an agent. A server process is an agent. A factory robot arm is an agent. A single drone is an agent. These people always had the same problem — **"if I have several independent things, how do I make them work together?"** That problem has existed since the 1970s. LLMs are just the most recent type of agent.

**Do I really need to learn them?** As an analogy — can you build a building without knowing what "columns and beams" are? You can. But once you add a second floor, it'll collapse. These patterns are like **structural engineering** for buildings. When Jarvis has 3-4 agents, gut feel works. But once it exceeds 10, or needs to react in real time, or has many users — gut feel fails and you need structure.

**What can you actually do once you know them?** In practice:

1. **When designing** — you immediately judge "this problem fits Sequential" vs "this is more of a Blackboard situation"
2. **When debugging** — if agents tangle, you can look at the structure and find where the problem is
3. **When scaling** — designing for scale from the start reduces the need to rip things apart later
4. **When reading someone else's system** — CrewAI, AutoGen, LangGraph are all combinations of these patterns. Once you know patterns, framework docs become readable instantly

But going through all 20 at this stage is overkill. Deeply understand the 3 you'll use directly in Jarvis (Hierarchical, Blackboard, Handoff). For the rest, "ah, this kind of thing exists" is enough. When you actually need them, dig deep then.

---

## C. Pattern-Related Careers and Learning Paths

> Question: "Where do people who study this learn? Schools don't seem to teach it."

It's normal that schools don't teach it. It's not a single subject — it's scattered across many fields.

**Universities do teach it, but under different names:**

- In CS, you learn Gossip, Pub-Sub, Actor Model in "Distributed Systems" courses
- In AI, some schools have a separate "Multi-Agent Systems" course — but it's graduate-level, rarely undergraduate
- In industrial engineering, you learn Holonic and Contract Net in "Manufacturing Systems" courses
- In economics, you learn Auction and Market-Based in "Mechanism Design"
- In robotics, you learn Stigmergy and Swarm in "Swarm Robotics" courses

So no single person has learned all 20 patterns in one place. People in each field built them to solve their own problems, and someone later went "oh, these are all similar problems" and gathered them.

**The actual paths people take to learn:**

1. **Bumping into them in industry** — most common. Building a system that doesn't work, looking it up, and going "ah, this pattern existed"
2. **Papers** — academics learn from arXiv and AAMAS (conference) papers
3. **Reading open source** — Kafka source shows you Pub-Sub, Erlang/OTP shows you the Actor Model
4. **Books** — Wooldridge's book is essentially the only textbook that "puts it all in one place"

Because of the LLM agent boom, this is finally being taught "in one place" — through DeepLearning.ai courses or LangChain docs. But there's still almost no systematic organization.

> Question: "What jobs do this kind of work?"

There are roughly three tracks:

**1. Distributed systems engineers** — highest demand. People at Netflix, Uber, Spotify who make hundreds to thousands of servers work together. Operate Kafka, design microservices. They use Pub-Sub, Gossip, Orchestrator-Worker every day. Pay is at the high end.

**2. AI/ML engineers (agent-focused)** — exploding right now. People at OpenAI, Anthropic, and various startups building LLM agent systems. Use AutoGen, CrewAI, LangGraph or build their own. They use Hierarchical, Blackboard, Handoff, Group Chat.

**3. Industrial automation / robotics** — factories, logistics, drones, autonomous driving. People at Bosch, Amazon Robotics, DJI coordinating multiple robots. Use Swarm, Holonic, Contract Net.

**There are also:**
- Blockchain protocol developers (Gossip, Consensus)
- Game AI developers (BDI, Swarm)
- Financial quants (Market-Based, Auction)
- Senior-level SRE/DevOps (incident response automation)

Honestly, almost no one "knows all of them." Most people know 3-5 deeply within one track.

---

## D. Concrete Swarm + Agent Examples

> Question: "If you use swarm with agents, what kind of thing are you actually building?"

**The core idea of swarm:** each agent can be stupid. As long as everyone follows a few simple rules, the whole behaves intelligently. No central commander.

**Things people actually build:**

**Logistics delivery optimization** — places like Coupang or Amazon. You have 500 delivery trucks. Computing all 500 routes centrally is too slow. Instead, give each truck-agent a few rules — "go to the nearest place first," "avoid places another truck is heading to," "reroute if traffic is bad." That alone gets the whole delivery system to optimize itself.

**Drone swarms** — say 20 agricultural drones spray pesticide on a field. Give each drone "go to where it hasn't been sprayed," "stay 10m from adjacent drones," "return when battery is low" — those three lines and 20 drones cover the entire field without overlapping. If one fails, the others fill in.

**Using with LLM agents?**

- **Code review swarm** — 10 agents look at the code from different angles. Security, performance, readability, tests. No central orchestrator. Each follows "if you see a problem, leave a comment." When comments overlap, the important issues naturally surface.

- **Information gathering swarm** — when asked "research the AI semiconductor market," multiple agents search different sources. When one agent finds a keyword and posts it to a shared space, another agent sees that and digs deeper. Same principle as ants leaving pheromones. This is the point where Stigmergy joins in.

- **OpenAI Swarm framework** — the name itself is Swarm. Lightweight agents collaborate through handoff. Strictly speaking, it's closer to handoff than true swarm, but it borrows the concept.

**Honest take** — LLM agent swarms are still in research. Reason: LLM calls are expensive and slow, so running hundreds like ants is practically too costly. Once local models get faster and cheaper, real swarms will become possible. Local 7-10B models are heading that way.

---

## E. Academic Variant Patterns

> Question: "What about academic variants?"

**Orchestrator-Worker variants:**
- **Coalition Formation** — workers form their own teams. "Let's do this task together" creates dynamic groups that appear and dissolve. Heavily studied in military operation simulations
- **Team Formation** — similar to Coalition, but focused on building optimal teams based on capability. Problems like "this project needs 1 front-end and 2 back-end engineers"

**Contract Net variants:**
- **Iterated Contract Net** — multi-round negotiation that doesn't end in one shot. "That price is a bit…" "How about this?" repeated
- **Leveled Commitment** — you sign the contract but can break it for a penalty if a better option comes. Just like real-world contracts

**Voting/Consensus variants:**
- **Byzantine Fault Tolerance (BFT)** — reach consensus even with malicious participants. Core to blockchain
- **Raft, Paxos** — concrete algorithms for leader election and consensus in distributed DBs. etcd, CockroachDB use Raft

**Swarm variants:**
- **Ant Colony Optimization (ACO)** — pheromone mimicry. Specialized for path optimization
- **Particle Swarm Optimization (PSO)** — bird-flock mimicry. Widely used for parameter tuning
- **Artificial Bee Colony (ABC)** — bee mimicry. Splits roles into scout, worker, observer bees

**BDI variants:**
- **BOID** — adds Obligation to BDI. Handles "I want to but the rules don't allow it" type conflicts
- **Normative Agent** — embeds social norms into the agent. Behavior like "everyone else does it, so I do too"

**Hierarchical variants:**
- **Organization-Based (MOISE+)** — explicitly defines roles, groups, missions. Feels like porting a company org chart to code
- **Institution-Based** — mimics legal/rule systems. Agents recognize "in this space, I must follow these rules"

**Completely different lineages:**
- **Mediator Pattern** — similar to Orchestrator, but the mediator doesn't make decisions, only routes messages. Lightweight
- **Broker Pattern** — only matches services. Role of "find me an agent that can do this work"
- **Reputation-Based** — agents rate each other's reputation. Low-reputation agents don't get work. Same principle as eBay reviews

The reason there are so many patterns is simple — each field bent existing patterns slightly to fit its problems. The fundamental principles all fit within the 20, and the variants are tuning for specific situations.

---

## F. Pattern Automation — Can an Agent Build the Structure?

> Question: "Could you automate giving an agent these patterns to learn, then have it build a structure when given a task?"

Possible. And already being researched.

**What works today:**

If you give an LLM those patterns as a system prompt or knowledge base and say "design a structure for this problem," it picks pretty well.

Things actually heading in this direction:

**1. AutoGen (Microsoft)** — agents converse and create the agents they need dynamically. "This task needs a coder" → creates a coder agent. An early form of determining structure at runtime.

**2. CrewAI** — give it role, goal, backstory and it builds collaboration structures. But humans still set the roles.

**3. CAMEL** — two agents negotiate roles and split work themselves. "You research, I'll code."

**4. MetaGPT** — say "build me software" and it automatically assigns PM, architect, developer, QA roles and builds Sequential + Hierarchical structure itself.

**But the honest reality:**

"Picking patterns automatically and building structures fully autonomously" is still semi-automatic. Reasons:

- **Pattern selection itself is easy** — LLMs do "this problem fits this pattern" well
- **Actual implementation is hard** — picking a pattern isn't the end. Error handling, timeouts, retries, monitoring — engineering is 90% of the work. This is what isn't automated yet
- **Evaluation is hard** — automatically judging whether the built structure is good or bad is hard

**Realistic version:** put 20 patterns into a knowledge file, and have the Orchestrator "reference this pattern list and propose structures when adding new features." Agent proposes, human approves, then execute. That's the most practical version at this stage.

---

## G. Why Implementation Is Hard + Why Evaluation Is Hard

> Question: "Why is implementation hard and why is evaluation hard?"

### Why Implementation Is Hard

Picking a pattern is like deciding "let's build a two-story house." But to actually build it:

**What if an agent dies?** — A worker agent doesn't respond. How many seconds for timeout? How many retries? Hand it to another agent? What if that one dies too? This judgment depends on the situation. Numbers like "3-second timeout, 2 retries" can't be set without domain experience. Too short and you mark a healthy agent as dead; too long and the whole thing freezes.

**What if message order gets tangled?** — Agent A sends "start the task" to B, then sends "actually, cancel" right after. But due to network conditions, "cancel" arrives first. B goes "cancel what?" There are hundreds of edge cases like this. Pattern docs don't mention them.

**State management** — what if 5 agents modify the same data simultaneously? Say you use the Blackboard pattern. When two agents write to the blackboard at the same time, who wins? Locking slows things down, not locking corrupts data. This is a 40-year-old problem in distributed systems and there's still no clean answer. Trade-offs are decided situationally by humans.

**Resource management** — every LLM agent call costs money. Running 20 agents concurrently as a swarm can cost several dollars per run. Automatically judging "this task needs 3, but ran 20" is hard.

In short — patterns are "what to do," and implementation is "what to do when it goes wrong." There are too many failure cases, and the right answer differs by domain, which is why automation breaks down.

### Why Evaluation Is Hard

**Criteria conflict.** Is fast good? Cheap? Accurate? A medical diagnosis agent should be slow but accurate. A delivery agent should be slightly wrong but fast. You can't auto-set this priority — it's a business judgment.

**No comparison baseline.** To compare a Sequential version vs Concurrent version, you have to build both and run them. But just building each takes days to weeks.

**Long-term performance is unknown.** Works fine now, but with 10× users? 100× data? You don't know until you run it.

**LLM-specific issues** — the same prompt to the same model returns different answers each time. Agent A's judgment is non-deterministic. So you end up doing statistical evaluation like "10 runs, 7 succeed — is this a good structure?" But who decides the threshold is another problem.

---

## H. What Architectures Do Claude and Codex Use

> Question: "So what structures does Claude use, and what does Codex use?"

Neither fully discloses their internal architecture. But it's inferrable from public information.

### Claude (Anthropic)

- Claude Code uses a **subagent structure** — each subagent runs independently in its own context window, with a custom system prompt, specific tool access, and independent permissions. → **Orchestrator-Worker** pattern.

- For long-running agents, the **initializer agent sets up the environment** and the **coding agent makes incremental progress each session** — a 2-stage structure. → **Sequential**

- The initializer agent writes 200+ feature requirements into a file, and subsequent coding agents work by reading them. → **Blackboard**

- Claude Managed Agents are session-based — users send messages as events, and Claude autonomously executes tools and streams results. → Orchestrator-Worker variant

### Codex (OpenAI)

- The Codex agent runs inside a **secure isolated cloud container**. Base structure is **single agent + sandbox**. Not so much multi-agent as one strong agent running a tool loop.

- The Codex CLI manages interactions among user, language model, and tools as an iterative process. → Classic **Sequential agent loop** (think → run tool → check result → think again)

- At DevDay they ran 3-4 completely independent tasks concurrently. → **Concurrent** pattern

- OpenAI has stated it's still uncertain whether one general-purpose coding agent is best in all contexts, or whether multi-agent is better. So OpenAI is still experimenting too.

### Comparison Summary

| | Claude | Codex |
|---|---|---|
| Base structure | Orchestrator-Worker + Subagent | Single agent + tool loop |
| Collaboration | Blackboard (shared files) | None (independent sandbox) |
| Parallelism | Subagent forking possible | Task-level parallelism (each independent) |
| Long-running | Initializer → coder Sequential | Continues via context compaction |
| Philosophy | Multiple agents split roles and collaborate | One strong agent does everything |

---

## I. Beyond Patterns — What Else You Need to Know

> Question: "Besides those structures, what else should I know? Will knowing those make building my own agent much better?"

Patterns are the "skeleton." Just a skeleton doesn't run. The things you actually run into when building agents:

**1. Prompt Engineering / System Design** — how do you define the agent's role? It's not "you are a code reviewer" in one line. You have to design how it judges in different situations, what to do when it doesn't know, what to do when it fails. ETHOS.md is this.

**2. State Management** — what does the agent remember and what does it forget? Context window limits, memory storage, conversation history management.

**3. Tool Design** — what tools do you give the agent? Too many tools cause confusion; too few prevent capability. How clearly you define tool I/O directly affects agent performance.

**4. Evaluation / Guardrails** — how do you catch agent mistakes? The 3-Strike system is already a guardrail.

**5. Observability** — can humans see what the agent is doing? Logs, tracing, monitoring.

**Does knowing those help much?** Honestly — **"memorizing patterns" doesn't help much; "having judgment criteria" does.** Memorizing all 20 patterns is meaningless if you can't judge "what fits my problem?"

---

## J. Complexity Visualization Methods + Corporate Processes

> Derived explanation from questions

### Visualization Methods

**Architecture Diagram (C4 Model)** — the most universal. Draw the system at 4 zoom levels:
- Level 1: the whole system (a few boxes)
- Level 2: containers (servers, DBs, apps)
- Level 3: components (modules, classes)
- Level 4: code level

**Sequence Diagram** — order of messages between agents. "A requests B → B delegates to C → C returns result → B delivers to A" — visualizes this. Most useful when debugging.

**State Machine Diagram** — state transitions of an agent. Flows like "waiting → working → done → waiting."

**DAG (Directed Acyclic Graph)** — task dependencies. "This can only start after that finishes." LangGraph is built on this.

**Event Storming** — workshop using sticky notes on a wall. Visualizes "when this event happens → this command runs → this state changes." Domain experts and developers do it together.

### Corporate Processes

**Architect** — 1-2 senior engineers determine overall structure. Big decisions like "our system goes with Orchestrator-Worker." This person needs to know the most patterns. Usually 10+ years experience.

**Domain experts** — only know their field's patterns deeply. Infra team knows Gossip and Pub-Sub well. ML team knows Federated Learning well. Each only knows the others' patterns by name.

**ADR (Architecture Decision Record)** — documenting why a pattern was chosen. "Why we picked Orchestrator-Worker over Market-Based: …" So new joiners can read and understand. ETHOS.md actually plays this role.

**Design Review** — before architecture decisions, the team gathers around a diagram and debates. "Won't this structure cause a bottleneck here?" Multiple perspectives validate rather than one person deciding everything.

---

## K. TutorAgent Structure Analysis

> Question: "Let's try it. Propose a structure for https://github.com/mattheogim/TutorAgent"

### Patterns TutorAgent Currently Uses

| Pattern | Where Used | Working Well? |
|---|---|---|
| **Orchestrator-Worker** | CLAUDE.md is the orchestrator, 10 skills + 7 agents are workers | ✅ Core structure. Well established |
| **Sequential** | practice-notes: tutor → quiz → questions order | ✅ Matches the learning flow |
| **Blackboard** | Disk files (error_notes.md, knowledge_graph.json, meta_index.json) — shared spaces agents read/write | ✅ Core of the system. Working well |
| **Handoff** | end-session writes handoff.md, next session picks up | ✅ Appropriate for overcoming context window limits |
| **Layered** | hooks (immediate response) / skills (intermediate logic) / agents (background analysis), 3 layers | ✅ Might not have been intentional, but happened naturally |

### 3 Structural Improvement Points

**1. Blackboard conflict potential**

Multiple agents may touch error_notes.md, knowledge_graph.json, meta_index.json simultaneously. Since only one user is writing now, no problem occurs, but structurally it's a weak point.

→ **Proposal**: Define write order explicitly. Add rules to ETHOS.md like "only practice-questions skill can write to error_notes.md; error-analyzer is read-only."

**2. Agent dependencies are implicit**

→ **Proposal**: Create a DAG:
```
input-processing → note-organization → tutor → practice-questions
                                                      ↓
                                              error-analyzer
                                                      ↓
                                                exam-coach
```

**3. GC Agent does too much**

A 1,094-line GC agent runs all 10 health checks.

→ **Proposal**: Group the 10 health checks by category so they're easy to split later. 3 schema-related, 3 session-related, 4 file integrity.

### What Not to Touch

- ETHOS.md / CLAUDE.md structure — playing the ADR role well
- Hook system — Layered pattern works naturally
- Handoff.md — appropriate solution for session continuity
- Model cost optimization (Haiku/Sonnet/Opus) — already well partitioned

---

## L. Automation Design — Blackboard Conflict Prevention + Structure Reviewer

> Question: "What about an agent that prevents Blackboard conflicts based on my structure, and another agent that catches structural contradictions when something changes... what about that kind of thing?"

### #1: Blackboard Conflict Prevention — a hook is right, not an agent

Conflict prevention isn't "judgment," it's "rule enforcement." If you make it an agent, every write triggers an LLM call — slow, expensive, unnecessary.

```
write-access-control.ts (PreToolUse - Write)
├── read write_permissions.json
│   {
│     "error_notes.md": ["practice-questions"],
│     "knowledge_graph.json": ["tutor", "note-scanner"],
│     "meta_index.json": ["input-processing", "note-organization"],
│     "analytics/*.jsonl": ["session-lifecycle"]
│   }
├── check current active skill/agent
├── if not in allow list → block write + log
└── if allowed → pass through
```

### #2: Structure Reviewer Agent — refining

```
structure-reviewer/ (agent)
├── model: sonnet
├── inputs:
│   ├── proposed_plan.md       ← proposed change
│   ├── current_architecture.md ← description of current structure
│   └── review_checklist.md    ← validation criteria
│
├── review_checklist.md contents:
│   ├── 1. Blackboard conflict: does the new feature collide with existing file write permissions?
│   ├── 2. Dependencies: does the DAG get a cycle?
│   ├── 3. Single point of failure: any spots that halt the whole if they die?
│   ├── 4. Cost: how many LLM calls does the new agent add?
│   ├── 5. ETHOS violations: anything that breaks principles P1-P6?
│   └── 6. Conflict with existing hooks/agents: does it break existing flows?
│
├── loop_logic:
│   ├── round 1: identify problems against the checklist
│   ├── round 2: propose improvements
│   ├── round 3: re-validate improvements against the checklist
│   ├── round 4: final summary + ADR draft
│   ├── convergence: 0 new issues in round N → early termination
│   └── if more than 4 rounds needed → "N issues still remaining. Continue?"
│
└── outputs:
    ├── review_result.md       ← pros/cons + final recommendation
    ├── adr_draft.md           ← record of "why this structure was chosen"
    └── save to memory         ← summary of key decisions
```

**Honest advice:** Build #1 (hook) first. Takes 30 minutes. For #2, start by writing review_checklist.md.

---

## M. Pattern Combinations and Elimination

> Question: "Was there a reason you chose those patterns from 20+?"

### Elimination Criteria: 3 Constraint Filters

**Constraint 1: Solo use** — distributed group entirely eliminated
- ~~Peer-to-Peer~~ — only meaningful with multiple equally participating nodes
- ~~Gossip Protocol~~ — for syncing tens to hundreds of nodes
- ~~Heterarchical~~ — situation-dependent leadership without leader is unmanageable for one user
- ~~Federated Learning~~ — meaningless with one user

**Constraint 2: Minimize LLM cost** — high-call patterns eliminated
- ~~Swarm Intelligence~~ — tens of agents = cost explosion
- ~~Group Chat~~ — unpredictable turn count = unpredictable cost
- ~~Market-Based~~ — every bidding round, every agent calls LLM
- ~~Auction~~ — same reason

**Constraint 3: Claude Code infrastructure** — patterns needing runtime eliminated
- ~~Actor Model~~ — needs message-passing runtime like Erlang/Akka
- ~~Tuple Space~~ — needs shared memory abstraction runtime
- ~~BDI~~ — needs Beliefs-Desires-Intentions engine. Too heavy

### Why the Survivors Were Chosen

| Pattern | Why Chosen |
|---|---|
| **Stigmergy** | write_log.jsonl = just adding one file. 0 LLM calls. Best value |
| **Pub-Sub** | event_queue.jsonl = one more file. Also 0 LLM calls. Add later |
| **Contract Net** | splitting sub-reviewers across haiku/sonnet saves cost |
| **Concurrent** | Claude Code supports subagent parallelism. Infrastructure is there |
| **Voting** | combining 4 results is a few if-statements. No extra LLM calls |
| **Magentic** | the loop structure works on the same principle as the 3-Strike system. Familiar |

### Combined Pattern Architecture

```
┌─────────────────────────────────────────────┐
│           Structure Reviewer                 │
│         (Orchestrator + Contract Net)        │
├─────────────────────────────────────────────┤
│  Round 1-3: parallel validation (Concurrent) │
│  ┌──────────┬──────────┬──────────┬────────┐│
│  │ ethos    │dependency│  cost    │conflict││
│  │(haiku)   │(sonnet)  │(haiku)   │(sonnet)││
│  └────┬─────┴────┬─────┴────┬─────┴───┬────┘│
│       └──────────┴──────────┴─────────┘      │
│                    ↓                         │
│           Voting (3/4 consensus)              │
│                    ↓                         │
│  Round 4: write ADR + save to memory         │
├─────────────────────────────────────────────┤
│  Write Access Hook (Stigmergy)               │
│  write_log.jsonl ← record every decision     │
│  → can reference past decisions next review  │
└─────────────────────────────────────────────┘
```

Patterns used: **Contract Net** (role assignment) + **Concurrent** (parallel execution) + **Voting** (consensus) + **Magentic** (loop) + **Stigmergy** (indirect coordination via write_log) + **Blackboard** (shared files)

### Stigmergy More Detail

The hook logs every write to `write_log.jsonl`:

```jsonl
{"file": "error_notes.md", "writer": "practice-questions", "action": "append", "timestamp": "...", "size_delta": "+342"}
{"file": "knowledge_graph.json", "writer": "tutor", "action": "update", "timestamp": "...", "nodes_added": 3}
```

This lets exam-coach reason "error_notes.md was updated 5 minutes ago → let's plan strategy with the latest data." Ant pheromones — agents don't talk directly, but the traces left in the environment coordinate them indirectly.

### Pub-Sub Concept

```
write-access-control.ts
├── permission check (existing)
├── if allowed → log to write_log.jsonl (Stigmergy)
└── if allowed → publish event to event_queue.jsonl (Pub-Sub)
    {"event": "file_changed", "file": "error_notes.md", "subscribers": ["error-analyzer", "exam-coach"]}
```

Overkill right now. Just adding write_log.jsonl is enough.

### Implementation Order

| Step | What to Do | Difficulty |
|---|---|---|
| 1 | write-access hook + write_log.jsonl | Easy — 30 min |
| 2 | write review_checklist.md | Easy — 1 hour |
| 3 | Structure Reviewer agent single version (1 sonnet covers all 6 items) | Medium — half day |
| 4 | split into 4 sub-reviewers (Contract Net) | Medium — half day |
| 5 | add parallel execution + Voting | Hard — 1 day |
| 6 | integrate Stigmergy (reference past reviews) | Easy — 1 hour |

Up to step 3 is already plenty useful.

---

## N. Cost vs Accuracy Tradeoff

> Question: "If you don't minimize LLM cost? Does it get faster and more accurate?"

**Accuracy goes up, but you can't claim it's faster.**

### What Comes Back When Cost Is Unlocked

**Group Chat** — sub-reviewers debate freely. Cross-validation. Voting's 2:2 deadlock resolved by debate.

**Swarm** — increase reviewers to 10-15 for fine-grained perspectives. Coverage improves.

**Market-Based** — sub-reviewers bid based on confidence. The most confident agent takes it, improving quality.

### But Speed Doesn't Improve

| Structure | Current (cost minimized) | Cost unlimited |
|---|---|---|
| Concurrent 4 + Voting | ~30 sec (parallel) | ~30 sec (same) |
| Group Chat 4, 3-round debate | — | ~3 min |
| Swarm 15 | — | ~2 min |
| Market-Based bidding | — | ~1 min |

More LLM calls means network latency × call count. Spending more doesn't physically make it faster.

---

## O. Architecture Review Should Always Be Rigorous

> Question: "But normally architecture review should be safe, rigorous, and thorough, right?"

Right. Doing architecture review "lightly to save cost" misses the point.

**Structural decisions are the most expensive to reverse.** Get a line of code wrong and you fix it in 5 minutes. Pick the wrong pattern and you tear the whole thing apart.

Not Light/Deep — split into **completely separate processes**:

```
Code Review (feature additions, bug fixes)
├── light, fast
└── only changes that don't touch structure

Architecture Review (structural changes)
├── always rigorous
├── all 4 sub-reviewers
├── Group Chat cross-validation
├── full 4-round loop
└── anything that touches structure goes here
```

At companies, Code Review and Design Review are completely separate processes too.

---

## P. Four Creative Design Methodologies

> Question: "You used elimination, but what about designing creatively, thinking through scenarios?"

Elimination is "what to take out"; creative design is "what can be built."

### Limits of Elimination

Since you're only subtracting from the 20, **combinations that didn't exist before will never come out.**

### Method 1: Adversarial Design — Deliberately Break It

Start from **"how would you make this system fail?"**

```
Red Team Agent (opus)
├── Input: proposed structure
├── Mission: "Create 5 scenarios that could make this structure fail"
│
│   "What if error-analyzer goes into an infinite loop?"
│   "What if knowledge_graph.json exceeds 10MB?"
│   "What if the user gets 500 wrong in one session?"
│   "What if 2 hooks hit the same file simultaneously?"
│   "What if handoff.md gets corrupted?"
│
└── Output: failure scenarios + which pattern defends against each
```

Netflix's Chaos Monkey is this — randomly killing production servers to test if the system survives.

### Method 2: Evolutionary Design — Evolve It

Cross-breed scenarios:

```
Round 1: generate 5 scenarios
Round 2: select top 2 (by fitness)
Round 3: create 2 child scenarios combining strengths of the 2
Round 4: select top 2 from children + parents
Round 5: repeat
```

Genetic Algorithm. But more practical for hyperparameter tuning than for structural design.

### Method 3: Analogy-First — "What's This Like?"

```
Analogy Agent (opus)
├── Input: "add architecture review feature to TutorAgent"
│
├── "What's this like?"
│   ├── Hospital consultation → triage (sorting) → specialist assignment → consultation note
│   │   → Handoff + Contract Net combination emerges naturally
│   │
│   ├── Court trial → prosecutor (attack) vs defense (defend) → judge (decide)
│   │   → Adversarial + Voting emerges naturally
│   │
│   ├── Editor → draft → proofread → copy edit → review → publish
│   │   → Sequential + per-stage specialization
│   │
│   └── Ant colony → scouts → pheromones → swarm response
│       → Stigmergy + Swarm — but a new
│         "scout agent" concept appears
│         → light scan before full review?
│
└── Output: per-analogy structure proposals + new concepts like "scout agent"
```

Analogy thinks outside the pattern list. "Scout agent" doesn't exist in any of the 20 patterns. But it emerged from the ant analogy, and could actually be useful.

### Method 4: Constraint Relaxation — "What If This Constraint Weren't There?"

Doubt your own premises:

```
What if you relax the "solo use" constraint?
→ Peer-to-Peer returns
→ Wait — 4 sub-reviewers exchanging results as equals
  is essentially a mini P2P, isn't it?
→ "Solo use, so no P2P" might be wrong
→ Inter-agent P2P communication is independent of user count

What if you relax the "Claude Code infrastructure" constraint?
→ Actor Model returns
→ Wait — Claude Code subagents running in isolated contexts
  is already a lightweight Actor Model, isn't it?
→ What looked like a constraint was already implemented
```

### Full Creative Design Flow

```
┌──────────────────────────────────────────────────┐
│            Creative Architecture Agent            │
├──────────────────────────────────────────────────┤
│                                                  │
│  Phase 1: Scenario Generator (opus)              │
│  "Ignore constraints, generate 5 scenarios"      │
│  ← reference all of architecture_patterns.md     │
│                 ↓                                │
│  Phase 2: Scenario Simulator (sonnet)            │
│  "Virtually run each scenario"                   │
│  ← apply real-world context via my_system.md     │
│                 ↓                                │
│  Phase 3: Scenario Evaluator (sonnet)            │
│  "Compare + explore mix possibilities"           │
│  ← evaluate via review_checklist.md              │
│                 ↓                                │
│  Phase 4: Architecture Review - Deep (existing)  │
│  "Final candidates undergo rigorous validation"  │
│  ← 4 sub-reviewers + Group Chat                  │
│                                                  │
│  Loop: Phase 3 → 1 (if new mix emerges, diverge again) │
│  Max 3 rounds, convergence: 0 new scenarios      │
│  User permission: required if exceeds 3 rounds   │
├──────────────────────────────────────────────────┤
│  write_log.jsonl ← record all scenarios + decisions │
│  → Phase 1 references next time on similar problems │
└──────────────────────────────────────────────────┘
```

### Better Method — Full Architecture Design Agent

```
┌─────────────────────────────────────────────────┐
│         Full Architecture Design Agent           │
├─────────────────────────────────────────────────┤
│                                                 │
│  1. Analogy (opus) — frame problem in another domain │
│     "What's this like?" → ideas outside the pattern list │
│                  ↓                              │
│  2. Constraint Relaxation (opus) — doubt premises │
│     "Is this constraint really needed?" → re-examine eliminated patterns │
│                  ↓                              │
│  3. Scenario Generation (opus) — divergence     │
│     5 combinations from 1, 2 + patterns         │
│                  ↓                              │
│  4. Adversarial (sonnet) — deliberately break   │
│     "How would I break this?" → expose weaknesses │
│                  ↓                              │
│  5. Scenario Simulation (sonnet) — virtual run  │
│                  ↓                              │
│  6. Architecture Review Deep (existing) — rigorous validation │
│                  ↓                              │
│  7. Save ADR + memory                           │
│                                                 │
│  Loop: if 6 finds issues → back to 3            │
│  Max 3 rounds                                   │
└─────────────────────────────────────────────────┘
```

**Adding just Analogy + Adversarial** gives much better results than elimination alone. These two have the best value-for-cost.

---

## Q. Category Classification — From 7 to 14

> Question: "What is this? Is it included in the 20+? Or is it YAGNI KISS SOLID kind of stuff?"

Neither. It's a third category.

### 3 Basic Category Distinction

| # | Category | What It Covers | Analogy |
|---|---|---|---|
| 1 | Multi-Agent Patterns | Agent arrangement structure | Building structure systems (reinforced concrete, wood, steel) |
| 2 | Software Principles | Code writing rules | Construction rules (plumbing, wiring) |
| 3 | Design Thinking Methods | Design thinking process | An architect's sketching method |

#1 is **"what to build,"** #2 is **"how to build,"** #3 is **"how to decide."**

### Additions to Category 3

- **Design Thinking (IDEO)** — Empathize → Define → Ideate → Prototype → Test. From Stanford's d.school.
- **TRIZ** — Russian invention methodology. "Find the contradiction and solve it." 40 principles.
- **First Principles Thinking** — Elon Musk. "Ignore existing methods and rethink from physical laws."
- **Wardley Mapping** — Map "where this technology is in its evolution" to decide strategy.
- **Pre-mortem** — Adversarial variant. "Assume this project failed in 6 months. Why did it fail?"
Already known: Adversarial Design, Evolutionary Design, Analogy-First, Constraint Relaxation, Design Thinking (IDEO), TRIZ, First Principles, Wardley Mapping, Pre-mortem
Additional ones:
Backcasting — Decide the finished future state first, then work backward "how do we get there?" If Pre-mortem starts from a "failed future," this starts from a "successful future."
SCAMPER — Take an existing thing and Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse. Run through it like a checklist.
Biomimicry — Find solutions in nature. Like Analogy but with sources limited to biology. Swarm and Stigmergy came out of this.
Six Thinking Hats (de Bono) — Look at one problem from 6 perspectives (facts, emotion, criticism, optimism, creativity, management) in turn.
Theory of Inventive Problem Solving (TRIZ) extension — Contradiction Matrix — Combine 40 principles in a matrix. Find contradictions like "increasing speed reduces accuracy" and match with resolution principles.
Morphological Analysis — Decompose the problem into variables, list possible values for each, and explore combinations. Directly usable for pattern selection.
Design Sprint (Google Ventures) — Define problem → diverge → decide → prototype → test in 5 days. Faster and more practical than IDEO.
Jobs to be Done — Perspective of "what job does the user hire this product to do?" Think in terms of purpose, not features.

Category 3 is **the bridge connecting categories 1 and 2.**

### Expanding to 7 Categories

> Question: "Is there more besides category 3?"

| # | Category | What It Covers | Analogy |
|---|---|---|---|
| 1 | Multi-Agent Patterns | Agent arrangement structure | Building structure |
| 2 | Software Principles | Code writing rules | Construction rules |
| 3 | Design Thinking Methods | Design thinking process | Architect's sketches |
| 4 | Systems Thinking | Eye for the whole | Urban planning |
| 5 | Meta-Engineering | Designing the building process | Running a construction company |
| 6 | Domain Modeling | Reality → code translation | — |
| 7 | Human-AI Interaction | User touchpoints | — |

### #4: Systems Thinking Details

**Feedback Loops** — negative feedback loop (stabilization) vs positive feedback loop (runaway). If error-analyzer over-classifies errors, it runs away.

**Emergence** — 7 agents each follow their rules, but the whole exhibits unexpected behavior.

**Bottleneck Theory (TOC)** — Goldratt's theory of constraints. "Overall system performance is determined by the slowest part." Context window is the bottleneck → handoff quality determines overall performance.

**Second-Order Effects** — "Change A → B changes → C breaks."

**Leverage Points** — Donella Meadows. "Spots where small changes in a system produce large effects." ETHOS.md is a leverage point.

### #5: Meta-Engineering Details

**DevOps / CI/CD**, **Iteration Strategy**, **Technical Debt Management**, **Knowledge Management** (ADR, ETHOS.md, handoff.md), **Observability Design** (write_log.jsonl, analytics)

### Final Expansion to 14

> Question: "Is that all?"

```
Existing (established):
 1. Multi-Agent Patterns      ← agent arrangement
 2. Software Principles       ← code rules
 3. Design Thinking           ← design judgment
 4. Systems Thinking          ← eye for the whole
 5. Meta-Engineering          ← the making process
 6. Domain Modeling           ← reality → code
 7. Human-AI Interaction      ← user touchpoints

Missed (established but not included):
 8. Failure & Recovery        ← recovery strategy
 9. Security & Trust          ← permissions and trust
10. Data Architecture         ← data design
11. Performance & Resource    ← speed and cost

Creative proposals (not yet established as categories):
12. Temporal Design           ← evolution design over time
13. Knowledge Evolution       ← managing growth of knowledge itself
14. Context Engineering       ← designing what to show the agent
```

### Each Category in Detail

**8. Failure & Recovery Engineering** — "how do you survive when things go wrong?" auto-backup, GC agent health checks are part of this. Disaster Recovery, Chaos Engineering, Incident Response.

**9. Security & Trust** — "who can do what?" write-access hook is part of this. AI Safety, guardrails, sandboxing.

**10. Data Architecture** — "how does data flow and where does it live?" error_notes.md is markdown, knowledge_graph.json is JSON, analytics is JSONL — why all different formats? Event Sourcing, CQRS, Schema Evolution.

**11. Performance & Resource Engineering** — LLM cost optimization, context window management, caching, model routing.

**12. Temporal Design** — "how does the system change over time?" Phase planning:

```
Phase 1 (MVP): single agent, file-based
Phase 2 (expansion): multi-agent, hook system
Phase 3 (automation): architecture review, self-monitoring
```

Looks like it conflicts with YAGNI but doesn't — you're not building code in advance, you're building **structural slack** in advance.

**13. Knowledge Evolution** — designing the evolution of the knowledge base itself:

```
Knowledge Evolution Agent
├── After every Architecture Review:
│   ├── "Which patterns did we use this time?"
│   ├── "Were the matching conditions right?"
│   ├── "Did we miss any patterns?"
│   └── Auto-propose architecture_patterns.md updates
├── Periodically:
│   ├── "Which patterns haven't been used in 3 months?"
│   ├── "Which pattern combos always co-occur?" → register as new composite pattern
│   └── "Which patterns have high matching failure rates?" → revise matching conditions
└── Result: knowledge base grows more accurate with use
```

**14. Context Engineering** — "what to show and what to hide from the agent." boundary-check hook is this. Anthropic recently started using this term:

```
Context Engineering design elements:
├── What's always shown? (ETHOS.md — loaded every turn)
├── What's shown only when needed? (skills — only on trigger)
├── What's never shown? (other agents' SKILL.md)
├── Summary vs full text? (handoff.md is summary, error_notes is full text)
└── What happens when context window fills? (compaction strategy)
```

Why 12-14 aren't established yet — LLM agents are too recent. Pre-existing software engineering didn't have these problems.

---

## R. Feasibility of Implementing 14 Categories as Agents

> Question: "Can you build all of these as agents?"

### What Works Well as Agents

| Category | Automation Fit | Reason |
|---|---|---|
| 1. Multi-Agent Patterns | ★★★★★ | Pattern matching is knowledge base + rules |
| 2. Software Principles | ★★★★★ | Finding SOLID violations, code review — tools already exist |
| 3. Design Thinking | ★★★★☆ | Adversarial, Analogy — LLMs do well |
| 5. Meta-Engineering | ★★★★☆ | CI/CD, testing, log analysis — automation's home turf |
| 7. Human-AI Interaction | ★★★☆☆ | Pattern proposals possible, but "is it natural?" is human judgment |

### What's Hard as Agents

| Category | Automation Fit | Reason |
|---|---|---|
| 4. Systems Thinking | ★★☆☆☆ | Can't fit entire system into one context |
| 6. Domain Modeling | ★★☆☆☆ | Requires understanding of real world |

### Realistic Division of Labor

```
What humans do (irreplaceable):
├── 4. Systems Thinking — judging overall feedback loops
├── 6. Domain Modeling — defining "what is learning"
└── Final decisions

What agents assist (auxiliary):
├── 4. Systems Thinking — generate second-order effect candidates
└── 6. Domain Modeling — verify consistency of existing models

What agents do (automation):
├── 1. Pattern Matching
├── 2. Code Review
├── 3. Design Thinking
├── 5. Meta-Engineering
└── 7. HCI Pattern suggestions
```

### Architecture Agent Suite Composition

```
┌─────────────────────────────────────────────────────┐
│              Architecture Agent Suite                │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Agent 1: Pattern Advisor (Category 1)              │
│  ├── model: sonnet                                  │
│  ├── knowledge: architecture_patterns.md            │
│  └── role: pattern matching, elimination, combos    │
│                                                     │
│  Agent 2: Code Principles Checker (Category 2)      │
│  ├── model: haiku                                   │
│  ├── role: SOLID/YAGNI violations, duplication      │
│                                                     │
│  Agent 3: Creative Designer (Category 3)            │
│  ├── model: opus                                    │
│  ├── role: Adversarial, Analogy, Constraint Relax   │
│  └── owns divergence — most expensive, most valuable│
│                                                     │
│  Agent 4: Systems Analyzer (Category 4) ⚠️ assist only│
│  ├── model: sonnet                                  │
│  ├── role: generate "change A affects B, C" candidates│
│  └── ⚠️ output must always be human-verified         │
│                                                     │
│  Agent 5: Process Guardian (Category 5)             │
│  ├── model: haiku                                   │
│  ├── role: test coverage, tech debt tracking        │
│                                                     │
│  Human (you): final judgment for Category 4, 6 domain, 7 UX │
│                                                     │
├─────────────────────────────────────────────────────┤
│  Orchestrator: Architecture Review Deep             │
│  ├── Code change → Agent 2 only (light)             │
│  ├── Structure change → Agents 1, 2, 3, 4, 5 all    │
│  └── Agent 4 output always carries ⚠️ → user confirm │
└─────────────────────────────────────────────────────┘
```

### Are People Doing This?

**Almost no one does this systematically.**

Most people only do 1-2 categories. And manually. Regular developers only do Category 2; seniors do 1+2+3; Staff/Principal do 1+2+3+4. All in their heads.

**Places attempting similar things:**
- Anthropic — harness design research. But limited to coding agents.
- OpenAI Harness Engineering — environment design research. Also at coding level.
- MetaGPT — closest. But it's "code generation," not "creative structural design."

**Why this is unusual:** most people use agents as **executors**. What you're trying to do is use agents as **design partners**. That's the industry frontier right now.

---

## S. Will Agents 1-14 Fix Things Automatically? — Tier 1/2/3 Structure

> Question: "When something is changed, do agents 1-14 fix it automatically?"

No. And they shouldn't. If 14 agents fix code on their own — **you stop understanding the system.**

### Tier 1: Do It Automatically

Rule-based and only things with small impact if wrong:

```
├── write-access hook — block unauthorized writes (Category 9)
├── auto-backup — back up before changes (Category 8)
├── boundary-check — prevent context contamination (Category 14)
├── schema validation — validate data formats (Category 10)
└── cost guard — block LLM calls exceeding budget (Category 11)

In common: all are if-statements. No LLM judgment. Even when wrong, they only block; nothing breaks.
```

### Tier 2: Detect and Report

LLM analyzes, human decides:

```
├── Pattern Advisor — "this change has Blackboard conflict potential" (Category 1)
├── Code Checker — "3 SOLID violations found" (Category 2)
├── Creative Designer — "here's an alternative" (Category 3)
├── Systems Analyzer — "if you change this, there's a second-order effect here" (Category 4)
├── Process Guardian — "test coverage dropped from 80% to 65%" (Category 5)
├── Recovery Analyzer — "no rollback path after this change" (Category 8)
├── Knowledge Tracker — "this pattern combo used 3rd time — register as composite pattern?" (Category 13)
└── Context Advisor — "this agent's context has 2 unnecessary files loaded" (Category 14)

In common: all output "reports." Don't touch the code.
```

### Tier 3: Propose and Get Approval

```
├── "propose schema change for error_notes.md" → show diff → approve?
├── "propose hook execution order change" → show before/after → approve?
├── "propose new agent" → definition file draft → approve?
├── "modify matching conditions in architecture_patterns.md" → show changes → approve?
└── "Phase 2→3 transition point reached, propose structural changes" → roadmap → approve?
```

### Full Flow Example

```
You: "I'm thinking of adding a confidence score field to knowledge_graph.json"
     │
     ▼
Tier 1 (auto):
     schema validation detects "incompatible with current schema"
     write-access hook passes "permission check for this file"
     │
     ▼
Tier 2 (report):
     ┌─────────────────────────────────────────────┐
     │ Review Report                                │
     │                                             │
     │ [Category 1] Pattern impact:                 │
     │   Blackboard structure change — note-scanner │
     │   and tutor both read this file              │
     │                                             │
     │ [Category 4] Second-order effects:           │
     │   exam-coach uses graph-based recommendations│
     │   confidence score could change recommendation logic│
     │                                             │
     │ [Category 8] Recovery:                       │
     │   Backup of existing graph file needed       │
     │   No rollback without migration script       │
     │                                             │
     │ [Category 10] Data:                          │
     │   500 existing nodes — what default confidence?│
     │   0.5? 1.0? This is a domain judgment ⚠️     │
     │                                             │
     │ [Category 11] Cost:                          │
     │   If note-scanner reads confidence every time │
     │   context tokens expected to grow +15%        │
     └─────────────────────────────────────────────┘
     │
     ▼
You: read the report and "go with default 0.5, generate a migration script"
     │
     ▼
Tier 3 (propose + approve):
     ┌─────────────────────────────────────────────┐
     │ Proposal 1: schema change diff               │
     │ Proposal 2: migration script                 │
     │ Proposal 3: note-scanner modifications       │
     │ Proposal 4: ADR record                       │
     │ [Approve] [Request changes] [Reject]         │
     └─────────────────────────────────────────────┘
     │
     ▼
You: "Approve 1, 2, 4. Hold 3 for now"
     │
     ▼
Execute → done → write_log.jsonl recorded
```

Core principle: **be free with automating analysis, strict with automating execution.**

---

## T. General-Purpose Architecture Framework

> Question: "But what I was actually thinking wasn't TutorAgent — it was more like a class-like template that designs the 1-14 structure to build something, and also manages it."

You're not wrong. If anything, tying it to TutorAgent was the mistake.

### Core Difference

```
Any project → put into this framework → structure design + management happens
```

| | What we kept saying | What you actually had in mind |
|---|---|---|
| Scope | TutorAgent only | Any project |
| Nature | Feature | Tool |
| Reuse | None | Infinite |
| Knowledge | Context hardcoded | Injected per project |

### Framework Structure

```
architecture-framework/
├── README.md
├── core/
│   ├── analyzer.md          ← read project structure, assess status
│   ├── designer.md          ← structural design (diverge + converge + adversarial)
│   ├── reviewer.md          ← design validation (14 categories)
│   ├── executor.md          ← execute approved changes
│   └── evolver.md           ← manage evolution over time
│
├── knowledge/
│   ├── patterns.md          ← 20+ patterns + matching conditions
│   ├── principles.md        ← SOLID, YAGNI, etc.
│   ├── thinking_methods.md  ← Adversarial, Analogy, etc.
│   ├── anti_patterns.md     ← "don't do this"
│   └── past_decisions/      ← accumulated ADRs from past projects
│
├── checklist/
│   ├── 01_patterns.md ~ 14_context_engineering.md
│
├── templates/
│   ├── adr_template.md
│   ├── review_report.md
│   ├── system_doc.md
│   └── evolution_plan.md
│
└── config/
    ├── tier_rules.md
    └── cost_strategy.md
```

### Use It Like a Class

```python
framework = ArchitectureFramework()

# Analyzing TutorAgent
framework.load("tutoragent/my_system.md")
framework.review("Adding adaptive difficulty to Mock Exam")

# Analyzing Jarvis
framework.load("jarvis/my_system.md")
framework.review("Connecting HealthKit data to the scheduler")

# Analyzing a friend's project
framework.load("friend_project/my_system.md")
framework.review("Review the overall structure")
```

### Integration with harness-framework

```
harness-framework (R01-R18) = reference documents (passive)
Architecture Framework (1-14) = execution engine (active)

Combined:
├── harness tells you "these patterns exist" and
└── framework executes "apply them to your project like this"
```

---

## U. Building Jarvis with the Framework

> Question: "So can you basically build everything you want for Jarvis with this?"

### What the Framework Does vs Doesn't

```
Does: "what to build" → structure design → validation → implementation plan
Doesn't: actual Swift code, HealthKit API integration, UI implementation
```

A design firm draws blueprints — it doesn't lay the bricks. But once there's a blueprint, Claude Code or Codex lays the bricks.

### Full Flow

```
You: "I want to build a True Freetime Engine in Jarvis"
          │
          ▼
Architecture Framework (what you're building)
├── "Calendar agent writes to Blackboard, Freetime agent reads"
├── Adversarial: "What if GPS doesn't lock? What if there are 200 events?"
├── Review: passes 14-checklist
└── Output: design document + ADR + implementation roadmap
          │
          ▼
Claude Code / Codex (already exists)
├── reads the design and writes Swift code
├── API integration
└── writes tests
          │
          ▼
Architecture Framework (again)
├── reviews implemented code
├── "3 deviations from design found"
└── on to the next feature
```

### How Knowledge Accumulates

You use the same framework for every feature, but **knowledge accumulates.** Past ADRs stack up in past_decisions/, and matching conditions in patterns.md get more refined.

### Build First or in Parallel

**In parallel.** Filling out the framework while building Jarvis is the right move.

```
Week 1: Minimum Framework (Pattern Advisor + Creative Designer)
        + First Jarvis feature (use the framework to design it)
Week 2: Use framework, find what's missing
        + Second Jarvis feature
Week 3: Add categories to framework
        + Third Jarvis feature
```

The framework builds Jarvis; Jarvis improves the framework. They build each other.

---

## V. Hallucination Defense

> Question: "Running architecture and modifying — that's a huge activity, how do you handle hallucination?"

### The Core Problem

When an agent analyzes the 14-checklist — is the issue real, or did the agent make it up?

The more abstract, the higher the hallucination:

```
Category 1 (pattern matching): verifiable in files. Low hallucination
Category 4 (Systems Thinking): humans must infer to verify. High
Category 12 (Temporal Design): future prediction. Verification impossible. Very high
```

### Solution 1: Evidence Grade System

```
[FACT]     — directly verifiable in file/code. File name + line number citation required
[CALC]     — calculated from facts. Calculation steps required
[INFER]    — inference. Evidence chain required
[OPINION]  — agent judgment. ⚠️ mark required. Human verification mandatory
```

Distribution of evidence grades by category:

```
Category 1-2:   FACT 80%, CALC 15%, INFER 5%    → High trust
Category 3-5:   FACT 30%, CALC 20%, INFER 40%, OPINION 10% → Medium
Category 8-11:  FACT 50%, CALC 30%, INFER 20%   → Fairly high
Category 12-14: FACT 10%, INFER 50%, OPINION 40% → Caution required
```

### Solution 2: Hallucination Checker Agent

```
Hallucination Checker (sonnet)
├── For every [FACT] item: open the actual file and verify
│   → tag ❌ HALLUCINATION if missing
├── For every [CALC] item: redo the calculation
│   → tag ❌ CALC_ERROR if wrong
├── For every [INFER] item: validate the evidence chain
│   → tag ⚠️ UNGROUNDED if no evidence
└── Output: verified report (with tags)
```

### Solution 3: Per-Category Trust Strategy

```
Auto-trust: 1, 2, 10, 11 (high FACT ratio)
Trust after verification: 5, 8, 9 (mixed)
Mandatory human judgment: 3, 4, 12, 13, 14 (high OPINION ratio)
```

### Final Report Format

```
┌─────────────────────────────────────────────┐
│ Architecture Review Report                   │
│ Hallucination Check: ✅ complete             │
├─────────────────────────────────────────────┤
│                                             │
│ High confidence (FACT-based):                │
│ ✅ [FACT] Calendar agent writes directly to  │
│    blackboard (scheduler.swift:142)          │
│ ✅ [CALC] 200 events × ~50 tokens = 10K      │
│                                             │
│ Medium confidence (verified):                │
│ ✅ [INFER] No fallback on GPS failure        │
│    Evidence: no error handling in location.swift │
│    Hallucination Check: file verified ✅     │
│                                             │
│ Human judgment needed:                       │
│ ⚠️ [OPINION] As schedule data grows over 6 mo, │
│    Concurrent may beat Sequential            │
│    Evidence grade: weak. You must judge       │
│                                             │
│ Hallucinations detected:                     │
│ ❌ [HALLUCINATION] "config.json line 23"     │
│    → file has no line 23. Removed             │
│                                             │
└─────────────────────────────────────────────┘
```

---

## W. Hardcoded vs LLM Boundary

> Question: "So do I need to hardcode?"

Half and half.

### What to Hardcode (no LLM needed)

```typescript
// File/line verification
function verifyFact(claim: { file: string, line: number, content: string }) {
  const fileExists = fs.existsSync(claim.file)
  if (!fileExists) return { status: "HALLUCINATION", reason: "file missing" }
  
  const lines = fs.readFileSync(claim.file, 'utf-8').split('\n')
  if (claim.line > lines.length) return { status: "HALLUCINATION", reason: "line out of range" }
  
  const actualContent = lines[claim.line - 1]
  if (!actualContent.includes(claim.content)) 
    return { status: "HALLUCINATION", reason: "content mismatch" }
  
  return { status: "VERIFIED" }
}

// Calculation verification
function verifyCalc(claim: { expression: string, result: number }) {
  const actual = evaluate(claim.expression)
  if (actual !== claim.result) return { status: "CALC_ERROR", expected: actual }
  return { status: "VERIFIED" }
}
```

### What the LLM Must Do

"Is this inference logically valid?" — can't be done in code.

### 4-Layer Structure

```
Layer 1: Hardcoded verification (code)
├── [FACT] → verify actual file/line
├── [CALC] → re-run the calculation
└── LLM calls: 0

Layer 2: Structural verification (hardcoded + light LLM)
├── Is the report format correct?
├── Does the cited agent/skill name exist?
└── LLM calls: 0~1

Layer 3: Logical verification (LLM)
├── Is the [INFER] reasoning logical?
├── Is there a counterargument?
└── LLM calls: 1 (sonnet)

Layer 4: Human
├── Judge ⚠️ [OPINION] items
└── Final approval
```

**Layers 1-2 are hardcoded, Layer 3 is LLM, Layer 4 is human.** 60-70% of report items are filtered at Layers 1-2.

### Hardcoding Ratio Guide

```
Verifiable facts    → 100% hardcoded
Structural rules    → 90% hardcoded
Logical inference   → 100% LLM
Value judgments     → 100% human
```

Principle: **what can be verified goes in code, what requires thought goes to LLM, what requires decision goes to human.**

---

## X. Concrete Method for Building 1-14

> Question: "So if I want to build the 1-14, how do I go about it?"

### Classification of the 14

```
Just write files (knowledge):
├── 1. Multi-Agent Patterns    → patterns.md (already exists)
├── 2. Software Principles     → write principles.md
├── 3. Design Thinking Methods → write thinking_methods.md
└── This isn't "building" — it's "organizing"

Just write checklists (checklist):
├── 4. Systems Thinking        → 5-10 check items
├── 6~9, 12~13                 → 5-10 check items each
└── This is "writing question lists"

Need to code (actual implementation):
├── 5. Meta-Engineering        → CI/test/debt tracking tools
├── 10. Data Architecture      → schema validation tools
├── 11. Performance            → cost/token calculation tools
├── 14. Context Engineering    → context analysis tools
└── Only this is "coding"

Need to build agents:
├── Pattern Advisor / Creative Designer / Hallucination Checker / Systems Analyzer
└── This is .md file + prompt design
```

### Build Order by Phase

**Phase 0: Skeleton (1 day)**
```
architecture-framework/
├── README.md
├── core/     (empty)
├── knowledge/ (empty)
├── checklist/ (empty)
├── templates/
│   ├── adr_template.md
│   ├── review_report.md
│   └── my_system_template.md
└── config/
    └── tier_rules.md
```

**Phase 1: 3 Knowledge Files (2 days)**

Add matching conditions to patterns.md:
```markdown
## Stigmergy
**Matching condition**: when agents need to cooperate but can't communicate directly.
**Signal keywords**: write_log, audit_trail, event_log
**Doesn't fit**: real-time systems requiring immediate response
**Combines well with**: Blackboard, Pub-Sub
**Doesn't combine with**: Peer-to-Peer
```

**Phase 2: First Agent + Project Application (3 days)**

```
core/pattern-advisor.md
---
name: pattern-advisor
model: sonnet
tools: Read, Glob, Grep
---
You are a software architect.
Reference knowledge/patterns.md to analyze the current project structure
and propose pattern matches + improvements.
Every claim must carry an evidence grade [FACT][CALC][INFER][OPINION].
[FACT] must cite filename + line number.
```

**Phase 3: Add Hallucination Defense (2 days)**

```
core/hallucination-checker.ts    ← hardcoded Layer 1-2
core/hallucination-reviewer.md   ← LLM Layer 3
```

**Phase 4: Incrementally Add Checklists (ongoing)**

Checklists you write before using are vague. They only get concrete by actually using them.

**Phase 5: Creative Designer + Advanced Features (when needed)**

### Full Timeline

```
Week 1: Phase 0 + Phase 1 + Phase 2 (build and apply Pattern Advisor)
Week 2: Phase 3 (Hallucination defense) + start Phase 4
Week 3+: Phase 4 continues + Phase 5 begins
6 months later: 14 checklists + 5-7 agents + validation system complete
```

---

## Y. Design Methodologies — Pseudocode, Interface-First, etc.

> Question: "Are there methods like pseudocode for this kind of work?"

### 1. Pseudocode

```
WHEN user submits change_request:
    file_check = verify_all_facts(change_request)
    IF file_check has HALLUCINATION:
        RETURN error_report
    
    pattern_report = pattern_advisor.analyze(
        project = load(my_system.md),
        knowledge = load(patterns.md),
        change = change_request
    )
    
    FOR each claim IN pattern_report:
        IF claim.grade == FACT:
            verify_file_exists(claim.file, claim.line)
        IF claim.grade == CALC:
            recalculate(claim.expression)
        IF claim.grade == INFER:
            mark_as("human verification needed")
    
    PRESENT verified_report TO user
    WAIT FOR user.decision (approve / modify / reject)
```

### 2. Flowchart / Mermaid

Better than pseudocode for complex branches. But can't capture detailed logic.

### 3. User Story

```
AS    a solo developer
WHEN  adding a new feature
I WANT  to detect structural issues in advance
SO THAT  I don't have to rip things apart later

Acceptance Criteria:
- [ ] when a change request is submitted, a report comes back within 5 minutes
- [ ] every FACT item in the report has a file/line number
- [ ] HALLUCINATION detection is marked with ❌
- [ ] items needing human judgment are marked with ⚠️
```

### 4. Interface-First

Define I/O before internal logic:

```typescript
interface ArchitectureFramework {
  load(projectPath: string): ProjectContext
  review(change: ChangeRequest): ReviewReport
  design(problem: ProblemDescription): DesignProposal[]
  verify(report: ReviewReport): VerifiedReport
}

interface ChangeRequest {
  description: string
  affected_files: string[]
  category: "code" | "structure" | "data"
}

interface ReviewReport {
  claims: Claim[]
  overall_risk: "low" | "medium" | "high"
}

interface Claim {
  content: string
  grade: "FACT" | "CALC" | "INFER" | "OPINION"
  evidence: { file?: string; line?: number; calculation?: string }
  verified: boolean
  hallucination: boolean
}

interface VerifiedReport extends ReviewReport {
  hallucinations_found: number
  weak_inferences: number
  human_review_needed: Claim[]
}
```

### 5. Decision Table

```
| Change kind | Evidence grade | FACT verification | Result              |
|-------------|---------------|-------------------|---------------------|
| code        | FACT          | ✅ pass           | Auto-approve         |
| code        | FACT          | ❌ fail           | HALLUCINATION        |
| code        | INFER         | -                 | Human verification   |
| structure   | FACT          | ✅ pass           | Human verification (it's structure) |
| structure   | INFER         | -                 | Mandatory human verification |
| structure   | OPINION       | -                 | ⚠️ For reference only |
| data        | FACT          | ✅ pass           | Add schema validation |
| data        | CALC          | ✅ pass           | Auto-approve         |
| data        | CALC          | ❌ fail           | CALC_ERROR           |
```

### 6. Scenario Walkthrough

```
SCENARIO: "Add sleep data → schedule adjustment feature to Jarvis"

Step 1: user calls framework.review({
  description: "Auto-adjust morning schedule using HealthKit sleep data",
  affected_files: ["scheduler.swift", "healthkit.swift"],
  category: "structure"
})

Step 2: pattern_advisor analysis
  - Current structure: scheduler only reads calendar
  - Proposal: HealthKit → Blackboard → Scheduler structure
  - [FACT] scheduler.swift:42 only imports calendar ✅
  - [INFER] Pub-Sub is appropriate since sleep data changes daily ⚠️

Step 3: hallucination_check
  - check scheduler.swift:42 → actually imports calendar ✅
  - "changes daily" is INFER → unverifiable → keep ⚠️

Step 4: report has 1 INFER → request human judgment

Things discovered in this scenario:
- ChangeRequest needs a "data sources to connect" field
- External APIs like HealthKit need a separate checklist
```

### Recommended Combination Order

```
Step 1: User Story (WHY first)
Step 2: Interface-First (define I/O)
Step 3: Decision Table (branch logic)
Step 4: Scenario Walkthrough (validate)
Step 5: Pseudocode (before detailed implementation)
Step 6: Coding
```

Steps 1-4 finish before coding. 80% of design holes are caught here.

---

## Z. Seeing the Whole Picture — Dependency Tracking and Mental Organization

> Question: "What I'm wondering is how do I see the whole picture. With a structure, when you change one thing you might have to change everything it connects to."

### C4 Model — Zoom In / Zoom Out

The point: **look at one level at a time:**

```
Level 1: Whole system (3-5 boxes)
  "TutorAgent connects to user, file system, LLM API"

Level 2: Containers (5-10 boxes)
  "CLAUDE.md manages skills, agents, hooks"

Level 3: Components (10-20 boxes)
  "practice-questions skill writes to error_notes.md
   error-analyzer agent reads it"

Level 4: Code
  "Zod schema for the error_notes.md append function"
```

**If you see the problem at Level 1, you don't need to drop to Level 2.**

### Dependency Map — Tracking Chain Effects

```
If you change knowledge_graph.json:

knowledge_graph.json
├── Who writes? (write)
│   ├── tutor skill → adds nodes at section end
│   └── note-scanner agent → adds concept links
│
├── Who reads? (read)
│   ├── exam-coach skill → uses for weakness recommendations
│   ├── practice-questions skill → asks questions on related concepts
│   └── knowledge_graph_viewer.html → visualization
│
├── If the schema changes?
│   ├── src/types/ → Zod schema needs modification
│   ├── src/state/ → store needs modification
│   ├── GC agent → health check rules need modification
│   └── eval scenarios → test data needs modification
│
└── Indirect effects?
    ├── If exam-coach's input data changes
    │   → recommendation logic shifts
    │   → different strategies suggested to student
    │   → error_notes.md patterns may change
    └── That's 2nd-, 3rd-order effects
```

### Impact Mapping — Start from "Why"

```
WHY:    Improve student learning outcomes
├── WHO:  Student (user)
│   ├── HOW: Focused practice on weak areas
│   │   ├── WHAT: improve exam-coach
│   │   └── WHAT: strengthen error_notes analysis
│   └── HOW: Prevent overconfidence
│       └── WHAT: strengthen verification-quiz
└── WHO:  System (automation)
    └── HOW: Data accuracy
        ├── WHAT: schema validation
        └── WHAT: hallucination prevention
```

### ADR — Chain Effect Tracking Tool

```markdown
# ADR-007: Add confidence field to knowledge_graph.json

## Context
Student says "I understand" but actually doesn't grasp some concepts

## Decision
Add confidence: number (0.0~1.0) to nodes

## Affected
- [ ] src/types/graph.ts — add field to schema
- [ ] src/state/graph-store.ts — update read/write
- [ ] tutor skill — confidence update logic
- [ ] exam-coach skill — confidence-based recommendations
- [ ] note-scanner agent — confidence reading
- [ ] GC agent — add confidence range validation
- [ ] eval scenarios — tests covering the new field
- [ ] migration — default 0.5 for existing 500 nodes

## Not Doing (intentionally)
- practice-questions doesn't look at confidence yet

## How to Revert
- git revert + migration rollback script
- All 7 affected files must be rolled back
```

### Wardley Map — Evolution Stages

```
                  Certain ←────────────────→ Uncertain
                  
Closer to user   [Student Interface]
                      │
  │             [Socratic Tutor]  [Mock Exam]
  │                  │                │
  │             [error tracking]  [knowledge graph]
  │                  │                │
  │             [file I/O]       [Zod schemas]
  │                  │                │
Closer to infra [Claude Code]    [LLM API]
                 Mature ──────────────────→ Early
```

Don't touch what's mature. Focus on what's early-stage and close to the user.

### Practical Summary: dependencies.md

A file always maintained at the project root:

```markdown
## File Dependencies

### knowledge_graph.json
- WRITE: tutor, note-scanner
- READ: exam-coach, practice-questions, viewer
- SCHEMA: src/types/graph.ts
- STORE: src/state/graph-store.ts
- TEST: eval/scenarios/graph-*.md

### error_notes.md
- WRITE: practice-questions
- READ: error-analyzer, exam-coach
- SCHEMA: src/types/error.ts
- TEST: eval/scenarios/error-*.md

### meta_index.json
- WRITE: input-processing, note-organization
- READ: tutor, practice-questions, exam-coach
- SCHEMA: src/types/meta.ts
- STORE: src/state/meta-store.ts
- TEST: eval/scenarios/meta-*.md
```

This file itself can be **auto-updated by an agent** — finding import/read/write patterns via grep in code can be hardcoded.

### Mental Organization Summary

```
Seeing the whole picture → C4 Level 1 (3-5 boxes)
Tracing chain effects   → Dependency Map
Organizing the "why"    → Impact Mapping
Recording decisions     → ADR
Setting priorities      → Wardley Map
```

**Just maintaining Dependency Map + ADR** solves 90%.

---

## Appendix: What You Can Do With This Framework

> Question: "What can you do once you build this?"

1. **Faster development** — idea → 5-min agent consult → code with confidence → right the first time. Prevents large refactors like Week 4.

2. **Analyze other people's projects** — give a URL and "analyze the structure" → pattern mapping + weakness analysis.

3. **Productizable** — for solo developers, small teams, students. A tool for "developers designing solo without a senior."

4. **Jarvis core module** — a structure where Jarvis designs itself. First step toward a self-improving system.

5. **harness-framework execution engine** — turns R01~R18 pattern references from passive to active.

6. **Content source** — "How a solo developer automated architecture review with agents," "20 multi-agent patterns applied to a real project" — early-mover content.
