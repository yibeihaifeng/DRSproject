from . import views

from rest_framework.routers import DefaultRouter


urlpatterns=[



]

router = DefaultRouter()  # 可以处理视图的路由器
router.register(r'books',views.BookInfoViewSet)  # 向路由器注册视图集

urlpatterns += router.urls  # 将路由器中的所有路由信息追到django的路由列表中

