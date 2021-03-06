# Generated by Django 3.1.1 on 2020-09-28 10:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+996123456789' или '0505123456'. Максимум 15 цифер.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Контакт клинта',
                'verbose_name_plural': 'Контакты клиентов',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='NoPhoto', upload_to='customer/')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Наш клиент',
                'verbose_name_plural': 'Наши клиенты',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_text', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='equipment/')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудование',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='NoPhoto', upload_to='portfolio/')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
                'ordering': ('-title',),
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(default='NoPhoto', upload_to='price/')),
            ],
            options={
                'verbose_name': 'Прайслист',
                'verbose_name_plural': 'Прайслист',
                'ordering': ('-title',),
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(default='NoPhoto', upload_to='production/')),
            ],
            options={
                'verbose_name': 'Производство',
                'verbose_name_plural': 'Производство',
                'ordering': ('-title',),
            },
        ),
        migrations.CreateModel(
            name='ServiceListCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Категории Услуг',
                'verbose_name_plural': 'Категории Услуг',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='NoPhoto', upload_to='services/')),
                ('text', models.TextField(null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Наша услуга',
                'verbose_name_plural': 'Наши услуги',
                'ordering': ('-title',),
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('image', models.ImageField(default='NoPhoto', upload_to='customer/')),
            ],
            options={
                'verbose_name': 'Наша команда',
                'verbose_name_plural': 'Наша команда',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField()),
                ('body', models.TextField()),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'История',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ServicePanel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('image', models.ImageField(default='NoPhoto', upload_to='service_panel/')),
                ('text', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_categories', to='services.servicelistcategory')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуги',
                'ordering': ('-title',),
            },
        ),
    ]
