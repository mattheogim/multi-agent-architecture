# Design Thinking Methods — Knowledge Base

> 1번(패턴)과 2번(원칙)을 연결하는 다리.
> "어떤 패턴을 고를지, 어떻게 결정할지"의 사고 도구.

---

## 언제 뭘 쓰나 (빠른 참조)

| 상황 | 방법 |
|------|------|
| "이걸 왜 만들지?" 안 잡힐 때 | Jobs to be Done |
| "이게 진짜 필요해?" 의심될 때 | First Principles |
| "어떻게 만들지 감이 안 올 때" | Analogy / Biomimicry |
| "후보는 있는데 뭐가 나은지 모를 때" | Adversarial / Pre-mortem |
| "두 개 다 좋은데 양립 안 될 때" | TRIZ (Contradiction Matrix) |
| "기존 설계가 찝찝할 때" | SCAMPER |
| "변수가 너무 많아 정리 안 될 때" | Morphological Analysis |
| "만들긴 했는데 방향이 맞나 싶을 때" | Backcasting |
| "뭐부터 해야 할지 모를 때" | Wardley Mapping |
| "놓친 관점이 있을 것 같을 때" | Six Thinking Hats |
| "빨리 검증하고 싶을 때" | Design Sprint |
| "사용자 입장에서 봐야 할 때" | Design Thinking (IDEO) |
| "후보끼리 섞으면 더 나을 것 같을 때" | Evolutionary Design |
| "전제가 맞나 의심될 때" | Constraint Relaxation |

---

## 자주 묶이는 조합

```
발상 + 검증:      Analogy → Adversarial
모순 해결:        Adversarial → TRIZ
구조 잡기:        Morphological → Adversarial
방향 점검:        First Principles → Backcasting
리팩터링:         SCAMPER → Adversarial
```

거의 매번 Adversarial이 뒤에 붙음. 뭘 만들든 "이거 어떻게 망해?"는 항상 유용.

---

## 방법 상세

### Jobs to be Done
- 목적: "뭘 만들까"가 아니라 "뭘 해결하려고?"
- 방법: "사용자가 이 제품을 고용해서 어떤 일을 시키냐?"
- 예: 드릴을 사는 게 아니라 벽에 구멍이 필요한 거. 구멍이 필요한 이유는 선반. 선반이 필요한 이유는 책 정리.
- 출력: 진짜 문제 정의

### First Principles
- 목적: "원래 그래"를 의심
- 방법: 기존 방식 무시하고 물리 법칙/기본 원리부터 다시 생각
- 예: "로켓은 원래 비싸요" → 원자재 가격은 2%뿐. 나머지 98%는 관습.
- 출력: 근본적 재설계 가능성
- Constraint Relaxation과 함께 사용하면 효과적

### Design Thinking (IDEO)
- 목적: 사용자 입장에서 진짜 문제 찾기
- 방법: Empathize → Define → Ideate → Prototype → Test
- 예: 응급실 대기 불만 → 진짜 문제는 "잊혀진 건 아닌지" 불안 → 진행 화면 추가
- 출력: 사용자 중심 문제 정의 + 프로토타입

### Analogy-First
- 목적: 완전 다른 분야에서 해결책 빌려오기
- 방법: "이 문제는 뭐랑 비슷하지?" 최소 3개 도메인에서 비유
- 예: 신칸센 소음 → 물총새 부리 → 소음 해결 + 속도 10% 향상
- 출력: 패턴 목록 밖의 새로운 발상
- 항상 사용 권장. 가성비 최고.

### Biomimicry
- 목적: 자연에서 해결책 찾기. Analogy의 생물학 특화 버전
- 예: 에어컨 없는 건물 → 흰개미집 공기 순환 모방
- Swarm, Stigmergy가 여기서 나옴

### Adversarial Design
- 목적: 일부러 부수기. "어떻게 망하지?"
- 방법: Red Team이 실패 시나리오 5개 만들기
- 예: Netflix Chaos Monkey — 프로덕션 서버를 랜덤으로 죽여서 테스트
- 출력: 약점 목록 + 방어 방법
- 거의 모든 다른 방법 뒤에 붙여서 사용

