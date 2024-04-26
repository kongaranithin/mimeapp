from .import views
from django.urls import path
app_name='mimeapp'
urlpatterns = [
    path('html', views.htmlview.as_view(), name='htmlview'),
    path('excel', views.excelview.as_view(), name='excelview'),
    path('xml', views.xmlview.as_view(), name='xmlview'),
    path('pdf', views.pdfview.as_view(), name='pdfview'),
    path('json', views.jsonview.as_view(), name='jsonview'),
    path('pptx', views.pptxview.as_view(), name='pptxview'),

]