# Generated by Django 4.1.7 on 2023-05-16 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_alter_form_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LongRebateData',
        ),
        migrations.DeleteModel(
            name='Penalty',
        ),
        migrations.RemoveField(
            model_name='shortrebate',
            name='Memebers',
        ),
        migrations.RemoveField(
            model_name='shortrebate',
            name='biling',
        ),
        migrations.RemoveField(
            model_name='shortrebate',
            name='circulation',
        ),
        migrations.RemoveField(
            model_name='shortrebate',
            name='infoToCaterer',
        ),
        migrations.RemoveField(
            model_name='shortrebate',
            name='link',
        ),
        migrations.RemoveField(
            model_name='shortrebate',
            name='note',
        ),
        migrations.RemoveField(
            model_name='shortrebate',
            name='policy',
        ),
    ]
