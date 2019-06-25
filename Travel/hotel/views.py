from django.shortcuts import render
from django.http import HttpResponse
from . import models
import os
# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'hotel/order_hotel.html')

def test(requesst,x):
    print(x)
    return HttpResponse('测试成功%s'%x)


def init_db(request):
            pwd=os.path.dirname(__file__)
            fd=open(pwd+'hotel_db','r+')
            line="31#'富力希尔顿大酒店'#'新城区东新街199号（近民乐园）'#'029-87388888'#'西安富力希尔顿酒店坐落于古城西安市中心，周边繁华购物区林立，是商务出行和休闲度假的理想之选。步行即可到达闻名于世的明城墙和西安地标建筑钟楼。乘坐出租车仅需5分钟即可到达东大街、骡马市步行街及回民街，这里有西安特色的餐厅、购物及娱乐场所。 拥有城中稀缺宽敞大容量客房，西安富力希尔顿酒店客房面积均大于43平方米。酒店高雅的客房别出心裁将唐朝元素融入其中，并突出了房间的温馨舒适。所有客房均配备高速宽带无线上网及高水准的客用品。 西安富力希尔顿酒店将成为您在西安的会议和用餐新选择。三间风格各异的餐厅及酒吧、一间1200平方米的大宴会厅及6间多功能厅可为您提供多种规模的会议及宴会需求。'#'../../static/images/hotel/3star_hotel/1fulixierdun/11.jpg'#'../../static/images/hotel/3star_hotel/1fulixierdun/12.png'#'../../static/images/hotel/3star_hotel/1fulixierdun/13.png'#'../../static/images/hotel/3star_hotel/1fulixierdun/14.png'#'../../static/images/hotel/3star_hotel/1fulixierdun/15.png'#'星级酒店'"
            list=line.split('#')
            hotel=models.Hotel(id=list[0],hotel_name=list[1],address=list[2],phone=list[3],info=list[4],
                               hotel_p11=list[5],hotel_p12=list[6],hotel_p13=list[7],hotel_p14=list[8],hotel_p15=list[9]
                               ,hotel_level=list[10])
            hotel.save()
            return HttpResponse('初始化成功')




def fu_li_xi_er_dun(request):
    
    dict={
        'id':31,
        'hotel_name':'富力希尔顿大酒店',
        'hotel_p11':'/static/images/hotel/3star_hotel/1fulixierdun/11.jpg',
        'hotel_p12':'/static/images/hotel/3star_hotel/1fulixierdun/12.png',
        'hotel_p13':'/static/images/hotel/3star_hotel/1fulixierdun/13.png',
        'hotel_p14':'/static/images/hotel/3star_hotel/1fulixierdun/14.png',
        'hotel_p15':'/static/images/hotel/3star_hotel/1fulixierdun/15.png',
        'phone':'029-87388888',
        'address':'新城区东新街199号（近民乐园）',
        'infor':'西安富力希尔顿酒店坐落于古城西安市中心，周边繁华购物区林立，是商务出行和休闲度假的理想之选。步行即可到达闻名于世的明城墙和西安地标建筑钟楼。乘坐出租车仅需5分钟即可到达东大街、骡马市步行街及回民街，这里有西安特色的餐厅、购物及娱乐场所。 拥有城中稀缺宽敞大容量客房，西安富力希尔顿酒店客房面积均大于43平方米。酒店高雅的客房别出心裁将唐朝元素融入其中，并突出了房间的温馨舒适。所有客房均配备高速宽带无线上网及高水准的客用品。 西安富力希尔顿酒店将成为您在西安的会议和用餐新选择。三间风格各异的餐厅及酒吧、一间1200平方米的大宴会厅及6间多功能厅可为您提供多种规模的会议及宴会需求。',
        'room1_p':'../../static/images/hotel/3star_hotel/1fulixierdun/21.jpg',
        'room1_name':'希尔顿大床房',
        'room1_window':'窗户 有',
        'room1_area':'面积 43㎡',
        'room1_bed':'床型 大床1.8×2.0米1张',
        'room1_price':'977.00',
        'room2_p': '../../static/images/hotel/3star_hotel/1fulixierdun/22.jpg',
        'room2_name': '希尔顿双床客房',
        'room2_window': '窗户 有',
        'room2_area': '43㎡',
        'room2_bed': '床型 大床1.5×1.8米2张',
        'room2_price': '997.00',
        'room3_p': '../../static/images/hotel/3star_hotel/1fulixierdun/23.jpg',
        'room3_name': '希尔顿豪华套房',
        'room3_window': '窗户 有',
        'room3_area': '50㎡',
        'room3_bed': '大床1.8×2.0米1张',
        'room3_price': '1196.00',

    }
    return render(request,'hotel/hotel_ticket.html',dict)