# Generated by Django 4.1.1 on 2022-09-23 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lc_question_id', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lc_username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('date_joined', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SolvedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('last_checked', models.DateTimeField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streakapp.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streakapp.user')),
            ],
        ),
    ]