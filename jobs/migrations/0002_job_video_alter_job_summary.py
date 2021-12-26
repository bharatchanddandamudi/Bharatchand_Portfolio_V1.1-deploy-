# Generated by Django 4.0 on 2021-12-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='video',
            field=models.FileField(null=True, upload_to='video/'),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(max_length=500),
        ),
    ]
