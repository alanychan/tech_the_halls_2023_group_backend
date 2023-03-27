from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_category_customuser_user_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_categories',
            new_name='categories',
        ),
    ]
