# MLOps 중국어 학습 커리큘럼

> DeepSeek / Qwen / Zhihu / CSDN 같은 중국어 MLOps 자료를 영어 자료 없이 직접 읽기 위한 4개월 커리큘럼.

[English](README.md) · [中文版](README.zh.md)

---

## 왜 만들었나

중국에서 LLM·MLOps 분야 SOTA 연구가 대량 쏟아지고 있는데, 실무자 수준의 깊이 있는 논의는 대부분 중국어에서 이루어집니다. ModelScope의 모델 카드, Zhihu의 트러블슈팅 스레드, CSDN의 엔지니어링 글, 掘金의 구현 후기 — 기계 번역으로는 표면 의미만 잡힐 뿐 미공개 벤치마크나 모호한 에러 처리 같은 디테일은 빠져나갑니다.

이 커리큘럼은 **말하기·듣기를 의도적으로 제외**하고 4개월 안에 중국어 MLOps 자료를 실용적 수준으로 읽고 쓰는 데 도달하는 게 목표입니다.

## 누구를 위한 것인가

- 개발자 백그라운드를 가진 학습자
- 회화가 아닌 **읽기 능력**이 필요한 사람
- 평일 45분 + 주말 90분 정도를 4개월간 투자할 수 있는 사람

## 의도적으로 제외한 것

- 말하기 연습
- 듣기 학습
- 성조 암기 (식별 정도만)
- HSK 시험 대비

## 4개월 후 도달 지점

- DeepSeek / Qwen / GLM 공식 문서를 DeepL 없이 1차 독해
- Zhihu·CSDN 기술 게시글을 네이티브 페이스로 통독
- 중국 오픈소스 프로젝트에 GitHub Issue 중국어 작성·제출
- Zhihu 또는 CSDN에 300자 이상 중국어 답변 게시

## 전체 로드맵

| 기간 | 단계 | 산출물 |
|------|------|--------|
| Month 1 | 한자·문법 뼈대 | 한자 500자 + 핵심 문법 15개 + 도메인 어휘 200개 |
| Month 2 | 기술 문서 독해 | DeepSeek/Qwen README 5건, 논문 abstract 10건 |
| Month 3 | 커뮤니티 독해 | 누적 한자 1,000자, 도메인 어휘 400개 |
| Month 4 | 쓰기·실전 | GitHub Issue 1건 + Zhihu 답변 1건 작성 |

## 레포 구조

```
.
├── README.md              ← 영어 (GitHub 기본 노출)
├── README.ko.md           ← 한국어 (이 파일)
├── README.zh.md           ← 중국어
│
├── docs/
│   ├── ko/
│   │   ├── grammar.md     ← 문법 15개 예문집
│   │   ├── github-issue-template.md
│   │   └── checklist.md   ← 16주 주간 체크리스트
│   ├── en/                ← 영어 버전
│   └── zh/                ← 중국어 버전
│
├── vocab/
│   ├── mlops-domain-vocab.csv    ← 다국어 통합 마스터 파일
│   └── build/                    ← 언어별 빌드 결과 (gitignored)
│
└── scripts/
    └── build_vocab.py            ← 언어별 Anki CSV 빌드
```

## 시작하기

```bash
git clone https://github.com/<your-handle>/mlops-chinese-curriculum.git
cd mlops-chinese-curriculum

# 언어별 Anki 임포트용 CSV 생성
python3 scripts/build_vocab.py

# vocab/build/ 디렉토리에 결과 파일 생성됨
#   vocab-ko.csv  ← Front: 한자 | Back: 한국어 (병음)
#   vocab-en.csv  ← Front: 한자 | Back: 영어 (병음)
#   vocab-zh.csv  ← Front: 한자 | Back: 병음만
```

Anki에 임포트: `파일 → 가져오기 → vocab/build/vocab-ko.csv`. Front 필드는 "front", Back 필드는 "back"으로 매핑.

## 학습 원칙

1. **읽기·쓰기만 한다.** 발음은 한자 식별 보조 수단.
2. **도메인 어휘 우선.** 일상 회화 단어 외울 시간에 `推理` `部署` `量化` 외우기.
3. **DeepL은 검증용.** 1차는 직접, DeepL은 교차 확인용.
4. **실전 자료로 빨리 옮긴다.** 교재는 1개월차에 졸업.
5. **목표는 산출물.** Issue 1건 + Zhihu 답변 1건 작성으로 완주 판정.

## 한국어 화자의 가속 효과

