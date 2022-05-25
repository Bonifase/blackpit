from rest_framework import pagination
from rest_framework.response import Response


class Pagination(pagination.PageNumberPagination):
    page_size = 100
    page_query_param = 'page'
    page_size_query_param = 'per_page'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'all_pages': self.page.paginator.num_pages,
            'page': self.page.number,
            'results': data
        })