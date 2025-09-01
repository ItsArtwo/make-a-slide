# Make A Slide

Este projeto foi desenvolvido para agilizar a criação de slides ao final de sprints. Ele se conecta via API ao Trello para buscar informações dos participantes — nome, cards e listas (`Concluído`, `Andamento`, `Pendente`, `Correção`).
Cada usuário é vinculado aos seus respectivos cards, organizados por lista, e o programa gera automaticamente um slide para cada participante.


## 🧪 Como usar

Para iniciar o projeto, primeiramente crie uma chave API no Trello e insira no arquivo config.py, após iniciar o programa, os slides serão gerados automaticamente com base nos dados do Trello. Certifique-se de que os nomes das listas estejam corretamente configurados: `Concluído`, `Andamento`, `Pendente` e `Correção`.
Os slides serão salvos na pasta `output/`, um para cada participante.


## 🚀 Tecnologias

- Python
- PyPttx
- TrelloAPI


## 💡 Considerações finais

O projeto ainda está em desenvolvimento e futuramente terá compatibilidade com a plataforma Jira.
Em caso de erro, consulte o arquivo `MANUAL.md` para soluções comuns, para erros não listados, comente na aba "Discussions" do repositório.


## 📦 Instalação

````bash
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
pip install -r requirements.txt
python main.py