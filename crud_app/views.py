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
        first_name = request.GET.get("first_name")
        try:
            person = Person.objects.get(first_name=first_name)
        except Person.DoesNotExist:
            return Response({"error": "The first name provided does not exist!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(instance=person)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """Create new person profile."""
    if request.method == "POST":
        if request.GET.get("first_name"):
            first_name = request.GET.get("first_name")
            if not isinstance(first_name, str):
                return Response({"error": "First name must be a string format."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    """Update existing person profile through the first_name argument."""
    if request.method in ["PUT", "PATCH"]:
        # from the argument
        name_exists = request.GET.get('first_name')

        # from the submitted data
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        bio = request.data.get("bio")

        if not isinstance(first_name, str):
            return Response({"error": "First name must be a string format."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # To check if the person profile exists
            person = Person.objects.get(first_name=name_exists)
        except Person.DoesNotExist:
            return Response({"error": "The name does not exist!"}, status=status.HTTP_404_NOT_FOUND)

        person.first_name = first_name
        person.last_name = last_name
        person.bio = bio

        serializer = PersonSerializer(instance=person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    """Delete the profile by First Name."""
    if request.method == "DELETE":
        first_name = request.GET.get("first_name")
        try:
            person = Person.objects.get(first_name=first_name)
        except Person.DoesNotExist:
            return Response({"error": "The name does not exist!"}, status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'PATCH', 'POST'])
def read_edit_person_profile_by_id(request, user_id):
    """Retrieve, Update or Delete a person profile."""
    try:
        person = Person.objects.get(id=user_id)
    except Person.DoesNotExist:
        return Response({"error": "Profile does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # if request.GET.get('first_name'):
        #     first_name = request.GET.get('first_name')
        #     try:
        #         queryset = Person.objects.get(first_name=first_name)
        #     except Person.DoesNotExist:
        #         return Response({"error": "This name does not exist!"}, status=status.HTTP_404_NOT_FOUND)
        #
        # if request.GET.get('last_name'):
        #     last_name = request.GET.get('last_name')
        #     try:
        #         queryset = Person.objects.get(first_name=last_name)
        #     except Person.DoesNotExist:
        #         return Response({"error": "This name does not exist!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method in ["POST", "PUT", "PATCH"]:
        serializer = PersonSerializer(instance=person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_person_profile(request, user_id):
    try:
        person = Person.objects.get(id=user_id)
    except Person.DoesNotExist:
        return Response({"error": "Profile does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# SAMPLE DATA:

# {
#     "first_name": "john",
#     "last_name": "doe",
#     "bio": "today is a good day!"
# }