### Pre-mortem
- 목적: 실패를 미리 경험
- 방법: "6개월 후 이 프로젝트가 완전히 망했다. 왜?" 역추적
- Adversarial과 비슷하지만 시점이 다름 (미래에서 시작)
- 출력: 숨겨진 위험 목록

### Constraint Relaxation
- 목적: 제약이 진짜 제약인지 확인
- 방법: "만약 이 제약이 없으면?" 하나씩 풀어보기
- 예: "Claude Code 인프라 제약 때문에 Actor Model 탈락" → 근데 subagent가 이미 경량 Actor Model 아닌가?
- 출력: 불필요한 제약 발견 + 부활하는 선택지

### TRIZ (Contradiction Matrix)
- 목적: 타협 대신 모순 자체를 해결
- 방법: "A 올리면 B 떨어진다" 모순 찾기 → 40가지 원리로 해결
- 분리 원리: 시간으로 분리 / 공간으로 분리 / 조건으로 분리
- 예: "예측 가능성 vs 창의성" → 시간 분리: 1차 계획대로, 2차 자율 cascade
- 출력: 모순 해결안

### SCAMPER
- 목적: 기존 설계를 강제로 변형
- 방법: 7가지 질문 기계적 적용
  - Substitute (대체), Combine (결합), Adapt (적용)
  - Modify (변형), Put to other use (다른 용도)
  - Eliminate (제거), Reverse (뒤집기)
- 예: 14개 레이어에서 Eliminate → "Knowledge Evolution 없애면?" → Data Architecture가 커버 가능?
- 출력: 생각 안 하던 변형들

### Morphological Analysis
- 목적: 가능한 모든 조합을 펼쳐놓고 좋은 거 고르기
- 방법: 문제를 변수로 쪼개고 각 변수의 선택지 나열 → 유효 조합 선택
- 예: 커피 = 크기(S/M/L) × 온도(핫/아이스) × 우유(없음/우유/오트) = 조합 펼치기
- 출력: 빠뜨리는 없이 후보 생성
- 변수가 많을 때 특히 유용

### Evolutionary Design
- 목적: 후보끼리 교배해서 더 나은 거 만들기
- 방법: 후보 → 상위 선택 → 장점 합친 자식 생성 → 반복
- 예: 후보A 채광 좋음 + 후보B 단열 좋음 = 자식C 둘 다
- 출력: 혼합 후보

### Backcasting
- 목적: 완성된 미래에서 역추적
- 방법: "성공한 모습" 먼저 그리고 → "그러려면 3개월 전에 뭐가?" → "이번 주에 뭐가?"
- Pre-mortem이 실패에서 시작하면, 이건 성공에서 시작
- 출력: 역방향 로드맵

### Wardley Mapping
- 목적: 성숙도 기반 우선순위
- 방법: 각 구성 요소를 성숙도(검증됨 ↔ 실험적) 축에 배치
- 예: Pattern Matching(성숙) → 먼저 만들어. Knowledge Evolution(실험적) → 작게 시도.
- 출력: 뭘 먼저 할지 판단

### Six Thinking Hats
- 목적: 관점 전환 강제
- 방법: 6가지 모자 번갈아 쓰기
  - 흰(사실), 빨강(감정), 검정(비판), 노랑(낙관), 초록(창의), 파랑(관리)
- 출력: 놓친 관점 발견

### Design Sprint (Google Ventures)
- 목적: 5일 만에 프로토타입 + 검증
- 방법: 월(문제) → 화(아이디어) → 수(결정) → 목(프로토타입) → 금(테스트)
- IDEO보다 빠르고 실무적
- 출력: 검증된 프로토타입

---

## Framework에서의 사용

```
Phase 1 (정의):     Jobs to be Done + First Principles
Phase 2 (발산):     Analogy + Morphological + SCAMPER
Phase 3 (검증):     Adversarial + Pre-mortem + Six Hats
Phase 4 (수렴):     TRIZ + Evolutionary + Wardley + Backcasting
Phase 5 (실행):     Design Sprint
```

단, 매번 전부 돌릴 필요 없음. 상황에 맞는 것만 꺼내 쓰는 도구함.
Analogy + Adversarial 두 개만 써도 80%.
