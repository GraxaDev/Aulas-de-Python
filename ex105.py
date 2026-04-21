def notas(*n, sit=False):
    """-> A FUNÇÃO SERVE PARA ANALISAR NOTAS E SITUAÇÕES DE VÁRIOS ALUNOS
:param n: uma ou mais notas dos alunos
:param sit: valor opcional para mostrar ou não a situação do aluno
:return: dicionário com todas as informações sobre a situação da turma."""
    
    r = {}
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n) / len(n)
    if sit:
        if r["media"] >= 7:
            r["situação"] = "BOA"
        elif r["media"] >= 5:
            r["situação"] = "RAZOÁVEL"
        else:
            r["situação"] = "RUIM"
    return r

resp = notas(5.5, 4.5, 4.5, sit=True)
print(resp)
help(notas)