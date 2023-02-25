#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

distances = {}

msk_lndn = ((moscow[0] - london[0])**2 + (moscow[1]-london[1])**2)**.5
msk_prs = ((moscow[0] - paris[0])**2 + (moscow[1]-paris[1])**2)**.5
lndn_prs = ((london[0] - paris[0])**2 + (london[1]-paris[1])**2)**.5

# TODO здесь заполнение словаря
distances['MSK'] = {'London':msk_lndn, 'Paris':msk_prs}
distances['LNDN'] = {'Moscow': msk_lndn, 'Paris':lndn_prs}
distances['PRS'] = {'Moscow':msk_prs, 'London': lndn_prs}
print(distances)


dist = {}
dist['Moscow'] = {}
dist['Moscow']["London"] = msk_lndn
dist['Moscow']['Paris'] = msk_prs
dist['London'] = {}
dist['London']['Moscow'] = msk_lndn
dist['London']['Paris'] = lndn_prs
dist['Paris'] = {}
dist['Paris']['Moscow'] = msk_prs
dist['Paris']['London'] = msk_lndn

pprint(dist)