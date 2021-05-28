# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def lista_clientes(request):
    return render(request, 'clientes.html')

