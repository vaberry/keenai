# Generated by Django 4.2.4 on 2023-08-19 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_url', models.URLField(max_length=1000)),
                ('image_url', models.URLField(max_length=1000)),
                ('title', models.CharField(max_length=1000)),
                ('subtitle', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=1000)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
