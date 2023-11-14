# Generated by Django 4.2.7 on 2023-11-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qtty', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='static/images/products')),
            ],
        ),
    ]
