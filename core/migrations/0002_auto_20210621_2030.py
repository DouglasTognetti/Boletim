# Generated by Django 3.2.4 on 2021-06-21 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultado',
            name='idTurma',
        ),
        migrations.AddField(
            model_name='resultado',
            name='idMateria',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='core.materia'),
            preserve_default=False,
        ),
    ]
