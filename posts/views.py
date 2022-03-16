# posts/views.py
from urllib import request
from rest_framework import generics, permissions , status
from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer , UserSerializer
from .permissions import IsAuthorOrReadOnly , IsAdminUser
from rest_framework.response import Response 
from django.core.mail import send_mail

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
   

    def post(self,request,format=None):
       serializer = PostSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            user = User.objects.get(id = request.data['author'] )
            mail=send_mail(
                    'confirmed',
                    'Here is the message.',
                        'fagrhesham@gmail.com',
                        [user.email],
                        fail_silently=False,
                        )

            data = {        "data" : serializer.data,
                            "success" : True
                            }
                            
            return Response(data,status=status.HTTP_201_CREATED)       

       else:
           return Response(status=status.HTTP_400_BAD_REQUEST)            


   

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer    
    permission_classes = (IsAuthorOrReadOnly,) 

class Users(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    permission_classes = (permissions.IsAdminUser,) 


