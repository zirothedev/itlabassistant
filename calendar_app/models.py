from django.db import models
from django.urls import reverse

class CalendarEntry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    entry_type = models.CharField(max_length=10, choices=[('TODO', 'Todo'), ('NOTE', 'Note')])
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'created_at']
        verbose_name_plural = 'Calendar Entries'

    def __str__(self):
        return f"{self.title} ({self.date})"
    
    def get_absolute_url(self):
        return reverse('calendar_app:entry_detail', args=[str(self.id)])


