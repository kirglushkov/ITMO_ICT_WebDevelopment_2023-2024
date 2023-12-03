from .models import Warrior, Skill, Profession
from .serializers import WarriorSerializer, ProfessionSerializer, SkillSerializer
from rest_framework import generics


class WarriorList(generics.ListCreateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class ProfessionCreateView(generics.CreateAPIView):
   serializer_class = ProfessionSerializer
   queryset = Profession.objects.all()


class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillCreateView(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer