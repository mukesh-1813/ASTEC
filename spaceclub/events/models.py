from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_image = models.ImageField(upload_to='events/images/')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    EVENT_STATUS_CHOICES = [
        ('active', 'Active'),
        ('closed', 'Closed'),
    ]
    event_status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES, default='active')
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, default=200.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_event = Event.objects.get(pk=self.pk)
            # If the event transitions to closed, vanish all registrations
            if old_event.event_status != 'closed' and self.event_status == 'closed':
                self.registrations.all().delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date', '-time']

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    college = models.CharField(max_length=255, verbose_name="College / Organization")
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    ]
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True, null=True, help_text="UPI Transaction ID")
    payment_date = models.DateTimeField(blank=True, null=True)
    
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"

    class Meta:
        ordering = ['-registered_at']
