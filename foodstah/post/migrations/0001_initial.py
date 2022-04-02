# Generated by Django 4.0.3 on 2022-03-31 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "post_description",
                    models.TextField(blank=True, max_length=140, null=True),
                ),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("main_image", models.ImageField(upload_to="post_pics")),
                ("is_recipe", models.BooleanField()),
                ("ingredients", models.TextField(blank=True, null=True)),
                ("recipe_description", models.TextField(blank=True, null=True)),
                (
                    "cooking_time",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
