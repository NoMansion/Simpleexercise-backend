# Generated by Django 5.0.6 on 2024-08-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_note_focus_alter_note_length_alter_note_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='cv',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='length',
            field=models.TextField(default='no length given'),
        ),
    ]
