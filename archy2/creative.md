1. 구조해석이 뭐냐
건물이나 구조물이 있을 때 힘을 받으면 어디가 얼마나 휘고, 버티고, 깨질 위험이 있는지 계산하는 것이 구조해석이야.
예를 들면:
* 기둥이 하중을 얼마나 버티는지
* 보(beam)가 얼마나 휘는지
* 어떤 부재에 응력이 집중되는지
* 지진, 바람, 사람 하중을 받으면 전체 구조가 어떻게 반응하는지
건축에서 예쁜 도면만 그리는 게 아니라, 이 설계가 실제로 안전한지 수학적으로 확인해야 하잖아. 그때 구조해석을 해.
2. 유한요소해석(FEA)이 뭐냐
이건 구조해석의 대표적인 계산 방법이야.
실제 구조물은 너무 복잡해서 한 번에 통째로 계산하기 어려우니까, 그걸 작은 조각들(element) 로 잘게 나눠서 계산해.
예를 들면:
* 큰 판을 작은 삼각형/사각형으로 쪼갬
* 건물 부재를 작은 요소들로 나눔
* 각 조각이 어떻게 변형되는지 계산
* 그걸 다 합쳐서 전체 구조의 변형/응력/진동을 구함
왜 이름이 finite element냐면 무한히 연속적인 물체를 계산 가능한 유한 개의 요소로 나눠서 푸니까.
즉,
* 현실 세계: 연속체
* 컴퓨터 계산: 작은 블록들로 분해
* 결과: 전체 거동 근사
이런 방식이야.
3. 프레임 해석은 뭐냐
프레임 해석은 건물 골조처럼 기둥 + 보 + 연결부 중심 구조를 해석하는 거야.
예를 들면:
* 철골 구조
* RC frame
* 건물 뼈대
* 교량 골조
이건 FEA보다 더 “골조 중심”으로 보는 느낌이야.
예를 들어 기둥 하나, 보 하나를 선형 부재로 보고:
* 축력
* 전단력
* bending moment
* 처짐
이런 걸 계산해.
쉽게 말하면:
* FEA = 구조를 잘게 쪼개는 범용 해석 방식
* 프레임 해석 = 보/기둥 중심 골조 구조 해석
프레임 해석도 넓게 보면 수치해석의 한 갈래고, FEA와 겹치는 부분도 많아.

1. OpenSees / OpenSeesPy 구조·지반 시스템의 정적/동적 응답, 특히 지진 응답 시뮬레이션에 강한 오픈소스다. OpenSeesPy는 그걸 Python에서 쓰게 해주는 버전이라, 네가 AI나 자동화 붙이려면 오히려 이쪽이 더 편할 수 있다.


이런걸 응용할수도있나? 지금 우리가 하는거에?


재미있는 질문이야. 비유가 아니라 **진짜 응용 가능한지** 물어보는 거지?

답은: 직접 응용은 안 돼. 근데 **개념을 빌려오는 건 엄청 유용해.**

---

## 구조해석이 하는 것 vs 네 framework가 하는 것

```
구조해석:
  건물에 힘(하중)을 가하면 → 어디가 휘고, 깨지고, 버티는지 계산
  입력: 구조 + 힘
  출력: 응력 분포, 변형, 파괴 위험 지점

네 framework:
  소프트웨어에 변경(하중)을 가하면 → 어디가 영향받고, 깨지고, 버티는지 분석
  입력: 구조 + 변경사항
  출력: 연쇄 영향 맵, 위험 지점, 병목
```

거의 같은 구조야. 그래서 빌려올 수 있는 개념이 있어:

---

## FEA 개념 → 네 framework에 적용

**"잘게 쪼개서 각각 계산하고 합친다"**

FEA가 건물을 작은 삼각형으로 쪼개서 각각 응력 계산하고 합치잖아. 네 framework도 똑같아:

```
FEA:
  건물 → 삼각형 1000개로 분해 → 각각 응력 계산 → 합쳐서 전체 파악

네 framework:
  프로젝트 → 모듈/파일/함수로 분해 → 각 agent가 자기 관점에서 분석 → 합쳐서 전체 파악
```

네 14개 agent가 사실 **유한요소**야. 각 agent가 하나의 "요소"로서 자기 영역을 분석하고, orchestrator가 합치는 거.

---

## 프레임 해석 → 네 framework에 적용

**"기둥과 보의 연결부를 본다"**

프레임 해석에서 중요한 건 부재 자체가 아니라 **연결부(joint)**야. 기둥이 튼튼해도 연결부가 약하면 무너져.

네 소프트웨어에서도 같아:

```
프레임 해석:
  기둥 = 튼튼 ✅
  보 = 튼튼 ✅
  연결부 = 약함 ❌ → 여기서 무너짐

소프트웨어:
  모듈 A = 잘 짜여짐 ✅
  모듈 B = 잘 짜여짐 ✅
  A↔B 인터페이스 = 불명확 ❌ → 여기서 버그 발생
```

Systems Thinking agent가 하는 "연쇄 영향 분석"이 사실 **연결부 응력 분석**인 거야.

---

## 진짜 응용 가능한 부분

**응력 집중(Stress Concentration)** 개념:

구조해석에서 구멍이나 모서리에 응력이 집중되잖아. 소프트웨어에서도 동일해:

```
구조해석:
  판에 구멍 → 구멍 주변에 응력 3배 집중 → 거기서 균열 시작

소프트웨어:
  GC agent 1,094줄 → 변경이 이 파일에 집중 → 여기서 버그 발생
  knowledge_graph.json → 5개 agent가 읽고 2개가 쓰기 → 여기에 부하 집중
```

이걸 **정량화**할 수 있어:

```
파일별 "응력 점수" = (읽는 agent 수 × 쓰는 agent 수) + 변경 빈도

knowledge_graph.json: (5 × 2) + 높음 = 위험 ❌
error_notes.md:       (2 × 1) + 중간 = 보통 ⚠️
meta_index.json:      (3 × 2) + 낮음 = 관찰 ✅
```

이건 FACT로 계산 가능하고 하드코딩 할 수 있어. grep으로 import/read/write 패턴 찾으면 자동으로 "응력 맵" 생성 가능.

---

## OpenSeesPy 같은 도구를 진짜 쓸 수 있나?

OpenSees 자체를 직접 쓰긴 어려워 — 물리적 힘/변형 계산이니까. 근데 **그래프 기반 분석**으로 비슷한 걸 구현할 수 있어:

```python
# 소프트웨어 "구조해석" 개념

# 노드 = 모듈/파일
# 엣지 = 의존관계 (import, read, write)
# 하중 = 변경사항
# 응력 = 영향받는 정도

graph = {
    "knowledge_graph.json": {
        "read_by": ["tutor", "practice-questions", "exam-coach", "note-scanner", "viewer"],
        "write_by": ["tutor", "note-scanner"],
        "change_frequency": "high"
    },
    "error_notes.md": {
        "read_by": ["error-analyzer", "exam-coach"],
        "write_by": ["practice-questions"],
        "change_frequency": "medium"
    }
}

# "응력" 계산
for node, deps in graph.items():
    stress = len(deps["read_by"]) * len(deps["write_by"]) 
    coupling = stress * change_freq_score(deps["change_frequency"])
    print(f"{node}: stress={stress}, coupling={coupling}")

# 변경 "하중" 적용
def apply_change(target_node):
    affected = set()
    # 1차: 직접 의존
    for reader in graph[target_node]["read_by"]:
        affected.add(reader)  # FACT
    # 2차: 간접 의존 (reader가 쓰는 다른 파일의 reader)
    for reader in list(affected):
        for node, deps in graph.items():
            if reader in deps["write_by"]:
                for secondary_reader in deps["read_by"]:
                    affected.add(secondary_reader)  # INFER
    return affected
```

이건 **하드코딩 가능하고, LLM 호출 없이 돌아가고, FACT 기반**이야. Systems Thinking agent의 연쇄 영향 분석을 보조하는 도구로 쓸 수 있어.

---

## 정리

```
직접 응용 (OpenSees 그대로):  ❌ 안 됨. 물리 계산이라.
개념 차용:                    ✅ 매우 유용.
  - FEA → 잘게 쪼개서 분석하고 합치기 (이미 하고 있음)
  - 응력 집중 → 파일별 부하 점수 정량화 (추가 가능)
  - 연결부 분석 → 모듈 간 인터페이스 품질 (Systems Thinking)
  - 하중 전파 → 의존 그래프 기반 연쇄 영향 자동 추적 (코드로 구현 가능)
```

특히 **응력 맵 + 하중 전파**를 코드로 구현하면 Systems Thinking agent의 정확도가 크게 올라가. INFER에 의존하던 연쇄 영향의 상당 부분이 FACT/CALC가 되거든.


https://github.com/OpenSees/OpenSees

여기서 참고할거가 더있나?
좋은 질문이야. OpenSees에서 더 가져올 것도 있고, **다른 분야**에서 가져올 것도 있어.

---

## OpenSees에서 더 가져올 것

**Load Pattern + Time Series — 변경의 종류를 분류**

OpenSees에서 하중은 종류가 있어. 정적 하중(일정), 동적 하중(시간에 따라 변함), 지진 하중(불규칙). 하중 종류에 따라 분석 방법이 달라져.

