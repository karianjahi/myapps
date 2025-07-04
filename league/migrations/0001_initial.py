# Generated by Django 5.2.4 on 2025-07-04 19:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('season', models.CharField(choices=[('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022')], max_length=40)),
                ('winner', models.CharField(blank=True, max_length=40)),
                ('second', models.CharField(blank=True, max_length=40)),
                ('third', models.CharField(blank=True, max_length=40)),
                ('fourth', models.CharField(blank=True, max_length=40)),
                ('first_relegated', models.CharField(blank=True, max_length=40)),
                ('second_relegated', models.CharField(blank=True, max_length=40)),
                ('third_relegated', models.CharField(blank=True, max_length=40)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on', 'season'],
            },
        ),
    ]
