# Generated by Django 4.2.7 on 2023-12-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_about_1_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=25)),
                ('link', models.URLField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
