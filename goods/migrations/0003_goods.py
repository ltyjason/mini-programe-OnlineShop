# Generated by Django 2.2.3 on 2019-11-24 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20191124_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=128, verbose_name='商品名称')),
                ('g_imgs', models.CharField(max_length=1024, verbose_name='轮播图')),
                ('g_details', models.CharField(max_length=1024, verbose_name='商品详情')),
                ('g_price', models.FloatField(default=0, verbose_name='折后价')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodType', verbose_name='父类商品')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
                'db_table': 'goods',
            },
        ),
    ]
