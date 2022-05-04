from django.urls import path, re_path
from .views import(
     MyQuizListAPI, QuizListAPI, QuizDetailAPI, SaveUsersAnswer, SubmitQuizAPI
)

urlpatterns = [
	path("my-quizzes/", MyQuizListAPI.as_view()),
	path("quizzes/", QuizListAPI.as_view()),
	path("save/", SaveUsersAnswer.as_view()),
	re_path(r"quizzes/(?P<slug>[\w\-]+)/$", QuizDetailAPI.as_view()),
	re_path(r"quizzes/(?P<slug>[\w\-]+)/submit/$", SubmitQuizAPI.as_view()),
]