# Generated by Django 4.1.4 on 2023-02-05 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0004_rename_labels_csv_label"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Csv",
        ),
        migrations.RenameField(
            model_name="news",
            old_name="fakeortrue",
            new_name="label",
        ),
    ]