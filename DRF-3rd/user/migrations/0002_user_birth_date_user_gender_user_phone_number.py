# Generated by Django 4.0.5 on 2022-06-13 08:34

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='생년월일'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', '남성(Man)'), ('W', '여성(Woman)')], max_length=20, null=True, verbose_name='성별'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, null=True, region=None, unique=True, verbose_name='전화번호'),
        ),
    ]