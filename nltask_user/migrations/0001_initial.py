# Generated by Django 3.2.8 on 2021-10-30 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nltask_app', '0003_auto_20211030_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('advisors', models.ManyToManyField(to='nltask_app.Advisor')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nltask_app.advisor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nltask_user.user')),
            ],
        ),
    ]
