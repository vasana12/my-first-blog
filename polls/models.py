# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Htdocs(models.Model):
    keyword = models.CharField(max_length=200, blank=True, null=True)
    stdate = models.DateField(blank=True, null=True)
    endate = models.DateField(blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    accesstime = models.DateTimeField(blank=True, null=True)
    publishtime = models.DateTimeField(blank=True, null=True)
    nlike = models.IntegerField(blank=True, null=True)
    nreply = models.IntegerField(blank=True, null=True)
    iscommercial = models.CharField(max_length=5, blank=True, null=True)
    htmltext = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htdocs'



class Breakdown(models.Model):
    ByWhat = models.CharField(db_column='ByWhat', max_length=200, blank=True, null=True)  # Field name made lowercase.
    keywordA = models.CharField(db_column='keywordA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    keywordB = models.CharField(db_column='keywordB', max_length=200, blank=True, null=True)  # Field name made lowercase.
    keywordC = models.CharField(db_column='keywordC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    channelA = models.CharField(db_column='channelA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    channelB = models.CharField(db_column='channelB', max_length=200, blank=True, null=True)  # Field name made lowercase.
    channelC = models.CharField(db_column='channelC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    channelD = models.CharField(db_column='channelD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    periodA = models.CharField(db_column='periodA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    periodB = models.CharField(db_column='periodB', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nUrlA = models.IntegerField(db_column='nUrlA', blank=True, null=True)  # Field name made lowercase.
    nUrlB = models.IntegerField(db_column='nUrlB', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.keywordA

class Urllist(models.Model):
    keyword = models.CharField(max_length=200, blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    stdate = models.DateField(blank=True, null=True)
    endate = models.DateField(blank=True, null=True)
    accesstime = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    publishtime = models.DateTimeField(blank=True, null=True)
    crawled = models.CharField(max_length=5, blank=True, null=True)
    crawltime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'urllist'
