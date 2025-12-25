from django.db import models

# Create your models here.
class Certificate(models.Model):
    certificate_id = models.CharField(max_length=100, unique=True)
    student_id = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    institution = models.CharField(max_length=150)
    issue_date = models.DateField()
    certificate_hash = models.CharField(max_length=256)
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"{self.student_name} - {self.course}"
        