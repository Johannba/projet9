# Generated by Django 4.1 on 2022-10-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0005_review_ticket_ticket_time_created_ticket_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]