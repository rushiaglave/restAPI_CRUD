from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import employees
from .serializers import employeesSerializer
from rest_framework import status

# Create your views here.
# creating the GET request here to extract the data
@api_view(['GET'])
def tasklist(request):
        employees1 = employees.objects.all()
        Serializer =employeesSerializer(employees1, many=True)
        return Response(Serializer.data)

@api_view(['GET'])
def tasklistid(request, pk):
    try:
        employee = employees.objects.get(emp_id=pk)
    except employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = employeesSerializer(employee)
    return Response(serializer.data)

#  creating the POST request here to update the data   
@api_view(['POST'])
def taskcreate(request):
        Serializer =employeesSerializer(data=request.data)

        if Serializer.is_valid():
                Serializer.save()

        return Response(Serializer.data)

# creating the POST request here by id to update the particular id in the database
@api_view(['POST'])
def taskupdate(request, pk):
        employees1 = employees.objects.get(id=pk)
        Serializer =employeesSerializer(instance=employees1, data=request.data)

        if Serializer.is_valid():
                Serializer.save()
                
        return Response(Serializer.data)

# creating the DELETE request here by id to delete the particular data in the database
@api_view(['DELETE'])
def taskdelete(request, pk):
        employees1 = employees.objects.get(id=pk)
        employees1.delete()
       
        return Response('item deleted successefuly')