Esse arquivo tem o propósito de ensinar a utilizar a automação e resolver possíveis erros.

Sumário:
    1. Processo da automação
    2. Chaves API, Token de acesso, ID's de quadro e ID's de listas
    3. Configurações necessárias
    4. Resolução de erros

1. Processo da automação
    O projeto é organizado em um diretório principal com o arquivo main.py (ponto de entrada) e uma pasta trello_report/ que contém os módulos principais.
    Ele utiliza bibliotecas como python-trello para integração com a API do Trello e python-pptx para manipulação de apresentações PowerPoint.
    O software ainda está em desenvolvimento e planeja adicionar suporte à plataforma Jira no futuro.


    **Configuração (trello_report/config.py):**
        Este arquivo contém as configurações essenciais para o funcionamento: 
        *API_KEY e TOKEN:*Chaves de autenticação da API do Trello, que devem ser obtidas no painel do Trello e inseridas manualmente. 
        *BOARD_ID* ID do quadro (board) do Trello do qual os dados serão extraídos. 
        *LIST_IDS* Um dicionário com os IDs das listas específicas do Trello, mapeadas para categorias "pendente", "andamento", "concluido" e "correcao". Esses IDs devem corresponder exatamente às listas no quadro para que a coleta de dados funcione 
    

    **ATENÇÃO!!!**
        Sem essas configurações preenchidas, o software não consegue se conectar ao Trello devidamente!!!.


    **Fluxo Principal (main.py)**
        O arquivo main.py é o ponto de entrada do programa. Ele executa os seguintes passos sequenciais: 

        Inicialização: Importa funções dos módulos em trello_report/. 
        Criação do Cliente Trello: Chama get_client() para estabelecer uma conexão com a API do Trello usando as chaves de configuração. 
        Obtenção do Quadro e Listas: Usa get_board_and_lists() para buscar o quadro específico e suas listas mapeadas. 
        Coleta de Dados dos Membros: Executa coletar_dados_membros() para extrair informações sobre os membros do quadro, seus cards categorizados por lista e totais gerais. 
        Geração da Apresentação: Chama gerar_apresentacao() para criar os slides baseados nos dados coletados. 
        Finalização: Imprime uma mensagem de sucesso com o tempo de execução. 
        O tempo total de execução é medido e exibido no console. 


    **Cliente Trello (trello_report/trello_client.py)**
        Este módulo gerencia a interação com a API do Trello: 

        get_client(): Cria e retorna um objeto TrelloClient autenticado com a API_KEY e TOKEN. 
        get_board_and_lists(client, board_id, list_ids): Busca o quadro pelo ID e recupera as listas específicas como objetos, retornando o quadro e um dicionário de listas. 
        Essas funções garantem que o software tenha acesso aos dados do Trello de forma segura e estruturada. 


    **Coleta de Dados (trello_report/report_builder.py)**
        Este módulo processa os dados dos membros e cards: 

        coletar_dados_membros(client, board, list_ids): 
        Obtém todos os membros do quadro. 
        Para cada membro, coleta os cards atribuídos a ele em cada lista (usando _get_cards()). 
        Organiza os dados em um dicionário por membro, incluindo listas de cards por categoria e totais individuais. 
        Calcula totais globais por categoria e total geral. 
        Retorna a lista de membros, o dicionário de dados e os totais. 
        _get_cards(client, membro_id, list_id): Uma função auxiliar que filtra os cards de uma lista específica atribuídos a um membro, verificando se o ID do membro está na lista de membros do card. 
        Essa etapa é crucial para categorizar e quantificar o trabalho de cada participante. 


    **Geração de Slides (trello_report/slide_generator.py)**
        Este módulo cria a apresentação PowerPoint: 

        gerar_apresentacao(membros, dados_membros, totais): 
        Carrega um template de apresentação PowerPoint existente (tutorial_presentation 1.pptx). 
        Atualiza o slide de visão geral (overview) substituindo placeholders como "List tittle 1" pelos nomes das listas e "Card 1 quantity" pelos totais de cards. 
        Para cada membro, copia um slide de template, substitui "User Name" pelo nome completo do membro e preenche placeholders de cards (como "Card list 1", "Card 1 name") com as categorias e nomes dos cards associados. 
        Remove o slide de template original e limpa placeholders não utilizados, textos vazios e elementos desnecessários (como "Concluído0"). 
        Salva a apresentação gerada como tutorial_presentation.pptx. 
        Funções auxiliares incluem copiar_slide() para duplicar slides, excluir_slide() para remover slides e limpar_placeholders_e_textos_vazios() para limpeza. 

    **Arquivos Adicionais**
        tutorial_presentation 1.pptx: O template de PowerPoint usado como base para gerar as apresentações. 
        tutorial_presentation.pptx: Arquivo gerado no final do programa 

    **Como Executar**
        Instale as dependências com *pip install -r requirements.txt.* 
        Configure *config.py* com as chaves e IDs do Trello. 
        Execute *python main.py.* 
        Os slides serão gerados automaticamente e salvos como *tutorial_presentation.pptx.* 

2. Chaves API, Token de acesso, ID's de quadro e ID's de listas
    a. Como obter a API Key e o Token de acesso do Trello 
        Acesse o site oficial da API do Trello: Vá para developer.atlassian.com/cloud/trello. 

        Gerar sua API Key: 
            Faça login com sua conta Trello. 
            Acesse https://trello.com/app-key para visualizar sua chave de API. 
            Gerar seu Token de acesso: 
            Na mesma página, clique no link para gerar o token. 
            Autorize o acesso à sua conta. 
            Com a API Key e o Token, você poderá fazer chamadas autenticadas à API REST do Trello. 

    b. Como obter o ID de um quadro (Board ID)
        Abra o quadro desejado no navegador. 

        Verifique a URL. Ela será algo como: https://trello.com/b/CwAVCgfQz/nome-do-quadro 
        O trecho CwAVCgfQz é o Board ID. 

    c. Como obter o ID de uma lista (List ID) 

        Atualmente esse processo precisa ser feito ou de forma manual ou pelo arquivo board_id.py(Em desenvolvimento). Futuramente o processo será atualizado para funcionar automáticamente 

        Use a API para listar as listas de um quadro: Acesse a seguinte URL no navegador (substitua BOARD_ID pela ID do quadro): https://api.trello.com/1/boards/BOARD_ID/lists?key=YOUR_API_KEY&token=YOUR_TOKEN 

        O retorno será um JSON com todas as listas do quadro. 

        Localize o campo "id" antes do "name" da lista desejada. 

        Exemplo de resposta: 

        [
          {
            "id": "5f1a2b3c4d5e6f7g8h9i0j",
            "name": "Tarefas Pendentes",
            ...
          }
        ]


3. Configurações necessárias

    a. Organização dos ID's.
        No arquivo config.py (caminho: trello_report/config.py) troque os textos indicados pelos ID's que recolheu durante as instruções anteriores.

    b. Organização dos slides.
        Para adaptar um slide, é preciso que ele siga um padrão onde o overview é o terceiro segundo slide e os de usuários começam a partir do terceiro.
        As caixas de texto precisam seguir o padrão de nomes mostrado nos slides:

        Overview:
            Titulo da lista: List tittle
            Quantidade de cards: Card quantity

        Card dos usuários
            Nome do usuário: User Name
            Nome das listas: Card list
            Nome da atividade: Car name
        
4. Resolução de erros
