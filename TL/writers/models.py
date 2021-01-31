from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save


class Profile(models.Model):

    PROFESSION = (

        ('Writer', 'Writer'),
        ('Programmer', 'Programmer'),
        ('Biologist', 'Biologist'),
        ('Mathematician', 'Mathematician'),
        ('Other', 'Other')
    )

    RANKING = (

        ('Level 1', 'Level 1'),
        ('Level 2', 'Level 2'),
        ('Level 3', 'Level 3'),
        ('Level 4', 'Level 4'),
        ('Level 5', 'Level 5')
    )

    STATUS = (

        ('Probation', 'Probation'),
        ('Beginner', 'Beginner'),
        ('Under Investigation', 'Under Investigation'),
        ('Novice', 'Novice'),
        ('Expert', 'Expert')
    )
    user = models.OneToOneField(User, on_delete=CASCADE, related_name='user_profile')
    phone = models.CharField(max_length=64, blank=True, null=True)
    profession = models.CharField(max_length=124, choices=PROFESSION, default='Writer', help_text='Type of Employee')
    ranking = models.CharField(max_length=128, choices=RANKING, help_text='Employees are ranked from level 1-5 according to their expertise.')
    rating = models.CharField(max_length=128, choices=STATUS, help_text="Status of the employee's account")

    def __str__(self):
        return "%s's Profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

