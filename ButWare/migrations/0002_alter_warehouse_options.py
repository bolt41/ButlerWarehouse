# Generated by Django 4.0.3 on 2022-03-11 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ButWare', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='warehouse',
            options={'ordering': ['name'], 'verbose_name': 'Наименование', 'verbose_name_plural': 'Склады'},
        ),
    ]