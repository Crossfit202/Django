# Generated by Django 4.2.1 on 2023-06-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_post_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='book_author',
            field=models.CharField(default='unknown author', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.CharField(default='unknown condition', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='contact',
            field=models.CharField(default='unknown contact info', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='course',
            field=models.CharField(default='unknown course', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='edition',
            field=models.CharField(default='unknown edition', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='isbn',
            field=models.CharField(default='unknown isbn', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(default='unknown location', max_length=100),
        ),
    ]
