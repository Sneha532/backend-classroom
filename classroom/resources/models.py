from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='profile_pics', blank=True)
    roles = [
        ('s', 'student'),
        ('t', 'teacher')
    ]
    role = models.CharField(
        max_length=2,
        choices=roles,
        default='-'
    )

class classSubject(models.Model):
    titleClass = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    codeClasse = models.CharField(max_length=10)
    creationDateClasse = models.DateField()
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)

class JoinClass(models.Model):
    classId = models.ForeignKey(classSubject, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)

class course(models.Model):
    desc = models.TextField(max_length=50)
    creationDateCourse = models.DateField()
    courseFile = models.FileField(upload_to='documents', null=True)
    course = models.ForeignKey(classSubject, on_delete=models.CASCADE)

class TD(models.Model):
    titleTd = models.CharField(max_length=50)
    creationDateTd = models.DateField()
    tdFile = models.FileField(upload_to='documents', null=True)
    course = models.ForeignKey(classSubject, on_delete=models.CASCADE)

class TP(models.Model):
    titleTp = models.CharField(max_length=50)
    creationDateTp = models.DateField()
    tpFile = models.FileField(upload_to='documents', null=True)
    course = models.ForeignKey(classSubject, on_delete=models.CASCADE)

class correction_TD_TP(models.Model):
    title = models.CharField(max_length=50)
    creationDateTdTp = models.DateField()
    corrFile = models.FileField(upload_to='documents', null=True)
    course = models.ForeignKey(classSubject, on_delete=models.CASCADE)

class Todo(models.Model):
    title = models.CharField(max_length=50)
    creationDateTodo = models.DateField()
    TodoTFile = models.FileField(upload_to='documents', null=True)
    TodoSFile = models.FileField(upload_to='documents', null=True)
    course = models.ForeignKey(classSubject, on_delete=models.CASCADE)


class Resource(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('in_use', 'In Use'), ('maintenance', 'Maintenance')])
    last_maintenance = models.DateField()


class SecurityAlert(models.Model):
    alert_type = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.alert_type
    

class Attendance(models.Model):
    classSubject = models.ForeignKey(classSubject, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.ManyToManyField(Users, related_name='present_users')
    absent = models.ManyToManyField(Users, related_name='absent_users')

    def __str__(self):
        return f"Attendance Report for {self.classSubject.titleClass} on {self.date}"