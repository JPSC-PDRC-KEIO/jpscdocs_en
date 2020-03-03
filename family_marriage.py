# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq

html = open("./_build/html/family_marriage.html").read()

dom = pq(html)



for tr_node in dom.find("tr"):
    pq_tr_node = pq(tr_node)
    header = pq_tr_node.find("th")
    if header.is_("th"):
        print([th.text for th in pq_tr_node('th')])
    else:
        #print("hello", pq_tr_node('td').each(lambda i, e: pq(e).text))
        print([d.text for d in pq_tr_node('td')])
    td_node = pq_tr_node.find("td")
