from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60, default = 'Anonimo')
    image = models.ImageField(upload_to='post_images/', default='default.jpg')  # Aquí se añade el campo de imagen

    def __str__(self):
        return self.title

    
