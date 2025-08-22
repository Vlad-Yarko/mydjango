from django.db import models


# Many to one / one to many


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# One to one


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    level = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.level
    
    
# many to many


class Student(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name="courses")
    
    def __str__(self):
        return self.title   
