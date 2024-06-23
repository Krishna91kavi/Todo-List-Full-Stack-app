from django.db import models  # Import Django's model library
from django.utils import timezone  # Import Django's timezone utilities

class Todo(models.Model):
    task = models.CharField(max_length=200)  # CharField for task with max length of 200 characters
    description = models.TextField(max_length=1000)  # TextField for description with max length of 1000 characters
    completed = models.BooleanField(default=False)  # BooleanField for task completion status, default is False
    created_at = models.DateTimeField(default=timezone.now)  # DateTimeField for creation timestamp, default is current time
    due_at = models.DateTimeField()  # DateTimeField for due date of the task

    def __str__(self):
        return self.task  # String representation of the model instance, returns the task title
