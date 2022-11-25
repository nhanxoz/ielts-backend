# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Account(AbstractBaseUser):
    id = models.AutoField(db_column='ID', primary_key=True) # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=50, blank=True, null=True, unique=True)  # Field name made lowercase.
    USERNAME_FIELD = 'username'
    idgroup = models.ForeignKey('Group', models.DO_NOTHING, db_column='IDGROUP', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CREATEDTIME', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='IMAGE', blank=True, null=True)  # Field name made lowercase.
    is_staff=True
    
    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
    class Meta:
        managed = False
        db_table = 'ACCOUNT'


class Answer(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANSWER'


class Certificate(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    image = models.TextField(db_column='IMAGE', blank=True, null=True)  # Field name made lowercase.
    band = models.CharField(db_column='BAND', max_length=10, blank=True, null=True)  # Field name made lowercase.
    l = models.CharField(db_column='L', max_length=10, blank=True, null=True)  # Field name made lowercase.
    r = models.CharField(db_column='R', max_length=10, blank=True, null=True)  # Field name made lowercase.
    w = models.CharField(db_column='W', max_length=10, blank=True, null=True)  # Field name made lowercase.
    s = models.CharField(db_column='S', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CERTIFICATE'


class Comment(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accountid = models.ForeignKey(Account, models.DO_NOTHING, db_column='ACCOUNTID', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateField(db_column='CREATETIME', blank=True, null=True)  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DISPLAYORDER', blank=True, null=True)  # Field name made lowercase.
    supercommentid = models.ForeignKey('self', models.DO_NOTHING, db_column='SUPERCOMMENTID', blank=True, null=True)  # Field name made lowercase.
    postid = models.ForeignKey('Post', models.DO_NOTHING, db_column='POSTID', blank=True, null=True)  # Field name made lowercase.
    vote = models.IntegerField(db_column='VOTE', blank=True, null=True)  # Field name made lowercase.
    downvote = models.IntegerField(db_column='DOWNVOTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMMENT'


class Course(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='STARTDATE', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateField(db_column='CREATEDATE', blank=True, null=True)  # Field name made lowercase.
    roomid = models.CharField(db_column='ROOMID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COURSE'


class Essayquestion(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    information = models.TextField(db_column='INFORMATION', blank=True, null=True)  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DISPLAYORDER', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateField(db_column='CREATEDTIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESSAYQUESTION'


class Exam(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    createddate = models.CharField(db_column='CREATEDDATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    questions = models.CharField(db_column='QUESTIONS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    idcourse = models.ForeignKey(Course, models.DO_NOTHING, db_column='IDCOURSE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EXAM'


class Group(models.Model):
    groupid = models.IntegerField(db_column='GROUPID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Role', models.DO_NOTHING, db_column='ROLEID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GROUP'


class History(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='STARTTIME', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='ENDTIME', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='ACTIVE', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    accountid = models.ForeignKey(Account, models.DO_NOTHING, db_column='ACCOUNTID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HISTORY'


class Mail(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    createdtime = models.DateField(db_column='CREATEDTIME', blank=True, null=True)  # Field name made lowercase.
      # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.ForeignKey(Account, models.DO_NOTHING, db_column='TO', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAIL'


class Post(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='TITLE', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    vote = models.IntegerField(db_column='VOTE', blank=True, null=True)  # Field name made lowercase.
    downvote = models.IntegerField(db_column='DOWNVOTE', blank=True, null=True)  # Field name made lowercase.
    authorid = models.ForeignKey(Account, models.DO_NOTHING, db_column='AUTHORID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POST'


class Question(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    subquestions = models.CharField(db_column='SUBQUESTIONS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    examid = models.ForeignKey(Exam, models.DO_NOTHING, db_column='EXAMID', blank=True, null=True)  # Field name made lowercase.
    audiofile = models.CharField(db_column='AUDIOFILE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    imagefile = models.CharField(db_column='IMAGEFILE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QUESTION'


class Questiontype(models.Model):
    typeid = models.IntegerField(db_column='TYPEID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QUESTIONTYPE'


class Recording(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recordid = models.CharField(db_column='RECORDID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    roomid = models.ForeignKey('Roominfo', models.DO_NOTHING, db_column='ROOMID', blank=True, null=True)  # Field name made lowercase.
    recoredid = models.CharField(db_column='RECOREDID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FILEPATH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    size = models.FloatField(db_column='SIZE', blank=True, null=True)  # Field name made lowercase.
    published = models.IntegerField(db_column='PUBLISHED', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CREATEDTIME', blank=True, null=True)  # Field name made lowercase.
    modified = models.DateTimeField(db_column='MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RECORDING'


class Reportperlesson(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='STUDENTID', blank=True, null=True)  # Field name made lowercase.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='TEACHERID', blank=True, null=True)  # Field name made lowercase.
    isabsent_field = models.BooleanField(db_column='ISABSENT?', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    reasonabsent = models.TextField(db_column='REASONABSENT', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase.
    scorehomework = models.FloatField(db_column='SCOREHOMEWORK', blank=True, null=True)  # Field name made lowercase.
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='COURSEID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REPORTPERLESSON'


class Role(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='ROLENAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idrolegroup = models.ForeignKey('Rolegroup', models.DO_NOTHING, db_column='IDROLEGROUP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROLE'


class Rolegroup(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROLEGROUP'


class Roominfo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    roomtitle = models.CharField(db_column='ROOMTITLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    roomid = models.CharField(db_column='ROOMID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    joinedparticipants = models.IntegerField(db_column='JOINEDPARTICIPANTS', blank=True, null=True)  # Field name made lowercase.
    isrunning = models.BooleanField(db_column='ISRUNNING', blank=True, null=True)  # Field name made lowercase.
    isrecording = models.IntegerField(db_column='ISRECORDING', blank=True, null=True)  # Field name made lowercase.
    recorderid = models.CharField(db_column='RECORDERID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isactivertmp = models.IntegerField(db_column='ISACTIVERTMP', blank=True, null=True)  # Field name made lowercase.
    rtmpnodeid = models.CharField(db_column='RTMPNODEID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    webhookurl = models.CharField(db_column='WEBHOOKURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isbreakoutroom = models.IntegerField(db_column='ISBREAKOUTROOM', blank=True, null=True)  # Field name made lowercase.
    parentroomid = models.BinaryField(db_column='PARENTROOMID', blank=True, null=True)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CREATIONTIME', blank=True, null=True)  # Field name made lowercase.
    endedtime = models.DateTimeField(db_column='ENDEDTIME', blank=True, null=True)  # Field name made lowercase.
    modified = models.DateTimeField(db_column='MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROOMINFO'


class Student(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FULLNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(db_column='LEVEL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='STARTDATE', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PHONENUMBER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currentcourse = models.TextField(db_column='CURRENTCOURSE', blank=True, null=True)  # Field name made lowercase.
    learnedcourse = models.TextField(db_column='LEARNEDCOURSE', blank=True, null=True)  # Field name made lowercase.
    accountid = models.ForeignKey(Account, models.DO_NOTHING, db_column='ACCOUNTID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STUDENT'


class Subquestion(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    questiontype = models.ForeignKey(Questiontype, models.DO_NOTHING, db_column='QUESTIONTYPE', blank=True, null=True)  # Field name made lowercase.
    questionid = models.ForeignKey(Question, models.DO_NOTHING, db_column='QUESTIONID', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'SUBQUESTION'


class Teacher(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FULLNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ieltscertificate = models.ForeignKey(Certificate, models.DO_NOTHING, db_column='IELTSCERTIFICATE', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='STARTDATE', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PHONENUMBER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billing_account = models.CharField(db_column='BILLING ACCOUNT', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_bank = models.CharField(db_column='BILLING BANK', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='NOTE', blank=True, null=True)  # Field name made lowercase.
    taughtcourse = models.TextField(db_column='TAUGHTCOURSE', blank=True, null=True)  # Field name made lowercase.
    accountid = models.ForeignKey(Account, models.DO_NOTHING, db_column='ACCOUNTID', blank=True, null=True) 
    class Meta:
        managed = False
        db_table = 'TEACHER'


class Transaction(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    transcode = models.TextField(db_column='TRANSCODE', blank=True, null=True)  # Field name made lowercase.
    transtime = models.DateTimeField(db_column='TRANSTIME', blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    studentid = models.ForeignKey(Student, models.DO_NOTHING, db_column='STUDENTID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRANSACTION'


class Writingessay(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    questionid = models.ForeignKey(Essayquestion, models.DO_NOTHING, db_column='QUESTIONID', blank=True, null=True)  # Field name made lowercase.
    studentid = models.ForeignKey(Student, models.DO_NOTHING, db_column='STUDENTID', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    teacherid = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='TEACHERID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WRITINGESSAY'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)