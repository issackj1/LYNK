# Generated by Django 2.1.7 on 2019-02-17 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compillerwebsite', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=20)),
                ('points', models.FloatField()),
                ('letter_grade', models.CharField(choices=[('a+', 'A+'), ('a', 'A'), ('a-', 'A-'), ('b+', 'B+'), ('b', 'B'), ('b-', 'B-'), ('c+', 'C+'), ('c', 'C'), ('c-', 'C-'), ('d+', 'D+'), ('d', 'D'), ('d-', 'D-'), ('f', 'F')], default='A+', max_length=3)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compillerwebsite.Assignment')),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='grade',
            new_name='level',
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compillerwebsite.Student'),
        ),
    ]