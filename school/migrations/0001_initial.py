# Generated by Django 5.0.1 on 2024-10-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=256)),
            ],
        ),
    ]
