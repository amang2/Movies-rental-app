from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound
from collections import OrderedDict
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    # def paginate_queryset(self, queryset, request, view=None):
    #     try:
    #         return super().paginate_queryset(queryset, request, view)
    #     except NotFound:
    #         # Handle the NotFound exception and return an empty page
    #         self.page = self.django_paginator_class(queryset, self.get_page_size(request)).page(1)
    #         self.request = request
    #         return list()
    def get_paginated_response(self, data):
        if self.get_next_link() and '?' in self.get_next_link():
            next_page = f'?{self.get_next_link().split("?")[-1]}'
        else:
            next_page = self.get_next_link()

        if self.get_previous_link() and '?' in self.get_previous_link():
            previous_page = f'?{self.get_previous_link().split("?")[-1]}'
        else:
            previous_page = self.get_previous_link()

        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', next_page),
            ('previous', previous_page),
            ('current', self.page.number),
            ('results', data)
        ]))