# Generated by Django 4.2.5 on 2023-09-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=50)),
                ('productbrand', models.CharField(max_length=50)),
            ],
        ),
    ]
