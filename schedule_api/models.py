from django.db import models

subjects = [('MATH-1', 'Math-1'),('MATH-2', 'Math-2'),('PHYSICS','Physics'),('CHEMISTRY','Chemistry'),('RELIGEON','Religeon'),('SSTUDIES','Social Studies'),
 ('GAMES','Games'),('BENG-1','Bengali-1'),('BENG-2','Bengali-2'),('ENG-1','English-1'),('ENG-2','English-2'),('GEOGRAPHY','Geography'),('DRAWING','Drawing'),
 ('PSYCHO','Psychology'),('PHYLO','Philosophy'),('CSC','Computer Science')]


# Create your models here.
class Subjects(models.Model):
    subject_id = models.BigAutoField(primary_key=True)
    subject_name = models.CharField(max_length=10,choices=subjects)
    subject_weight = models.IntegerField()

    def __str__(self):
        return f"{self.subject_name}:{self.subject_weight}"

class Teachers(models.Model):
    teacher_id = models.BigAutoField(primary_key=True)
    teacher_name = models.CharField(max_length=20)
    teaching_subjects = models.ManyToManyField(Subjects)
    


