# Generated by Django 4.1.7 on 2023-05-05 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmsapp', '0008_remove_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
