from django.urls import path,include
from testapp import views
urlpatterns = [
    path('show_view/', views.show_view,name='show_view'),
    path('insert_view/', views.insert_view,name='insert_view'),
    path('update_view/<int:id>', views.update_view,name='update_view'),
    path('delete_view/<int:id>', views.delete_view,name='delete_view')

]