# Generated by Django 2.2.12 on 2020-05-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polaris", "0014_auto_20200512_2200"),
    ]

    operations = [
        migrations.AddField(
            model_name="asset", name="symbol", field=models.TextField(default="$"),
        ),
    ]
