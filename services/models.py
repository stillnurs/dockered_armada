from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
from django.urls import reverse


class Services(models.Model):
    """Модель для наших услуг"""
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/', default='NoPhoto')
    text = models.TextField(null=True)
    phone = models.CharField(max_length=20, null=True)

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Наша услуга'
        verbose_name_plural = 'Наши услуги'

    def __str__(self):
        return self.title


class ServiceListCategory(models.Model):
    """Модель для раздела 'Услуги' """
    title = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категории Услуг'
        verbose_name_plural = 'Категории Услуг'

    def get_absolute_url(self):
        return reverse('service_list_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class ServicePanel(models.Model):
    """Модель для наших услуг (во разделе "Услуги")"""
    title = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='service_panel/', default='NoPhoto')
    text = models.TextField()
    category = models.ForeignKey(ServiceListCategory, related_name='service_categories', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    """Модуль для     'Наши работы'    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/', default='NoPhoto')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return self.title


class Production(models.Model):
    """Модуль для    'Производство'    """
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='production/', default='NoPhoto')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Производство'
        verbose_name_plural = 'Производство'

    def __str__(self):
        return self.title


class Price(models.Model):
    """Модуль для 'Наш прайс'    """
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='price/', default='NoPhoto')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Прайслист'
        verbose_name_plural = 'Прайслист'

    def __str__(self):
        return self.title


class Customer(models.Model):
    """Модуль для   'Наши клиенты'  """
    image = models.ImageField(upload_to='customer/', default='NoPhoto')
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Наш клиент'
        verbose_name_plural = 'Наши клиенты'

    def __str__(self):
        return self.name


class Staff(models.Model):
    """Модуль для     'Наша команда'     """
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='customer/', default='NoPhoto')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Наша команда'
        verbose_name_plural = 'Наша команда'

    def __str__(self):
        return self.name


class ContactClient(models.Model):
    """Модуль для   'Наши клиенты'    """
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер телефона должен быть в формате: '+996123456789' или '0505123456'. "
                                         "Максимум 15 цифер.")
    phone = models.CharField(validators=[phone_regex], max_length=17, verbose_name='Телефон')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Контакт клинта'
        verbose_name_plural = 'Контакты клиентов'

    def __str__(self):
        return self.name


class Work(models.Model):
    """  Модуль для 'О нас'  """
    title = models.IntegerField()
    body = models.TextField()

    class Meta:
        ordering = ('title',)
        verbose_name = 'История'
        verbose_name_plural = 'История'

    def __str__(self):
        return str(self.title)


class Equipment(models.Model):
    """ модулья для карусели в Производство-Оборудование"""
    carousel_text = models.CharField(max_length=150)
    image = models.ImageField(upload_to='equipment/')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return str(self.carousel_text)
