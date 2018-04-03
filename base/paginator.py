# coding=utf-8
import pdb
from django.core.paginator import Paginator,PageNotAnInteger,InvalidPage

class ToolPaginator():
    range=5

    def paginate(self,objects,page=1,page_size=10):
        paginator = Paginator(objects, page_size)
        try:
            partial=paginator.page(page)
        except PageNotAnInteger:
            partial=paginator.page(1)
        except InvalidPage:
            partial=paginator.page(paginator.num_pages)

        total_page=paginator.num_pages

        page=int(page)
        page_header,page_footer=1,total_page
        has_page_hader,has_page_footer=True,True

        # 总共分页数没有10页
        # 总共分页数大于10页,并且当前分页数在前5条范围内
        if (total_page <= self.range):
            has_page_footer=False
            has_page_hader=False
            page_range=xrange(1,total_page)
        elif (page < self.range):
            has_page_hader=False
            page_range=xrange(1,self.range+1)
        elif page + self.range > total_page + 1:
            has_page_footer=False
            page_range=xrange(total_page+1 -self.range,total_page)
        else:
            page_range=xrange(page-2,page+3)

        page_result=dict(page=page if page < total_page else total_page,
                       page_size=page_size,
                       has_page_footer=has_page_footer,
                       has_page_hader=has_page_hader,
                       page_range=page_range,
                       page_header=page_header,
                       page_footer=page_footer,
                       has_previous=partial.has_previous(),
                       has_next=partial.has_next(),
                       total_page=total_page,
                       total_count=paginator.count,
                       previous_page_number=partial.previous_page_number() if partial.has_previous() else 1,
                       next_page_number=partial.next_page_number() if partial.has_next() else paginator.num_pages)

        return partial,page_result