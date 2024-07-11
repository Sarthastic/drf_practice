
from .models import Person
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ss.serializers import peopleserializer
from .serializers import peopleserializer
from .serializers import loginserializer
from rest_framework.views import APIView
from rest_framework import viewsets
from ss.serializers import peopleserializer, loginserializer, registerserilizer
from rest_framework import status
from django.contrib.auth import authenticate   
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError




class LoginAPI(APIView):
    def get(self, request):
        return Response({
            'status': True,
            'message': 'This is the login endpoint. Use POST to log in.'
        }, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        print("Received data:", data)
        serializer = loginserializer(data=data)

        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)
            return Response({
                'status': False,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])

        if not user:
            return Response({
                'status': False,
                'message': 'Invalid credentials'
            }, status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'status': True,
            'message': 'User logged in',
            'token': str(token)
        }, status=status.HTTP_201_CREATED)
        

        




class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer =registerserilizer(data= data)
        
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
                    
            },status.HTTP_400_BAD_REQUEST )
        serializer.save()
        return Response({'status': True,'message': 'user created'}, status.HTTP_201_CREATED)
            
        
 

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        json_response = {
            'name': 'scalar',
            'courses': ['c++', 'python'],
            'method': 'GET'
        }
    elif request.method == 'POST':
        try:
            data = request.data
        except ParseError as e:
            return Response({'detail': 'JSON parse error: ' + str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        print(data)
        json_response = {
            'name': 'scalar',
            'courses': ['c++', 'python'],
            'method': 'POST',
            'received_data': data
        }
    
    return Response(json_response)  

@api_view(['POST'])
def login(request):
    data = request.data
    serializer =loginserializer(data =data)
    if serializer.is_valid():
        data = serializer.data
        print(data)
        return Response({"message": "success"})
    
    return Response(serializer.errors)    



class personAPI(APIView):
    
     
    def get(self, request):
        return Response({'message': 'this is get request'})
    
    def put(self,request):
        return Response({'message': 'this is put request'})
    
    def delete(self,request):
        return Response({'message': 'this is delete request'})
    
    def push(self,request):
        return Response({'message': 'this is push request'})
    
    def patch(self,request):
        return Response({'message': 'this is patch request'})
    
    

@api_view(['GET','PUT','PATCH','POST','DELETE'])           
def person(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color__isnull=False)
        serializer =peopleserializer(objs,many=True)  
        return Response(serializer.data)
    
    elif request.method == 'POST':
            
        data = request.data
        serializer = peopleserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    elif request.method == 'PUT':
            
        data = request.data
        serializer = peopleserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
            
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = peopleserializer(obj,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    else: 
        data = request.data
        obj =Person.objects.get(id=data['id'])
        obj.delete()
        return Response({"message": "person deleted"})        
    
from .serializers import peopleserializer 
class peopleviewset(viewsets.ModelViewSet):  
    serializer_class=peopleserializer
    queryset =Person.objects.all()
    
    
