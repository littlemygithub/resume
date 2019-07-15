from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	typelist = TypeInfo.objects.all()
	type1_0 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
	type1_1 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
	type2_0 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
	type2_1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
	type3_0 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
	type3_1 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
	type4_0 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
	type4_1 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
	type5_0 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
	type5_1 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
	type6_0 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
	type6_1 = typelist[5].goodsinfo_set.order_by('-id')[0:4]

	context = {
		'title': '首页',
		'type1_0': type1_0,
		'type1_1': type1_1,
		'type2_0': type2_0,
		'type2_1': type2_1,
		'type3_0': type3_0,
		'type3_1': type3_1,
		'type4_0': type4_0,
		'type4_1': type4_1,
		'type5_0': type5_0,
		'type5_1': type5_1,
		'type6_0': type6_0,
		'type6_1': type6_1,
	}
	return render(request, 'df_goods/index.html', context)

def list(request, tid, pindex, sort):
	typeinfo = TypeInfo.objects.get(pk=int(tid))
	news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
	if sort=='1': # 最新
		goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
	elif sort=='2': # 价格
		goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
	elif sort=='3': # 人气, 点击量
		goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
	paginator = Paginator(goods_list, 10)
	page = paginator.get_page(int(pindex))
	context = {
		'title': typeinfo.ttitle,
		'news': news,
		'page': page,
		'paginator': paginator,
		'sort': sort,
		'typeinfo': typeinfo,
		'guest_cart': 1
	}
	return render(request, 'df_goods/list.html', context)

def detail(request, id):
	goods = GoodsInfo.objects.get(id=int(id))
	goods.gclick = goods.gclick + 1
	goods.save()
	news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
	context = {
		'title': goods.gtype.ttitle,
		'goods': goods,
		'news': news,
		'id': id
	}

	# 记录最近浏览使用, 在用户中心使用
	if request.session.has_key('user_id'):
		key = str(request.session.get('user_id', ''))
		goods_ids = request.session.get(key, '')
		goods_id = str(goods.id)

		if goods_ids != '':
			if goods_ids.count(goods_id) >= 1:
				goods_ids.remove(goods_id)
			goods_ids.insert(0,goods_id)
			if len(goods_ids) >= 6:
				del goods_ids[5]
		else:
			goods_ids = []
			goods_ids.append(goods_id)
		request.session[key] = goods_ids
	return render(request, 'df_goods/detail.html', context)

