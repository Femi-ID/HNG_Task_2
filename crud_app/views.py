from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def view_all_persons(request):
    """Instructions on the URL format and a list of all persons."""
    api_urls = {
        'View All persons account': '/',
        'Create person': '/api',
        'Read, Update and Delete person detail': '/api/<user_id>',
    }
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)

    return Response({'serializer_persons': serializer.data, 'api_urls': api_urls},
                    status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def crud_person_profile_by_firstname(request):
    """Retrieve profile by First Name"""
    if request.method == "GET":
        # retrieve person through the name argument
        if request.GET.get("name"):
            name = request.GET.get("name")
            try:
                person = Person.objects.get(name=name)
            except Person.DoesNotExist:
                return Response({"error": "The name provided does not exist!"}, status=status.HTTP_404_NOT_FOUND)
            serializer = PersonSerializer(instance=person)
            return Response(serializer.data, status=status.HTTP_200_OK)

        persons = Person.objects.all()
        serializer = PersonSerializer(instance=persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    """Create new person profile."""
    if request.method == "POST":
        if request.data.get("name"):
            name = request.data.get("name")
            if not isinstance(name, str):
                return Response({"error": "Name must be a string format."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    """Update existing person profile through the name argument."""
    if request.method in ["PUT", "PATCH"]:
        # from the argument
        name_exists = request.GET.get('name')

        # from the submitted data
        name = request.data.get("name")
        bio = request.data.get("bio")

        if not isinstance(name, str):
            return Response({"error": "Name must be a string format."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # To check if the person profile exists
            person = Person.objects.get(name=name_exists)
        except Person.DoesNotExist:
            return Response({"error": "The name does not exist!"}, status=status.HTTP_404_NOT_FOUND)

        person.name = name
        person.bio = bio

        serializer = PersonSerializer(instance=person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    """Delete the profile by First Name."""
    if request.method == "DELETE":
        name = request.GET.get("name")
        try:
            person = Person.objects.get(name=name)
        except Person.DoesNotExist:
            return Response({"error": "The name does not exist!"}, status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response({"message": "Profile successfully deleted!"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'PATCH', 'POST', "DELETE"])
def read_edit_delete_person_profile_by_id(request, user_id):
    """Retrieve, Update or Delete a person profile."""
    try:
        person = Person.objects.get(id=user_id)
    except Person.DoesNotExist:
        return Response({"error": "Profile does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "DELETE":
        try:
            person = Person.objects.get(id=user_id)
        except Person.DoesNotExist:
            return Response({"error": "Profile does not exist!"}, status=status.HTTP_404_NOT_FOUND)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method in ["POST", "PUT", "PATCH"]:
        serializer = PersonSerializer(instance=person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# SAMPLE DATA:
# {
#     "first_name": "john",
#     "last_name": "doe",
#     "bio": "today is a good day!"
# }
# {
#     "name": "john",
#     "bio": "today is a good day!"
# }