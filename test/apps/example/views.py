# -*- coding: utf-8 -*-
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from django.core.serializers.json import DjangoJSONEncoder


@login_required
def view_example_index(request):
    return render_to_response(
        'base.html',
        RequestContext(
            request,
            {}
        ),
    )
