from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
data=""" <table>
<tr><th>empolyee id </th><th>ename</th><th>esal</th></tr>
<tr><td>1001</td><td>siva</td><td>30000</td></tr>
<tr><td>1002</td><td>nithin</td><td>35000</td></tr>
<tr><td>1003</td><td>sri</td><td>25000</td></tr>
<tr><td>1004</td><td>chan</td><td>32000</td></tr>
</table>"""
class htmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/html")
class excelview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/vnd.ms-excel")
class  xmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/xml")
class pdfview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/pdf")
class jsonview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/json")
class pptxview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/vnd.ms-powerpoint")
# Create your views here.
