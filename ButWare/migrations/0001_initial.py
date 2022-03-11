# Generated by Django 4.0.3 on 2022-03-11 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='Страна производитель')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
                'ordering': ['name'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='GroupProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Группа товаров',
                'verbose_name_plural': 'Группы товаров',
                'ordering': ['name'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('address', models.CharField(max_length=400, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Наименование',
                'verbose_name_plural': 'Возможные варианты',
                'ordering': ['name'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
                'ordering': ['name'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('address', models.CharField(blank=True, max_length=400, verbose_name='Адрес')),
                ('contact', models.CharField(blank=True, max_length=400, verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'ordering': ['name'],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('art_butler', models.SlugField(blank=True, max_length=100, verbose_name='Артикул Butler')),
                ('art_vendor', models.CharField(blank=True, max_length=100, verbose_name='Артикул поставщика')),
                ('art_manufact', models.CharField(blank=True, max_length=100, verbose_name='Артикул производителя')),
                ('price_in', models.FloatField(blank=True, null=True, verbose_name='Цена поставщика')),
                ('price_out', models.FloatField(blank=True, null=True, verbose_name='Цена продажи')),
                ('price_rrc', models.FloatField(blank=True, null=True, verbose_name='РРЦ')),
                ('weight', models.FloatField(blank=True, verbose_name='Вес')),
                ('size', models.CharField(blank=True, max_length=60, verbose_name='Размеры')),
                ('in_box', models.BooleanField(default=False, verbose_name='Щитовое оборудование')),
                ('din_size', models.IntegerField(blank=True, null=True, verbose_name='Занимаемое DIN мест')),
                ('in_serv', models.BooleanField(default=False, verbose_name='Стоечное оборудование')),
                ('unit_size', models.IntegerField(blank=True, null=True, verbose_name='Кол-во Unit')),
                ('acdc', models.CharField(blank=True, max_length=50, verbose_name='Питание')),
                ('lan', models.BooleanField(default=False, verbose_name='Оборудование LAN')),
                ('knx', models.BooleanField(default=False, verbose_name='Оборудование KNX')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ButWare.brands', verbose_name='Производитель')),
                ('group', models.ManyToManyField(to='ButWare.groupproduct', verbose_name='Группа товаров')),
                ('unit', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ButWare.units', verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Номенклатура',
                'verbose_name_plural': 'Товары',
                'ordering': ['name'],
                'unique_together': {('name',)},
            },
        ),
    ]