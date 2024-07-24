from rest_framework import serializers
from .models import color, Person
from django.contrib.auth.models import User   


class registerserilizer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                
                raise serializers.ValidationError('user name is taken')
               

        if data['email']:
            
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email is taken')
            
        return data    
             
            
    def create(self, validated_data):       
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        return validated_data
         
        print(validated_data)







class loginserializer(serializers.Serializer):
    username = serializers.CharField()    
    password = serializers.CharField()
      
    




class colorserializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = color 
        fields = "__all__"


class peopleserializer(serializers.ModelSerializer):
    color=colorserializer()
    color_info  = serializers.SerializerMethodField()

    
    
    class Meta:
        model = Person 
        fields = "__all__"
        #depth = 1
    def get_color_info(self, obj):
        color_obj =color.objects.get(id = obj.color.id)
        return {'color_name': color_obj.color_name, 'hex_code':'#000'}        
     
    def validate(self, data):
        
        if data['age']<18:
            raise serializers.ValidationError("age should be greter than 18")
        return data
                
                