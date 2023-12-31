# Generated by Django 3.2.19 on 2023-06-28 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_onlinebooking_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=256)),
                ('address', models.CharField(blank=True, max_length=256)),
                ('online_booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_booking', to='reservation.onlinebooking')),
            ],
        ),
    ]
