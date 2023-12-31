# Generated by Django 4.2.1 on 2023-07-01 08:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_profile_username"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("report", "0008_sort"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cashbook",
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
                    "seireki",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(200001),
                            django.core.validators.MaxValueValidator(299912),
                        ]
                    ),
                ),
                ("income_total", models.IntegerField()),
                ("cost_total", models.IntegerField()),
                ("total", models.IntegerField()),
                ("create_at", models.DateField(auto_now_add=True)),
                ("update_at", models.DateField(auto_now=True)),
                (
                    "exec_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cashbook_exec_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "exec_user_number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cashbook_exec_user_number",
                        to="main.profile",
                        to_field="member_number",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(999),
                        ],
                    ),
                ),
                (
                    "member_number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cashbook_member_number",
                        to="main.profile",
                        to_field="member_number",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(999),
                        ],
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cashbook_username",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
