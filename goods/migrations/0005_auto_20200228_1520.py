# Generated by Django 2.2.3 on 2020-02-28 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20191124_2313'),
    ]

    operations = [

        migrations.AlterField(
            model_name='goods',
            name='g_imgs',
            field=models.CharField(max_length=1024, verbose_name='商品封面图'),
        ),
        migrations.CreateModel(
            name='GoodDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgUrl', models.CharField(max_length=2048, verbose_name='商品图片')),
                ('name', models.CharField(max_length=128, verbose_name='商品简介')),
                ('details', models.CharField(max_length=2048, verbose_name='详情图片')),
                ('price', models.FloatField(default=0, verbose_name='商品价格')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '商品详情',
                'verbose_name_plural': '商品详情',
                'db_table': 'GoodDetail',
            },
        ),
        migrations.CreateModel(
            name='GoodAutoImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgUrl', models.CharField(max_length=2048, verbose_name='商品图片')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shopGoodsImageList', to='goods.GoodDetail', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '商品轮播图',
                'verbose_name_plural': '商品轮播图',
                'db_table': 'GoodAutoImg',
            },
        ),
    ]
