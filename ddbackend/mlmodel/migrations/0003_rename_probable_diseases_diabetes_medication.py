# Generated by Django 4.1.9 on 2023-09-26 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlmodel', '0002_diabetes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diabetes',
            old_name='probable_diseases',
            new_name='medication',
        ),
    ]
