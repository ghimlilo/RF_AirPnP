# Generated by Django 4.0 on 2021-12-24 07:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_number', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('total_price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.host')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'bookings',
            },
        ),
    ]
