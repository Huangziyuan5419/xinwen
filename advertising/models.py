from django.db import models


class Advertising(models.Model):
    '''
    广告轮播表
    '''
    picture_url = models.CharField(max_length=200, verbose_name='图片url')
    link_url = models.CharField(max_length=200, verbose_name='点击url')
    sort = models.IntegerField(verbose_name='排序')
    mod = models.CharField(max_length=32, verbose_name='模块')
    status = models.BooleanField(default=True, verbose_name='状态')
    change_time = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        db_table = 'tb_advertising'
        verbose_name = '广告轮播表'
        verbose_name_plural = verbose_name