from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    year = models.TextField(
        choices=YEAR_IN_SCHOOL_CHOICES,
    )

    def __str__(self):
        return self.owner.get_full_name() + f" (Year {str(self.year)})"



class PromDate(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    year = models.TextField(
        choices=YEAR_IN_SCHOOL_CHOICES,
    )

    class Meta:
        verbose_name = "Crush"
        verbose_name_plural = "Crushes"
    def __str__(self):
        return self.profile.__str__() + f" likes {self.name} (Year {self.year})"
