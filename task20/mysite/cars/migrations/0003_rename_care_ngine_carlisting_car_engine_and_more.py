# Generated by Django 4.0.4 on 2022-06-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_carengine_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carlisting',
            old_name='care_ngine',
            new_name='car_engine',
        ),
        migrations.RenameField(
            model_name='carlisting',
            old_name='mak_emodel',
            new_name='car_model',
        ),
        migrations.AlterField(
            model_name='carbrend',
            name='car_brend',
            field=models.CharField(blank=True, choices=[('', 'Ваш выбор...'), ('Audi', 'Audi'), ('Bmw', 'Bmw'), ('Mersedes', 'Mersedes')], default='Ваш выбор...', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='carengine',
            name='car_engine',
            field=models.CharField(blank=True, choices=[('', 'Ваш выбор...'), ('2.0 бензин', '2.0 бензин'), ('3.0 бензин', '3.0 бензин'), ('2.0 дизель', '2.0 дизель'), ('3.0 дизель', '3.0 дизель')], default='Ваш выбор...', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='carengine',
            name='year',
            field=models.CharField(blank=True, choices=[('', 'Ваш выбор...'), ('2000-20010гг', '2000-20010гг'), ('2010-2015гг', '2010-2015гг'), ('2015-2020гг', '2015-2020гг'), ('2020-2022гг', '2020-2022гг')], default='Ваш выбор...', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='car_drive',
            field=models.CharField(blank=True, choices=[('', 'Ваш выбор...'), ('полный', 'полный'), ('передний', 'передний'), ('задний', 'задний')], default='Ваш выбор...', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='car_model',
            field=models.CharField(blank=True, choices=[('', 'Ваш выбор...'), ('седан', 'седан'), ('универсал', 'универсал'), ('хэтчбэк', 'хэтчбэк'), ('джип', 'джип')], default='Ваш выбор...', max_length=150, null=True),
        ),
    ]