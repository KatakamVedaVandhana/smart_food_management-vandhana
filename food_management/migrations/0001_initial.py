# Generated by Django 2.2.1 on 2020-07-01 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Indian-Bread', 'Indian-Bread'), ('Curry', 'Curry'), ('Rice', 'Rice')], max_length=200)),
                ('units', models.CharField(choices=[('pieces', 'pieces'), ('cups', 'cups'), ('laddles', 'laddles')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_type', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=200)),
                ('from_time_string', models.TimeField()),
                ('to_time_string', models.TimeField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MealCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_course', models.CharField(choices=[('Half-meal', 'Half-meal'), ('Full-meal', 'Full-meal'), ('Custom-meal', 'Custom-meal'), ('Skip-meal', 'Skip-meal')], max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_management.Items')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_management.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('quality', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('taste', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_management.Items')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_management.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='UserMealStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('custom_meal_quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food_management.Items')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_management.Meal')),
                ('meal_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_management.MealCourse')),
            ],
        ),
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_management.Meal')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='item',
            field=models.ManyToManyField(through='food_management.MealCourse', to='food_management.Items'),
        ),
        migrations.CreateModel(
            name='FoodWastage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_wasted', models.IntegerField()),
                ('food_prepared', models.IntegerField()),
                ('base_unit', models.CharField(choices=[('pieces', 'pieces'), ('kg', 'kg')], max_length=100)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_management.Items')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_management.Meal')),
            ],
        ),
    ]
