# Generated by Django 2.0.13 on 2019-07-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190718_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tgid',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]