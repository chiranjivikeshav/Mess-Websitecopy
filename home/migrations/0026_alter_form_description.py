# Generated by Django 4.1.7 on 2023-05-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_todayrebate_options_unregisteredstudent_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='description',
            field=models.CharField(blank=True, help_text='This contains the description of the form to be added.', max_length=120, verbose_name='Form Description'),
        ),
    ]
