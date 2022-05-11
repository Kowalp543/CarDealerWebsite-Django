# Generated by Django 3.2.13 on 2022-04-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Samochod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('przebieg', models.IntegerField()),
                ('rok_produkcji', models.IntegerField()),
                ('paliwo', models.CharField(choices=[('b', 'Benzyna'), ('d', 'Diesel'), ('l', 'LPG')], max_length=1)),
                ('moc', models.IntegerField()),
            ],
        ),
    ]