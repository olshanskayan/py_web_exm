from django.shortcuts import render
from django.db.models import Avg, Q
from rest_framework.response import Response
from .models import Note
from rest_framework.views import APIView
from .serializers import NotesSerializer

class NotesView(APIView):
    """ Статьи для блога """

    def get(self, request):
        """ Получить статьи для блога """
        # notes = Note.objects.filter(public=True).order_by('-date_add', 'title')
        # notes = Note.objects.all()

        # Это НЕ оптимизированный запрос
        notes = Note.objects.filter(Q(public=True) | Q(author=request.user)).order_by('-date_add', 'title')

        # `select_related` - это оптимизация запроса (join). Отношение Один к Одному
        # https://django.fun/docs/django/ru/3.1/ref/models/querysets/#select-related
        # notes = Note.objects.filter(public=True).order_by('-date_add', 'title').select_related('author')
        # notes = notes.only('id', 'title', 'message', 'date_add', 'author__username')

        # Рассчитать средний рейтинг
        # notes = notes.annotate(average_rating=Avg('comments__rating'))

        serializer = NotesSerializer(notes, many=True)

        return Response(serializer.data)