이 커리큘럼은 **한국어 화자 기준**으로 설계됨. 한국어 한자어 직관이 한자 학습 부담을 절반 가까이 줄여줍니다.

| 중국어 | 한국 한자음 | 의미 |
|--------|-------------|------|
| 模型 | 모형 | 모델 |
| 训练 | 훈련 | training |
| 部署 | 부서 | deploy |
| 容器 | 용기 | container |
| 集群 | 집군 | cluster |

다만 **함정 단어**는 주의:
- `汽车` (기차) = 자동차 (한국어 기차 ≠ 중국어 汽车)
- `工夫` (공부) = 노력·시간 (공부는 学习)
- `新闻` (신문) = 뉴스 (신문은 报纸)

## 상세 자료

### 강의 시리즈

| # | 제목 | 분량 |
|---|------|------|
| 01 | [지금이 중국어를 읽어야 하는 날](docs/ko/lecture-intro.md) | ~12분 |
| 02 | [왜 도메인 어휘부터 외우는가](docs/ko/lecture-02.md) | ~9분 |
| 03 | [문법 15개로 충분한 이유](docs/ko/lecture-03.md) | ~9분 |
| 04 | [첫 ModelScope 모델 카드 같이 읽기](docs/ko/lecture-04.md) | ~11분 |

위 4개 강의는 본격 학습 전에 한 번씩 보시는 도입 시리즈입니다. 회화·듣기를 제외한 학습이 왜 가능한지(intro), 무엇부터 외울지(02), 문법은 어디까지 필요한지(03), 실제 자료를 어떻게 풀어내는지(04)를 차례로 다룹니다.

### 학습 가이드 (실제 강의 자료)

각 강의(영상)에 대응하는 본격 학습 자료입니다. 읽기만 해도 이해되도록 서술형 + 풍부한 예시로 작성했습니다.

| # | 제목 | 분량 |
|---|------|------|
| **00** | **[중국어 0단계 — 한 번도 본 적 없는 사람의 시작점](docs/ko/guide-00-foundations.md)** | 30-45분 통독 |
| 01 | [학습 전략과 4개월 계획](docs/ko/guide-01-curriculum.md) | 30분 통독 |
| 02 | [어휘 마스터 (입문 → 220개 졸업)](docs/ko/guide-02-vocabulary.md) | 45분 통독 + 매주 참조 |
| 03 | [문법 마스터 (15문형 입문 → 심화)](docs/ko/guide-03-grammar.md) | 60분 통독 + 매 문형 5번 만날 때마다 재참조 |
| 04 | [모델 카드 독해 (5단락 졸업)](docs/ko/guide-04-model-card.md) | 60분 통독 + 모델 카드 1편 읽을 때마다 참조 |

**가이드 00은 중국어를 한 번도 본 적 없는 분의 진입로**입니다. 한자가 무엇인지, 부수가 어떻게 의미를 만드는지, 병음·사성을 어떻게 다루는지를 처음부터 자세히 풀어 드립니다. 가이드 01-04를 시작하기 전에 한 번 통독하시기를 강력히 권장합니다.

### 보조 자료

- [문법 예문집 (15개 + 보너스 4개)](docs/ko/grammar.md)
- [GitHub Issue 중국어 템플릿](docs/ko/github-issue-template.md)
- [16주 주간 체크리스트](docs/ko/checklist.md)

## 도구 스택

| 도구 | 용도 | 비용 |
|------|------|------|
| [Anki](https://apps.ankiweb.net/) | 한자·어휘 SRS | 무료 (모바일 유료) |
| [Pleco](https://www.pleco.com/) | 한자 사전 (필수) | 무료 |
| [DeepL](https://www.deepl.com/) | 번역 검증 | 무료 |
| [Immersive Translate](https://immersivetranslate.com/) | 브라우저 이중 표시 | 무료 |
| HelloChinese | 병음 입문 (Week 1만) | 무료 |

## 기여 환영

다음 PR 환영:

- 번역 수정 (모든 언어)
- 새 도메인 어휘 (특히 에이전트, 로봇, 멀티모달 등 신생 분야)
- 실제 자료에서 추출한 예문으로 가공 예문 교체
- 추가 언어 버전 (일본어, 베트남어 등)

어휘 추가 시 마스터 파일(`vocab/mlops-domain-vocab.csv`)만 수정. 언어별 CSV는 자동 생성됩니다.

## 라이선스

MIT — 자유롭게 fork·수정·재배포 가능.
