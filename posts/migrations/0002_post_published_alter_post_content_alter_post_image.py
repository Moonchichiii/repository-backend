# Generated by Django 4.2.7 on 2023-12-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="published",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]