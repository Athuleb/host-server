# Generated by Django 4.2.16 on 2024-11-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_images', models.ImageField(upload_to='Topdestinations/')),
                ('location', models.CharField(max_length=100)),
                ('dest_describe', models.TextField()),
            ],
        ),
    ]