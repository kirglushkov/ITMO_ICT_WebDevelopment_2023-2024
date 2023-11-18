from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(req):
    person = {'name': 'name', 'age': 22}
    return Response(person)