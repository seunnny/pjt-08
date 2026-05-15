# pjt-08 Travels API

Django REST Framework 기반 여행 장소와 접근성 후기 API입니다.

## 실행

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API

| Method | URL | 설명 |
| --- | --- | --- |
| GET | `/api/places/` | 전체 여행 장소 목록 조회 |
| GET | `/api/places/<place_pk>/` | 단일 여행 장소 상세 조회 |
| GET | `/api/reviews/` | 전체 접근성 후기 목록 조회 |
| GET | `/api/reviews/<review_pk>/` | 단일 접근성 후기 조회 |
| PUT | `/api/reviews/<review_pk>/` | 접근성 후기 수정 |
| DELETE | `/api/reviews/<review_pk>/` | 접근성 후기 삭제 |
| POST | `/api/places/<place_pk>/reviews/` | 특정 장소에 접근성 후기 작성 |
| GET | `/api/places/search/?q=장소명&keyword=휠체어` | 장소 이름과 접근성 키워드 기반 검색 |

## 요청 예시

```json
{
  "title": "휠체어 접근이 편했습니다",
  "content": "입구 경사로와 엘리베이터가 있어 이동이 쉬웠습니다.",
  "accessibility_keywords": "휠체어, 경사로, 엘리베이터",
  "rating": 5
}
```
