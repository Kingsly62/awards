from django.db import models

# Create your models here.


from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=40)
    author=models.CharField(max_length=40,default="Anonymous")
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title