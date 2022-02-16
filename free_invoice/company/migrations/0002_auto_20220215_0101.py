# Generated by Django 3.1.5 on 2022-02-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='sign',
            field=models.ImageField(blank=True, null=True, upload_to='company/sign', verbose_name='Sign'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='company/logo', verbose_name='Logo'),
        ),
    ]