from django.urls import path
from  myapp.views import Home, UserView, PBCView, PUIView, AddUserView, EditUserView, DeleteUserView, AddPBCView, EditPBCView, DeletePBCView, AddPUIView, EditPUIView, DeletePUIView, DetailPBCView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('users', UserView.as_view(), name='users'),
    path('pbc-cases', PBCView.as_view(), name='pbc'),
    path('pui-cases', PUIView.as_view(), name='pui'),
    path('add-user', AddUserView.as_view(), name='adduser'),
    path('edit-user/<int:pk>', EditUserView.as_view(), name='edituser'),
    path('delete-user/<int:pk>', DeleteUserView.as_view(), name='deleteuser'),
    path('add-pbc', AddPBCView.as_view(), name='addpbc'),
    path('details-pbc/<str:pk>', DetailPBCView.as_view(), name='detailpbc'),
    path('edit-pbc/<str:pk>', EditPBCView.as_view(), name='editpbc'),
    path('delete-pbc/<str:pk>', DeletePBCView.as_view(), name='deletepbc'),
    path('add-pui', AddPUIView.as_view(), name='addpui'),
    path('edit-pui/<str:pk>', EditPUIView.as_view(), name='editpui'),
    path('delete-pui/<str:pk>', DeletePUIView.as_view(), name='deletepui')
]
