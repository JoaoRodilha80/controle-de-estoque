from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('equipamentos-disponiveis/', views.equipamentos_disponiveis, name='equipamentos_disponiveis'),
    path('assinalar-equipamento/<int:equipamento_id>/', views.assinalar_equipamento, name='assinalar_equipamento'),
    path('equipamentos-em-uso/', views.equipamentos_em_uso, name='equipamentos_em_uso'),
    path('funcionarios/', views.funcionarios, name='funcionarios'),
    path('editar-funcionario/<int:funcionario_id>/', views.editar_funcionario, name='editar_funcionario'),
    path('equipamentos-em-uso/desassinalar/<int:equipamento_id>/', views.desassinalar_equipamento, name='desassinalar_equipamento'),
    
    # --- NOVAS URLS ---
    path('adicionar-equipamento/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('adicionar-funcionario/', views.adicionar_funcionario, name='adicionar_funcionario'),
]