# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    is_superuser = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=254)
    email = models.CharField(max_length=150)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)

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
    polls = models.ForeignKey('PollsBreakdown', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'htdocs'


class NaverNews(models.Model):
    keyword = models.CharField(max_length=200, blank=True, null=True)
    stdate = models.DateField(blank=True, null=True)
    endate = models.DateField(blank=True, null=True)
    publishtime = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    reporter = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    pcompany = models.CharField(max_length=200, blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    htmltext = models.TextField(blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    polls = models.ForeignKey('PollsBreakdown', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'naver_news'


class PolPhrase(models.Model):
    keyword = models.CharField(max_length=200, blank=True, null=True)
    function = models.CharField(max_length=200, blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    phrase = models.TextField(blank=True, null=True)
    pol = models.CharField(max_length=20, blank=True, null=True)
    stdate = models.DateField(blank=True, null=True)
    endate = models.DateField(blank=True, null=True)
    nurl = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pol_phrase'


class PolRate(models.Model):
    polls = models.ForeignKey('PollsBreakdown', models.DO_NOTHING, blank=True, null=True)
    keyword = models.CharField(max_length=200, blank=True, null=True)
    function = models.CharField(max_length=200, blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    fun_count = models.IntegerField(blank=True, null=True)
    pos_num = models.IntegerField(blank=True, null=True)
    neg_num = models.IntegerField(blank=True, null=True)
    pos_rate = models.CharField(max_length=20, blank=True, null=True)
    neg_rate = models.CharField(max_length=20, blank=True, null=True)
    stdate = models.DateField(blank=True, null=True)
    endate = models.DateField(blank=True, null=True)
    nurl = models.IntegerField(blank=True, null=True)
    crawltime = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pol_rate'


class PollsKeywordNumber(models.Model):
    polls = models.ForeignKey('PollsBreakdown', models.DO_NOTHING, blank=True, null=True)
    keyword = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    stdate = models.DateField(blank=True, null=True)
    endate = models.DateField(blank=True, null=True)
    nurl = models.IntegerField(db_column='nUrl', blank=True, null=True)  # Field name made lowercase.
    top300 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polls_keyword_number'

class PollsBreakdown(models.Model):
    bywhat = models.CharField(blank=True, db_column='ByWhat', max_length=200, null=True)
    keywordA = models.CharField(blank=True, db_column='keywordA', max_length=200, null=True)
    keywordB = models.CharField(blank=True, db_column='keywordB', max_length=200, null=True)
    keywordC = models.CharField(blank=True, db_column='keywordC', max_length=200, null=True)
    channelA = models.CharField(blank=True, db_column='channelA', max_length=200, null=True)
    channelB = models.CharField(blank=True, db_column='channelB', max_length=200, null=True)
    channelC = models.CharField(blank=True, db_column='channelC', max_length=200, null=True)
    periodA = models.CharField(blank=True, db_column='periodA', max_length=200, null=True)
    periodB = models.CharField(blank=True, db_column='periodB', max_length=200, null=True)
    periodC = models.CharField(blank=True, db_column='periodC', max_length=200, null=True)
    nUrlA = models.IntegerField(blank=True, db_column='nUrlA', null=True)
    nUrlB = models.IntegerField(blank=True, db_column='nUrlB', null=True)
    nUrlC = models.IntegerField(blank=True, db_column='nUrlC', null=True)
    saved_path = models.CharField(blank=True, max_length=200, null=True)
    saved_name = models.CharField(blank=True, max_length=200, null=True)
    usr_id = models.CharField(blank=True,db_column='usr_id',max_length=254, null=True)
    usr_key = models.IntegerField(blank=True, db_column='usr_key', null=True)
    status = models.CharField(blank=True, max_length=1, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    gather_st_time = models.DateTimeField(blank=True, null=True)
    gather_en_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polls_breakdown'

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
    polls = models.ForeignKey('PollsBreakdown', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'urllist'
