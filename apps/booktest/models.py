# coding=utf-8
from django.db import models


# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)  # 图书名称
    bpub_date = models.DateField()  # 发布日期
    bread = models.IntegerField(default=0)  # 阅读量
    bcomment = models.IntegerField(default=0)  # 评论量
    image = models.CharField(max_length=50, default='测试')
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    class Meta:  # 元信息类
        db_table = 'bookinfo'  # 指定表的名称

    def __str__(self):
        """显示模型类描述信息"""
        return self.btitle


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄姓名
    hgender = models.BooleanField(default=True)  # 英雄性别
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    hcontent = models.CharField(max_length=100)  # 英雄描述信息
    test = models.CharField(max_length=100)  # 测试
    hbook = models.ForeignKey('BookInfo', on_delete=models.PROTECT)  # 英雄与图书表的关系为一对多，所以属性定义在英雄模型中

    class Meta:
        db_table = "heroinfo"

    def __str__(self):
        """显示模型类描述信息"""
        return self.hname
