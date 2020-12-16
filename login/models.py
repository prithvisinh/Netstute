from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from faculty.models import *
#account
class MyUserManager(BaseUserManager):
    def create_user(self, enrollment, first_name, last_name, Email, password=None):
        if not enrollment:
            raise ValueError('Users must have an enrollment')
        user = self.model(
            enrollment= enrollment,
            first_name= first_name,
            last_name= last_name,
            Email = Email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, enrollment, first_name, last_name, Email, password=None):
        user = self.create_user(
            enrollment,
            first_name,
            last_name,
            Email,
            password=password,
        )
        user.is_admin = True
        user.is_Faculty=True
        user.is_HOD=True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    enrollment = models.BigIntegerField(
        verbose_name='enrollment',
        unique=True,
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    Email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_HOD = models.BooleanField(default=False)
    is_Faculty = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    objects = MyUserManager()

    USERNAME_FIELD = 'enrollment'
    REQUIRED_FIELDS = ['first_name','last_name','Email']


    def has_perm(self, perm, obj=None):
    	return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_superuser(self):
        return self.is_staff

    def is_staff(self):
        return self.is_admin

    def __str__(self):
       return str(self.enrollment)



# login

class Field(models.Model):
    course = models.CharField(max_length = 10)
    field = models.CharField(max_length = 10)

    def __str__(self):
	    return self.field

class Faculty(models.Model):
	Enrollment = models.ForeignKey(Account, verbose_name='Enrollment', on_delete=models.CASCADE)
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	is_HOD = models.BooleanField(default=False)

	def __str__(self):
		return str(self.Enrollment)

class subjectList(models.Model):
    Subject = models.CharField(max_length=30)
    shortname = models.CharField(max_length=5)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    semister =models.IntegerField()
    
    def __str__(self):
        return self.shortname

class Classroom(models.Model):
    classname = models.CharField(max_length=20)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    subject = models.ForeignKey(subjectList,on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)

    def __str__(self):
        return self.classname

class Student(models.Model):
    Enrollment = models.ForeignKey(Account, verbose_name='Enrollment', on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    classname = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Enrollment)


class SubjectUpload(models.Model):
    classname = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    subject = models.ForeignKey(subjectList, on_delete=models.CASCADE)
    filename = models.CharField(max_length=30)
    video = models.FileField(upload_to=f'lecture/')

    def __str__(self):
        return self.filename