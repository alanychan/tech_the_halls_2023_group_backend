# Generated by Django 4.0.2 on 2023-03-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['category_name'],
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_categories',
            field=models.ManyToManyField(related_name='user_categories', to='users.Category'),
        ),
    ]
