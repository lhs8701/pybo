from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)  # CharField 글자수의 길이가 제한된 텍스트
    content = models.TextField()  # TextField 글자 수 제한이 없는 텍스트
    create_date = models.DateTimeField()  # DateTimeField 날짜와 시간에 관계된 속성
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # ForeignKey : 다른 모델과 연결하기 위해 사용
    # on_delete 삭제 될 경우 답변도 함께 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User,related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
