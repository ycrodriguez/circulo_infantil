# Generated by Django 4.1.7 on 2023-02-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_familypickup_child_family_pickup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='child',
            name='weight',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='disease',
            name='child_disease',
            field=models.ManyToManyField(related_name='child_disease', to='main.child'),
        ),
    ]
