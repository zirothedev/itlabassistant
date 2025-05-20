from django.urls import path
from . import views

app_name = 'calendar_app'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('entry/new/', views.EntryCreate.as_view(), name='entry_new'),
    path('entry/<int:pk>/', views.EntryDetail.as_view(), name='entry_detail'),
    path('entry/<int:pk>/edit/', views.EntryUpdate.as_view(), name='entry_update'),
    path('entry/<int:pk>/delete/', views.EntryDelete.as_view(), name='entry_delete'),
    path('entry/<int:pk>/toggle/', views.toggle_completed, name='toggle_completed'),
]