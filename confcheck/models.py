from django.db import models

# Create your models here.

class Item(models.Model):
    Id = models.IntegerField(primary_key=True, null=False)
    NamespaceId = models.IntegerField(null=False)
    Key = models.CharField(max_length=128, null=False)
    Value = models.TextField(null=False)
    Comment = models.CharField(max_length=1024, null=True)
    LineNum = models.IntegerField(null=True)
    IsDeleted = models.BooleanField(default=False, null=True)
    DataChange_CreatedBy = models.CharField(max_length=32, null=False)
    DataChange_CreatedTime = models.DateTimeField(null=False)
    DataChange_LastModifiedBy = models.CharField(max_length=32, null=True)
    DataChange_LastTime = models.DateTimeField(null=True)


class Namespace(models.Model):
    Id = models.IntegerField(primary_key=True, null=False)
    AppId = models.CharField(max_length=500, null=False)
    ClusterName = models.CharField(max_length=500, null=False)
    NamespaceName = models.CharField(max_length=500, null=False)
    IsDeleted = models.BooleanField(default=False, null=True)
    DataChange_CreatedBy = models.CharField(max_length=32, null=False)
    DataChange_CreatedTime = models.DateTimeField(null=False)
    DataChange_LastModifiedBy = models.CharField(max_length=32, null=True)
    DataChange_LastTime = models.DateTimeField(null=True)