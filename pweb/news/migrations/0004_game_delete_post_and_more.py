# Generated by Django 4.0.4 on 2022-06-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_post_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.RenameField(
            model_name='siteuser',
            old_name='is_editor',
            new_name='is_publisher',
        ),
        migrations.RenameField(
            model_name='siteuser',
            old_name='is_subscriber',
            new_name='is_user',
        ),
    ]
