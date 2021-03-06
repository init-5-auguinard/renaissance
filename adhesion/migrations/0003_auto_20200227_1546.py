# Generated by Django 2.2.9 on 2020-02-27 15:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adhesion', '0002_auto_20200226_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adhesion',
            old_name='pays',
            new_name='pays_de_residence',
        ),
        migrations.RemoveField(
            model_name='adhesion',
            name='commune',
        ),
        migrations.RemoveField(
            model_name='adhesion',
            name='nom_complet',
        ),
        migrations.RemoveField(
            model_name='adhesion',
            name='quartier',
        ),
        migrations.RemoveField(
            model_name='adhesion',
            name='ville',
        ),
        migrations.AddField(
            model_name='adhesion',
            name='genre',
            field=models.CharField(choices=[('', 'Choisir...'), ('M', 'Masculin'), ('F', 'Feminin')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adhesion',
            name='lieu_de_naissance',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adhesion',
            name='nom_et_prenom',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adhesion',
            name='ville_de_residence',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adhesion',
            name='domicile',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='adhesion',
            name='profession',
            field=models.CharField(max_length=100),
        ),
    ]
