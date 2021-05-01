# -*- coding: UTF-8 -*-

spilt_list = []
filtered_string = ''
origin_string = ''

subscribe_path = '/Users/walker/.config/clash/火星聯盟-學習交流.yaml'
template_path = '/Users/walker/.config/clash/火星联盟-模板.yaml'
save_path = '/Users/walker/.config/clash/火星联盟.yaml'

with open(subscribe_path, 'r') as f: 
    file_string = f.read()
    file_string = file_string[file_string.find('proxies:')+9:file_string.find('proxy-groups:')]

proxies = 'proxies: \n' + file_string
origin_list = file_string.split('\n')

for str in origin_list: 
    str = str[str.find('name: ')+6:str.find('type: ')]
    if (str.find('靠前节点较为拥挤，请优先使用后排节点') == -1) and (str.find('发布:http://hxlm.io 电报:https://t.me/hxlm2') == -1): 
        spilt_list.append(str)
        origin_string = origin_string + str
origin_string = origin_string[:-2]

for str in spilt_list: 
    if not str.find('NF') == -1: 
        filtered_string = filtered_string + str
filtered_string = filtered_string[:-2]

proxy_groups = "\nproxy-groups: \n    "
proxy_groups = proxy_groups + "- { name: 代理节点, type: select, proxies: [Auto, Fallback, " + origin_string + "]}\n    "
proxy_groups = proxy_groups + "- { name: 媒体节点, type: select, proxies: [Auto-Medias, " + filtered_string + "]}\n    "
proxy_groups = proxy_groups + "- { name: ---------------------------------------------, type: select, proxies: [DIRECT]}\n    - { name: Apple, type: select, proxies: [代理节点, DIRECT]}\n    - { name: Medias, type: select, proxies: [媒体节点, 代理节点, DIRECT]}\n    - { name: China-Websites, type: select, proxies: [DIRECT, 代理节点]}\n    - { name: Final, type: select, proxies: [代理节点, DIRECT]}\n    - { name: --------------------------------------------, type: select, proxies: [DIRECT]}\n    "
proxy_groups = proxy_groups + "- { name: Auto, type: url-test, proxies: [" + origin_string + "], url: 'https://www.google.com/', interval: 86400 }\n    "
proxy_groups = proxy_groups + "- { name: Auto-Medias, type: url-test, proxies: [" + filtered_string + "], url: 'http://fast.com/', interval: 86400 }\n    "
proxy_groups = proxy_groups + "- { name: Fallback, type: fallback, proxies: [" + origin_string + "], url: 'https://www.google.com/', interval: 7200 }\n"

with open(template_path, 'r') as f: 
    file_string = f.read()
    fore = file_string[:file_string.find('proxies:')]
    back = '\n' + file_string[file_string.find('rules:'):]

new_file = fore + proxies + proxy_groups + back

with open(save_path, 'w') as f: 
    f.write(new_file)
