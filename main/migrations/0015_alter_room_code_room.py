# Generated by Django 4.1.7 on 2023-02-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_child_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code_room',
            field=models.CharField(max_length=8, unique=True, verbose_name='Código del Salon'),
        ),
    ]
