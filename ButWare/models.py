from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Модель производителей оборудования
class Brands(models.Model):
    name = models.CharField('Наименование', max_length=100)
    country = models.CharField('Страна производитель', max_length=100, blank=True)

    class Meta:
        unique_together = ['name']
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = ['name']

    def __str__(self):
        return self.name


# Модель единиц измерения
class Units(models.Model):
    name = models.CharField('Единица измерения', max_length=100)

    class Meta:
        unique_together = ['name']
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'
        ordering = ['name']

    def __str__(self):
        return self.name

# Модель групп товаров
class GroupProduct(models.Model):
    name = models.CharField('Наименование', max_length=200)

    class Meta:
        unique_together = ['name']
        verbose_name = 'Группа товаров'
        verbose_name_plural = 'Группы товаров'
        ordering = ['name']

    def __str__(self):
        return self.name

# Модель товара
class Product(models.Model):
    name = models.CharField('Наименование', max_length=200)
    description = models.TextField('Описание', blank=True)
    art_butler = models.SlugField('Артикул Butler', max_length=100, blank=True)
    art_vendor = models.CharField('Артикул поставщика', max_length=100, blank=True)
    art_manufact = models.CharField('Артикул производителя', max_length=100, blank=True)
    group = models.ManyToManyField('GroupProduct', verbose_name='Группа товаров')
    unit = models.ForeignKey('Units', verbose_name='Единица измерения', null = True, blank = True, default=None, on_delete=models.SET_NULL)
    price_in = models.FloatField('Цена поставщика', blank=True, null = True)
    price_out = models.FloatField('Цена продажи', blank=True, null=True)
    price_rrc = models.FloatField('РРЦ', blank=True, null=True)
    brand = models.ForeignKey('Brands', verbose_name='Производитель', null= True, blank=True, on_delete=models.SET_NULL)
    weight = models.FloatField('Вес', null=True, blank=True)
    size = models.CharField('Размеры', max_length=60, blank=True)
    in_box = models.BooleanField('Щитовое оборудование', default=False)
    din_size = models.IntegerField('Занимаемое DIN мест', blank=True, null=True)
    in_serv = models.BooleanField('Стоечное оборудование', default=False)
    unit_size = models.IntegerField('Кол-во Unit', blank=True, null=True)
    acdc = models.CharField('Питание', max_length=50, blank=True)
    lan = models.BooleanField('Оборудование LAN', default=False)
    knx = models.BooleanField('Оборудование KNX', default=False)

    class Meta:
        unique_together = ['name']
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return self.name

    # Функция возвращает перечень систем в которых может использоваться устройство
    def get_groups(self):
        return ", ".join([p.name for p in self.group.all()])

    # Для отображения в админке поля с "человеческим" названием
    get_groups.short_description = "Группы"

# Модель складов
class Warehouse(models.Model):
    name = models.CharField('Наименование', max_length=200)
    address = models.CharField('Адрес', max_length=400)

    class Meta:
        unique_together = ['name']
        verbose_name = 'Наименование'
        verbose_name_plural = 'Склады'
        ordering = ['name']

    def __str__(self):
        return self.name

# Модель поставщиков
class Provider(models.Model):
    name = models.CharField('Наименование', max_length=200)
    address = models.CharField('Адрес', max_length=400, blank=True)
    contact = models.CharField('Контакты', max_length=400, blank=True)

    class Meta:
        unique_together = ['name']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['name']

    def __str__(self):
        return self.name

#Модель систем

class Systems(models.Model):
    name = models.CharField('Наименование', max_length=300)

    class Meta:
        unique_together = ['name']
        verbose_name = 'Система'
        verbose_name_plural = 'Системы'
        ordering = ['name']

    def __str__(self):
        return self.name

