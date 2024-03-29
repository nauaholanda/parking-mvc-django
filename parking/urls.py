from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('parking', views.goingIn, name="entrada"),
	path('pay', views.payment, name="pagamento"),
	path('<id>/pay', views.paying),
	path('out', views.departure, name="saida"),
	path('<id>/out', views.goingOut),
	path('searchHistory', views.searchHistory, name="pesquisa"),
	path('parking/<plate>', views.searching),
]