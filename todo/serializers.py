from rest_framework import serializers  # Import serializers module from Django REST Framework
from .models import Todo  # Import Todo model from current directory

class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer class for Todo model.
    Converts Todo model instances to JSON and vice versa.
    """
    class Meta:
        model = Todo  # Specify the model to serialize (Todo model)
        fields = ['id', 'task', 'description', 'completed', 'created_at', 'due_at']
        # List of fields from Todo model to include in serialization
