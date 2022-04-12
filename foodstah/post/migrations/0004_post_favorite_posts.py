# Generated by Django 4.0.3 on 2022-04-11 14:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("post", "0003_alter_post_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="favorite_posts",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                related_name="favorite_posts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]