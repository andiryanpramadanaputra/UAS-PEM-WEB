# Generated by Django 5.0.6 on 2024-06-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url_to_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
