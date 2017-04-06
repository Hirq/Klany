from django.conf.urls import url, include



from Rental.views import RentListView, RentDetailView, RentDeleteView


urlpatterns = [
    url(r'^List/$', RentListView.as_view(), name='rental_list'),
    url(r'^List/(?P<pk>\d+)/$', RentDetailView.as_view(), name='rental_detail'),
    url(r'^List1/(?P<pk>\d+)/$', RentDeleteView.as_view(), name='rental_delete'),
        ]