```
OpenSees:
  Static load   → 정적 분석
  Dynamic load  → 동적 분석 (시간 적분 필요)
  Earthquake    → 지진 분석 (비선형 + 동적)

네 framework:
  코드 변경 (변수명, 함수 수정)     → Quick Check (agent 1~2개)
  구조 변경 (패턴 전환)            → Full Review (agent 전부)
  긴급 변경 (프로덕션 버그)        → Fast Track (핵심만 + 즉시)
  점진적 변경 (리팩터링)           → Incremental (이전 분석 참조)
```

지금 orchestrator가 "전부 돌리기 vs 일부 돌리기"만 구분하는데, **변경의 종류를 먼저 분류**하면 더 효율적이야.

**Constraint Handler — 제약 조건 처리**

OpenSees에서 "이 노드는 움직이면 안 돼" 같은 경계 조건을 처리하는 방법이 여러 개야. Transformation, Penalty, Lagrange. 네 framework에서:

```
OpenSees:
  "이 노드는 고정" → 변위 = 0 강제

네 framework:
  "이 파일은 수정 불가" → write-access 차단
  "이 패턴은 바꾸면 안 돼" → 구조 제약
  "이 API는 하위 호환 유지" → 인터페이스 제약
```

제약 조건을 명시적으로 정의하고 분석에 반영하면, agent가 "이건 바꿀 수 없으니까 다른 방법 찾아야 해"를 자동으로 판단할 수 있어.

**Eigenvalue Analysis — 시스템의 "고유 약점" 찾기**

이게 제일 재미있어. 건물의 고유진동수를 찾으면 "이 건물은 이 주파수의 지진에 취약하다"를 미리 알 수 있어. 소프트웨어에 비유하면:

```
OpenSees:
  건물 고유진동수 = 건물이 자연적으로 흔들리는 패턴
  지진 주파수가 고유진동수와 일치하면 → 공진 → 붕괴

네 framework:
  시스템 "고유 약점" = 시스템이 자연적으로 취약한 변경 유형
  그 유형의 변경이 오면 → 연쇄 붕괴

예: "knowledge_graph.json 스키마 변경"이 이 시스템의 고유 약점
    → 이 변경이 오면 5개 모듈이 동시에 영향받음
    → 미리 알고 있으면 대비 가능
```

의존 그래프에서 **가장 많이 연결된 노드**를 찾으면 그게 "고유 약점"이야. 하드코딩으로 계산 가능.

**Sensitivity Analysis — "뭐가 제일 영향 크냐"**

OpenSees에서 "이 재료 강도를 10% 바꾸면 전체 변위가 얼마나 변하냐"를 계산해. 네 framework에서:

```
OpenSees:
  dOutput/dInput = 민감도
  "콘크리트 강도 ±10% → 처짐 ±2%" → 둔감 (괜찮아)
  "철근 위치 ±10% → 처짐 ±30%" → 민감 (위험)

네 framework:
  "이 모듈을 바꾸면 전체에 얼마나 영향?" = 민감도
  "config.ts 변경 → 영향 2개 모듈" → 둔감 (안전한 변경)
  "knowledge_graph.json 스키마 변경 → 영향 7개 모듈" → 민감 (위험한 변경)
```

이것도 의존 그래프에서 자동 계산 가능. **변경 전에 민감도 점수를 보여주면** "이 변경은 위험도 높음, 주의" 경고를 자동으로 할 수 있어.

---

## 다른 분야에서 가져올 것

**회로 분석 (SPICE) — 전류 흐름 = 데이터 흐름**

```
회로:
  전압원 → 저항 → LED → 접지
  키르히호프 법칙: 들어오는 전류 = 나가는 전류

소프트웨어:
  입력 → 처리 모듈 → 출력 모듈 → 사용자
  데이터 보존: 들어오는 데이터 = 나가는 데이터 (변환될 뿐)
```

회로에서 "단락(short circuit)"이 위험하듯, 소프트웨어에서 "두 모듈이 같은 데이터를 동시에 쓰는 것"이 위험해. 회로 분석의 **전류 추적**을 데이터 흐름 추적에 쓸 수 있어.

**제어 이론 (PID Controller) — 피드백 안정성**

```
PID:
  P (비례): 현재 오차에 비례해서 조절
  I (적분): 과거 오차 누적 보정
  D (미분): 오차 변화율 예측

네 framework에 적용:
  P: 현재 분석에서 발견된 문제 수에 비례해서 검토 깊이 조절
  I: 과거 분석에서 반복되는 문제 패턴 누적 → 체크리스트 자동 강화
  D: 문제가 늘어나는 추세면 → 조기 경고
```

아까 adaptive difficulty에서 "감쇠 계수"가 필요하다고 했잖아. 그게 제어 이론에서 온 거야. 네 framework 전체에도 적용 가능해 — "분석 깊이를 상황에 따라 자동 조절"하는 메커니즘.

**의학 진단 — 감별 진단 프로세스**

```
의사:
  증상 수집 → 가능한 질병 목록 → 검사로 하나씩 제거 → 확정 진단
  핵심: "이 증상이 있으면 이 질병은 아니다" (배제)

네 framework:
  프로젝트 스캔 → 가능한 문제 목록 → 코드 확인으로 하나씩 제거 → 확정 진단
  핵심: "이 파일에 이게 있으면 이 문제는 아니다" (배제)
```

지금 agent가 "문제 찾기"를 하는데, "문제 배제"를 추가하면 정확도가 올라가. "이건 문제 아니야, 왜냐면 이 코드가 있으니까 [FACT]" — 이게 오진을 줄여.

**비행기 안전 시스템 — 다중 독립 검증**

```
비행기:
  3개 독립된 컴퓨터가 같은 계산을 동시에 함
  2개 이상 같은 답 → 채택
  1개만 다른 답 → 그 컴퓨터 결함으로 판단

네 framework:
  핵심 판단을 2~3개 다른 방법으로 동시에 분석
  결과가 일치 → 신뢰도 높음
  결과가 다름 → "여기 불확실해" 표시
```

이게 Concurrent + Voting이긴 한데, **같은 질문을 다른 방법으로** 하는 게 포인트야. Pattern Advisor가 "후보 A 추천"하고, 별도로 Adversarial이 "후보 A 부수기"하고, 결과가 일관되면 신뢰도 ↑.

---

## 제일 가치 있는 3개

```
1순위: Sensitivity Analysis (민감도)
  → 변경 전에 "이 변경 위험도 점수" 자동 계산
  → 의존 그래프에서 FACT/CALC로 산출 가능
  → Systems Thinking agent 정확도 직접 향상

2순위: Eigenvalue (고유 약점 분석)
  → 프로젝트의 "급소"를 미리 파악
  → 가장 많이 연결된 노드 = 가장 위험한 파일
  → 진찰 단계에서 자동 실행

3순위: 감별 진단 (배제법)
  → "문제 찾기"뿐 아니라 "문제 아닌 것 확인"
  → 오진율 감소
  → FACT 기반 배제 → 보고서 신뢰도 향상
```

이 세 개를 추가하면 네 framework가 "느낌으로 분석"에서 "정량적으로 분석"으로 레벨업해. 특히 1, 2번은 코드로 구현 가능하고 LLM 호출 안 필요해서 Tier 1에 들어갈 수 있어.

더 넓게 가볼게.

---

## 생물학

**면역 체계 — T세포 기억**

```
면역:
  바이러스 처음 만남 → 느리게 대응 (1~2주)
  같은 바이러스 다시 만남 → 기억 T세포가 즉시 대응

네 framework:
  처음 보는 패턴 문제 → 5개 agent 전부 돌림 (느림)
  전에 본 적 있는 문제 → 과거 ADR 참조해서 즉시 답 (빠름)
  → past_decisions/ 폴더가 "면역 기억"이야
```

지금 past_decisions/가 있긴 한데 수동으로 참조해. 이걸 **자동 매칭**으로 바꾸면 — 새 변경이 들어왔을 때 "이거 ADR-003이랑 비슷한데?" 하고 과거 결정을 먼저 보여주는 거야. 같은 실수를 두 번 안 해.

**유전학 — 유전자 발현 조절**

```
유전학:
  모든 세포가 같은 DNA를 갖고 있지만
  피부 세포는 피부 유전자만 "켜짐"
  근육 세포는 근육 유전자만 "켜짐"
  → 같은 정보, 다른 활성화

네 framework:
  모든 agent가 같은 knowledge 파일을 참조하지만
  코드 변경 시 → Principles Checker만 "켜짐"
  구조 변경 시 → 전부 "켜짐"
  → 같은 knowledge, 다른 활성화
```

이건 이미 하고 있긴 한데, 유전자 발현에서 빌려올 건 **억제자(repressor)** 개념이야. "이 상황에서는 이 agent를 명시적으로 끄겠다"를 정의하는 거. 켜는 것보다 **끄는 규칙**이 더 정확할 수 있어.

**신경계 — 반사와 의식**

```
신경계:
  뜨거운 거 만짐 → 반사로 손 뺌 (뇌 안 거침, 0.05초)
  "이게 뭐였지?" → 뇌가 판단 (1~2초)
  → 위험한 건 즉시, 복잡한 건 천천히

네 framework:
  .env 파일이 git에 올라감 → Tier 1 hook이 즉시 차단 (LLM 안 거침)
  "이 구조 변경이 맞나?" → 5개 agent가 분석 (1~2분)
  → 위험한 건 즉시, 복잡한 건 천천히
```

