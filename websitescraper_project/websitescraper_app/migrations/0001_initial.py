# Generated by Django 4.2.6 on 2023-10-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkaddress', models.CharField(blank=True, max_length=500, null=True)),
                ('linkname', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
