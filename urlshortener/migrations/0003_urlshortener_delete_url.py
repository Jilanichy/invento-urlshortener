# Generated by Django 4.1.1 on 2022-09-10 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0002_url_delete_urlshortener'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.CharField(max_length=255)),
                ('shorturl', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Url',
        ),
    ]
