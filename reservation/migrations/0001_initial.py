# Generated by Django 3.2.19 on 2023-06-26 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='No_of_guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OnlineBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('6 PM', '6 PM'), ('6:30 PM', '6:30 PM'), ('7 PM', '7 PM'), ('7:30 PM', '7:30 PM'), ('8 PM', '8 PM'), ('8:30 PM', '8:30 PM'), ('9 PM', '9 PM'), ('9:30 PM', '9:30 PM'), ('10 PM', '10 PM'), ('10:30 PM', '10:30 PM')], max_length=60, null=True)),
                ('occassion', models.CharField(choices=[('Birthday', 'Birthday'), ('Anniversary', 'Anniversary'), ('Date night ', 'Date night '), ('Business Meal', 'Business Meal'), ('Other', 'Other')], default='Birthday', max_length=150)),
                ('special_request', models.TextField(blank=True, max_length=300)),
                ('no_of_guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.no_of_guest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_booking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('no_of_guest', 'date', 'time')},
            },
        ),
    ]