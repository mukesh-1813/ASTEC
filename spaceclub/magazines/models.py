from django.db import models

class Magazine(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='magazines/covers/')
    pdf_file = models.FileField(upload_to='magazines/pdfs/')
    publish_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']
