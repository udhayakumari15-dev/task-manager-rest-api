from rest_framework omport serializers
from .models import Task
class TaskSerializer(serializers.ModelsSerializer):
    class Meta:
        model=Task
        fields=['id','title','is_done','create_at']