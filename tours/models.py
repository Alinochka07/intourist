from django.db import models



class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views_quantity = models.IntegerField(default=0)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'тур'
        verbose_name_plural = 'Туры'
        ordering = ['created_date']
