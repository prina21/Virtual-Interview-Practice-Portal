# Generated by Django 3.2.9 on 2021-12-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0004_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='filename',
            field=models.IntegerField(max_length=12),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
