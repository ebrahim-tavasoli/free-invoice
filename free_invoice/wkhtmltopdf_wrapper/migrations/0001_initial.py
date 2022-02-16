# Generated by Django 3.1.5 on 2022-02-15 12:23

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice', '0004_auto_20220214_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='WkhtmltopdfLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField()),
                ('time', django_jalali.db.models.jDateTimeField(verbose_name='Time')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_wkhtmltopdf_log', to='invoice.invoice', verbose_name='Invoice')),
            ],
        ),
    ]