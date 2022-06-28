from django.contrib import admin
# from django.urls import path, include
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls'))
    path('info/', views.InfoList.as_view()),
    path('info/<int:pk>/', views.InfoRetrieve.as_view()),
    path('infoAdd/', views.InfoCreate.as_view()),
    path('infoUpdate/<int:pk>/', views.InfoUpdate.as_view()),
    path('infoDelete/<int:pk>/', views.InfoDestroy.as_view()),

]
