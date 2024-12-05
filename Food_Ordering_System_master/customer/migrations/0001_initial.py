# Generated by Django 5.1.2 on 2024-10-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailId', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=200)),
                ('street', models.TextField(max_length=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
