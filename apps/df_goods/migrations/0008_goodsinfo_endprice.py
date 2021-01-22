# Generated by Django 2.0.12 on 2020-01-02 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0007_auto_20200102_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='endprice',
            field=models.DecimalField(decimal_places=2, default='5000', max_digits=10, null=True, verbose_name='最终价格'),
        ),
    ]