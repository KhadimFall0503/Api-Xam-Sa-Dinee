from django.db import models

class Rubrique(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image_url = models.ImageField(upload_to='uploads/images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Contenu(models.Model):
    rubrique = models.ForeignKey(Rubrique, related_name='contenus', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    video_url = models.URLField(blank=True, null=True)  # optionnel
    text_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
