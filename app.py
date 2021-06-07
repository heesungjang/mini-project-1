from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """
    Moive 26 메인 페이지로 영화 리스트 불러와서 index.html 랜더링
    """
    return render_template("index.html")

@app.route("/auth/login")
def login():
    """
    여기서 로그인 기능 구현
    """
    pass

@app.route("/auth/signup")
def signup():
    """
    여기서 회원가입 기능 구현
    """
    pass

@app.route("movie/:movie_id")
def movie_detail():
    """
    여기서 상세 페이지 정보 불러오기
    """
    pass

@app.route("/movie/comment")
def comment():
    """
    여기서 댓글 기능 구현
    """
    pass

@app.route("/movie/like")
def like():
    """
    여기서 좋아요 기능 구현
    """
    pass




    