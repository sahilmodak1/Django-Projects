# Generated by Django 2.1.3 on 2018-12-06 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.CharField(max_length=12)),
                ('body', models.CharField(max_length=1000)),
            ],
        ),
    ]
