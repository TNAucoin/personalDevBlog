# Generated by Django 4.1.5 on 2023-01-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="rendered_content",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
