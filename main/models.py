from django.db import models


# Create your models here.
class Contacts(models.Model):
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    address = models.CharField(max_length=100, verbose_name="Адресс")
    telegram = models.CharField(max_length=300, verbose_name="Ссылкка на чат в телеграмме")
    email = models.EmailField(max_length=300, verbose_name="Почта", default='')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Наши контакты"
        verbose_name_plural = "Наши контакты"


class Social(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    link = models.CharField(max_length=400, verbose_name="Ссылка")
    contact = models.ForeignKey("Contacts", related_name="contacts")
    icon_name = models.CharField(max_length=300, verbose_name="Css Иконка")
    cssClass = models.CharField(verbose_name="Css класс", max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Соц. сети"
        verbose_name_plural = "Соц. сети"


class Project(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    tagline = models.CharField(max_length=300, verbose_name="Слоган")
    type = models.ForeignKey("Type", verbose_name="Тип")
    category = models.ForeignKey("Category", verbose_name="Категория")
    img = models.ImageField(verbose_name="Изображение")
    cssClass = models.CharField(verbose_name="Css класс", max_length=300)

    def image_tag(self):
        return u'<img src="%s"/>' % self.img.url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Type(models.Model):
    name = models.CharField(max_length=300, verbose_name="Тип Проекта")

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=300, verbose_name="Категория проекта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class RecentlyInWork(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название", default="")
    img = models.ImageField(upload_to="media/", verbose_name="Изображение")
    link = models.CharField(max_length=400, verbose_name="Ссылка")

    class Meta:
        verbose_name = "В работе"
        verbose_name_plural = "В работе"

    def __str__(self):
        return self.name


class Contact(models.Model):
    email = models.CharField(max_length=400, verbose_name="Почта")
    name = models.CharField(max_length=400, verbose_name="Имя")
    name_company = models.CharField(max_length=400, verbose_name="Название компании")
    massage = models.TextField(verbose_name="Сообщение")
    phone = models.CharField(verbose_name="Телефон", max_length=300, default='')

    class Meta:
        verbose_name = "Обращения к нам"
        verbose_name_plural = "Обращения к нам"

    def __str__(self):
        return self.name


class Order(models.Model):
    order = models.CharField(max_length=300, verbose_name="Наименование заказа")
    email = models.CharField(max_length=400, verbose_name="Почта")
    name = models.CharField(max_length=400, verbose_name="Имя")
    name_company = models.CharField(max_length=400, verbose_name="Название компании")
    massage = models.TextField(verbose_name="Сообщение")
    phone = models.CharField(verbose_name="Телефон", max_length=300, default='')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.name
