# Generated by Django 4.1.7 on 2023-02-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_article_room_article_article_name_article_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='room_child',
            new_name='room',
        ),
        migrations.RenameField(
            model_name='economy',
            old_name='tutor_economy',
            new_name='tutor',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='child_disease',
        ),
        migrations.RemoveField(
            model_name='familypickup',
            name='child_family_pickup',
        ),
        migrations.RemoveField(
            model_name='intolerance',
            name='child_intolerance',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='child_tutor',
        ),
        migrations.AddField(
            model_name='child',
            name='diseases',
            field=models.ManyToManyField(to='main.disease', verbose_name='Enfermedades'),
        ),
        migrations.AddField(
            model_name='child',
            name='family_pickup',
            field=models.ManyToManyField(to='main.familypickup', verbose_name='Familiar de recogida'),
        ),
        migrations.AddField(
            model_name='child',
            name='intolerance',
            field=models.ManyToManyField(to='main.intolerance', verbose_name='Intolerancias'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='child',
            field=models.ManyToManyField(to='main.child'),
        ),
    ]