이건 Tier 1/2/3이랑 같은 원리인데, 신경계에서 가져올 건 **habitation(습관화)**. 같은 경고가 반복되면 무시하게 돼. 네 framework도 매번 같은 경고 내면 사용자가 무시하기 시작해. "이 경고는 3번째 반복됨 → 중요도 낮춤" 또는 "이 경고가 계속 나오면 근본 원인을 한 번 해결하세요" 제안.

---

## 경제학

**포트폴리오 이론 — 분산 투자**

```
투자:
  주식 하나에 올인 → 위험 최대
  여러 종목에 분산 → 위험 감소
  핵심: 상관관계가 낮은 자산을 조합

네 framework:
  agent 하나에 의존 → 그 agent 틀리면 전부 틀림
  여러 agent가 독립적으로 분석 → 위험 분산
  핵심: agent 간 판단이 독립적이어야 함
```

여기서 가져올 건 **상관관계 체크**. Pattern Advisor와 Principles Checker가 항상 같은 결론을 내면 "사실 둘이 같은 걸 보고 있는 거 아냐?" 의심해야 해. 독립적이지 않으면 agent가 5개여도 실질적으로 1개야.

**보험 — 리스크 프리미엄**

```
보험:
  위험한 운전자 → 보험료 높음
  안전한 운전자 → 보험료 낮음
  과거 사고 이력 → 보험료에 반영

네 framework:
  자주 문제 생기는 모듈 → 분석 깊이 높임
  안정적인 모듈 → 분석 깊이 낮춤
  과거 버그 이력 → 리스크 점수에 반영
```

**모듈별 "보험료"(리스크 점수)를 자동 계산**하면 어디에 분석 비용을 집중할지 판단할 수 있어. git 히스토리에서 "이 파일 수정 후 버그 발생 빈도"를 추출하면 FACT 기반으로 계산 가능.

---

## 항공/군사

**OODA Loop — 관찰-판단-결정-행동**

```
OODA (전투기 조종사 의사결정):
  Observe → Orient → Decide → Act → 다시 Observe
  핵심: Orient(상황 판단)이 가장 중요. 빠를수록 이김.

네 framework:
  Scan(진찰) → Analyze(5 agent) → Decide(추천) → Apply(실행) → 다시 Scan
  핵심: Scan 속도가 전체 루프 속도를 결정
```

가져올 건 **inside the OODA loop** 개념. 상대방보다 빠르게 루프를 도는 사람이 이겨. 네 framework가 "변경 → 분석 → 결과"를 2분에 하면, 수동으로 하루 걸리는 사람보다 12배 빠르게 판단 루프를 돈다.

**Swiss Cheese Model — 사고 방지**

```
항공 사고 모델:
  방어층이 여러 개 있는데, 각 층에 구멍(취약점)이 있음
  구멍이 우연히 일렬로 정렬되면 → 사고 발생
  한 층만 뚫려도 다른 층이 막으면 → 사고 안 남

네 framework:
  Tier 1 (hook)      → 구멍: 규칙에 없는 문제
  Tier 2 (agent 분석) → 구멍: hallucination
  Tier 3 (사람 승인)  → 구멍: 사람의 실수
  → 3개 층 전부 뚫려야 문제 발생
```

이건 이미 Tier 구조가 하고 있는 거야. 근데 Swiss Cheese에서 가져올 건 **"구멍 정렬 감지"**. "Tier 1이 못 잡고 + Tier 2도 INFER로만 판단하고 + 사람이 바쁘면" 세 구멍이 정렬돼. 이럴 때 **추가 경고**: "이 변경은 모든 방어층이 약합니다. 신중하게."

---

## 도시 계획

**교통 시뮬레이션 — 병목 예측**

```
교통:
  도로 하나 막으면 → 우회로에 차가 몰림 → 거기도 막힘 → 연쇄 정체
  해결: 우회로의 용량을 미리 계산

네 framework:
  모듈 하나 바꾸면 → 연결된 모듈에 부하 → 거기도 문제 → 연쇄 영향
  해결: 연결된 모듈의 "용량"(변경 수용력)을 미리 계산
```

**전력망 관리 — Cascading Failure**

```
전력망:
  발전소 하나 꺼짐 → 다른 발전소에 부하 전이 →
  과부하로 또 꺼짐 → 또 전이 → 대정전 (2003년 미국 동부)
  방지: 의도적으로 일부를 미리 차단 (load shedding)

네 framework:
  모듈 하나 깨짐 → 의존 모듈에 영향 → 거기도 깨짐 → 연쇄
  방지: "이 모듈이 깨지면 저 모듈은 미리 격리" (circuit breaker)
```

이건 Systems Thinking agent에 추가할 수 있어. "이 변경이 cascade failure를 유발할 수 있는가?" 체크. 의존 그래프에서 **한 노드 제거 시 연결이 끊기는 노드 수**를 계산하면 cascade 위험도가 나와.

---

## 요리

**미장플라스 (Mise en place) — 준비 완료 후 실행**

```
요리:
  요리 시작 전에 모든 재료를 계량하고 준비
  → 요리 중에 "아 양파 안 썰었네" 안 생김

네 framework:
  분석 시작 전에 모든 context를 준비
  → 분석 중에 "아 이 파일 안 읽었네" 안 생김
  → 진찰 단계의 커버리지 맵이 미장플라스
```

---

## 제일 가치 있는 것 정리

```
1. 면역 기억 (past_decisions 자동 매칭)
   → 같은 실수 반복 방지. 속도 향상.
   → 구현: ADR 키워드 매칭

2. 리스크 점수 (보험의 사고 이력 기반)
   → 모듈별 위험도 자동 계산. 분석 자원 집중.
   → 구현: git history + 의존 그래프

3. Cascade Failure 감지 (전력망)
   → 연쇄 붕괴 위험 사전 경고.
   → 구현: 그래프에서 노드 제거 시뮬레이션

4. Swiss Cheese 구멍 정렬 감지
   → 방어층 약할 때 추가 경고
   → 구현: Tier별 신뢰도 곱셈

5. 억제자 (유전학 — 끄는 규칙)
   → 불필요한 agent 비활성화로 비용/노이즈 감소
   → 구현: 변경 유형 → 비활성화 agent 목록 매핑
```

전부 **코드로 구현 가능하고 LLM 불필요**해서 Tier 1에 들어갈 수 있어. Systems Thinking의 INFER를 CALC로 올리는 데 직접 기여하고.


아니, OpenSees는 대부분 진짜야. 하나씩 걸러볼게.

---

## 진짜 쓸모 있는 것 (비유 없으면 못 떠올림)

**응력 집중 → 파일별 부하 점수**
```
비유 없이 생각 가능? → 어려움
"읽는 agent 수 × 쓰는 agent 수 = 위험도" 공식은
구조해석의 응력 계산에서 직접 온 거야.
코드로 바로 구현 가능. grep으로 자동 계산.
→ ✅ 진짜
```

**Sensitivity Analysis → 변경 위험도 점수**
```
비유 없이 생각 가능? → 어려움
"이 파일 바꾸면 영향받는 모듈 수"를 자동 계산하는 건
민감도 분석 개념이 없으면 떠올리기 힘들어.
의존 그래프에서 FACT로 산출 가능.
→ ✅ 진짜
```

**Eigenvalue → 고유 약점**
```
비유 없이 생각 가능? → 좀 애매
"가장 많이 연결된 노드 = 가장 위험" 자체는
그래프 이론으로도 나올 수 있어 (centrality).
근데 "고유진동수처럼 특정 유형의 변경에만 취약"이라는
발상은 구조해석에서 온 거라 가치 있어.
→ ✅ 쓸 만함
```

**Node/Element/Material 분리**
```
비유 없이 생각 가능? → 가능
모듈, 의존관계, 패턴 특성을 나누는 건
객체 지향 설계에서도 나오는 거야.
OpenSees가 알려준 게 아니라 이미 아는 개념에
이름을 붙인 거에 가까움.
→ ⚠️ 과한 편
```

**Plugin Architecture**
```
비유 없이 생각 가능? → 당연히 가능
OCP(Open/Closed Principle)에서 바로 나와.
OpenSees에서 빌려올 필요 없음.
→ ❌ 과함
```

**Convergence Test**
```
비유 없이 생각 가능? → 이미 하고 있음
"새 이슈 0개면 멈춰"는 네가 이미 정한 거.
OpenSees 용어 갖다 붙인 것뿐.
→ ❌ 과함
```

**Recorder**
```
비유 없이 생각 가능? → write_log.jsonl 이미 있음
→ ❌ 과함
```

**Analysis 교체 가능 구조**
```
비유 없이 생각 가능? → 가능하긴 한데
"변경 유형별로 분석 방법을 교체한다"는 발상이
OpenSees의 Static/Dynamic/Eigenvalue 교체에서
구체적으로 형태가 잡혔어.
→ ✅ 쓸 만함
```

**Load Pattern → 변경 유형 분류**
```
비유 없이 생각 가능? → 좀 어려움
"변경에도 종류가 있고 종류별로 다르게 분석한다"는
하중 유형 개념에서 직접 온 거.
→ ✅ 진짜
```

