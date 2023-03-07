from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('fund_wallet/', views.fund, name='fund'),
    path('resolution_center/', views.center, name='center'),
    path('buy_data/', views.buydata, name='buydata'),
    path('load_plans/', views.load_plans, name='load_plans'),
    path('load_cable_plans/', views.load_cable_plans, name='load_cable_plans'),
    path('load_edu_quantity/', views.load_edu_quantity, name='load_edu_quantity'),
    path('buy_success/', views.response, name='response'),
    path('pay_bills/', views.bill, name='bill'),
    path('buy_airtime/', views.buyairtime, name='buyairtime'),
    path('get_success/', views.success, name='success'),
    path('bank_details/', views.bank, name='bank'),
    path('add_success/', views.banker, name='banker'),
    path('delete_detail/<int:_id>',views.delete,name='delete'),
    path('default_detail/<int:_id>',views.default,name='default'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('withdraw_update/', views.withdrawer, name='withdrawer'),
    path('faq/', views.faq, name='faq'),
    path('query_data/', views.data, name ='querydata'),
    path('queried_data/<int:_id>', views.querydata, name ='querydate'),
    path('query_airtime/', views.airtime, name ='queryairtime'),
    path('queried_airtime/<int:_id>', views.queryairtime, name ='queryair'),
    path('query_withdrawal/', views.withe, name ='querywithdrawal'),
    path('queried_withdrawal/<int:_id>', views.querywithe, name ='querywith'),
    path('electricity_bill/', views.elect, name='elect'),
    path('purchase/', views.purchase, name='purchase'),
    path('education_bill/', views.edu, name='edu'),
    path('education_success/', views.sock, name='sock'),
    path('cable_bill/', views.cable, name='cable'),
    path('cable_success/', views.cab, name='cab'),
    path('query_bill/', views.querybill, name ='querybill'),
    path('query_bill1/<int:_id>', views.querybill1, name ='querybill1'),
    path('query_bill2/<int:_id>', views.querybill2, name ='querybill2'),
    path('query_bill4/<int:_id>', views.querybill4, name ='querybill4'),
]