# Generated by Django 3.2 on 2022-03-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1000)),
                ('video', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('PostImage', models.ImageField(blank=True, null=True, upload_to='feedpost/')),
                ('publisheddate', models.DateTimeField(auto_now_add=True)),
                ('updateddate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-publisheddate',),
            },
        ),
    ]