**Constraint Handler → 제약 조건**
```
비유 없이 생각 가능? → 가능
"이 파일 수정 불가"는 당연한 건데
OpenSees 용어를 쓸 필요 없음.
→ ❌ 과함
```

---

## 정리

```
✅ 진짜 가져올 것:
  1. 응력 집중 → 파일별 부하 점수 (자동 계산)
  2. Sensitivity → 변경 위험도 점수 (자동 계산)
  3. Load Pattern → 변경 유형 분류 (분석 방법 선택)
  4. Analysis 교체 → 유형별 다른 agent 조합

❌ 과한 것 (이미 알고 있거나 당연한 것에 이름만 붙인 거):
  5. Node/Element/Material → 그냥 객체 지향
  6. Plugin → 그냥 OCP
  7. Convergence → 이미 하고 있음
  8. Recorder → write_log 이미 있음
  9. Constraint → 당연한 거
  
⚠️ 쓸 만한데 필수는 아닌 것:
  10. Eigenvalue → 그래프 centrality로도 됨
```

4개만 진짜야. 나머지는 내가 과하게 비유 붙인 거 맞아.


네 framework가 하는 걸 한 줄로 하면 — **"복잡한 시스템을 여러 관점에서 분석하고, 변경의 영향을 예측하는 것"**이잖아.

이걸 하는 분야들:

---

**구조공학 (방금 본 거)**
- 건물에 힘 가하면 어디가 휘는지 계산
- 네 거에 준 것: 응력 집중, 민감도, 하중 유형

**시스템 엔지니어링 (Systems Engineering)**
- NASA, 보잉, 군사에서 씀. 로켓이나 전투기 같은 복잡 시스템 설계
- V-Model: 요구사항 → 설계 → 구현 → 테스트 → 검증, 각 단계가 대칭
- MBSE (Model-Based Systems Engineering): 시스템 전체를 모델로 만들고 시뮬레이션
- 네 거에 줄 수 있는 것: **요구사항 추적(Traceability)** — "이 기능은 이 요구사항에서 나왔고, 이 코드가 구현한다" 연결 고리. 변경 시 "이 요구사항에 영향"까지 추적

**신뢰성 공학 (Reliability Engineering)**
- 원자력, 항공, 의료 기기에서 씀. "이 시스템이 고장날 확률은?"
- FMEA (Failure Mode and Effects Analysis): 모든 부품에 대해 "이게 어떻게 고장나? 고장나면 뭐가 영향받아?" 체계적으로 나열
- Fault Tree Analysis: 최종 사고에서 거꾸로 "이게 일어나려면 뭐가 선행돼야 해?" 역추적
- 네 거에 줄 수 있는 것: **FMEA를 모듈별로 적용** — 각 모듈이 "어떻게 실패할 수 있는지" 목록화. 이건 Adversarial이랑 합치면 강력해

**제어 이론 (Control Theory)**
- 자율주행, 로봇, 화학 플랜트에서 씀
- 안정성 분석: 시스템에 작은 충격 주면 원래로 돌아오나, 발산하나?
- 네 거에 줄 수 있는 것: **feedback loop 안정성 판단 기준**. 지금 Systems Thinking이 "진동할 수 있어 ⚠️"만 하는데, 제어 이론 쓰면 "감쇠율 0.3이면 안정, 0.8이면 진동" 같은 정량 기준이 나옴

**역학 (Epidemiology)**
- 전염병 확산 모델. SIR 모델 — 감염자가 주변에 퍼뜨리는 속도
- 네 거에 줄 수 있는 것: **변경 전파 모델**. "이 변경이 의존 그래프를 따라 얼마나 빠르게 퍼지나?" R0 같은 전파 계수를 모듈에 적용

**위험 분석 (Risk Analysis)**
- 금융, 보험, 프로젝트 관리에서 씀
- Monte Carlo 시뮬레이션: 변수를 랜덤으로 바꿔가면서 결과 분포를 봄
- 네 거에 줄 수 있는 것: **불확실성 정량화**. "이 변경의 영향은 최소 2모듈 ~ 최대 7모듈, 평균 4모듈" 같은 범위 제시. INFER를 "맞을 수도 있고 아닐 수도 있어"가 아니라 "70% 확률로 영향 있음"으로 바꾸기

**네트워크 과학 (Network Science)**
- 인터넷, 소셜 네트워크, 생태계 분석에서 씀
- Centrality: 어떤 노드가 제일 중요한지
- Clustering: 밀접하게 연결된 그룹 찾기
- Resilience: 노드 제거했을 때 네트워크가 살아남는지
- 네 거에 줄 수 있는 것: **의존 그래프를 네트워크로 분석** — 가장 중요한 파일, 모듈 클러스터, 제거 시 네트워크 분리 위험 전부 자동 계산 가능

---

## 과한 거 걸러내면

```
✅ 진짜 쓸모 있는 것 (코드로 바로 구현 가능):
  네트워크 과학 → centrality, clustering, resilience 전부 그래프 알고리즘
  역학 전파 모델 → 의존 그래프에서 전파 계수 계산
  위험 분석 → 영향 범위를 확률로 제시

⚠️ 쓸 만한데 구현 복잡:
  FMEA → 모듈별 실패 모드 목록화 (수동 작업 필요)
  시스템 엔지니어링 → 요구사항 추적 (프로젝트에 요구사항 문서가 있어야 함)

❌ 과한 거:
  제어 이론 → 감쇠율 정량화는 소프트웨어에서 숫자가 안 나옴
```

**네트워크 과학이 제일 직접적이야.** 네 의존 그래프가 이미 네트워크이고, centrality/resilience 알고리즘은 Python 한 줄이면 돌아가거든. 이걸 진찰 단계에 넣으면 "이 프로젝트의 급소는 여기"가 FACT로 나와.
분야별 오픈소스 도구 정리:

---

## 구조공학

| 도구 | 설명 | 네 framework에 쓸 수 있는 것 |
|------|------|--------------------------|
| **OpenSees / OpenSeesPy** | 구조 해석, 지진 응답 시뮬레이션 | 응력 집중, 민감도 분석, 하중 유형 개념 |
| GitHub: OpenSees/OpenSees | Python 바인딩 있음 | |

→ 코드를 직접 쓰진 않고, **개념만 차용**하는 거였으니 도구보다 아이디어가 중요.

---

## 시스템 엔지니어링 (MBSE)

| 도구 | 설명 |
|------|------|
| **Capella** | Thales가 개발한 오픈소스 MBSE 도구. Arcadia 방법론 기반으로 복잡 시스템 아키텍처 설계. 운영 분석부터 물리 아키텍처까지 5단계 엔지니어링 페이즈 |
| **SysON** | SysML V2 표준을 준수하는 차세대 모델링 도구. 웹 기반. Capella, Papyrus와 상호운용 가능 |
| **OpenMBEE** | 오픈소스 협업 엔지니어링 시스템. 엔지니어가 원하는 언어로 작업하고 다른 도구 간에 쉽게 공유하고 문서화. TMT 망원경 프로젝트에서 산업 규모로 사용됨 |
| **Papyrus** | Eclipse 기반 UML/SysML 모델링. 오픈소스 |
| **OpenModelica** | 기계, 전기, 유압 시스템부터 소프트웨어, 제어 시스템까지 모델링하고 시뮬레이션하는 플랫폼 |

→ 네 거에 쓸 것: **요구사항 추적(Traceability)** 개념. Capella의 Arcadia 방법론에서 "각 설계 단계가 이전 단계로 추적 가능"한 구조 참고.

---

## 신뢰성 공학 (FMEA / Fault Tree)

| 도구 | 설명 |
|------|------|
| **EMFTA** | Carnegie Mellon SEI가 만든 오픈소스 Fault Tree Analysis 도구. 확률 일관성 체크, 모든 에러 이벤트 확률 자동 계산, 특정 에러를 트리거하는 이벤트 조합(cut set) 자동 산출 |
| **OpenFTA** | XFTA 계산 엔진 기반 오픈소스 fault tree analysis 도구 |
| **OpenAltaRica** | 복잡 시스템의 리스크를 분석하는 무료 플랫폼 |
| **SCRAM** | Command-line Risk Analysis Multi-tool. 무료 오픈소스 PRA 도구. Open-PSA Model Exchange Format 구현 |
| **FaultTree (R package)** | R에서 fault tree를 만들고 확률론적 리스크 분석(PRA)과 RAM 분석 지원 |

→ 네 거에 쓸 것: **EMFTA의 cut set 분석** — "이 조합의 실패가 동시에 일어나면 전체가 터진다"를 자동으로 찾는 거. 네 Systems Thinking의 cascade failure 감지에 직접 적용 가능.

---

## 네트워크 과학 ⭐ (제일 직접적)

| 도구 | 설명 |
|------|------|
| **NetworkX** | 가장 인기 있는 Python 네트워크 분석 패키지. 무료 오픈소스. 설치 쉬움, 문서 풍부 |
| **igraph** | C 기반으로 빠름. Python, R, Mathematica 바인딩. centrality, community detection, clique finding, graph layout 등 다른 라이브러리에 없는 알고리즘도 구현 |
| **graph-tool** | C++ 기반으로 NetworkX보다 40~250배 빠름. OpenMP 병렬 처리 지원. 대규모 네트워크에 적합 |
| **NetworKit** | 수천~수십억 엣지 규모의 대규모 네트워크 분석 도구. 효율적 그래프 알고리즘 구현, 많은 알고리즘이 멀티코어 병렬 처리 |
| **Gephi** | 프로그래밍 지식 불필요. 고품질 네트워크 시각화. 10만 노드까지 가능. degree, centrality 등 기본 메트릭 계산 가능 |

