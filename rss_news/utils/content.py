import re


def filter_html_tags(string):
    # 正则过滤html字符串
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', string)
    return dd
