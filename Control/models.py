from __future__ import unicode_literals

from auth import auth_models
from django.db import models

class HostInfo(models.Model):
    sys_type = (
        ('linux', 'Linux'),
        ('windows', 'Windows')
    )
    state_type = (
        ('up', 'UP'),
        ('down', 'Down')
    )
    HostName = models.CharField(max_length=128)
    System = models.CharField(choices=sys_type, max_length=64,  default='linux')
    Port = models.IntegerField(default=22)
    IpAddress = models.GenericIPAddressField(unique=True)
    NetMask = models.GenericIPAddressField()
    Status = models.CharField(choices=state_type,  max_length=64, default='up')
    Idc = models.ForeignKey('IDC', blank=True, null=True)
    Memo = models.CharField(max_length=128, blank=True, null=True)

    def __unicode__(self):
        return '%s,%s' % (self.HostName, self.IpAddress)

class HostUser(models.Model):
    auth_type = (
        ('key_rsa', 'KEY/RSA'),
        ('password', 'PASSWORD'),
    )
    UserName = models.CharField(max_length=64)
    PassWord = models.CharField(max_length=256, blank=True, null=True)
    AuthType = models.CharField(choices=auth_type, max_length=64, default='password')

    def __unicode__(self):
        return self.UserName

class HostGroup(models.Model):
    Name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.Name

class IDC(models.Model):
    Name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.Name

class UserAuthorized(models.Model):
    HostGroup = models.ManyToManyField('HostGroup')

