from locust import HttpUser, task, between, SequentialTaskSet

# 비회원 시나리오
class GuestUser(HttpUser):
    wait_time = between(1, 3)

    # 비회원 뉴스 페이지 조회 시나리오
    @task(2)
    def view_news(self):
        self.client.get("/api/news/", name="비회원 뉴스 페이지 조회")

    # 비회원 게시판 페이지 조회 시나리오
    @task(3)
    def view_board(self):
        self.client.get("/api/board/posts/", name="비회원 게시판 페이지 조회")

    # 비회원 경기 일정 조회 시나리오
    @task(2)
    def view_event_schedule(self):
        self.client.get("/api/event/schedules/", name="비회원 경기 일정 조회")

    # 비회원 이벤트 참여 페이지 조회 시나리오
    @task(3)
    def view_event_part(self):
        self.client.get("/api/event/participate/", name="비회원 이벤트 참여 페이지 조회")

    # @task(3)
    # def go_signup(self):
    #     self.client.post("/api/user/signup/", name="비회원 회원가입 페이지 이동")

# 회원 시나리오
# class RegisteredUser(HttpUser):
#     # 로그인한 사용자 역할
#     wait_time = between(2, 5)

#     @task
#     def login(self):
#         # 로그인 로직을 여기에 구현
#         pass

#     @task(2)
#     def my_page(self):
#         self.client.get("/mypage", name="마이페이지 조회")

#     @task(1)
#     def participate_event(self):
#         self.client.post("/event/participate", name="이벤트 참여")