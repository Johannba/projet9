# Generated by Django 4.1.1 on 2022-09-14 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0002_alter_ticket_description_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='ticket',
        ),
    ]