# Generated by Django 5.0.7 on 2024-07-26 08:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ariza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='body',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
