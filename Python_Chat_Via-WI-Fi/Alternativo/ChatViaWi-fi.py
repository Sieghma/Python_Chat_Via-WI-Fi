# Importar o Flet
import flet as ft

# Criando a função principal do sistema
def main(pagina):
    # Criar o título
    titulo = ft.Text("Chat Wi-fi")

    # Para chegar mensagem para todos
    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        # Atualizar a página
        pagina.update()

    # PubSub - Nome dado ao túnel pelo Flet
    # Dentro da "Pagina", quero criar um "Tubo de comunicação (PubSub)" e ele vai usar a função "enviar_mensagem_tunel"
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    titulo_janela = ft.Text("Bem-vindo ao Chat!")
    # Campo de texto que o usuário pode escrever: (TextField).
    # Para colocar a palavra no local para digitar (Label=).
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    # Função para enviar mensagem
    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        # Enviar a mensagem no chat:
        # Usuário: Mensagem

        # Enviar mensagem no túnel para todos
        pagina.pubsub.send_all(texto)  # Envia uma mensagem no túnel

        # Limpar o campo de mensagem
        texto_mensagem.value = ""
        pagina.update()

    # On_Submit = Sempre que der Enter, irá enviar a mensagem
    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    chat = ft.Column()
    # Colunas e linhas
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    # Função para entrar no chat
    def entrar_chat(evento):
        # Tirar o título da página
        pagina.remove(titulo)
        # Tirar o botão iniciar
        pagina.remove(botao_iniciar)
        # Fechar o pop-up/Janela
        janela.open = False
        # Criar o chat
        pagina.add(chat)
        # Adicionar a linha de mensagem / Ficando um do lado do outro
        pagina.add(linha_mensagem)
        # Escrever a mensagem: "Usuário entrou no chat" em laranja
        texto_entrou_chat = ft.Text(
            f"{campo_nome_usuario.value} entrou no chat",
            color="orange"
        )
        # Append - Adicionar item na lista do chat
        chat.controls.append(texto_entrou_chat)  # Adiciona a mensagem diretamente no chat
        pagina.update()  # Para as atualizações serem feitas na hora que executar as funções

    # Sempre que quiser dar uma função a algo (on_click).
    botao_entrar_chat = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        # Como geralmente podem ser adicionados vários botões em um código, o código criado para o botão será colocado em uma lista.
        actions=[botao_entrar_chat]
    )

    # Toda função que é usada dentro de um botão, tem que receber um evento como parâmetro.
    def abrir_popup(evento):
        # O que quero que apareça no dialog (Janela de diálogo) quando abrir o popup.
        pagina.dialog = janela
        # Como por padrão ele abre fechado então:
        janela.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # Colocar essa coisa na página.
    # Colocar o título na página.
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# Executar o sistema (Código)
# Caso queira abrir o arquivo em WEB = 'view=ft.WebBrowser'
ft.app(main, view=ft.WEB_BROWSER)