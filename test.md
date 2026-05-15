---

# 2인 역할 분담안 및 구현 상태

## 팀원 A - 프로젝트 세팅 / 장소 기능 담당

| 담당 요구사항 | 작업 내용 | 상태 |
| --- | --- | --- |
| F801 프로젝트 구성 | Django 프로젝트 및 `travels` 앱 생성 | 완료 |
| F802 Place 클래스 | 여행 장소 데이터를 저장할 `Place` 모델 구현 | 완료 |
| F804 Serializer 클래스 일부 | `PlaceSerializer` 구현 | 완료 |
| F805 place_list | 전체 여행 장소 목록 조회 API 구현 | 완료 |
| F806 place_detail | 단일 여행 장소 상세 조회 API 구현 | 완료 |
| NF802 RESTful 원칙 | 장소 관련 URL 구조 정리 | 완료 |
| NF803 HTTP Method 허용 | 장소 조회 API는 GET 요청만 허용되도록 구현 | 완료 |

### A 담당 파일

```text
config/settings.py
config/urls.py
travels/models.py
travels/serializers.py
travels/urls.py
travels/views.py
```

### A 주요 API

```http
GET /api/places/
GET /api/places/<place_pk>/
```

---

## 팀원 B - 접근성 후기 / 생성·수정·삭제 담당

| 담당 요구사항 | 작업 내용 | 상태 |
| --- | --- | --- |
| F803 Review 클래스 | 장소에 대한 접근성 후기를 저장할 `Review` 모델 구현 | 완료 |
| F804 Serializer 클래스 일부 | `ReviewSerializer` 구현 | 완료 |
| F807 review_list | 전체 접근성 후기 목록 조회 API 구현 | 완료 |
| F808 review_detail | 단일 접근성 후기 조회, 수정, 삭제 API 구현 | 완료 |
| F809 create_review | 특정 장소에 접근성 후기를 작성하는 API 구현 | 완료 |
| F810 AI 활용 | 장소 이름과 접근성 키워드 기반 검색 기능 구현 | 완료 |
| NF801 Git 활용 | 브랜치 관리, merge 충돌 확인, commit convention 관리 | 별도 수행 필요 |

### B 담당 파일

```text
travels/models.py
travels/serializers.py
travels/urls.py
travels/views.py
README.md
travels/tests.py
```

### B 주요 API

```http
GET /api/reviews/
GET /api/reviews/<review_pk>/
PUT /api/reviews/<review_pk>/
DELETE /api/reviews/<review_pk>/
POST /api/places/<place_pk>/reviews/
GET /api/places/search/
```

---

# 구현된 기능 요약

## 모델

- `Place`: 여행 장소 이름, 주소, 설명, 접근성 정보, 위도, 경도 저장
- `Review`: 특정 장소에 연결된 접근성 후기, 키워드, 평점 저장
- `Review.place`는 `Place`를 참조하며, 장소 삭제 시 후기도 함께 삭제됨

## Serializer

- `PlaceSerializer`: 장소 정보와 `reviews_count` 제공
- `ReviewSerializer`: 후기 정보와 `place`, `place_name` 제공

## View/API

- 장소 목록 조회
- 장소 상세 조회
- 후기 목록 조회
- 후기 상세 조회
- 후기 수정
- 후기 삭제
- 특정 장소에 후기 생성
- 장소명, 주소, 설명, 접근성 정보, 후기 키워드, 후기 내용 기반 검색

## 테스트

`travels/tests.py`에 다음 테스트를 추가했습니다.

- 장소 목록 조회
- 장소 상세 조회
- 장소 API가 GET만 허용되는지 확인
- 후기 목록 조회
- 후기 생성
- 후기 수정
- 후기 삭제
- 검색 기능

## 샘플 데이터

`travels/fixtures/sample_data.json`에 샘플 장소 2개와 후기 2개를 추가했습니다.

```bash
python manage.py loaddata sample_data
```

---

# 실행 순서

```bash
source .venv/Scripts/activate
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

관리자 페이지에서 장소 데이터를 먼저 등록합니다.

```text
http://127.0.0.1:8000/admin/
```

이후 API를 확인합니다.

```text
http://127.0.0.1:8000/api/places/
http://127.0.0.1:8000/api/reviews/
```

---

# 남은 수동 작업

## 관리자 계정 생성

`createsuperuser`는 비밀번호 입력이 필요하므로 직접 실행해야 합니다.

```bash
python manage.py createsuperuser
```

## Git 브랜치/커밋 정리

현재 기능 구현은 완료되어 있으므로 제출 전에 브랜치와 커밋 메시지만 팀 규칙에 맞게 정리하면 됩니다.

예시:

```bash
git checkout -b develop
git add .
git commit -m "feat: implement travels accessibility review API"
```
