from django.db import models

# Create your models here.
class Topic(models.Model):
    """Um assunto sobnre o qual o usuário está aprendendo"""
    text= models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text 

    class Meta:
        verbose_name_plural = 'Topics'

class Entry(models.Model):
    """Algo específico aprendido sobre um tópico"""
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    text=models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name_plural = "Entries" 

    def __str__(self):
        return self.text[:50] + '...'


    