from django.db import models
import uuid

class BaseModel(models.Model):
    class Meta:
        abstract=True
    
    id = models.BigAutoField(primary_key=True, unique=True)
    public_id = models.BigIntegerField(editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
    @classmethod
    def get_new_public_id(cls):
        return uuid.uuid4().int >> 75

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = self.get_new_public_id()
        super(BaseModel, self).save(*args, **kwargs)