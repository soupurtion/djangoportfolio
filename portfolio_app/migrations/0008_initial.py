# Generated by Django 4.2.5 on 2023-10-11 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio_app', '0007_remove_project_portfolio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('contact_email', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('about', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('Portfolio', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, verbose_name='UCCS Email')),
                ('major', models.CharField(choices=[('CSCI-PhD', 'PhD in Computer Science'), ('CSCI-BS', 'BS in Computer Science'), ('CPEN-BS', 'BS in Computer Engineering'), ('BIGD-BI', 'BI in Game Design and Development'), ('BICS-BI', 'BI in Computer Science'), ('BISC-BI', 'BI in Computer Security'), ('CSCI-BA', 'BA in Computer Science'), ('DASE-BS', 'BS in Data Analytics and Systems Engineering')], max_length=200)),
                ('portfolio', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectsInPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.project')),
            ],
            options={
                'unique_together': {('portfolio', 'project')},
            },
        ),
    ]