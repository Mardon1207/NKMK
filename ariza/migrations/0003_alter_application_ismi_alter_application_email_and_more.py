# Generated by Django 5.0.7 on 2024-07-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ariza', '0002_application_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Ismi',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='javob',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='application',
            name='lavozimi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='telfon_raqami',
            field=models.CharField(max_length=15),
        ),
    ]
