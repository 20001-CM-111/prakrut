# Generated by Django 4.1.2 on 2022-10-06 07:40

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
            name='Vegetable',
            fields=[
                ('Name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Image', models.ImageField(default='', upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='YellowCucumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='YellowCucumber', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Tomato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Tomato', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Taro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Taro', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Sweetpotato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Sweetpotato', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='SpineGourd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='SpineGourd', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Spinach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Spinach', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='SnakeGourd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='SnakeGourd', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='RunnerBeans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='RunnerBeans', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='RidgeGourd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='RidgeGourd', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Radish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Radish', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=100)),
                ('name', models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('product', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Potato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Potato', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Onion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Onion', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Okra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Okra', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='IvyGourd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='IvyGourd', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='GreenBeans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='GreenBeans', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Ginger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Ginger', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Garlic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Garlic', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='DrumStick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='DrumStick', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='CurryLeaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='CurryLeaves', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Coriander',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Coriander', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Chillies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Chillies', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Cauliflower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Cauliflower', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Carrot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Carrot', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Capsicum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Capsicum', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Cabbage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Cabbage', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Brinjal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Brinjal', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='BottleGourd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='BottleGourd', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='BitterGourd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='BitterGourd', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Beetroot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Beetroot', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Amaranthus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('user', models.CharField(max_length=100, unique=True)),
                ('name', models.ForeignKey(default='Amaranthus', on_delete=django.db.models.deletion.CASCADE, to='try.vegetable')),
            ],
            options={
                'unique_together': {('Price', 'user')},
            },
        ),
    ]
