# pjt-08 Travels API

## 프로젝트 소개

여행 장소와 장소별 접근성 후기를 관리하는 Django REST Framework 기반 API 프로젝트입니다.

사용자는 여행 장소 목록을 조회하고, 특정 장소에 접근성 후기를 작성할 수 있습니다. 후기에는 경사로, 엘리베이터, 휠체어 이동 가능 여부 같은 접근성 키워드를 함께 남길 수 있습니다.

이 프로젝트는 화면 중심 웹 서비스가 아니라 JSON 데이터를 주고받는 API 서버입니다.

## 개발 환경

| 항목 | 내용 |
| --- | --- |
| Language | Python 3.11 |
| Framework | Django 5.2.14 |
| API | Django REST Framework |
| Database | SQLite |
| App | `travels` |

## 팀원 역할 분담

### 팀원 A - 프로젝트 세팅 / 장소 기능

| 담당 요구사항 | 작업 내용 |
| --- | --- |
| F801 프로젝트 구성 | Django 프로젝트 및 `travels` 앱 생성 |
| F802 Place 클래스 | 여행 장소 데이터를 저장할 `Place` 모델 구현 |
| F804 Serializer 클래스 일부 | `PlaceSerializer` 구현 |
| F805 place_list | 전체 여행 장소 목록 조회 API 구현 |
| F806 place_detail | 단일 여행 장소 상세 조회 API 구현 |
| NF802 RESTful 원칙 | 장소 관련 URL 구조 정리 |
| NF803 HTTP Method 허용 | 장소 조회 API는 GET 요청만 허용 |

### 팀원 B - 접근성 후기 / 수정 / 삭제 / 검색

| 담당 요구사항 | 작업 내용 |
| --- | --- |
| F803 Review 클래스 | 장소에 대한 접근성 후기를 저장할 `Review` 모델 구현 |
| F804 Serializer 클래스 일부 | `ReviewSerializer` 구현 |
| F807 review_list | 전체 접근성 후기 목록 조회 API 구현 |
| F808 review_detail | 단일 접근성 후기 조회, 수정, 삭제 API 구현 |
| F809 create_review | 특정 장소에 접근성 후기를 작성하는 API 구현 |
| F810 AI 활용 | 장소 이름과 접근성 키워드 기반 검색 기능 구현 |
| NF801 Git 활용 | 기능 단위 작업 및 변경 사항 관리 |

## 모델 구조

### Place

여행 장소 정보를 저장합니다.

| 필드 | 설명 |
| --- | --- |
| `name` | 장소 이름 |
| `address` | 주소 |
| `description` | 장소 설명 |
| `accessibility_info` | 접근성 정보 |
| `latitude` | 위도 |
| `longitude` | 경도 |
| `created_at` | 생성 시각 |
| `updated_at` | 수정 시각 |

### Review

장소에 대한 접근성 후기를 저장합니다.

| 필드 | 설명 |
| --- | --- |
| `place` | 후기가 연결된 장소 |
| `title` | 후기 제목 |
| `content` | 후기 내용 |
| `accessibility_keywords` | 접근성 키워드 |
| `rating` | 평점, 1점부터 5점 |
| `created_at` | 생성 시각 |
| `updated_at` | 수정 시각 |

`Review`는 `Place`를 ForeignKey로 참조합니다. 장소가 삭제되면 해당 장소의 후기도 함께 삭제됩니다.

## 주요 기능

- 전체 여행 장소 목록 조회
- 단일 여행 장소 상세 조회
- 전체 접근성 후기 목록 조회
- 단일 접근성 후기 조회
- 특정 장소에 접근성 후기 작성
- 접근성 후기 수정
- 접근성 후기 삭제
- 장소 이름, 주소, 설명, 접근성 키워드 기반 검색
- Django admin을 통한 장소 및 후기 데이터 관리

## 실행 방법

### 1. 가상환경 활성화

Git Bash:

```bash
source .venv/Scripts/activate
```

PowerShell:

