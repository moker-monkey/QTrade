# Generated by Django 2.2.3 on 2019-11-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QTdeal', '0002_auto_20191102_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycapital',
            name='hold_days',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='持有时间'),
        ),
    ]
