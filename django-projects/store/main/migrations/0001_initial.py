# Generated by Django 4.2.1 on 2023-05-10 11:59

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='*')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='*')),
                ('image', models.ImageField(upload_to='product_images/', verbose_name='Product image')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Price')),
                ('description', django_quill.fields.QuillField()),
                ('in_stock', models.PositiveIntegerField(default=1, verbose_name='Count')),
                ('colors', models.CharField(blank=True, choices=[('white', 'WHITE'), ('black', 'BLACK'), ('blue', 'BLUE'), ('green', 'GREEN'), ('yellow', 'YELLOW'), ('red', 'RED'), ('tomato', 'TOMATO'), ('pink', 'PINK'), ('teal', 'TEAL'), ('brown', 'BROWN')], max_length=50)),
                ('stars', models.PositiveIntegerField(default=0, verbose_name='Stars')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Discount %')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='main.category')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='*')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Tovar alohida rasmlari')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='main.product')),
            ],
            options={
                'verbose_name': 'Tovar rasmlari',
                'verbose_name_plural': 'Tovar rasmlari',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='main.tag'),
        ),
    ]
