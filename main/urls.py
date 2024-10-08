from main.views import register, login_user, logout_user, edit_product, delete_product, product_page
from django.urls import path
from main.views import show_main, create_product,  show_json, show_xml, show_xml_by_id, show_json_by_id, add_product_entry_ajax



    

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name= "create_product"),
    path('json/', show_json, name = "show_json"),
    path('xml/', show_xml, name = "show_xml"),
    path('json/<str:id>/', show_json_by_id, name = "show_json_by_id"),
    path('xml/<str:id>/', show_xml_by_id, name = "show_xml_by_id"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('products/', product_page, name='products'),

    path('create-product-entry-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),


    ]