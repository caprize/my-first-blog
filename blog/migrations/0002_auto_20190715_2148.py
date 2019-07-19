# Generated by Django 2.0.13 on 2019-07-15 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='maintext',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]