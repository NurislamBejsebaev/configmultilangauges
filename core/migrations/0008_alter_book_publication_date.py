# Generated by Django 4.2.6 on 2023-10-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_book_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
    ]
