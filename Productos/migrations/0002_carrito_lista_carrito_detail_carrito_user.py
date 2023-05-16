# Generated by Django 4.1 on 2023-04-05 01:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('total', models.IntegerField()),
                ('create', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.carrito')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.products')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='detail',
            field=models.ManyToManyField(through='Productos.Lista', to='Productos.products'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
