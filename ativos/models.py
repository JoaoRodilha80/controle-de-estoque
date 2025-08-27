from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    # Adicionamos as opções de categoria aqui
    CATEGORIAS = [
        ('Perifericos', 'Periféricos'),
        ('Maquinas', 'Máquinas'),
        ('Monitores', 'Monitores'),
    ]
    
    nome = models.CharField(max_length=200)
    numero_serie = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=20, 
        choices=[('Disponivel', 'Disponível'), ('Em uso', 'Em uso')],
        default='Disponivel'
    )
    # Novo campo para a categoria
    categoria = models.CharField(
        max_length=20, 
        choices=CATEGORIAS,
        default='Maquinas'
    )
    funcionario = models.ForeignKey(
        Funcionario, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return f"{self.nome} - {self.numero_serie}"