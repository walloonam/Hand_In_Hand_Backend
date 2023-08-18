# Hand-In-Hand Backend (Django)

![image](https://github.com/walloonam/Hand_In_Hand_Backend/assets/80560040/08a2a9d8-e6a4-48cb-85b1-f9afa8fc4ef7)

Hand-In-Hand Backend 프로젝트는 디지털 정보의 격차를 줄이기 위한 홈페이지의 Django 백엔드 부분을 담당합니다. 이 프로젝트는 변화하는 현대 사회의 기술을 어려워 하는 사람들에게 간편하게 도움을 주고 받을 수 있는 채팅 웹사이트를 구축하는 것을 목표로 합니다.

## 프로젝트 소개

현대 사회에서 기술의 발전으로 디지털 정보의 양이 무척 많아졌습니다. 하지만 이에 대한 접근성이나 이해도에는 격차가 존재합니다. Hand-In-Hand Backend는 이러한 격차를 줄이기 위해 사용자들이 쉽게 도움을 얻을 수 있는 환경을 제공합니다.

### 주요 기능

- **출석체크 및 포인트 획득:** 사용자들은 매일 출석체크를 통해 포인트를 얻을 수 있습니다. 이 포인트를 나중에 물건을 구매하는 데 사용할 수 있습니다.
- **채팅 기능:** 사용자들은 웹사이트를 통해 간편한 채팅을 할 수 있습니다. 채팅이 채택되면 사용자는 포인트를 얻게 됩니다.
- **포인트를 통한 물건 구매:** 사용자들은 얻은 포인트로 추후에 물건을 구매할 수 있습니다.

## 기술 스택

- **Backend:** Django 프레임워크를 사용하여 백엔드 서버를 구축하였습니다.
- **실시간 채팅:** 실시간 채팅 기능을 구현하기 위해 WebSocket을 활용했습니다.
- **데이터베이스 캐싱:** Redis를 사용하여 데이터베이스 쿼리를 캐싱하였습니다.

## 설치 및 실행 방법

1. 이 저장소를 클론합니다:
```bash
git clone https://github.com/walloonam/Hand_In_Hand_Backend.git
```
2. 필요한 종속성을 설치합니다:
```bash
pip install -r requirements.txt
```
3. 데이터베이스 마이그레이션을 수행합니다:
```bash
python manage.py migrate
```
4. 서버실
```bash
python manage.py runserver
```
#기여 방법

이 프로젝트에 기여하려면 다음 단계를 따라주세요:

1. 이 저장소를 포크합니다.
2. 새로운 브랜치를 생성하여 작업합니다: git checkout -b feature/your-feature-name
3. 변경 사항을 커밋하고 푸시합니다: git commit -m "Add some feature" -> git push origin feature/your-feature-name
4. 포크한 저장소에서 Pull Request를 생성합니다.

