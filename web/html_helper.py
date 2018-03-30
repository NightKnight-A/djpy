# -*- coding: utf-8 -*-
from django.utils.safestring import mark_safe


class PageInfo:
    def __init__(self,current_page,all_count,per_item=5):
        self.CurrentPage = current_page
        self.AllCount = all_count
        self.PerItem = per_item

    @property
    def start(self):
        return (self.CurrentPage-1)*self.PerItem

    @property
    def end(self):
        return self.CurrentPage*self.PerItem

    @property
    def all_pages_count(self):
        temp = divmod(self.AllCount, self.PerItem)

        if temp[1] == 0:
            all_pages_count = temp[0]
        else:
            all_pages_count = temp[0] + 1

        return all_pages_count


def Pager(page,all_pages_count):
    '''

    :param page:當前頁
    :param all_pages_count:總頁數
    :return:
    '''
    page_html = []

    first_html = '<a href="/index/%d">首頁</a>' % (1,)
    page_html.append(first_html)

    prev_html = '<a href="/index/%d">上一頁</a>' % (page - 1,)
    page_html.append(prev_html)

    begin = page - 6
    end = page + 5

    if all_pages_count < 11:
        begin = 0
        end = all_pages_count
    else:
        if page < 6:
            begin = 0
            end = 11
        else:
            if page + 6 > all_pages_count:
                begin = page - 6
                end = all_pages_count
            else:
                begin = page - 6
                end = page + 5

    for i in range(begin,end):
        if page == i + 1:
            a_html = '<a class="selected" href="/index/%d">%d</a>' % (i + 1, i + 1)
        else:
            a_html = '<a href="/index/%d">%d</a>' % (i + 1, i + 1)
        page_html.append(a_html)

    next_html = '<a href="/index/%d">下一頁</a>' % (page + 1,)
    page_html.append(next_html)

    end_html = '<a href="/index/%d">尾頁</a>' % (all_pages_count,)
    page_html.append(end_html)

    page_string = mark_safe(''.join(page_html))


    return page_string