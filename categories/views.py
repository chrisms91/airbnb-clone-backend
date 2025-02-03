from rest_framework.response import Response
from rest_framework.exceptions import NotFoundexi
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# class Categories(APIView):

#     def get(self, request):
#         all_categories = Category.objects.all()
#         serializers = CategorySerializer(all_categories, many=True)
#         return Response(serializers.data)

#     def post(self, request, category_id):
#         serializers = CategorySerializer(data=request.data)
#         if serializers.is_valid():
#             new_category = serializers.save()
#             return Response(CategorySerializer(new_category).data)
#         else:
#             return Response(serializers.errors)


# class CategoryDetail(APIView):

#     def get_object(self, category_id):
#         try:
#             print(category_id)
#             category = Category.objects.get(pk=category_id)
#         except Category.DoesNotExist:
#             raise NotFound
#         return category

#     def get(self, request, category_id):
#         serializers = CategorySerializer(self.get_object(category_id))
#         print(serializers)
#         return Response(serializers.data)

#     def put(self, request, category_id):
#         serializer = CategorySerializer(
#             self.get_object(category_id),
#             data=request.data,
#             partial=True,
#         )
#         if serializer.is_valid():
#             updated_category = serializer.save()
#             return Response(CategorySerializer(updated_category).data)
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, category_id):
#         self.get_object(category_id).delete()
#         return Response(status=HTTP_204_NO_CONTENT)


# # Create your views here.
# @api_view(["GET", "POST"])
# def categories(request):
#     if request.method == "GET":
#         all_categories = Category.objects.all()
#         serializers = CategorySerializer(all_categories, many=True)
#         return Response(serializers.data)
#     elif request.method == "POST":
#         serializers = CategorySerializer(data=request.data)
#         if serializers.is_valid():
#             new_category = serializers.save()
#             return Response(CategorySerializer(new_category).data)
#         else:
#             return Response(serializers.errors)


# @api_view(["GET", "PUT", "DELETE"])
# def category(request, category_id):
#     try:
#         category = Category.objects.get(pk=category_id)
#     except Category.DoesNotExist:
#         raise NotFound

#     if request.method == "GET":
#         serializers = CategorySerializer(category)
#         return Response(serializers.data)
#     elif request.method == "PUT":
#         serializer = CategorySerializer(
#             category,
#             data=request.data,
#             partial=True,
#         )
#         if serializer.is_valid():
#             updated_category = serializer.save()
#             return Response(CategorySerializer(updated_category).data)
#         else:
#             return Response(serializer.errors)
#     elif request.method == "DELETE":
#         category.delete()
#         return Response(status=HTTP_204_NO_CONTENT)
