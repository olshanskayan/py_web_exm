from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class NotesSerializer(serializers.ModelSerializer):
    """ Статьи для блога """

    # Меняем вывод, вместо `ID` пользователя будет `Имя`
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'message', 'date_add', 'author', 'condition', 'mark', ]



