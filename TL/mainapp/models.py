from django.db import models
from django.utils import timezone

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

    SOURCES = (

        ("1", "1"), 
        ("2", "2"), 
        ("3", "3"), 
        ("4", "4"), 
        ("5", "5"), 
        ("6", "6"), 
        ("7", "7"), 
        ("8", "8"),
        ("8+", "8+"), 
    )

    STYLE = (

        ('APA', 'APA'),
        ('MLA', 'MLA'),
        ('Havard', 'Havard'),
        ('Chicago', 'Chicago'),
        ('Turbia', 'Turbian'),
        ('Other', 'Other'),
    )

    words = models.CharField(max_length=32, help_text="Number of words, e.g: 300")

    level = models.CharField(max_length=32,
                            choices=LEVEL,
                            default='College'
                            )
    language = models.CharField(max_length=32,
                                choices=LANGUAGE,
                                default='English US'
                                )

    deadline = models.DateTimeField(blank=True, null=True)

    topic = models.CharField(max_length=256, default="", help_text="Topic of the assignment")

    subject = models.CharField(max_length=128, default="", help_text="Subject, e.g: Computer Science, Nursing")

    sources = models.CharField(max_length=16,
                                choices=SOURCES,
                                default="1"
                                )

    style = models.CharField(max_length=64,
                            choices=STYLE,
                            default='APA'
                            )

    description = models.TextField(default="", help_text="Assignment Descritption")

    uploads = models.FileField(default="", help_text='File uploads for the assignment')

    price = models.IntegerField(default='2.50', help_text='Total payment of the assignment')

    def __str__(self) -> str:
        return self.topic

