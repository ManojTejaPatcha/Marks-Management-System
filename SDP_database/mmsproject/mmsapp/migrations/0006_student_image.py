# Generated by Django 4.1.7 on 2023-04-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmsapp', '0005_remove_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.FileField(blank=True, upload_to='studentimages'),
        ),
    ]