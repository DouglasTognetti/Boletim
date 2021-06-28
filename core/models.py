from django.db import models

# Create your models here.


class Turma(models.Model):
    serie = models.CharField(max_length=50)
    letra = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.serie} - {self.letra}'

    class Meta:
        verbose_name_plural = 'Turmas'


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    dataNascimento = models.DateField(auto_now_add=None)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_alunos')
    idTurma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.idTurma}'

    class Meta:
        verbose_name_plural = 'Alunos'


class Materia(models.Model):
    nome = models.CharField(max_length=100)
    numeroTotalAulas = models.IntegerField()

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name_plural = 'Matérias'


class Resultado(models.Model):
    idAluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    idMateria = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nota1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    faltas1 = models.IntegerField(blank=True, null=True)
    nota2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    faltas2 = models.IntegerField(blank=True, null=True)
    nota3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    faltas3 = models.IntegerField(blank=True, null=True)
    nota4 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    faltas4 = models.IntegerField(blank=True, null=True)
    notaFinal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    aprovado = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f'{self.idAluno} - {self.idMateria}'

    class Meta:
        verbose_name_plural = 'Resultados'

    def notaFinal(self):
       try:
         self.notaFinal = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
         return self.notaFinal
       except:
         self.notaFinal = 0
         return self.notaFinal

    def aprovado(self):
        somaFaltas = self.faltas1 + self.faltas2 + self.faltas3 + self.faltas4
        if self.notaFinal >= 6 and somaFaltas <= 20:
            self.aprovado = True
            return self.aprovado
        self.aprovado = False
        return self.aprovado
