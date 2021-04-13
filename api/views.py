import datetime
from api.serializers import LoanSerializer, BookSerializer, ProfileSerializer
from accounts.models import Profile, LibraryUser
from books.models import Loan, Book
from rest_framework import generics, status, permissions
from rest_framework.response import Response


class ProfilesView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class LoansView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class BooksView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserLoansView(generics.ListCreateAPIView):
    serializer_class = LoanSerializer

    def get(self, request, userid, format=None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(
            queryset, many=True, context={"request": request}
        )
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = Loan.objects.all()
        if "userid" in self.kwargs and self.kwargs["userid"]:
            queryset = queryset.filter(user__id=self.kwargs["userid"])
        else:
            queryset = Loan.objects.none()
        return queryset

    def post(self, request, *args, **kwargs):

        if "userid" in self.kwargs and self.kwargs["userid"]:
            user = self.kwargs["userid"]
            user_profile = Profile.objects.get(user__id=user)
            # book_instance = Book.objects.get(id=request.data['book'])
            data = {
                "user": user,
                "book": request.data['book'],
                }
            serializer = LoanSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get(self, request, userid, format=None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(
            queryset, many=True, context={"request": request}
        )
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = Profile.objects.all()
        if "userid" in self.kwargs and self.kwargs["userid"]:
            queryset = queryset.filter(user__id=self.kwargs["userid"])
        else:
            queryset = Profile.objects.none()
        return queryset