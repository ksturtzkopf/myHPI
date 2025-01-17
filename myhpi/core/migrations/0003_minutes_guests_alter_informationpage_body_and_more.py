# Generated by Django 4.0.7 on 2022-09-15 20:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import myhpi.core.markdown.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0002_rootpage"),
    ]

    operations = [
        migrations.AddField(
            model_name="minutes",
            name="guests",
            field=models.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name="informationpage",
            name="body",
            field=myhpi.core.markdown.fields.CustomMarkdownField(),
        ),
        migrations.AlterField(
            model_name="minutes",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="minutes",
            name="moderator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="moderator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="minutes",
            name="body",
            field=myhpi.core.markdown.fields.CustomMarkdownField(),
        ),
    ]
