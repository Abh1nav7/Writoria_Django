# Generated by Django 5.1.6 on 2025-04-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_userprofile_contact_number_userprofile_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="category",
            field=models.CharField(
                choices=[
                    ("tech", "Technology"),
                    ("lifestyle", "Lifestyle"),
                    ("travel", "Travel"),
                    ("food", "Food & Cooking"),
                    ("health", "Health & Fitness"),
                    ("arts", "Arts & Culture"),
                    ("business", "Business"),
                    ("other", "Other"),
                ],
                default="other",
                max_length=20,
            ),
        ),
    ]
