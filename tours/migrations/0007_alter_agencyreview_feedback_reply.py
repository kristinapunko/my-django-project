# Generated by Django 5.1.5 on 2025-04-08 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tours", "0006_agencyreview_cons_agencyreview_pros"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agencyreview",
            name="feedback",
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name="Reply",
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
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="tours.agencyreview",
                    ),
                ),
            ],
        ),
    ]
