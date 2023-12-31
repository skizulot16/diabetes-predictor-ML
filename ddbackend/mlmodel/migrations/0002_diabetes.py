# Generated by Django 4.1.9 on 2023-09-26 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlmodel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diabetes_probabilty', models.FloatField()),
                ('health_risk', models.CharField(max_length=100)),
                ('precautions', models.TextField()),
                ('probable_diseases', models.TextField()),
            ],
        ),
    ]
