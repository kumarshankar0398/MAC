# Generated by Django 3.1.6 on 2021-03-19 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210319_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead00',
            new_name='chead0',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead11',
            new_name='chead1',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead22',
            new_name='chead2',
        ),
    ]
