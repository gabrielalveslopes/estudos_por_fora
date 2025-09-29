class Tarefa:
    def __init__(self,titulo,descricao,status ="Pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        

    def concluir_tarefa(self):
        self.status = "Concluída"

    def tarefa_pendente(self):
        self.status ="pendente"

    def editar_titulo(self, novo_titulo):
        self.titulo = novo_titulo
    
    def editar_descricao(self, nova_descricao):
        self.descricao = nova_descricao


class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        if tarefa  in self.tarefas:
            print("Erro ao adicionar a tarefa.")
        else:
            self.tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")

    def remover_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
        else:
            print("Tarefa não encontrada.")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            for idx, tarefa in enumerate(self.tarefas, start=1):
                print(f"{idx}. {tarefa.titulo} - {tarefa.descricao} [{tarefa.status}]")
    
    def buscar_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo.lower() == titulo.lower():
                return tarefa
        return None
    
    def buscar_tarefas_por_status(self, status):
        return [tarefa for tarefa in self.tarefas if tarefa.status.lower() == status.lower()]
    
    def concluir_tarefa(self):
        for tarefa in self.tarefas:
            if tarefa.status.lower() == "pendente":
                tarefa.concluir_tarefa()

    
