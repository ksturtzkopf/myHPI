# Generated by Django 4.0.7 on 2022-12-17 09:06

from django.db import migrations

import myhpi.core.markdown.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_informationpage_attachments_minutes_attachments_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footer",
            name="column_1",
            field=myhpi.core.markdown.fields.CustomMarkdownField(),
        ),
        migrations.AlterField(
            model_name="footer",
            name="column_2",
            field=myhpi.core.markdown.fields.CustomMarkdownField(),
        ),
        migrations.AlterField(
            model_name="footer",
            name="column_3",
            field=myhpi.core.markdown.fields.CustomMarkdownField(),
        ),
        migrations.AlterField(
            model_name="footer",
            name="column_4",
            field=myhpi.core.markdown.fields.CustomMarkdownField(),
        ),
    ]
