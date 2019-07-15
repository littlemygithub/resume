from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from df_user.models import *
from df_user import user_decorator


# Create your views here.

@user_decorator.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title': '购物车',
        'page_name': 1,
        'carts': carts
    }
    return render(request, 'df_cart/cart.html', context)


@user_decorator.login
def add(request, gid, count):
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)
    if gid == 0 and request.is_ajax() and count == 0:
        count = CartInfo.objects.filter(user_id=uid).count()
        return JsonResponse({'count': count})

    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()

    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=uid).count()
        return JsonResponse({'count': count})
    else:
        return redirect('/cart/')

@user_decorator.login
def edit(request, cid, count):
    try:
        if request.is_ajax():
            goods = CartInfo.objects.get(id=int(cid))
            goods.count = int(count)
            goods.save()
            data = {'ok': 1}
    except Exception as e:
        data = {'ok': 0, 'e': e}
    return JsonResponse(data)

@user_decorator.login
def delete(request, cid):
    try:
        if request.is_ajax():
            goods = CartInfo.objects.get(id=int(cid))
            goods.delete()
            data = {
                'ok': 1
            }
    except Exception as e:
        data = {
            'ok': 0, 'e': e
        }
    return JsonResponse(data)
