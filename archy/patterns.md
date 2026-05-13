# Multi-Agent Patterns — Knowledge Base (Complete)

## 1. 중앙집중형

### Sequential
- 매칭: 단계가 명확하고 순서가 중요할 때
- 키워드: pipeline, step, phase, 순서
- 장점: 예측 가능, 디버깅 쉬움 | 단점: 앞 단계 막히면 전체 정지
- 결합 ✅ Handoff, Blackboard | ❌ Concurrent

### Orchestrator-Worker
- 매칭: 중앙에서 작업 분배하고 결과 모을 때
- 장점: 워커 확장 쉬움 | 단점: 오케스트레이터 병목
- 결합 ✅ Sequential, Blackboard, Contract Net | ❌ Peer-to-Peer
- 변형: **Coalition Formation** (동적 팀 구성), **Team Formation** (능력 기반 팀 구성)

### Master-Slave
- 매칭: 단순 복제/읽기 분산 | 실제: MySQL 복제, Redis 클러스터

## 2. 계층형

### Hierarchical
- 매칭: 문제를 상위/하위로 나눌 수 있을 때
- 변형: **MOISE+** (역할/그룹/미션 명시적 정의), **Institution-Based** (공간별 규칙 적용)

### Holonic
- 매칭: 각 부분이 독립적이면서도 전체의 일부일 때 | 실제: TELETRUCK

### Layered (시간 계층)
- 매칭: 상위는 느리게 계획, 하위는 빠르게 반응 | 실제: 자율주행

## 3. 분산형

### Peer-to-Peer
- 매칭: 중앙 없이 동등한 노드 협력 | 실제: 블록체인, BitTorrent

### Heterarchical
- 매칭: 필요할 때만 리더. 유동적 구조 | 실제: 드론 군집

### Gossip Protocol
- 매칭: 중앙 없이 상태 동기화 | 실제: Cassandra, Bitcoin

### Publish-Subscribe
- 매칭: 발행자-구독자 느슨한 결합 | 결합 ✅ Blackboard, Stigmergy | ❌ Sequential

## 4. 공유공간형

### Blackboard
- 매칭: 여러 agent가 공유 데이터 읽고 쓸 때
- 결합 ✅ Orchestrator-Worker, Stigmergy
- 주의: 동시 쓰기 충돌 → write-access 규칙 필요

### Tuple Space (Linda)
- 매칭: 단순 공유 메모리 | API: out, in, read

### Stigmergy
- 매칭: 직접 통신 안 하는데 협조 필요. 환경에 흔적
- 결합 ✅ Blackboard, Pub-Sub | ❌ Group Chat
- 실제: 개미 페로몬, 위키피디아, write_log.jsonl

## 5. 시장/협상형

### Market-Based
- 매칭: 자원 효율적 배분 | 실제: 전력 거래, 클라우드 스팟

### Contract Net
- 매칭: 동적 작업 할당. "누가 할 수 있어?" → 입찰 → 계약
- 변형: **Iterated Contract Net** (여러 라운드 협상), **Leveled Commitment** (더 좋은 옵션 오면 계약 파기)

### Auction
- 매칭: 공정한 자원 배분 | 실제: Google 광고 (Vickrey Auction)

## 6. 협력형

### Group Chat
- 매칭: 자유 토론 합의 | 주의: 3명 넘으면 통제 어려움

### Concurrent
- 매칭: 같은 문제 여러 관점 동시 분석

### Voting/Consensus
- 매칭: 다수결/합의 결정
- 변형: **BFT** (악의적 agent 대비), **Raft/Paxos** (리더 선출 합의)

### Swarm Intelligence
- 매칭: 단순 agent 다수 → 복잡 행동 창발
- 변형: **ACO** (페로몬/경로), **PSO** (새떼/파라미터), **ABC** (꿀벌/역할 분리)

## 7. 동적계획형

### Handoff
- 매칭: 전문가에게 넘길 때 | 주의: 무한 위임 루프

### Magentic
- 매칭: 계획이 미리 안 정해진 문제

## 8. 학습형

### Federated Learning
- 매칭: 데이터 중앙화 없이 학습

### BDI
- 매칭: 믿음-욕구-의도 추론
- 변형: **BOID** (의무 추가), **Normative Agent** (사회 규범 내장)

### Actor Model
- 매칭: 독립 프로세스 메시지 통신 | 실제: Erlang, Akka

## 9. 라우팅형

### Mediator
- 판단 없이 메시지 라우팅만. Orchestrator보다 가벼움

### Broker
- 서비스 매칭만. "이 작업 할 수 있는 agent 찾아줘"

### Reputation-Based
- agent끼리 평판 점수. 신뢰도 낮으면 일 안 시킴 | 실제: 이베이 리뷰

---

## Agent Engineering — 패턴 외 필수 지식

### Prompt Engineering / System Design
- agent 역할 정의. 상황별 판단 기준, 실패 시 행동, 모를 때 행동
- 구현체: ETHOS.md, SKILL.md

### State Management
- context window 한계, 메모리 저장, 세션 간 상태 전달
- 구현체: handoff.md, knowledge_graph.json

### Tool Design
- 도구 수 적정선, 입출력 명확성이 agent 성능 직접 좌우

### Evaluation / Guardrails
- 3-Strike, 근거 등급 (FACT/CALC/INFER/OPINION), Tier 1/2/3
- hallucination checker

### Observability
- 로그, 트레이싱, 모니터링
- 구현체: write_log.jsonl

---

## 매칭 요약

| 상황 | 패턴 |
|------|------|
| 단계 명확 | Sequential |
| 확장 필요 | Orchestrator-Worker |
| 복잡 조직 | Hierarchical / Holonic |
| 중앙 싫음 | Peer-to-Peer, Gossip |
| 간접 협조 | Stigmergy, Blackboard |
| 자원 경쟁 | Market-Based, Contract Net, Auction |
| 다양한 의견 | Group Chat, Concurrent |
| 결과 합의 | Voting, Raft, BFT |
| 전문가 배정 | Handoff, Broker |
| agent 신뢰 불균일 | Reputation-Based, BFT |
| 동적 팀 | Coalition/Team Formation |
| 재협상 | Iterated Contract Net, Leveled Commitment |
