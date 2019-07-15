from django.db import models
from DjangoUeditor.models import UEditorField


class TypeInfo(models.Model):
	ttitle = models.CharField(max_length=20, verbose_name='类别名称')
	isDelete = models.BooleanField(default=False, verbose_name='是否删除')

	def __str__(self):
		return self.ttitle

	class Meta:
		verbose_name = '类别信息'
		verbose_name_plural = verbose_name

class GoodsInfo(models.Model):
	gtitle = models.CharField(max_length=20, verbose_name='商品名称')
	gpic = models.ImageField(upload_to='df_goods/', verbose_name='商品图片')
	gprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='商品价格')
	gunit = models.CharField(max_length=20, verbose_name='单位')
	gclick = models.IntegerField(verbose_name='点击量')
	gjianjie = models.CharField(max_length=200, verbose_name='简介')
	gkucun = models.IntegerField(verbose_name='库存')
	gcontent = UEditorField(width=600, height=300, toolbars="full", imagePath="images/", filePath="files/",upload_settings={"imageMaxSize":1204000},settings={}, verbose_name='内容')
	gtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE, verbose_name='类别')
	isDelete = models.BooleanField(default=False, verbose_name='是否删除')

	def __str__(self):
		return self.gtitle

	class Meta:
		verbose_name = '商品信息'
		verbose_name_plural = verbose_name