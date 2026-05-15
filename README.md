# pjt-08 Travels API

Django REST Framework 기반의 여행 장소 및 접근성 후기 API입니다.

## 실행 방법

### Git Bash

```bash
source .venv/Scripts/activate
python manage.py migrate
python manage.py runserver
```

### PowerShell

```powershell
.\.venv\Scripts\activate
python manage.py migrate
python manage.py runserver
```

서버 실행 후 아래 주소로 접속합니다.

```text
http://127.0.0.1:8000/api/places/
```

## 관리자 페이지

장소 데이터는 관리자 페이지에서 등록합니다.

```bash
python manage.py createsuperuser
python manage.py runserver
```

```text
http://127.0.0.1:8000/admin/
```

## 샘플 데이터

관리자 페이지를 쓰기 전에 샘플 장소와 후기를 바로 넣어볼 수 있습니다.

```bash
python manage.py loaddata sample_data
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

## 리뷰 작성 예시

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

## 검색 예시

```text
/api/places/search/?q=서울
/api/places/search/?keyword=휠체어
/api/places/search/?q=서울&keyword=경사로
```

## 테스트

```bash
python manage.py test
```
