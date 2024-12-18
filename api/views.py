from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialiser import NoteSerializer
from .models import Note


# Create your views here.
@api_view(["GET"]) # Write all methods you want to use
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Return array of notes'

        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Return single note'

        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Create new note'

        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Update existing note'

        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete note'

        },


    ]
    return Response(routes)


@api_view(["Get"])
def getNotes(request):
    notes = Note.objects.all()
    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)

@api_view(["Get"])
def getNote(request,pk):
    notes = Note.objects.get(id=pk)
    serializer=NoteSerializer(notes,many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createNote(request):
    data=request.data
    note=Note.objects.create(
        body=data["body"]
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def updateNote(request,pk):

    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def deleteNote(request,pk):

    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Data Deleted Successfully")