# Generated by Django 3.2.5 on 2021-08-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=400)),
                ('image', models.ImageField(blank=True, null=True, upload_to=1)),
            ],
            options={
                'db_table': 'entrys',
            },
        ),
    ]