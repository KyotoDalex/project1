# Generated by Django 4.2.2 on 2023-06-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_postpage_categories'),
        ('snippets', '0002_newscategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakingNewsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('open_in_new_tab', models.BooleanField(blank=True, default=True)),
                ('page', models.ManyToManyField(to='post.postpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