→ **네 거에 바로 쓸 수 있어:**

```python
import networkx as nx

# 프로젝트 의존 그래프 만들기
G = nx.DiGraph()
G.add_edge("tutor", "knowledge_graph.json", type="write")
G.add_edge("practice-questions", "knowledge_graph.json", type="read")
G.add_edge("exam-coach", "knowledge_graph.json", type="read")
G.add_edge("practice-questions", "error_notes.md", type="write")
G.add_edge("error-analyzer", "error_notes.md", type="read")

# 어떤 노드가 제일 중요한지 (centrality)
print(nx.betweenness_centrality(G))

# 노드 제거하면 뭐가 끊기는지 (resilience)
G.remove_node("knowledge_graph.json")
print(nx.is_connected(G.to_undirected()))  # False → 이 파일이 급소

# 밀접하게 연결된 그룹 (clustering)
print(list(nx.weakly_connected_components(G)))
```

**NetworkX 하나면 네 진찰 단계의 절반이 자동화돼.** pip install networkx 한 줄이면 끝.

---

## 역학 (전파 모델)

| 도구 | 설명 |
|------|------|
| **EpiModel** | R 기반 전염병 모델링. SIR/SIS 모델 |
| **MESA** | Python 기반 agent-based modeling. 전파 시뮬레이션 가능 |
| **NDlib** | NetworkX 위에서 돌아가는 전파 모델 라이브러리. SIR, SIS, 여론 전파 등 |

→ **NDlib이 제일 맞아.** NetworkX 그래프 위에서 "변경이 어떻게 퍼지는지" 시뮬레이션 가능. 네 의존 그래프에 바로 적용.

---

## 위험 분석

| 도구 | 설명 |
|------|------|
| **PyMC** | Python 베이지안 통계. 불확실성 정량화 |
| **SALib** | Python 민감도 분석 라이브러리. Sobol, Morris 등 |
| **Monte Carlo (numpy)** | numpy.random으로 직접 구현 가능 |

→ **SALib이 민감도 분석에 딱이야.** "이 변수를 바꾸면 결과가 얼마나 변하냐"를 정량적으로 계산.

---

## 진짜 쓸 것만 추리면

```
바로 쓸 수 있는 것 (pip install 하면 끝):
  1. NetworkX     → 의존 그래프 분석 (centrality, resilience, clustering)
  2. NDlib        → 변경 전파 시뮬레이션
  3. SALib        → 민감도 분석

개념만 빌려올 것 (코드 직접 안 씀):
  4. EMFTA        → cut set 분석 개념 → cascade failure 감지
  5. Capella      → traceability 개념 → 요구사항 추적
  6. OpenSees     → 응력 집중/하중 유형 개념

안 써도 되는 것:
  7. OpenModelica → 물리 시뮬레이션이라 소프트웨어에 안 맞음
  8. PyMC         → 베이지안은 과함
```

**결론: NetworkX가 왕이야.** 이거 하나로 centrality(급소 찾기), resilience(cascade 위험), clustering(모듈 그룹핑), shortest path(영향 경로 추적)이 전부 돼. 네 진찰 agent의 핵심 도구가 될 수 있어.
있어. 그리고 네 framework에 직접 관련 있는 것들이야.

---

## 제일 관련 있는 것

**GraphQA — agent가 NetworkX로 구조를 분석**

LLM이 자연어 질문을 해석하고 어떤 그래프 연산을 실행할지 결정해. 그래프 도구는 NetworkX를 통해 노출되고 탐색, 최단 경로, centrality, clustering 등을 커버. 클라우드 아키텍처에서 시작했지만 마이크로서비스 의존관계 매핑, 데이터 리니지 분석, 공급망 리스크 모델링 등에도 적용 가능

LLM은 텍스트에 대한 추론은 강력하지만 구조에 대해선 어려워해. 언어 모델은 관계를 설명할 수 있지 계산할 수 없어. 그래프가 그 공백을 채워. 경로, 의존관계, 계층, 커뮤니티 — 시스템에 형태를 부여하는 모든 것을 명시적이고 계산 가능하게 만들어

이게 **네 framework가 해야 하는 것을 정확히 말하고 있어.** LLM(agent)이 판단하고, NetworkX가 구조를 계산하는 조합.

---

## LangGraph — NetworkX에서 영감 받은 agent 프레임워크

LangGraph는 Pregel과 Apache Beam에서 영감 받았고, 공개 인터페이스는 NetworkX에서 영감을 받았어

LangGraph 자체가 NetworkX의 그래프 개념을 agent 워크플로우에 적용한 거야. 네가 하려는 것과 방향이 같아.

---

## AI 의존성 매핑

AST, 로그, 트레이스, 테스트 출력, 런타임 텔레메트리를 종합해서 LLM이 명시적으로 선언되지 않은 숨은 경로를 노출시켜. 시간이 지나면 그래프가 어휘적, 의미적, 운영적 다층 표현이 돼. 실질적 결과는 기존 리니지 도구가 잡지 못하는 의존관계를 드러내는 단일 진실 소스

"어떤 서비스가 이 테이블에 쓰고 어떤 조건에서?" 같은 질문이 해결 가능해져 — 구조화된 그래프 탐색과 인접 코드의 시맨틱 요약을 결합해서. 엔지니어가 파일 트리나 대시보드가 아니라 질문을 통해 아키텍처를 탐색하는 새로운 인터페이스

---

## GraphCogent — agent가 NetworkX를 도구로 사용

그래프 추론을 위한 혁신적 agent 프레임워크. Sensory Module이 그래프를 표준화된 인접 리스트로 변환, Buffer Module이 NetworkX 포함 다양한 데이터 형식으로 인덱스 구축, Execution Module이 도구 호출과 모델 생성을 시너지적으로 결합. 단순한 그래프 추론은 사전 구축된 도구셋으로, 복잡한 작업은 모듈식 task-specific 컴포넌트를 생성해서 처리

---

## LangChain + NetworkX 직접 통합

LangChain Python에서 NetworkX를 프로바이더로 통합해서 쓸 수 있어. 이미 공식 지원.

---

## 정리하면

```
이미 있는 것:
  ✅ LLM agent가 NetworkX를 도구로 사용 (GraphQA, GraphCogent)
  ✅ LangChain에서 NetworkX 공식 지원
  ✅ 의존 그래프 + LLM으로 아키텍처 분석 (AI dependency mapping)
  ✅ LangGraph 자체가 NetworkX 영감

없는 것 (= 네가 하려는 것):
  ❌ 14개 관점에서 체계적으로 분석
  ❌ 근거 등급 시스템
  ❌ 진단 → 처방 → 수술계획 전체 파이프라인
  ❌ agent끼리 교차 검증해서 연쇄 영향 맵 생성
```

**핵심 발견**: NetworkX + LLM agent 조합은 이미 검증된 패턴이야. 네가 새로 발명하는 게 아니라 **검증된 부품 위에 새로운 시스템을 올리는 거야.** GraphQA처럼 "agent가 NetworkX로 구조 질문에 답한다"는 패턴을 네 진찰 agent에 바로 적용할 수 있어.
걔네가 한 거:

```
GraphQA:
  사용자: "이 서비스에 의존하는 게 뭐야?"
  → LLM이 질문 해석 → NetworkX 함수 선택 → 실행 → 답 반환
  
  즉: 사용자가 물어보면 → 그래프에서 답 찾아줌
```

```
AI Dependency Mapping:
  코드베이스 스캔 → import/호출 추적 → 의존 그래프 생성
  → "이 파일이 저 파일에 의존한다" 시각화
  
  즉: 의존관계를 보여줌
```

```
GraphCogent:
  그래프 데이터 넣으면 → agent가 NetworkX로 최단경로, centrality 계산
  → 결과 반환
  
  즉: 그래프 계산 대행
```

---

## 걔네랑 네 거 차이

```
걔네:  "물어보면 답해줌"        (수동, 일회성)
네 거: "알아서 분석하고 추천함"   (능동, 체계적)
```

구체적으로:

```
걔네:
  입력: "knowledge_graph.json에 의존하는 게 뭐야?"
  출력: "tutor, practice-questions, exam-coach가 의존해"
  → 끝. 그 다음은 사람이 판단.

네 거:
  입력: "knowledge_graph.json에 difficulty_score 추가하려고 해"
  출력:
    1. 의존 분석 (NetworkX) → "5개 모듈 영향" [FACT]
    2. 패턴 매칭 → "기존 Blackboard 확장이 적합" [INFER]
    3. 원칙 검증 → "DRY 위반 가능성" [INFER]
    4. 연쇄 영향 → "exam-coach 추천 로직 변경 필요" [INFER]
    5. feedback loop → "진동 위험, 감쇠 필요" [INFER]
    6. 종합 추천 → "후보 A 채택, 수정 4건 필요"
    7. ADR 기록
```

