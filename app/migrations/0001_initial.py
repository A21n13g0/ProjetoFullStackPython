# Generated by Django 4.2 on 2023-04-20 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=150)),
                ('cnpj', models.CharField(max_length=14)),
                ('stateRegistration', models.IntegerField()),
                ('telephone', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
