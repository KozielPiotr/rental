from rest_framework import routers

from rental_app import api_views


router = routers.DefaultRouter()
router.register("friends", api_views.FriendViewset)
router.register("belongings", api_views.BelongingViewset)
router.register("borrowings", api_views.BorrowedViewset)
