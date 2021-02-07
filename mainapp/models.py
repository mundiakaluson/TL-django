from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from djmoney.models.fields import MoneyField

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
                            default='College',
                            help_text='The educational level of the paper'
                            )
    language = models.CharField(max_length=32,
                                choices=LANGUAGE,
                                default='English US',
                                help_text='Preferred English version of the client'
                                )

    deadline = models.DateTimeField(blank=True, null=True, help_text='Precise deadline of the assignment')

    topic = models.CharField(max_length=256, default="", help_text="Topic of the assignment")

    subject = models.CharField(max_length=128, default="", help_text="Subject, e.g: Computer Science, Nursing")

    sources = models.CharField(max_length=16,
                                choices=SOURCES,
                                default="1",
                                help_text="Amount of sources needed by the client. Put 'Other' if exceeds eight."
                                )

    style = models.CharField(max_length=64,
                            choices=STYLE,
                            default='APA',
                            help_text='Preferred formatting style by the client.'
                            )

    description = models.TextField(default="", help_text="Assignment Descritption")

    uploads = models.FileField(default="", help_text='File uploads for the assignment', blank=True, null=True, upload_to='uploads/')

    price = MoneyField(decimal_places=2, max_digits=19, default_currency='USD', help_text='Total payment of the assignment')

    """writer = models.ForeignKey(User, 
                                on_delete=CASCADE, 
                                blank=True, 
                                null=True, 
                                help_text='Writer to undertake the assignment.')"""
    


    def __str__(self) -> str:
        return self.topic

    def summary(self):
        return self.description[:100]

class Bid(models.Model):

    order_id = models.PositiveIntegerField(null=True, blank=True)
    order_topic = models.CharField(max_length=4000, null=True, blank=True)
    bid_note = models.TextField(default="")
    bidder = models.CharField(max_length=128, null=True, blank=True)
<<<<<<< HEAD:mainapp/models.py
=======

>>>>>>> origin/main:TL/mainapp/models.py

class Assign(models.Model):

    writer_assigned = models.OneToOneField(User, on_delete=CASCADE, related_name='writer_topic')
    order_assigned = models.OneToOneField(Order, on_delete=CASCADE ,related_name='order_assigned')

    def __unicode__(self):
        return self.writer_assigned
