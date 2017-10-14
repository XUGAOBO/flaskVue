# -*- encoding: utf-8 -*-
import requests
'''
r = requests.get('https://m-flight.jd.id/tiket-pesawat/api/advertisement/page/mobile_ticket_ad_slot_page/module/carousel_moudel')
print r.json()
print r.status_code
print r.encoding
print r.cookies
'''
r = requests.get('https://m-flight.jd.id')
print r.content

