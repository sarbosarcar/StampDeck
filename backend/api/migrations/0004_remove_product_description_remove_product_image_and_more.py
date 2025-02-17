# Generated by Django 5.1.1 on 2024-10-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_customer_pda_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='brochure',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='denomination',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='fdcImage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='printer',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='releaseDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stampImage',
            field=models.URLField(blank=True, null=True),
        ),
    ]
