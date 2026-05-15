---

# 2인 역할 분담안

## 팀원 A — 프로젝트 세팅 / 장소 기능 담당

| 담당 요구사항 | 작업 내용 |
| --- | --- |
| F801 프로젝트 구성 | Django 프로젝트 및 `travels` 앱 생성 |
| F802 Place 클래스 | 여행 장소 데이터를 저장할 `Place` 모델 구현 |
| F804 Serializer 클래스 일부 | `PlaceSerializer` 구현 |
| F805 place_list | 전체 여행 장소 목록 조회 API 구현 |
| F806 place_detail | 단일 여행 장소 상세 조회 API 구현 |
| NF802 RESTful 원칙 | 장소 관련 URL 구조 정리 |
| NF803 HTTP Method 허용 | 장소 조회 API는 GET 요청만 허용되도록 구현 |

### A가 맡으면 좋은 파일

```text
config/settings.py
config/urls.py
travels/models.py
travels/serializers.py
travels/urls.py
travels/views.py
```

### A의 주요 구현 예시

```http
GET /api/places/
GET /api/places/<place_pk>/
```

---

## 팀원 B — 접근성 후기 / 생성·수정·삭제 담당

| 담당 요구사항 | 작업 내용 |
| --- | --- |
| F803 Review 클래스 | 장소에 대한 접근성 후기를 저장할 `Review` 모델 구현 |
| F804 Serializer 클래스 일부 | `ReviewSerializer` 구현 |
| F807 review_list | 전체 접근성 후기 목록 조회 API 구현 |
| F808 review_detail | 단일 접근성 후기 조회, 수정, 삭제 API 구현 |
| F809 create_review | 특정 장소에 접근성 후기를 작성하는 API 구현 |
| F810 AI 활용 | 장소 이름과 접근성 키워드 기반 검색 기능 구현 |
| NF801 Git 활용 | 브랜치 관리, merge 충돌 확인, commit convention 관리 |

### B가 맡으면 좋은 파일

```text
travels/models.py
travels/serializers.py
travels/urls.py
travels/views.py
README.md
```

### B의 주요 구현 예시

```http
GET /api/reviews/
GET /api/reviews/<review_pk>/
PUT /api/reviews/<review_pk>/
DELETE /api/reviews/<review_pk>/
POST /api/places/<place_pk>/reviews/
GET /api/places/search/
```

---

# 추천 개발 순서

## 1단계 — 같이 정해야 하는 것

처음에는 둘이 같이 이 정도만 먼저 정하면 됩니다.

| 항목 | 결정 내용 |
| --- | --- |
| 프로젝트명 | `galsuitshu` 또는 `config` |
| 앱 이름 | `travels` |
| 모델 | `Place`, `Review` |
| DB | SQLite |
| API 방식 | Django REST Framework |
| Git 브랜치 | `develop`, `feature/place`, `feature/review` |

---

## 2단계 — A 먼저 작업

A가 먼저 기본 프로젝트와 장소 모델을 만들어야 B가 후기 기능을 붙이기 쉽습니다.

```text
1. Django 프로젝트 생성
2. travels 앱 생성
3. settings.py 앱 등록
4. Place 모델 구현
5. PlaceSerializer 구현
6. place_list, place_detail 구현
7. 기본 URL 연결
```

---

## 3단계 — B 작업

A가 `Place` 모델을 만들면 B는 그 위에 `Review`를 연결하면 됩니다.

```text
1. Review 모델 구현
2. ReviewSerializer 구현
3. review_list 구현
4. review_detail 구현
5. create_review 구현
6. 검색 기능 구현
```

---

# Git 브랜치 분담

| 브랜치명 | 담당자 | 작업 |
| --- | --- | --- |
| `main` | 공통 | 최종 제출용 |
| `develop` | 공통 | 개발 통합 브랜치 |
| `feature/place` | 팀원 A | 프로젝트 세팅, Place 모델/API |
| `feature/review` | 팀원 B | Review 모델/API, 검색 기능 |

---

# 최종 역할 요약

| 팀원 | 역할 | 핵심 책임 |
| --- | --- | --- |
| 팀원 A | 장소 데이터 담당 | 프로젝트 세팅, 장소 모델, 장소 조회 API |
| 팀원 B | 접근성 후기 담당 | 후기 모델, 후기 CRUD, 검색 기능, Git 관리 |

---

이렇게 나누면 구현 난이도도 낮고, 예시 템플릿의 `Movie / Review` 구조처럼 자연스럽게 나뉩니다.

실제로는 **A가 Place를 먼저 만들고**, B가 그 Place를 참조하는 Review를 붙이는 순서로 진행하면 됩니다.
