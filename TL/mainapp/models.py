from django.db import models

class Order(models.Model):

    LEVEL = (

        ('School', 'School'),
        ('College', 'College'),
        ('University', 'University'),
        ('Masters', 'Masters'),
        ('PHD', 'PHD')
    )

    LANGUAGE = (

        ('English UK', 'English UK'),
        ('English US', 'English US'),
        ('English CA', 'English CA'),
        ('English AU', 'English AU'),
        ('Other', 'Other')
    )

    words = models.CharField(max_length=32)
    level = models.CharField(max_length=32,
                            choices=LEVEL,
                            default='College'
                            )
    language

