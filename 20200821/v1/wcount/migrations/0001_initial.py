# Generated by Django 2.2 on 2020-08-21 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('relation', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]