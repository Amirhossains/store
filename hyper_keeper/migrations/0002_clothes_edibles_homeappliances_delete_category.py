# Generated by Django 4.2.1 on 2023-05-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyper_keeper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.PositiveIntegerField(choices=[(1, 'edibles'), (2, 'home_appliances'), (3, 'clothes')], default=3, verbose_name='model type')),
                ('clothe_type', models.CharField(max_length=30, verbose_name='edible type')),
                ('price', models.PositiveBigIntegerField(blank=True, verbose_name='price')),
                ('is_available', models.BooleanField(default=True, verbose_name='is available')),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='categories/', verbose_name='category image')),
                ('discount', models.CharField(blank=True, max_length=10, verbose_name='discount')),
                ('Description', models.TextField(blank=True, max_length=300, null=True, verbose_name='description')),
                ('createdTime', models.DateTimeField(auto_now=True)),
                ('updatedTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'clothe',
                'verbose_name_plural': 'clothes',
                'db_table': 'clothes',
            },
        ),
        migrations.CreateModel(
            name='Edibles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.PositiveIntegerField(choices=[(1, 'edibles'), (2, 'home_appliances'), (3, 'clothes')], default=1, verbose_name='model type')),
                ('edible_type', models.CharField(max_length=30, verbose_name='edible type')),
                ('price', models.PositiveBigIntegerField(blank=True, verbose_name='price')),
                ('is_available', models.BooleanField(default=True, verbose_name='is available')),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='edibles/', verbose_name='category image')),
                ('discount', models.CharField(blank=True, max_length=10, verbose_name='discount')),
                ('Description', models.TextField(blank=True, max_length=300, null=True, verbose_name='description')),
                ('createdTime', models.DateTimeField(auto_now=True)),
                ('updatedTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'edible',
                'verbose_name_plural': 'edibles',
                'db_table': 'edibles',
            },
        ),
        migrations.CreateModel(
            name='HomeAppliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.PositiveIntegerField(choices=[(1, 'edibles'), (2, 'home_appliances'), (3, 'clothes')], default=2, verbose_name='model type')),
                ('home_appliance_type', models.CharField(max_length=30, verbose_name='home appliances type')),
                ('price', models.PositiveBigIntegerField(blank=True, verbose_name='price')),
                ('is_available', models.BooleanField(default=True, verbose_name='is available')),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='home-appliances/', verbose_name='category image')),
                ('discount', models.CharField(blank=True, max_length=10, verbose_name='discount')),
                ('Description', models.TextField(blank=True, max_length=300, null=True, verbose_name='description')),
                ('createdTime', models.DateTimeField(auto_now=True)),
                ('updatedTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'home appliances',
                'verbose_name_plural': 'home appliances',
                'db_table': 'home_appliances',
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
