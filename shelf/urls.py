from django.conf.urls import url, include

from shelf.views import AuthorListView, AuthorDetailView, BookListView, BookDetailView


urlpatterns = [
    url(r'^authors/$',AuthorListView.as_view(),name='author_list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(),name='author_detail'),
    url(r'^books/$',BookListView.as_view(),name='book_list'),
    url(r'^books/(?P<pk>\d+)/$', BookDetailView.as_view(),name='book_detail'),
]