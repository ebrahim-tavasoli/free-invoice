# Generated by Django 3.1.5 on 2022-02-14 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20220105_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Currency type')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.currencytype', verbose_name='Currency'),
        ),
    ]