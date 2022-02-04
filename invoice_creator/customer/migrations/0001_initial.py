# Generated by Django 3.1.5 on 2022-01-04 20:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Firstname')),
                ('last_name', models.CharField(max_length=256, verbose_name='Lastname')),
                ('company', models.CharField(max_length=256, verbose_name='Company')),
                ('phone_number', models.CharField(max_length=32, verbose_name='Phone number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('mobile_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('09\\d{9}')], verbose_name='Mobile number')),
                ('address', models.CharField(max_length=2048, verbose_name='Address')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ('last_name', 'first_name'),
            },
        ),
    ]