```powershell
.\.venv\Scripts\activate
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. DB 마이그레이션

```bash
python manage.py migrate
```

### 4. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

### 5. 서버 실행

```bash
python manage.py runserver
```

서버 실행 후 아래 주소로 접속합니다.

```text
http://127.0.0.1:8000/api/places/
```

## 관리자 페이지

장소 데이터는 관리자 페이지에서 등록할 수 있습니다.

```text
http://127.0.0.1:8000/admin/
```

## 샘플 데이터

관리자 페이지에서 직접 데이터를 입력하기 전에 샘플 장소와 후기를 넣어볼 수 있습니다.

```bash
python manage.py loaddata sample_data
```

샘플 데이터 적용 후 아래 URL에서 확인합니다.

```text
http://127.0.0.1:8000/api/places/
http://127.0.0.1:8000/api/reviews/
```

## API 목록

| Method | URL | 설명 |
| --- | --- | --- |
| GET | `/api/places/` | 전체 여행 장소 목록 조회 |
| GET | `/api/places/<place_pk>/` | 단일 여행 장소 상세 조회 |
| GET | `/api/reviews/` | 전체 접근성 후기 목록 조회 |
| GET | `/api/reviews/<review_pk>/` | 단일 접근성 후기 조회 |
| PUT | `/api/reviews/<review_pk>/` | 접근성 후기 수정 |
| DELETE | `/api/reviews/<review_pk>/` | 접근성 후기 삭제 |
| POST | `/api/places/<place_pk>/reviews/` | 특정 장소에 접근성 후기 작성 |
| GET | `/api/places/search/?q=장소명&keyword=키워드` | 장소 이름, 주소, 설명, 접근성 키워드 기반 검색 |

## API 사용 예시

### 장소 목록 조회

```http
GET /api/places/
```

### 장소 상세 조회

```http
GET /api/places/1/
```

### 후기 작성

```http
POST /api/places/1/reviews/
Content-Type: application/json
```

```json
{
  "title": "접근성이 좋았어요",
  "content": "입구에 경사로가 있고 엘리베이터가 있어서 이동이 편했습니다.",
  "accessibility_keywords": "휠체어, 경사로, 엘리베이터",
  "rating": 5
}
```

### 후기 수정

```http
PUT /api/reviews/1/
Content-Type: application/json
```

```json
{
  "title": "수정한 후기",
  "content": "엘리베이터 위치가 찾기 쉬웠고 이동 경로가 넓었습니다.",
  "accessibility_keywords": "엘리베이터, 휠체어",
  "rating": 4
}
```

### 후기 삭제

```http
DELETE /api/reviews/1/
```

### 검색

```text
/api/places/search/?q=서울
/api/places/search/?keyword=휠체어
/api/places/search/?q=서울&keyword=경사로
```

## RESTful 설계

이 프로젝트는 URL에는 자원을 표현하고, 행위는 HTTP Method로 표현하도록 구성했습니다.

| 목적 | URL | Method |
| --- | --- | --- |
| 장소 목록 조회 | `/api/places/` | GET |
| 장소 상세 조회 | `/api/places/1/` | GET |
| 후기 목록 조회 | `/api/reviews/` | GET |
| 후기 상세 조회 | `/api/reviews/1/` | GET |
| 후기 수정 | `/api/reviews/1/` | PUT |
| 후기 삭제 | `/api/reviews/1/` | DELETE |
| 장소에 후기 작성 | `/api/places/1/reviews/` | POST |

`/api/deleteReview/1/`처럼 URL에 행동을 직접 쓰지 않고, `/api/reviews/1/`에 DELETE 요청을 보내는 방식으로 설계했습니다.

## 테스트

테스트 실행:

```bash
python manage.py test
```

테스트한 내용:

- 장소 목록 조회
- 장소 상세 조회
- 장소 조회 API가 GET만 허용되는지 확인
- 후기 목록 조회
- 후기 생성
- 후기 수정
- 후기 삭제
- 검색 기능

## 트러블슈팅

### 1. Django 6.0.5 설치 실패

문제:

```text
ERROR: Could not find a version that satisfies the requirement Django==6.0.5
Requires-Python >=3.12
```

원인:

현재 환경은 Python 3.11이었고, Django 6.0.x는 Python 3.12 이상을 요구했습니다.

해결:

Python 3.11에서 사용 가능한 Django 5.2.14로 변경했습니다.

```txt
Django==5.2.14
```

### 2. Git Bash에서 가상환경 활성화 명령어 오류

문제:

```bash
.\.venv\Scripts\activate
```

Git Bash에서는 PowerShell 방식의 경로를 그대로 사용할 수 없었습니다.

해결:

Git Bash에서는 아래 명령어를 사용했습니다.

```bash
source .venv/Scripts/activate
```

### 3. 후기 작성 URL 오타

문제:

```text
/api/places/1/reivews/
```

`reviews`를 `reivews`로 잘못 입력해서 404가 발생했습니다.

해결:

정확한 URL로 다시 요청했습니다.

```text
/api/places/1/reviews/
```

### 4. PUT 요청 시 일부 필드만 보내면 수정 실패 가능

문제:

후기 수정 API는 `PUT` 방식이므로 일부 필드만 보내면 필수 필드 누락 오류가 발생할 수 있습니다.

해결:

수정할 때는 `title`, `content`, `accessibility_keywords`, `rating`을 모두 포함해서 요청했습니다.

## 배운 점

- Django 프로젝트와 앱의 기본 구조를 이해했습니다.
- 모델을 정의하고 마이그레이션을 통해 DB 테이블로 반영하는 흐름을 익혔습니다.
- ForeignKey를 사용해서 `Place`와 `Review`의 1:N 관계를 구성했습니다.
- Django REST Framework의 Serializer를 사용해 모델 데이터를 JSON으로 변환했습니다.
- `@api_view`를 사용해 HTTP Method별 API 동작을 제한했습니다.
- RESTful API에서는 URL이 자원을 표현하고, 행위는 GET, POST, PUT, DELETE 같은 HTTP Method가 표현한다는 점을 배웠습니다.
- Django admin을 통해 데이터를 직접 등록하고 관리하는 방법을 익혔습니다.
- 테스트 코드를 작성해 API가 의도대로 동작하는지 검증하는 방법을 배웠습니다.
- Python/Django 버전 호환성과 가상환경의 필요성을 경험했습니다.

## 프로젝트 마무리 상태

구현 완료:

- Place 모델 및 조회 API
- Review 모델 및 CRUD API
- 장소별 후기 작성 API
- 장소 및 접근성 키워드 검색 API
- 관리자 페이지 등록
- 샘플 데이터
- API 테스트
- README 문서 정리

추가로 개선할 수 있는 점:

- 장소 생성, 수정, 삭제 API 추가
- 로그인 사용자별 후기 작성 권한 관리
- 페이지네이션 적용
- 외부 관광 데이터 API 연동
