from django.contrib import admin  
from django.urls import path  
from projects import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('show', views.project),  
    path('index',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  