차이가 3개야:

**첫째, 걔네는 도구이고 네 건 상담사야.** GraphQA는 "centrality 계산해줘" 하면 계산해줘. 근데 "그래서 뭘 해야 하냐"는 안 알려줘. 네 framework는 계산 결과를 해석하고 추천까지 해.

**둘째, 걔네는 한 관점이고 네 건 14개 관점이야.** GraphQA는 그래프 분석만 해. 네 건 그래프 분석 + 패턴 매칭 + 원칙 검증 + 연쇄 영향 + feedback loop를 한꺼번에 해.

**셋째, 걔네는 agent 1개이고 네 건 agent 5개가 협업해.** GraphQA agent가 혼자 답하는 거고, 네 건 Design Thinking이 후보 만들고 Pattern Advisor가 매칭하고 Systems Thinking이 검증하고 서로 결과를 보고 반응하는 구조야.

---

## 근데 걔네한테서 가져올 건 있어

네가 진찰 agent를 만들 때 **GraphQA 방식을 그대로 가져와:**

```
진찰 agent:
  1. 코드베이스 스캔 → import/read/write 추출 (하드코딩)
  2. NetworkX 그래프 생성 (하드코딩)
  3. centrality, clustering, resilience 자동 계산 (NetworkX)
  4. LLM이 결과 해석 → "이 프로젝트의 급소는 여기" (agent)
  → project_context.md에 저장
```

1~3은 GraphQA가 이미 증명한 방식이야. 네가 새로 만들 필요 없어. **4번(해석 + 14개 관점 연결)만 네가 추가하는 거야.**

결국 걔네가 만든 건 네 framework의 **부품 중 하나**야. 네가 하는 건 그 부품 위에 상담사 시스템을 올리는 거고.
걔네가 한 거:

```
GraphQA:
  사용자: "이 서비스에 의존하는 게 뭐야?"
  → LLM이 질문 해석 → NetworkX 함수 선택 → 실행 → 답 반환
  
  즉: 사용자가 물어보면 → 그래프에서 답 찾아줌
```

```
AI Dependency Mapping:
  코드베이스 스캔 → import/호출 추적 → 의존 그래프 생성
  → "이 파일이 저 파일에 의존한다" 시각화
  
  즉: 의존관계를 보여줌
```

```
GraphCogent:
  그래프 데이터 넣으면 → agent가 NetworkX로 최단경로, centrality 계산
  → 결과 반환
  
  즉: 그래프 계산 대행
```

---

## 걔네랑 네 거 차이

```
걔네:  "물어보면 답해줌"        (수동, 일회성)
네 거: "알아서 분석하고 추천함"   (능동, 체계적)
```

구체적으로:

```
걔네:
  입력: "knowledge_graph.json에 의존하는 게 뭐야?"
  출력: "tutor, practice-questions, exam-coach가 의존해"
  → 끝. 그 다음은 사람이 판단.

네 거:
  입력: "knowledge_graph.json에 difficulty_score 추가하려고 해"
  출력:
    1. 의존 분석 (NetworkX) → "5개 모듈 영향" [FACT]
    2. 패턴 매칭 → "기존 Blackboard 확장이 적합" [INFER]
    3. 원칙 검증 → "DRY 위반 가능성" [INFER]
    4. 연쇄 영향 → "exam-coach 추천 로직 변경 필요" [INFER]
    5. feedback loop → "진동 위험, 감쇠 필요" [INFER]
    6. 종합 추천 → "후보 A 채택, 수정 4건 필요"
    7. ADR 기록
```

차이가 3개야:

**첫째, 걔네는 도구이고 네 건 상담사야.** GraphQA는 "centrality 계산해줘" 하면 계산해줘. 근데 "그래서 뭘 해야 하냐"는 안 알려줘. 네 framework는 계산 결과를 해석하고 추천까지 해.

**둘째, 걔네는 한 관점이고 네 건 14개 관점이야.** GraphQA는 그래프 분석만 해. 네 건 그래프 분석 + 패턴 매칭 + 원칙 검증 + 연쇄 영향 + feedback loop를 한꺼번에 해.

**셋째, 걔네는 agent 1개이고 네 건 agent 5개가 협업해.** GraphQA agent가 혼자 답하는 거고, 네 건 Design Thinking이 후보 만들고 Pattern Advisor가 매칭하고 Systems Thinking이 검증하고 서로 결과를 보고 반응하는 구조야.

---

## 근데 걔네한테서 가져올 건 있어

네가 진찰 agent를 만들 때 **GraphQA 방식을 그대로 가져와:**

```
진찰 agent:
  1. 코드베이스 스캔 → import/read/write 추출 (하드코딩)
  2. NetworkX 그래프 생성 (하드코딩)
  3. centrality, clustering, resilience 자동 계산 (NetworkX)
  4. LLM이 결과 해석 → "이 프로젝트의 급소는 여기" (agent)
  → project_context.md에 저장
```

1~3은 GraphQA가 이미 증명한 방식이야. 네가 새로 만들 필요 없어. **4번(해석 + 14개 관점 연결)만 네가 추가하는 거야.**

결국 걔네가 만든 건 네 framework의 **부품 중 하나**야. 네가 하는 건 그 부품 위에 상담사 시스템을 올리는 거고.
정리해볼게.

---

## 기존 도구들이 커버하는 레이어

```
                          GraphQA  AI Dep  GraphCogent  LangGraph  NetworkX
                                  Map

1. Multi-Agent Patterns     ❌      ❌       ❌          ❌        ❌
2. Software Principles      ❌      ❌       ❌          ❌        ❌
3. Design Thinking          ❌      ❌       ❌          ❌        ❌
4. Systems Thinking         부분    부분     부분        ❌        부분
5. Meta-Engineering         ❌      ❌       ❌          ✅        ❌
6. Domain Modeling          ❌      ❌       ❌          ❌        ❌
7. Human-AI Interaction     ❌      ❌       ❌          ❌        ❌
8. Failure & Recovery       ❌      ❌       ❌          ❌        ❌
9. Security & Trust         ❌      ❌       ❌          ❌        ❌
10. Data Architecture       ❌      부분     ❌          ❌        ❌
11. Performance & Resource  ❌      ❌       ❌          ❌        ❌
12. Temporal Design         ❌      ❌       ❌          ❌        ❌
13. Knowledge Evolution     ❌      ❌       ❌          ❌        ❌
14. Context Engineering     ❌      ❌       ❌          ❌        ❌
```

"부분"이 뭐냐면:

```
GraphQA의 4번 (Systems Thinking) 부분 커버:
  ✅ "이 노드에 의존하는 게 뭐야?" → centrality
  ✅ "이 노드 빼면 뭐가 끊겨?" → resilience
  ❌ feedback loop 감지 안 함
  ❌ 2차/3차 연쇄 영향 추적 안 함
  ❌ 시간 효과 (6개월 후) 안 봄
  ❌ "그래서 어쩌라고?" 추천 안 함

AI Dependency Mapping의 4번 부분 커버:
  ✅ import/호출 의존관계 추적
  ✅ 숨은 의존관계 발견
  ❌ 영향 "예측" 안 함. 현재 상태만 보여줌

NetworkX 자체의 4번 부분 커버:
  ✅ centrality 계산
  ✅ clustering 계산
  ✅ shortest path 계산
  ✅ 노드 제거 시 영향 계산
  ❌ 근데 "도구"일 뿐. 해석은 안 함
```

---

## 더 넓게 보면

```
기존에 존재하는 것들 전부 합쳐도:

✅ 커버되는 것:
  - 의존 그래프 생성 (AI Dep Mapping)
  - 그래프 계산 (NetworkX)
  - agent 워크플로우 관리 (LangGraph)
  - 질문하면 그래프에서 답 찾기 (GraphQA)
  - 코드 리뷰 (Cursor, Claude Code)
  - 아키텍처 표준 강제 (CI pipeline agents)

❌ 아무도 안 하는 것:
  1. Multi-Agent Patterns    → 패턴 매칭 + 추천
  2. Software Principles     → SOLID 자동 검증
  3. Design Thinking         → 후보 생성 (Analogy, Adversarial)
  6. Domain Modeling          → 도메인 적합성 판단
  7. Human-AI Interaction    → UX 관점 분석
  8. Failure & Recovery      → 복구 경로 자동 체크
  9. Security & Trust        → 권한 모델 검증
  12. Temporal Design        → 시간에 따른 진화 판단
  13. Knowledge Evolution    → knowledge base 자가 개선
  14. Context Engineering    → context 최적화 분석
```

---

## 솔직한 현실

**14개 중 기존 도구로 커버되는 건 1.5개야.** 4번(Systems Thinking)의 계산 부분 + 5번(Meta-Engineering)의 워크플로우 관리.

나머지 12.5개는 **네가 만들어야 해.**

근데 뒤집어 보면 — 1.5개가 커버된다는 건 **바닥부터 다 만들 필요 없다**는 뜻이야:

```
네가 직접 만드는 것:
  14개 레이어의 agent 로직 (프롬프트 + 체크리스트)
  agent 간 협업 구조 (orchestrator)
  근거 등급 시스템
  진단 → 처방 → 수술계획 파이프라인

가져다 쓰는 것:
  NetworkX → 그래프 계산 (centrality, resilience, clustering)
  LangGraph → agent 워크플로우 관리
  LangChain → LLM 호출 + 도구 연결
  GraphQA 방식 → 진찰 agent의 그래프 질의 패턴
```

