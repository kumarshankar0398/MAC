# Generated by Django 3.1.6 on 2021-03-19 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210319_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead0',
            new_name='chead00',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead1',
            new_name='chead11',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead2',
            new_name='chead22',
        ),
    ]
