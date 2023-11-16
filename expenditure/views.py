from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from categories.models import Category

from expenditure.models import Expenditure
from expenditure.serializers import ExpenditureCreateSerializer, ExpenditureDetailSerializer, ExpenditureListSerializer, ExpenditureSerializer


# api/v1/expenditure/
class ExpenditureAPIView(APIView):
    """
    지출 내역을 생성하고, 조회하는 기능 관련 API
    """
    permission_classes = [IsAuthenticated]


    @swagger_auto_schema(
            request_body=None,
            responses={
                status.HTTP_200_OK : ExpenditureListSerializer,
            }
    )
    def get(self, request):
        user = request.user

        user_expenditure = Expenditure.objects.filter(user=user)
        if user_expenditure.exists():
            serializer = ExpenditureListSerializer(user_expenditure, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"message" : "지출 내역이 존재하지 않습니다. 지출을 등록해주세요."}, status=status.HTTP_404_NOT_FOUND)
    

    @swagger_auto_schema(
            request_body=ExpenditureCreateSerializer,
            responses={
                status.HTTP_201_CREATED : ExpenditureDetailSerializer
            }
    )
    def post(self, request):
        """
        money : integer
        comment : text
        category : char
        expense_date : date
        is_sum : boolean
        """
        user = request.user
        input_category = request.data.get('category')

        expense_data = request.data
        required_field = (not expense_data['money']) or (not expense_data['category']) or (not expense_data['expense_date'])
        
        if required_field:
            raise ValueError("지출 금액, 지출일, 지출 카테고리는 필수 입력사항입니다. 다시 입력해주세요.")
        
        try:
            category = Category.objects.get(name=input_category)
            expense_data['category'] = category.id
        except Exception as e:
            raise ValueError("해당 카테고리는 사용할 수 없습니다. 다시 입력해주세요.")
        
        expense_data['user'] = user.id

        serializer = ExpenditureSerializer(data=expense_data)
        if serializer.is_valid():
            save_data = serializer.save()
            return Response(ExpenditureDetailSerializer(save_data).data, status=status.HTTP_201_CREATED)
        
        return Response({"message" : "지출 생성에 실패하였습니다. 다시 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)


# api/v1/expenditure/<int:expenditure_id>/
class ExpenditureDetailAPIView(APIView):
    """
    지출 내역을 상세 조회하고, 수정, 삭제하는 기능 관련 API
    """
    pass