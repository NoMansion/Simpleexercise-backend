# Generated by Django 5.0.6 on 2024-07-05 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_note_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='name',
            field=models.CharField(default='nameless', max_length=1024),
        ),
    ]