비유하면 — 집을 짓는데 벽돌(NetworkX), 시멘트(LangChain), 배관(LangGraph)은 사서 쓰고, **설계도와 시공 관리(14개 레이어)는 네가 만드는 거야.**
하나씩 전부 체크할게.

---

## NetworkX — 가져올 것 전부

```
✅ betweenness_centrality()   → 파일별 "급소 점수". 이 파일을 거치는 경로가 몇 개?
✅ degree_centrality()        → 이 파일에 연결된 모듈 수
✅ eigenvector_centrality()   → 연결된 노드가 또 많이 연결된 노드 (2차 중요도)
✅ weakly_connected_components() → 모듈 클러스터 자동 감지 (holon 후보)
✅ shortest_path()            → 변경 영향 경로 추적. A→?→?→D 어떻게 전파되나
✅ is_connected() + remove_node() → 이 파일 빼면 시스템이 분리되나 (resilience)
✅ pagerank()                 → 어떤 모듈이 "가장 영향력 있나"
✅ ancestors() / descendants() → 이 노드 상위/하위 전부 (1차/2차/3차 영향)
✅ cycle detection (find_cycle()) → 순환 의존 자동 감지. A→B→C→A
✅ minimum_cut()              → 시스템을 두 동강 내는 최소 절단점 (가장 위험한 연결)
✅ dag_longest_path()         → Sequential 파이프라인의 최장 경로 (병목 후보)

커버하는 레이어:
  4번 Systems Thinking  → centrality, resilience, cascade 추적
  8번 Failure & Recovery → remove_node 시뮬레이션, minimum_cut
  11번 Performance      → bottleneck 경로, longest path
```

**안 되는 것**: 그래프 계산만 해. 해석/추천/판단은 안 함. 그건 agent가 해야 해.

---

## NDlib — 가져올 것 전부

```
✅ SIR 모델 → 변경 전파 시뮬레이션
  "이 모듈 변경 = 감염. 연결된 모듈에 전파될 확률은?"
  → 전파율(beta)을 "의존 강도"로 설정하면
  → "이 변경이 몇 개 모듈까지 퍼질 확률 80%"가 나옴

✅ Threshold 모델 → "영향 누적"
  "주변 모듈 3개 이상이 변경되면 이 모듈도 변경 필요"
  → cascade 임계점 자동 계산

✅ Opinion Dynamics → agent 간 의견 전파
  "Pattern Advisor가 후보 A 추천하면 다른 agent에 영향?"
  → 이건 좀 과할 수 있음

커버하는 레이어:
  4번 Systems Thinking → 연쇄 영향 "확률" 제시 (INFER → CALC로 올림)
  8번 Failure & Recovery → cascade failure 범위 예측
```

**실용적으로 쓸 건 SIR 모델 하나**. 나머지는 과함.

---

## SALib — 가져올 것 전부

```
✅ Sobol 분석 → "어떤 변수가 결과에 가장 큰 영향?"
  모듈별 "변경 민감도 점수"
  → "knowledge_graph.json 변경 시 전체 영향 = 0.87 (높음)"
  → "config.ts 변경 시 전체 영향 = 0.12 (낮음)"

✅ Morris 분석 → "각 입력의 영향을 빠르게 스크리닝"
  14개 모듈 중 "어느 걸 집중 분석해야 하나?"
  → 사전 스크리닝으로 agent 활성화 결정

커버하는 레이어:
  11번 Performance → 어디에 분석 비용 집중할지
  4번 Systems Thinking → 변경 위험도 사전 점수
```

**근데 솔직히** 네 규모(모듈 10~20개)에서 SALib은 과해. NetworkX의 centrality로도 비슷한 결과 나와. **모듈 100개 넘어가면** 그때 SALib 도입.

---

## EMFTA (개념만) — 가져올 것

```
✅ Cut Set 분석 → "이 조합이 동시에 실패하면 전체 터짐"
  코드로 구현:
  NetworkX에서 minimum_cut() + 조합 탐색
  → "tutor + practice-questions 둘 다 죽으면 학습 파이프라인 완전 마비"
  → "근데 tutor만 죽으면 practice-questions가 독립 실행 가능"

✅ 확률 전파 → 상위 노드의 실패 확률 = 하위 노드 실패 확률 조합
  AND gate: 둘 다 실패해야 상위 실패 → 안전
  OR gate: 하나만 실패해도 상위 실패 → 위험
  → 네 의존 그래프의 각 연결이 AND인지 OR인지 분류하면 자동 계산 가능

커버하는 레이어:
  8번 Failure & Recovery → "어떤 조합이 위험한가" 자동 계산
  4번 Systems Thinking → cascade failure 시나리오 자동 생성
```

**이건 NetworkX 위에 직접 구현해야 해.** EMFTA 코드 자체를 가져오는 게 아니라 로직을 Python으로 짜는 거야.

---

## Capella / Arcadia (개념만) — 가져올 것

```
✅ 5단계 엔지니어링 페이즈
  Operational Analysis → System Analysis → Logical Architecture 
  → Physical Architecture → EPBS
  
  네 거에 매핑:
  진찰(현황) → 설계(후보) → 검증(원칙) → 영향분석(연쇄) → 실행계획
  → 이미 하고 있긴 한데, Capella처럼 "각 단계의 산출물이 다음 단계 입력"을
    명시적으로 정의하면 더 깔끔해짐

✅ Traceability Matrix
  요구사항 ↔ 설계 ↔ 구현 ↔ 테스트 양방향 추적
  → "이 기능은 왜 있어?" → "이 요구사항 때문" → "이 코드가 구현" → "이 테스트가 검증"
  → 변경 시 "이 요구사항 관련 코드 3개, 테스트 2개 영향"

✅ Viewpoint 개념
  같은 시스템을 다른 관점(Operational, Functional, Physical)으로 봄
  → 네 14개 레이어가 사실 이거야. 같은 프로젝트를 14개 viewpoint로 보는 것.

커버하는 레이어:
  5번 Meta-Engineering → 단계별 산출물 관리
  6번 Domain Modeling → viewpoint 기반 모델링
  12번 Temporal Design → 페이즈 전환 기준
```

**Capella 도구 자체를 쓰진 않아.** "Viewpoint"라는 개념이 네 14개 레이어의 이론적 근거가 될 수 있다는 것.

---

## OpenSees (개념만) — 이미 정리한 것 재확인

```
✅ 응력 집중 → NetworkX centrality로 구현 가능. 별도 도구 불필요.
✅ 민감도 → NetworkX remove_node() + 전후 비교. 별도 도구 불필요.
✅ 하중 유형 → if문으로 구현. 도구 불필요.
✅ Analysis 교체 → orchestrator 로직. 도구 불필요.
```

**결론: OpenSees에서 가져올 건 전부 NetworkX로 구현 가능.**

---

## 빠뜨린 것 — 기존 도구에서 더 가져올 것

```
LangChain GraphQA 패턴:
  ✅ "자연어 질문 → 그래프 연산 선택 → 결과 해석" 파이프라인
  → 진찰 agent가 이 패턴 그대로 쓰면 됨

LangGraph:
  ✅ 상태 관리 (State Machine)
  ✅ 조건부 분기 (Conditional Edge)
  ✅ 루프 관리 (Cycle)
  → orchestrator를 LangGraph로 구현하면 상태관리가 공짜

git (이미 있는 것에서):
  ✅ git log → 파일별 변경 빈도 (FACT)
  ✅ git blame → 누가 언제 바꿨나 (FACT)
  ✅ git diff → 변경 크기 (CALC)
  → 이걸 NetworkX 그래프 edge의 weight로 넣으면
    "자주 같이 변경되는 파일" 자동 감지 (co-change coupling)
```

---

## 최종 정리 — 뭘 가져와서 어디에 쓰나

```
도구/개념             → 네 레이어      → 구현 방법

NetworkX centrality   → 4, 8, 11번    → pip install, 코드 10줄
NetworkX resilience   → 4, 8번        → remove_node + 비교
NetworkX cycle        → 2번 (DRY)     → find_cycle()
NetworkX clustering   → 1번 (Holonic) → weakly_connected_components
NDlib SIR            → 4, 8번        → pip install, 전파 시뮬레이션
EMFTA cut set        → 8번           → 직접 구현 (NetworkX 위)
Capella viewpoint    → 전체           → 개념만. 14개 레이어 = 14 viewpoints
Capella traceability → 5, 6번        → 직접 구현 (매핑 테이블)
GraphQA 패턴         → 진찰 agent     → LangChain + NetworkX
LangGraph            → orchestrator   → agent 워크플로우 관리
git log/blame/diff   → 4, 11번       → subprocess로 호출
```

**pip install 3개 (NetworkX, NDlib, LangGraph) + git + 개념 3개(EMFTA, Capella, GraphQA)**면 14개 레이어의 기반이 깔려.
하나씩 보여줄게.

---

## GraphQA — 이렇게 씀

