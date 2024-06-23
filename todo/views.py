from rest_framework import viewsets  # Import viewsets module from Django REST Framework
from .serializers import TodoSerializer  # Import TodoSerializer from current directory
from .models import Todo  # Import Todo model from current directory

class TodoViewSet(viewsets.ModelViewSet):
    """
    ViewSet class for Todo model.
    Provides CRUD operations (Create, Retrieve, Update, Delete) for Todo objects.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    # Queryset of Todo objects, ordered by creation timestamp in descending order
    serializer_class = TodoSerializer
    # Serializer class to use for serializing and deserializing Todo objects
