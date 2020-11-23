from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=100 ,verbose_name='Subject')
    message = models.TextField(verbose_name='Message')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return f'{self.name} - {self.email}'
