# Generated by Django 3.1.6 on 2021-03-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210319_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='chead02',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default='', max_length=3000),
        ),
    ]