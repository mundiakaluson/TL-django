from django.db import models

class Order(models.Model):

    LEVEL = (

        ('School', 'School'),
        ('College', 'College'),
        ('University', 'University'),
        ('Masters', 'Masters'),
        ('PHD', 'PHD')
    )

    words = models.CharField(max_length=32)
    level = models.CharField(max_length=32,
                            choices=LEVEL,
                            default='College'
                            )

