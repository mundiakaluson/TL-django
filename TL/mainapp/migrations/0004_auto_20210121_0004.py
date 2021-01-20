# Generated by Django 3.1.5 on 2021-01-20 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0003_order_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='writer',
            field=models.ForeignKey(blank=True, help_text='Writer to undertake the assignment.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
