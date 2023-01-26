# Generated by Django 4.1.4 on 2023-01-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='media')),
                ('image2', models.ImageField(upload_to='media')),
                ('club1', models.CharField(max_length=100)),
                ('club2', models.CharField(max_length=100)),
                ('league', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('arena', models.CharField(max_length=100)),
            ],
        ),
    ]