# Generated by Django 5.0.7 on 2024-08-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metacode", "0002_alter_profile_chat_model_alter_profile_theme"),
    ]

    operations = [
        migrations.AddField(
            model_name="chat",
            name="edit_content",
            field=models.TextField(default=models.TextField()),
        ),
    ]
