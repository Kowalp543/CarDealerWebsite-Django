# Generated by Django 3.2.13 on 2022-05-04 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('komis', '0005_auto_20220503_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='samochod',
            name='image',
            field=models.ImageField(default=0, upload_to='static/media'),
            preserve_default=False,
        ),
    ]
