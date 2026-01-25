from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    housing_type = models.CharField(max_length=20,choices=[('house', 'Casa'),('apartment', 'Departamento')],blank=True)
    has_other_pets = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='profiles/',null=True,blank=True)

    def __str__(self):
        return self.user.username


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # Si el usuario se acaba de crear...
    if created:
        # ...creamos el perfil usando la clase definida arriba
        UserProfile.objects.get_or_create(user=instance)