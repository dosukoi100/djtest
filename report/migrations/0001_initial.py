# Generated by Django 4.2.1 on 2023-05-28 08:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cost",
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
                (
                    "member_number",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(999),
                        ]
                    ),
                ),
                (
                    "seireki",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(200001),
                            django.core.validators.MaxValueValidator(299912),
                        ]
                    ),
                ),
                ("koutuuhi", models.IntegerField(default=0)),
                ("shokuhi", models.IntegerField(default=0)),
                ("youfukuhi", models.IntegerField(default=0)),
                ("zeikinn", models.IntegerField(default=0)),
                ("hoken", models.IntegerField(default=0)),
                ("kounetuhi", models.IntegerField(default=0)),
                ("yachin", models.IntegerField(default=0)),
                ("chuushajoudai", models.IntegerField(default=0)),
                ("zapi", models.IntegerField(default=0)),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
