# Generated by Django 4.1.7 on 2023-02-18 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_room_child_child_room_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expedient',
            old_name='child_expedient',
            new_name='child',
        ),
    ]
