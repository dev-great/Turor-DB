from django.db import models
# Create your models here.

class Subjects(models.Model):
    subject= models.CharField(max_length=100)
    publisheddate= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publisheddate',)


    def __str__(self):
        return self.subject

class Syllable(models.Model):

    subject= models.ForeignKey(Subjects, on_delete=models.CASCADE,)
    Syllable = models.CharField(max_length=1000)
    publisheddate= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publisheddate',)


    def __str__(self):
        return self.Syllable[:100]