# Generated by Django 5.0.6 on 2024-08-06 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_note_cv_alter_note_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cvs/'),
        ),
    ]
