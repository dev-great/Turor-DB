from django.db import models

class TutorModel(models.Model):
    tutor = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=100)
    location = models.CharField(max_length=16)
    subjects = models.CharField(max_length=50)
    image = models.ImageField(upload_to='documents/')
    publisheddate= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publisheddate',)


    def __str__(self):
        return self.tutor

