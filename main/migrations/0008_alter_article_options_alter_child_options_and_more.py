# Generated by Django 4.1.7 on 2023-02-20 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_child_expedient_expedient_child'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.AlterModelOptions(
            name='child',
            options={'verbose_name': 'Niño', 'verbose_name_plural': 'Niños'},
        ),
        migrations.AlterModelOptions(
            name='disease',
            options={'verbose_name': 'Enfermedad', 'verbose_name_plural': 'Enfermedades'},
        ),
        migrations.AlterModelOptions(
            name='economy',
            options={'verbose_name': 'Dato Económico', 'verbose_name_plural': 'Datos Económicos'},
        ),
        migrations.AlterModelOptions(
            name='expedient',
            options={'verbose_name': 'Expediente', 'verbose_name_plural': 'Expedientes'},
        ),
        migrations.AlterModelOptions(
            name='familypickup',
            options={'verbose_name': 'Familiar de Recogida', 'verbose_name_plural': 'Familiares de Recogida'},
        ),
        migrations.AlterModelOptions(
            name='intolerance',
            options={'verbose_name': 'Intolerancia', 'verbose_name_plural': 'Intolerancias'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Salon', 'verbose_name_plural': 'Salones'},
        ),
        migrations.AlterModelOptions(
            name='tutor',
            options={'verbose_name': 'Tutor', 'verbose_name_plural': 'Tutores'},
        ),
        migrations.AlterField(
            model_name='expedient',
            name='child',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.child', verbose_name='Niño'),
        ),
        migrations.AlterField(
            model_name='expedient',
            name='code_expedient',
            field=models.CharField(max_length=8, unique=True, verbose_name='Codigo del expediente'),
        ),
        migrations.AlterField(
            model_name='familypickup',
            name='name_family',
            field=models.CharField(max_length=32, verbose_name='Nombre y apellidos del familiar'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='child',
            field=models.ManyToManyField(to='main.child', verbose_name='Niño'),
        ),
    ]
