from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipamento, Funcionario
from django.contrib import messages

def home_view(request):
    return render(request, 'home.html')

def equipamentos_disponiveis(request):
    equipamentos_disponiveis = Equipamento.objects.filter(status='Disponivel')
    funcionarios = Funcionario.objects.all()
    
    # Criamos um dicionário para agrupar os equipamentos por categoria
    categorias = {
        'Perifericos': equipamentos_disponiveis.filter(categoria='Perifericos'),
        'Maquinas': equipamentos_disponiveis.filter(categoria='Maquinas'),
        'Monitores': equipamentos_disponiveis.filter(categoria='Monitores'),
    }
    
    context = {
        'categorias': categorias, # Passamos o dicionário para o template
        'funcionarios': funcionarios,
    }
    return render(request, 'ativos/equipamentos_disponiveis.html', context)

def assinalar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, id=equipamento_id)
    if request.method == 'POST':
        funcionario_id = request.POST.get('funcionario_id')
        funcionario = get_object_or_404(Funcionario, id=funcionario_id)
        
        equipamento.funcionario = funcionario
        equipamento.status = 'Em uso'
        equipamento.save()
        
        messages.success(request, f'Equipamento {equipamento.nome} assinalado para {funcionario.nome}!')
        
    return redirect('equipamentos_disponiveis')

def equipamentos_em_uso(request):
    equipamentos_em_uso = Equipamento.objects.filter(status='Em uso', funcionario__isnull=False)
    
    # Fazemos a mesma lógica para os equipamentos em uso
    categorias = {
        'Perifericos': equipamentos_em_uso.filter(categoria='Perifericos'),
        'Maquinas': equipamentos_em_uso.filter(categoria='Maquinas'),
        'Monitores': equipamentos_em_uso.filter(categoria='Monitores'),
    }
    
    context = {
        'categorias': categorias, # Passamos o dicionário para o template
    }
    return render(request, 'ativos/equipamentos_em_uso.html', context)

def funcionarios(request):
    funcionarios_lista = Funcionario.objects.all()
    context = {
        'funcionarios': funcionarios_lista,
    }
    return render(request, 'ativos/funcionarios.html', context)

def editar_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    if request.method == 'POST':
        funcionario.nome = request.POST.get('nome')
        funcionario.email = request.POST.get('email')
        funcionario.save()
        return redirect('funcionarios')
    context = {
        'funcionario': funcionario,
    }
    return render(request, 'ativos/editar_funcionario.html', context)

def desassinalar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, id=equipamento_id)
    equipamento.funcionario = None
    equipamento.status = 'Disponivel'
    equipamento.save()
    messages.success(request, f'Equipamento {equipamento.nome} desassinalado com sucesso!')
    return redirect('equipamentos_em_uso')

# Adicionamos o novo campo 'categoria' na função de adição
def adicionar_equipamento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        numero_serie = request.POST.get('numero_serie')
        categoria = request.POST.get('categoria') # Novo campo
        Equipamento.objects.create(nome=nome, numero_serie=numero_serie, categoria=categoria, status='Disponivel')
        messages.success(request, f'Equipamento {nome} adicionado com sucesso!')
    return redirect('equipamentos_disponiveis')

def adicionar_funcionario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        Funcionario.objects.create(nome=nome, email=email)
        messages.success(request, f'Funcionário {nome} adicionado com sucesso!')
    return redirect('funcionarios')