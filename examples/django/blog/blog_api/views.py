from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import (
    Post,
)
from .serializers import (
    PostSerializer,
)

class PostListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the post items for given requested user
        '''
        posts = Post.objects.filter(user_id = request.user.id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Post with given post data
        '''
        data = {
            'title': request.data.get('title'),
            'text': request.data.get('text'),
            'user_id': request.user.id,
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, post_id, user_id):
        '''
        Helper method to get the object with given post_id, and user_id
        '''
        try:
            return Post.objects.get(id=post_id, user_id = user_id)
        except Post.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, post_id, *args, **kwargs):
        '''
        Retrieves the Post with given post_id
        '''
        post_instance = self.get_object(post_id, request.user.id)
        if not post_instance:
            return Response(
                {"res": "Object with post id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PostSerializer(post_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, post_id, *args, **kwargs):
        '''
        Updates the post item with given post_id if exists
        '''
        post_instance = self.get_object(post_id, request.user.id)
        if not post_instance:
            return Response(
                {"res": "Object with post id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'text': request.data.get('text'),
            'user_id': request.user.id,
        }
        serializer = PostSerializer(instance = post_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, post_id, *args, **kwargs):
        '''
        Deletes the post item with given post_id if exists
        '''
        post_instance = self.get_object(post_id, request.user.id)
        if not post_instance:
            return Response(
                {"res": "Object with post id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        post_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )