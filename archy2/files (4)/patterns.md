# Multi-Agent Patterns — Knowledge Base

## 1. Centralized

### Sequential
- Match: Clear steps with order dependency
- Keywords: pipeline, step, phase, chain
- Pros: Predictable, easy to debug | Cons: Blocked if any step fails
- Combines ✅ Handoff, Blackboard | ❌ Concurrent

### Orchestrator-Worker
- Match: Central dispatch + collect results
- Pros: Easy to scale workers | Cons: Orchestrator bottleneck, SPOF
- Combines ✅ Sequential, Blackboard, Contract Net | ❌ Peer-to-Peer
- Variants: **Coalition Formation** (dynamic team), **Team Formation** (skill-based team)

### Master-Slave
- Match: Simple replication/read distribution | Example: MySQL replication, Redis

## 2. Hierarchical

### Hierarchical
- Match: Problem decomposes into upper/lower levels
- Variants: **MOISE+** (explicit roles/groups/missions), **Institution-Based** (space-specific rules)

### Holonic
- Match: Parts are independent yet belong to whole | Example: TELETRUCK

### Layered (Temporal)
- Match: Upper layers plan slow, lower layers react fast | Example: Autonomous driving

## 3. Distributed

### Peer-to-Peer
- Match: Equal nodes cooperate without center | Example: Blockchain, BitTorrent

### Heterarchical
- Match: Leader emerges only when needed | Example: Drone swarms

### Gossip Protocol
- Match: State sync without center | Example: Cassandra, Bitcoin

### Publish-Subscribe
- Match: Loose coupling between publisher/subscriber
- Combines ✅ Blackboard, Stigmergy | ❌ Sequential

## 4. Shared Space

### Blackboard
- Match: Multiple agents read/write shared data
- Combines ✅ Orchestrator-Worker, Stigmergy
- Warning: Write collision → need write-access rules

### Tuple Space (Linda)
- Match: Simple shared memory | API: out, in, read

### Stigmergy
- Match: Indirect coordination through environment traces
- Combines ✅ Blackboard, Pub-Sub | ❌ Group Chat
- Example: Ant pheromone, Wikipedia edits, write_log.jsonl

## 5. Market/Negotiation

### Market-Based
- Match: Efficient resource allocation | Example: Power trading, cloud spot

### Contract Net
- Match: Dynamic task assignment. "Who can do this?" → bid → contract
- Variants: **Iterated Contract Net** (multi-round), **Leveled Commitment** (break contract if better option)

### Auction
- Match: Fair resource allocation | Example: Google Ads (Vickrey Auction)

## 6. Cooperative

### Group Chat
- Match: Free discussion for consensus | Warning: >3 agents hard to control

### Concurrent
- Match: Same problem, multiple perspectives simultaneously

### Voting/Consensus
- Match: Majority/agreement decisions
- Variants: **BFT** (handles malicious agents), **Raft/Paxos** (leader election consensus)

### Swarm Intelligence
- Match: Many simple agents → complex emergent behavior
- Variants: **ACO** (pheromone/path), **PSO** (flock/parameters), **ABC** (bee/role separation)

## 7. Dynamic Planning

### Handoff
- Match: Delegate to specialist | Warning: Infinite delegation loop

### Magentic
- Match: Plan unknown in advance

## 8. Learning

### Federated Learning
- Match: Learn without centralizing data

### BDI
- Match: Belief-Desire-Intention reasoning
- Variants: **BOID** (+Obligation), **Normative Agent** (social norms)

### Actor Model
- Match: Independent processes communicating via messages | Example: Erlang, Akka

## 9. Routing

### Mediator
- No judgment, just message routing. Lighter than Orchestrator.

### Broker
- Service matching only. "Find an agent that can do this."

### Reputation-Based
- Agents rate each other. Low-trust agents get fewer tasks. | Example: eBay reviews

---

## Agent Engineering — Beyond Patterns

### Prompt Engineering / System Design
- Define agent roles, judgment criteria, failure behavior, "I don't know" behavior
- Implementation: ETHOS.md, SKILL.md

### State Management
- Context window limits, memory storage, cross-session state transfer
- Implementation: handoff.md, knowledge_graph.json

### Tool Design
- Right number of tools, clear input/output specs directly affect agent performance

### Evaluation / Guardrails
- 3-Strike system, evidence grading (FACT/CALC/INFER/OPINION), Tier 1/2/3
- Hallucination checker

### Observability
- Logs, tracing, monitoring
- Implementation: write_log.jsonl

---

## Quick Match Table

| Situation | Pattern |
|-----------|---------|
| Clear steps | Sequential |
| Need scaling | Orchestrator-Worker |
| Complex hierarchy | Hierarchical / Holonic |
| No center wanted | Peer-to-Peer, Gossip |
| Indirect coordination | Stigmergy, Blackboard |
| Resource competition | Market-Based, Contract Net, Auction |
| Multiple perspectives | Group Chat, Concurrent |
| Result agreement | Voting, Raft, BFT |
| Specialist routing | Handoff, Broker |
| Uneven agent trust | Reputation-Based, BFT |
| Dynamic teams | Coalition/Team Formation |
| Renegotiation needed | Iterated Contract Net, Leveled Commitment |
