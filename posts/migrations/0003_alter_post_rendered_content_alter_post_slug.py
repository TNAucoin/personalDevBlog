# Generated by Django 4.1.5 on 2023-01-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_post_rendered_content_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="rendered_content",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]