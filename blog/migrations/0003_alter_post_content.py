# Generated by Django 5.0.1 on 2024-05-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_author_alter_post_date_alter_post_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(max_length=300),
        ),
    ]