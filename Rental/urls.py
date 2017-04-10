from django.conf.urls import url, include



from Rental.views import RentListView, RentDetailView, RentDeleteView, RentListView1,RentListView6


urlpatterns = [
    url(r'^List/$', RentListView.as_view(), name='rental_list'),
    url(r'^List/(?P<pk>\d+)/$', RentDetailView.as_view(), name='rental_detail'),
    url(r'^List1/(?P<pk>\d+)/$', RentDeleteView.as_view(), name='rental_delete'),
    url(r'^List_1/$', RentListView1.as_view(), name='rental_list_1'),
    url(r'^List_6/$', RentListView6.as_view(), name='rental_list_6'),
        ]
