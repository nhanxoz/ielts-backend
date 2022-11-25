# Generated by Django 3.2 on 2022-11-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='USERNAME', max_length=50, null=True)),
                ('createdtime', models.DateTimeField(blank=True, db_column='CREATEDTIME', null=True)),
                ('image', models.TextField(blank=True, db_column='IMAGE', null=True)),
            ],
            options={
                'db_table': 'ACCOUNT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=10, primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, db_column='CONTENT', max_length=10, null=True)),
            ],
            options={
                'db_table': 'ANSWER',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=10, primary_key=True, serialize=False)),
                ('image', models.TextField(blank=True, db_column='IMAGE', null=True)),
                ('band', models.CharField(blank=True, db_column='BAND', max_length=10, null=True)),
                ('l', models.CharField(blank=True, db_column='L', max_length=10, null=True)),
                ('r', models.CharField(blank=True, db_column='R', max_length=10, null=True)),
                ('w', models.CharField(blank=True, db_column='W', max_length=10, null=True)),
                ('s', models.CharField(blank=True, db_column='S', max_length=10, null=True)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=10, null=True)),
                ('time', models.DateTimeField(blank=True, db_column='TIME', null=True)),
            ],
            options={
                'db_table': 'CERTIFICATE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('createtime', models.DateField(blank=True, db_column='CREATETIME', null=True)),
                ('displayorder', models.IntegerField(blank=True, db_column='DISPLAYORDER', null=True)),
                ('vote', models.IntegerField(blank=True, db_column='VOTE', null=True)),
                ('downvote', models.IntegerField(blank=True, db_column='DOWNVOTE', null=True)),
            ],
            options={
                'db_table': 'COMMENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=50, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=50, null=True)),
                ('startdate', models.DateField(blank=True, db_column='STARTDATE', null=True)),
                ('createdate', models.DateField(blank=True, db_column='CREATEDATE', null=True)),
                ('roomid', models.CharField(blank=True, db_column='ROOMID', max_length=10, null=True)),
            ],
            options={
                'db_table': 'COURSE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Essayquestion',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, db_column='CONTENT', null=True)),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('information', models.TextField(blank=True, db_column='INFORMATION', null=True)),
                ('displayorder', models.IntegerField(blank=True, db_column='DISPLAYORDER', null=True)),
                ('createdtime', models.DateField(blank=True, db_column='CREATEDTIME', null=True)),
            ],
            options={
                'db_table': 'ESSAYQUESTION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('createddate', models.CharField(blank=True, db_column='CREATEDDATE', max_length=10, null=True)),
                ('questions', models.CharField(blank=True, db_column='QUESTIONS', max_length=10, null=True)),
                ('type', models.CharField(blank=True, db_column='TYPE', max_length=10, null=True)),
            ],
            options={
                'db_table': 'EXAM',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('groupid', models.IntegerField(db_column='GROUPID', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='NAME', null=True)),
            ],
            options={
                'db_table': 'GROUP',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('starttime', models.DateTimeField(blank=True, db_column='STARTTIME', null=True)),
                ('endtime', models.DateTimeField(blank=True, db_column='ENDTIME', null=True)),
                ('active', models.BooleanField(blank=True, db_column='ACTIVE', null=True)),
                ('content', models.TextField(blank=True, db_column='CONTENT', null=True)),
            ],
            options={
                'db_table': 'HISTORY',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('createdtime', models.DateField(blank=True, db_column='CREATEDTIME', null=True)),
                ('content', models.TextField(blank=True, db_column='CONTENT', null=True)),
            ],
            options={
                'db_table': 'MAIL',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, db_column='TITLE', null=True)),
                ('content', models.TextField(blank=True, db_column='CONTENT', null=True)),
                ('vote', models.IntegerField(blank=True, db_column='VOTE', null=True)),
                ('downvote', models.IntegerField(blank=True, db_column='DOWNVOTE', null=True)),
            ],
            options={
                'db_table': 'POST',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, db_column='CONTENT', null=True)),
                ('subquestions', models.CharField(blank=True, db_column='SUBQUESTIONS', max_length=10, null=True)),
                ('audiofile', models.CharField(blank=True, db_column='AUDIOFILE', max_length=10, null=True)),
                ('imagefile', models.CharField(blank=True, db_column='IMAGEFILE', max_length=10, null=True)),
            ],
            options={
                'db_table': 'QUESTION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Questiontype',
            fields=[
                ('typeid', models.IntegerField(db_column='TYPEID', primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, db_column='TYPE', max_length=10, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=10, null=True)),
            ],
            options={
                'db_table': 'QUESTIONTYPE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('recordid', models.CharField(blank=True, db_column='RECORDID', max_length=50, null=True)),
                ('recoredid', models.CharField(blank=True, db_column='RECOREDID', max_length=64, null=True)),
                ('filepath', models.CharField(blank=True, db_column='FILEPATH', max_length=255, null=True)),
                ('size', models.FloatField(blank=True, db_column='SIZE', null=True)),
                ('published', models.IntegerField(blank=True, db_column='PUBLISHED', null=True)),
                ('createdtime', models.DateTimeField(blank=True, db_column='CREATEDTIME', null=True)),
                ('modified', models.DateTimeField(blank=True, db_column='MODIFIED', null=True)),
            ],
            options={
                'db_table': 'RECORDING',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reportperlesson',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('isabsent_field', models.BooleanField(blank=True, db_column='ISABSENT?', null=True)),
                ('reasonabsent', models.TextField(blank=True, db_column='REASONABSENT', null=True)),
                ('comment', models.TextField(blank=True, db_column='COMMENT', null=True)),
                ('scorehomework', models.FloatField(blank=True, db_column='SCOREHOMEWORK', null=True)),
            ],
            options={
                'db_table': 'REPORTPERLESSON',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('rolename', models.CharField(blank=True, db_column='ROLENAME', max_length=50, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=100, null=True)),
            ],
            options={
                'db_table': 'ROLE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rolegroup',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=50, null=True)),
            ],
            options={
                'db_table': 'ROLEGROUP',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roominfo',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('roomtitle', models.CharField(blank=True, db_column='ROOMTITLE', max_length=50, null=True)),
                ('roomid', models.CharField(blank=True, db_column='ROOMID', max_length=50, null=True)),
                ('joinedparticipants', models.IntegerField(blank=True, db_column='JOINEDPARTICIPANTS', null=True)),
                ('isrunning', models.BooleanField(blank=True, db_column='ISRUNNING', null=True)),
                ('isrecording', models.IntegerField(blank=True, db_column='ISRECORDING', null=True)),
                ('recorderid', models.CharField(blank=True, db_column='RECORDERID', max_length=50, null=True)),
                ('isactivertmp', models.IntegerField(blank=True, db_column='ISACTIVERTMP', null=True)),
                ('rtmpnodeid', models.CharField(blank=True, db_column='RTMPNODEID', max_length=30, null=True)),
                ('webhookurl', models.CharField(blank=True, db_column='WEBHOOKURL', max_length=255, null=True)),
                ('isbreakoutroom', models.IntegerField(blank=True, db_column='ISBREAKOUTROOM', null=True)),
                ('parentroomid', models.BinaryField(blank=True, db_column='PARENTROOMID', max_length='max', null=True)),
                ('creationtime', models.DateTimeField(blank=True, db_column='CREATIONTIME', null=True)),
                ('endedtime', models.DateTimeField(blank=True, db_column='ENDEDTIME', null=True)),
                ('modified', models.DateTimeField(blank=True, db_column='MODIFIED', null=True)),
            ],
            options={
                'db_table': 'ROOMINFO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('fullname', models.CharField(blank=True, db_column='FULLNAME', max_length=100, null=True)),
                ('level', models.CharField(blank=True, db_column='LEVEL', max_length=10, null=True)),
                ('dob', models.DateField(blank=True, db_column='DOB', null=True)),
                ('startdate', models.DateField(blank=True, db_column='STARTDATE', null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PHONENUMBER', max_length=15, null=True)),
                ('image', models.CharField(blank=True, db_column='IMAGE', max_length=100, null=True)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=50, null=True)),
                ('currentcourse', models.TextField(blank=True, db_column='CURRENTCOURSE', null=True)),
                ('learnedcourse', models.TextField(blank=True, db_column='LEARNEDCOURSE', null=True)),
            ],
            options={
                'db_table': 'STUDENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subquestion',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=10, primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, db_column='CONTENT', null=True)),
            ],
            options={
                'db_table': 'SUBQUESTION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('definition', models.BinaryField(blank=True, max_length='max', null=True)),
            ],
            options={
                'db_table': 'sysdiagrams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('fullname', models.CharField(blank=True, db_column='FULLNAME', max_length=100, null=True)),
                ('dob', models.DateField(blank=True, db_column='DOB', null=True)),
                ('startdate', models.DateField(blank=True, db_column='STARTDATE', null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PHONENUMBER', max_length=15, null=True)),
                ('image', models.CharField(blank=True, db_column='IMAGE', max_length=100, null=True)),
                ('address', models.CharField(blank=True, db_column='ADDRESS', max_length=50, null=True)),
                ('billing_account', models.CharField(blank=True, db_column='BILLING ACCOUNT', max_length=25, null=True)),
                ('billing_bank', models.CharField(blank=True, db_column='BILLING BANK', max_length=25, null=True)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=50, null=True)),
                ('note', models.TextField(blank=True, db_column='NOTE', null=True)),
                ('taughtcourse', models.TextField(blank=True, db_column='TAUGHTCOURSE', null=True)),
            ],
            options={
                'db_table': 'TEACHER',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('transcode', models.TextField(blank=True, db_column='TRANSCODE', null=True)),
                ('transtime', models.DateTimeField(blank=True, db_column='TRANSTIME', null=True)),
                ('amount', models.IntegerField(blank=True, db_column='AMOUNT', null=True)),
            ],
            options={
                'db_table': 'TRANSACTION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Writingessay',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, db_column='CONTENT', null=True)),
                ('score', models.FloatField(blank=True, db_column='SCORE', null=True)),
            ],
            options={
                'db_table': 'WRITINGESSAY',
                'managed': False,
            },
        ),
    ]