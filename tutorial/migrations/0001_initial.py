# Generated by Django 3.2 on 2022-03-20 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('audio', models.FileField(upload_to='documents/')),
                ('publisheddate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-publisheddate',),
            },
        ),
        migrations.CreateModel(
            name='VideoPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='documents/')),
                ('publisheddate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-publisheddate',),
            },
        ),
    ]
