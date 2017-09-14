# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 12:30:32 2017

@author: swimb
"""

#num_periods = 1
parameter = 'tavg'
state_id = 44
num_months = 8
year = '2016'
template_base = 'http://www.ncdc.noaa.gov/temp-and-precip/climatological-'
template_base = template_base + 'rankings/download.xml?'
template_add = 'parameter=%s&state=%s&div=0&month=%s&'
template_add = template_add +'periods[]=6&year=%s#'
insert_these = (parameter,state_id,num_months,year)
template_add = template_add % insert_these
#print template_base + template_add
site = template_base + template_add



import requests
from lxml import objectify
from lxml import etree

response = requests.get(site).content
#ET.fromstring(requests.get(url).content)
#print "\nFormatted XML from web site"
#print "==========================="
#print response

root = objectify.fromstring(response)
#print 'Root Tag: ', root.tag, '\n'

#print "Formatted XML from web site"
#print "==========================="
etree.tostring(root, pretty_print=True), '\n'

user_name = 'allennox'
insert_this = (user_name)
print insert_this


print root['data']['value']
print root['data']['twentiethCenturyMean']
print root['data']['lowRank']
print root['data']['highRank']
#print 'Heat Index: ',root['heat_index_string']