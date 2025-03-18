from django.db import models
from django.contrib.auth.models import User

class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads/')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_files')
    genre = models.CharField(max_length=255)

    def __str__(self):
        return f"File {self.file.name} uploaded by {self.from_user.username}"
