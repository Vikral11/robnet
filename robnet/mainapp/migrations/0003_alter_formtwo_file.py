# Generated by Django 4.2.7 on 2023-11-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_formtwo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formtwo",
            name="file",
            field=models.FileField(upload_to="uploads/"),
        ),
    ]