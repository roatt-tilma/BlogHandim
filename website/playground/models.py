from django.db import models

class Answer(models.Model):
    idanswer = models.IntegerField(primary_key=True)
    idquestion = models.IntegerField()
    idwriter = models.IntegerField()
    totalpoints = models.IntegerField(blank=True, null=True)
    numberofevaluations = models.IntegerField(blank=True, null=True)  
    upvotes = models.IntegerField(blank=True, null=True)
    downvotes = models.IntegerField(blank=True, null=True)
    answer = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'answer'

    def __str__(self):
        return self.answer

class Question(models.Model):
    idquestion = models.IntegerField(primary_key=True)
    question = models.CharField(unique=True, max_length=255)
    iddomain = models.IntegerField()
    asked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'question'

    def __str__(self):
        return self.question
