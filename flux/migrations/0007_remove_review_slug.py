# Generated by Django 4.1 on 2022-10-09 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0006_review_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='slug',
        ),
    ]
