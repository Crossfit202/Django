# Generated by Django 4.2.1 on 2023-06-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_post_book_author_post_condition_post_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='course',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
