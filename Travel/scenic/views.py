from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.db.models import F

# def index(request):
#     if request.method=='GET':
#         return render(request,'scenic/information.html')
def ticket(request):
    if request.method == 'GET':
        return render(request, 'scenic/ticket.html', locals())
def scenic2(request):
    if request.method == 'GET':
        return render(request,'scenic/information02.html')

def insert_scenic1(request):
    dic={
        'sce_name':"秦岭野生动物园",
        'sce_topic': '野生动物保护教育基地',
        'brief_des': '徜徉在丛林与花径之间，听百鸟与清风唱和，看猛兽与群山相伴。',
        'bus_go':'环山旅游１号线、334路',
        'car_go':'西安火车站-曲江路-包茂高速公路-关中环线-西安秦岭野生动物园。',
        'pre_price':60,
        'local_price':40,
        # 'rebate':rebate,
        'low_time':"2019-8-10",
        'grage':'AAAA',
        'sce_address':"陕西省西安市长安区滦镇",
        'open_time':"1月1日-2月28日（淡季） 09:00-17:00；3月1日-10月31日（旺季） 09:00-17:30；11月1日-12月31日（淡季） 09:00-17:00秦岭野生动物园虫虫乐园：全年 09:30-17:00；最晚入园时间：17:00．",
        'img_1':"/static/images/scenic/info/h1.jpg",
        'img_2':"/static/images/scenic/info/h2.jpg",
        'img_3':"/static/images/scenic/info/h3.jpg",
        'img_4':"/static/images/scenic/info/h4.jpg",
        'img_5':"/static/images/scenic/info/h5.jpg",
        'word1':'动物园',
        'word2':'游乐场',
        }
    # re = dic['local_price'] / dic['pre_price']
    # dic['rebate']=re
    hf_scenic=models.Scenic1(
        sce_name=dic['sce_name'],
        sce_topic=dic['sce_topic'],
        brief_des=dic['brief_des'],
        bus_go=dic['bus_go'],
        car_go=dic['car_go'],
        pre_price=dic['pre_price'],
        local_price=dic['local_price'],
        low_time=dic['low_time'],
        grage=dic['grage'],
        sce_address=dic['sce_address'],
        open_time=dic['open_time'],
        img_1=dic['img_1'],
        img_2=dic['img_2'],
        img_3=dic['img_3'],
        img_4=dic['img_4'],
        img_5=dic['img_5'],
        word1=dic['word1'],
        word2=dic['word2'],
    )
    hf_scenic.save()
    return HttpResponse("插入成功")
def add_scen(request):
    if request.method == 'GET':
        sens=models.Scenic1.objects.all()
        sens.update(rebate=F('local_price')/F('pre_price')*10)
        for sen in sens:
            sen.rebate = round(sen.rebate, 1)
        return render(request,'scenic/information.html',locals())


def add_ticket1(request):
    if request.method == 'GET':
        sens = models.Scenic1.objects.all()
        for sen in sens:
            if sen.sce_name=='秦岭野生动物园':
                return render(request,'scenic/ticket.html',locals())

def add_ticket2(request):
    if request.method == 'GET':
        intrs=models.Introduce.objects.all()
        for intr in intrs:
            if intr.sce_name2.scen_name == '秦岭野生动物园':
                return render(request, 'scenic/ticket.html', locals())
def add_ticket3(request,map):
    pass
def add_ticket4(request,tic):
    pass
# def ticket(request):
#     if request.method == 'GET':
#
#         sen1=models.Scenic1.objects.get(sce_name='秦岭野生动物园')
#         intrs=models.Introduce.objects.all()
#         for intr in intrs:
#             if intr.sce_name2.scen_name=='秦岭野生动物园':
#                 return render(request, 'scenic/ticket.html', locals())

