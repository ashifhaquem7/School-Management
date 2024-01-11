from django.db import models
from django.dispatch import receiver
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    role_id = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    joindate = models.DateField(auto_now_add=True)
    salary = models.CharField(max_length=20,blank=True, null=True)
    mobile = models.CharField(max_length=40,blank=True,null=True)
    status = models.CharField(max_length=1,blank=True,null=True)
    objects = models.Manager()

    def __str__(self):
        return self.user.first_name
    class Meta:
        db_table = 'school_teacher'
        managed = True
        verbose_name_plural = 'Teacher'


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    roll = models.CharField(max_length=12, blank=True, null=True)
    mobile = models.CharField(max_length=12, null=True, blank=True)
    fee = models.CharField(max_length=50, blank=True, null=True)
    class1 = models.CharField(max_length=10,blank=True,null=True)
    status = models.CharField(max_length=1,blank=True,null=True,default='T')

    def __str__(self) -> str:
        return self.user.first_name
    
    class Meta:
        db_table = 'school_student'
        managed = True
        verbose_name_plural = 'Student'
    
class Notice (models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=True)
    byy= models.CharField(max_length=20, null=True,default='school')
    message = models.CharField(max_length=200)

    def __str__(self)->str:
        return self.date

    class Meta:
        db_table = 'school_notice'
        managed = True
        verbose_name_plural = 'Notice'

class Attendence(models.Model):
    id = models.AutoField(primary_key=True)
    roll = models.CharField(max_length=10, null=True)
    date = models.DateField()
    class1 = models.CharField(max_length=10)
    present_status = models.CharField(max_length=30)

    def __str__(self):
        return self.roll
    
    class Meta:
        db_table = 'school_attendence'
        managed = True
        verbose_name_plural = 'Attendence'



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender,instance,created,**kwrargs):
    if created:
        if instance.role_id == 66:
            Teacher.objects.create(user=instance)    
        elif instance.role_id == 99:
            Student.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender,instance,**kwrargs):
    if instance.role_id == 66:
        teacher_profile = instance.teacher
        if teacher_profile:
            teacher_profile.save()
    elif instance.role_id == 99:
        student_profile = instance.student
        if student_profile:
            student_profile.save()
        