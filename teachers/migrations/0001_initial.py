# Generated by Django 3.2.8 on 2021-10-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('teacher_pic', models.ImageField(upload_to='photos/%Y/m/%d/')),
                ('description', models.TextField(blank=True)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
    ]