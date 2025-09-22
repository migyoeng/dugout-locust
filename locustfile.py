from locust import HttpUser, task, between, SequentialTaskSet

class GuestUser(HttpUser):
    # 일반 방문자 역할
    wait_time = between(1, 3)

    @task(3)  # 가중치 3: 가장 자주 실행되는 작업
    def view_news(self):
        self.client.get("/news", name="뉴스 페이지 조회")

    @task(1)  # 가중치 1: 상대적으로 덜 자주 실행
    def view_info(self):
        self.client.get("/info", name="선수 및 구단 정보 조회")

class RegisteredUser(HttpUser):
    # 로그인한 사용자 역할
    wait_time = between(2, 5)

    @task
    def login(self):
        # 로그인 로직을 여기에 구현
        pass

    @task(2)
    def my_page(self):
        self.client.get("/mypage", name="마이페이지 조회")

    @task(1)
    def participate_event(self):
        self.client.post("/event/participate", name="이벤트 참여")