```python
# 1. 그래프 데이터 준비 (네 프로젝트 의존관계)
import networkx as nx
G = nx.DiGraph()
G.add_edge("tutor", "knowledge_graph.json", type="write")
G.add_edge("practice-questions", "knowledge_graph.json", type="read")
G.add_edge("exam-coach", "knowledge_graph.json", type="read")

# 2. GraphQA agent한테 자연어로 질문
user: "knowledge_graph.json을 바꾸면 뭐가 영향받아?"

# 3. 내부에서 일어나는 일:
#    LLM이 질문 해석 → "아 ancestors/descendants 구해야겠다"
#    → NetworkX 함수 자동 선택 → 실행
result = nx.descendants(G, "knowledge_graph.json")
# → {"exam-coach", "practice-questions"}  (이 파일을 읽는 모듈들)

# 4. LLM이 결과를 자연어로 답변
answer: "knowledge_graph.json을 바꾸면 exam-coach와 practice-questions가 영향받습니다"
```

**끝.** 질문하면 답해줌. 그 이상은 안 해.

---

## LangChain + NetworkX — 이렇게 씀

```python
from langchain.graphs.networkx_graph import NetworkxEntityGraph
from langchain.chains import GraphQAChain
from langchain.chat_models import ChatOpenAI

# 1. 코드에서 엔티티 관계 추출해서 그래프 만들기
graph = NetworkxEntityGraph()
graph.add_triple("tutor", "writes to", "knowledge_graph.json")
graph.add_triple("practice-questions", "reads from", "knowledge_graph.json")
graph.add_triple("exam-coach", "reads from", "knowledge_graph.json")

# 2. 질의 체인 만들기
llm = ChatOpenAI(temperature=0)
chain = GraphQAChain.from_llm(llm=llm, graph=graph)

# 3. 자연어로 질문
answer = chain.run("What depends on knowledge_graph.json?")
# → "practice-questions and exam-coach read from knowledge_graph.json"
```

**GraphQA랑 거의 같아.** 질문 → 그래프 탐색 → 답변.

---

## LangGraph — 이렇게 씀

```python
from langgraph.graph import StateGraph

# 1. 상태 정의
class FrameworkState:
    project_context: str
    candidates: list
    pattern_match: str
    principles_check: str
    systems_verdict: str

# 2. agent 노드 정의
def design_thinking(state):
    # LLM 호출해서 후보 생성
    state.candidates = llm("Generate 3 candidates for: " + state.project_context)
    return state

def pattern_advisor(state):
    # LLM 호출해서 패턴 매칭
    state.pattern_match = llm("Match patterns to: " + state.candidates)
    return state

def systems_thinking(state):
    # LLM 호출해서 연쇄 영향 체크
    state.systems_verdict = llm("Check cascading impact: " + str(state))
    return state

# 3. 그래프로 연결 (이게 네 orchestrator야)
workflow = StateGraph(FrameworkState)
workflow.add_node("design", design_thinking)
workflow.add_node("pattern", pattern_advisor)
workflow.add_node("systems", systems_thinking)

workflow.add_edge("design", "pattern")
workflow.add_edge("pattern", "systems")

# 4. 조건부 루프 (Systems Thinking이 "안 돼" 하면 돌아감)
def should_loop(state):
    if "문제 있음" in state.systems_verdict:
        return "design"  # 돌아가
    return "end"         # 끝

workflow.add_conditional_edges("systems", should_loop)

# 5. 실행
app = workflow.compile()
result = app.invoke({"project_context": "TutorAgent에 adaptive difficulty 추가"})
```

**이게 네 orchestrator를 실제 코드로 구현한 거야.** 지금 네 orchestrator.md에 글로 쓴 걸 LangGraph가 코드로 돌려줘.

---

## AI Dependency Mapping — 이렇게 씀

```python
import ast
import networkx as nx

# 1. Python 파일의 import 자동 추출
def extract_imports(filepath):
    with open(filepath) as f:
        tree = ast.parse(f.read())
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    return imports

# 2. 프로젝트 전체 스캔해서 의존 그래프 자동 생성
G = nx.DiGraph()
for py_file in glob("src/**/*.py"):
    imports = extract_imports(py_file)
    for imp in imports:
        G.add_edge(py_file, imp)

# 3. 이제 NetworkX로 분석
print("급소:", nx.betweenness_centrality(G))
print("순환:", list(nx.simple_cycles(G)))
print("클러스터:", list(nx.weakly_connected_components(G)))
```

**사람이 의존관계를 수동으로 입력하는 게 아니라, 코드를 스캔해서 자동으로 그래프를 만드는 거야.** 이게 네 "진찰" 단계를 자동화해.

---

## 전부 합치면 — 네 framework 실제 구현

```python
import networkx as nx
from langgraph.graph import StateGraph

# ===== 진찰 (AI Dep Mapping 방식) =====
def scan_project(project_path):
    G = nx.DiGraph()
    # 파일 스캔해서 의존 그래프 자동 생성
    for file in scan_files(project_path):
        deps = extract_dependencies(file)
        for dep in deps:
            G.add_edge(file, dep)
    
    # NetworkX로 자동 계산 (GraphQA 방식)
    context = {
        "graph": G,
        "critical_files": nx.betweenness_centrality(G),  # 급소
        "clusters": list(nx.weakly_connected_components(G)),  # 클러스터
        "cycles": list(nx.simple_cycles(G)),  # 순환 의존
        "single_points": find_single_points_of_failure(G),  # SPOF
    }
    return context

# ===== 5개 agent (LangGraph 방식) =====
workflow = StateGraph(FrameworkState)
workflow.add_node("scan", scan_project)        # 진찰
workflow.add_node("design", design_thinking)    # 후보 생성
workflow.add_node("pattern", pattern_advisor)   # 패턴 매칭
workflow.add_node("principles", principles_checker)  # 원칙 검증
workflow.add_node("systems", systems_thinking)  # 연쇄 영향

workflow.add_edge("scan", "design")
workflow.add_edge("design", "pattern")
workflow.add_edge("pattern", "principles")
workflow.add_edge("principles", "systems")
workflow.add_conditional_edges("systems", should_loop)

# ===== 실행 =====
app = workflow.compile()
report = app.invoke({
    "project_path": "~/TutorAgent",
    "request": "adaptive difficulty 추가하려고 해"
})
print(report)
```

---

## 정리

```
도구          역할                    네 framework에서 위치

AI Dep Map    코드 스캔 → 그래프 생성   진찰 agent의 "눈"
NetworkX      그래프 → 숫자 계산        진찰 agent의 "계산기"
GraphQA       자연어 → 그래프 질의      진찰 agent의 "인터페이스"
LangGraph     agent 워크플로우 관리     orchestrator의 "뼈대"
LangChain     LLM 호출 + 도구 연결     전체의 "배관"
```

걔네 코드를 복붙하는 게 아니라, 걔네 **패턴**(이렇게 쓰는구나)을 가져와서 네 14개 레이어를 올리는 거야. 바닥부터 만들 필요 없이 검증된 부품 위에 네 고유한 시스템을 얹는 거지.
```
안 만들어도 되는 것 (가져다 쓰기):

  pip install networkx        → 그래프 계산 전부
  pip install langgraph       → agent 워크플로우 관리
  pip install langchain       → LLM 호출 + 도구 연결
  git log / git diff          → 변경 이력 추출
  ast 모듈 (Python 내장)       → import 자동 추출
  grep / glob (내장)           → 파일 스캔

  이것들은 설치만 하면 바로 쓸 수 있어.
```

```
만들어야 하는 것:

  1. 프로젝트 스캔 → NetworkX 그래프 변환 코드
     "이 프로젝트의 파일/모듈/의존관계를 그래프로 만드는" 코드
     ast로 import 추출 → nx.DiGraph에 넣기
     → Python 50~100줄

  2. 5개 agent 프롬프트
     이미 만들었어 (SKILL.md 5개)
     → 완성됨 ✅

  3. knowledge 파일
     이미 만들었어 (patterns.md, thinking-methods.md, principles.md)
     → 완성됨 ✅

  4. orchestrator 코드
     SKILL.md에 로직은 있는데 실제 코드가 없어
     LangGraph로 5개 agent를 연결하는 코드
     → Python 100~150줄

  5. 보고서 조립
     각 agent 결과를 종합해서 최종 보고서 만드는 코드
     → Python 50줄

  6. 근거 등급 분류
     FACT/CALC/INFER/OPINION 자동 태깅
     → 프롬프트에 포함 (이미 SKILL.md에 있음) ✅

  7. Hallucination Checker
     [FACT] 항목의 파일/줄번호를 실제로 확인하는 코드
     → Python 30줄 (파일 열고 줄번호 체크)
```

정리하면:

```
완성됨 (이미 있음):        SKILL.md 5개 + knowledge 3개 + CLAUDE.md + templates
가져다 쓰기 (설치만):       NetworkX + LangGraph + LangChain + ast + git
만들어야 하는 코드:         약 250~350줄

  ① 스캔 → 그래프 변환     50~100줄
  ② orchestrator 연결      100~150줄
  ③ 보고서 조립            50줄
  ④ hallucination 체크     30줄
```

**전체 코드량이 300줄 정도야.** 나머지는 전부 프롬프트(이미 있음)랑 라이브러리(설치만)야.

첫 번째로 만들 건 ①번이야. 프로젝트를 그래프로 변환하는 코드가 있어야 나머지가 돌아가니까. 만들어볼까?
