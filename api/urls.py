from django.urls import path, include
from ss.views import index, person, login, personAPI, peopleviewset, RegisterAPI, LoginAPI
from rest_framework.routers import DefaultRouter



router =DefaultRouter()
router.register(r'people',peopleviewset,basename='people')
urlpatterns= router.urls


urlpatterns = [ 
    path('', include(router.urls)),
    path('index/', index),
    path('login/',LoginAPI.as_view()),
    path('register/',RegisterAPI.as_view()),
    path('person/', person),
    path('login/', login),
    path('persons/', personAPI.as_view()),
    
    
     
]