#Модель статусов объектов
class StatusObject(models.Model):
    name = models.CharField('Значение', max_length=100)

    class Meta:
        unique_together = ['name']
        verbose_name = 'Статус объекта'
        verbose_name_plural = 'Статусы объектов'
        ordering = ['name']

    def __str__(self):
        return self.name

#Модель объектов
class ObjectsCurrent(models.Model):
    name = models.CharField('Наименование', max_length=300)
    status = models.ForeignKey('StatusObject', verbose_name='Статус', null= True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField('Адрес', max_length=800)
    client = models.CharField('Клиент', max_length=200, blank=True)
    contact_face = models.CharField('Контактное лицо', max_length=200, blank=True)
    contractor = models.CharField('Генподрядчик', max_length=200, blank=True)
    designer = models.CharField('Дизайнер', max_length=200, blank=True)
    dir_client_project = models.CharField('Руководитель проекта заказчика', max_length=200, blank=True)
    dir_butler_project = models.ForeignKey(User, verbose_name='Руководитель проекта Butler', null= True, blank=True,  on_delete=models.SET_NULL)
    developer = models.CharField('Проектировщик', max_length=200, blank=True)
    foroman = models.CharField('Прораб', max_length=200, blank=True)
    electrician = models.CharField('Электрик', max_length=200, blank=True)
    ovik = models.CharField('ОВиК', max_length=200, blank=True)
    system = models.ManyToManyField('Systems',  verbose_name='Системы')
    contract = models.CharField('Договор', max_length=200, blank=True)

    class Meta:
        unique_together = ['name']
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
        ordering = ['name']

    def __str__(self):
        return self.name

#Модель статуса смет
class StatusEstimate(models.Model):
    name = models.CharField('Значение', max_length=100)

    class Meta:
        unique_together = ['name']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы смет'
        ordering = ['name']

    def __str__(self):
        return self.name

#Модель смет
class Estimate(models.Model):
    object = models.ForeignKey('ObjectsCurrent', verbose_name='Объект', on_delete=models.CASCADE)
    date_doc = models.DateField('Дата', default=date.today)
    status_doc = models.ForeignKey('StatusEstimate', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Смета'
        verbose_name_plural = 'Сметы'

    def __str__(self):
        return self.object.name

#Модель товаров в смете
class ProductEstimate(models.Model):
    product = models.ForeignKey('Product', verbose_name='Номенклатура', on_delete=models.CASCADE)
    estimate = models.ForeignKey('Estimate', verbose_name='Смета', on_delete=models.CASCADE)
    count = models.PositiveIntegerField('Количество')

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Номенклатуры смет'

    def __str__(self):
        return self.product.name

#модель приходов
class Entrance(models.Model):
    provider = models.ForeignKey('Provider', verbose_name='Поступление',blank=True, null=True, on_delete=models.SET_NULL)
    entrance_prod = models.ForeignKey('Product', verbose_name='Номенклатура', on_delete=models.CASCADE)
    count = models.IntegerField('Количество')
    source_doc = models.CharField('Документ-основание', max_length=300, blank=True)
    warehouse = models.ForeignKey('Warehouse', blank=True, null = True, on_delete=models.SET_NULL)
    to_object = models.ForeignKey('ObjectsCurrent', verbose_name='Объект', blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateField('Дата', default=date.today)

    class Meta:
        verbose_name = 'Поступление'
        verbose_name_plural = 'Поступления'

    def __str__(self):
        return self.to_object.name

#модель резервов
class Reserved(models.Model):
    product = models.ForeignKey('Product', verbose_name='Номенклатура', on_delete=models.CASCADE)
    count = models.IntegerField('Количество')
    to_object = models.ForeignKey('ObjectsCurrent', verbose_name='Объект', blank=True, null=True,
                                  on_delete=models.SET_NULL)
    warehnouse = models.ForeignKey('Warehouse', verbose_name='Склад', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Резерв'
        verbose_name_plural = 'Резервы'

    def __str__(self):
        return self.to_object.name