# Generated by Django 4.0.4 on 2022-05-17 09:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_alter_queries_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='text_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='top_image',
            field=models.ImageField(upload_to='frontend/static/uploads', verbose_name='Обложка статьи'),
        ),
    ]
