# Generated by Django 2.0.13 on 2019-07-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_order_tgid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dops',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='tgid',
            field=models.CharField(max_length=200),
        ),
    ]