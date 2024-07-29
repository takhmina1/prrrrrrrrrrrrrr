# Generated by Django 5.0.6 on 2024-07-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('logo', models.URLField()),
                ('rate_to_usd', models.DecimalField(decimal_places=6, max_digits=15)),
                ('category', models.CharField(choices=[('Фиат', 'Фиат'), ('Криптовалюта', 'Криптовалюта')], max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
