# Generated by Django 4.2.4 on 2023-11-13 08:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20, verbose_name='رنگ')),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='تعداد')),
                ('completed', models.BooleanField(default=False, verbose_name='تکمیل شده؟')),
            ],
            options={
                'verbose_name': 'رنگ',
                'verbose_name_plural': 'رنگ\u200cها',
            },
        ),
        migrations.CreateModel(
            name='cuts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cut', models.CharField(max_length=200, verbose_name='برش')),
                ('customcode', models.IntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='کد دلخواه')),
                ('weight', models.DecimalField(decimal_places=3, max_digits=12, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='ورن')),
                ('colortype', models.CharField(max_length=8, verbose_name='نوع رنگ')),
                ('sizetype', models.CharField(max_length=8, verbose_name='نوع سایز')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('cdate', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('edate', models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ تصحیح')),
                ('completed', models.BooleanField(default=False, verbose_name='تکمیل شده؟')),
            ],
            options={
                'verbose_name': 'برش',
                'verbose_name_plural': 'برش\u200cها',
            },
        ),
        migrations.CreateModel(
            name='sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5, verbose_name='سایز')),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='تعداد')),
                ('completed', models.BooleanField(default=False, verbose_name='تکمیل شده؟')),
                ('cut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.cuts', verbose_name='برش')),
            ],
            options={
                'verbose_name': 'سایز',
                'verbose_name_plural': 'سایزها',
            },
        ),
        migrations.CreateModel(
            name='lines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=32, verbose_name='خط دوخت')),
                ('price', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='قیمت')),
                ('completed', models.BooleanField(default=False, verbose_name='تکمیل شده؟')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.colors', verbose_name='رنگ')),
                ('cut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.cuts', verbose_name='برش')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.sizes', verbose_name='سایز')),
            ],
            options={
                'verbose_name': 'خط',
                'verbose_name_plural': 'خط\u200cها',
            },
        ),
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False, verbose_name='تکمیل شده؟')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.colors', verbose_name='رنگ')),
                ('cut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.cuts', verbose_name='برش')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.lines', verbose_name='خط دوخت')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.sizes', verbose_name='سایز')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='دوزنده')),
            ],
            options={
                'verbose_name': 'کار',
                'verbose_name_plural': 'کارها',
            },
        ),
        migrations.AddField(
            model_name='colors',
            name='cut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.cuts', verbose_name='برش'),
        ),
        migrations.AddField(
            model_name='colors',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.sizes', verbose_name='سایز'),
        ),
        migrations.CreateModel(
            name='amounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalcolors', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='تعداد رنگ')),
                ('totalsizes', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='تعداد سایز')),
                ('totallines', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='تعداد خط')),
                ('cut', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='workshop.cuts', verbose_name='برش')),
            ],
            options={
                'verbose_name': 'تعداد',
                'verbose_name_plural': 'تعدادها',
            },
        ),
    ]
