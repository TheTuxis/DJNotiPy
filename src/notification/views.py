# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.utils import simplejson
from apps.notification.models import Notification


@login_required
def get_all(request):
    response_data = []
    ntf_list = Notification.objects.filter(
        to=request.user
    ).order_by('-date_created')
    for ntf in ntf_list:
        s = {
            'id': ntf.id,
            'type': ntf.type.name,
            'title': ntf.title,
            'body': ntf.body,
            'author': ntf.author.get_full_name(),
            'readed': ntf.readed,
            'date': ntf.date_created.strftime('%d/%m/%Y %H:%M'),
        }
        response_data.append(s)
    return HttpResponse(
        simplejson.dumps(response_data),
        mimetype='application/json'
    )


@login_required
def get_new(request):
    response_data = []
    ntf_list = Notification.objects.filter(
        to=request.user, readed=False
    ).order_by('-date_created')
    for ntf in ntf_list:
        s = {
            'id': ntf.id,
            'type': ntf.type.name,
            'title': ntf.title,
            'body': ntf.body,
            'author': ntf.author.get_full_name(),
            'date': ntf.date_created.strftime('%d/%m/%Y %H:%M'),
        }
        response_data.append(s)
    return HttpResponse(
        simplejson.dumps(response_data),
        mimetype='application/json'
    )


@login_required
def readed(request, id_ntf):
    ntf_list = Notification.objects.get(pk=id_ntf)
    ntf_list.readed = True
    ntf_list.save()
    return HttpResponse(
        'OK'
    )
