# Generated by Django 2.2 on 2021-04-17 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210204_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
