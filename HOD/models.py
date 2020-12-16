from django.db import models
from login.models import *

class timetableHOD(models.Model):
    Enrollment = models.ForeignKey(Account, verbose_name='Enrollment', on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    timetable = models.FileField(upload_to='time_table/Faculty/')
   
    def __str__(self):
        return str(self.Enrollment)


class timetableStudent(models.Model):
    Field =models.ForeignKey(Field, on_delete=models.CASCADE)
    timetable = models.FileField(upload_to='time_table/student/')