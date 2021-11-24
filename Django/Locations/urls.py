from . import views
from django.urls import path
from django.urls import include
from .router import router


urlpatterns = [
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('index/',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('addmod/',views.addmod,name='addmod'),
    path('add/',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('updated/',views.updated,name='updated'),
    path('api/',include(router.urls))
]
