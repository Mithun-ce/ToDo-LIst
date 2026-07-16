from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TaskHistory(models.Model):
    ACTION_CHOICES = [
        ('added', 'Added'),
        ('completed', 'Marked Completed'),
        ('uncompleted', 'Marked Incomplete'),
        ('deleted', 'Deleted'),
    ]

    task_title = models.CharField(max_length=200)   # store title as text, since the task might get deleted
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']   # newest first

    def __str__(self):
        return f"{self.task_title} — {self.action} at {self.timestamp}"