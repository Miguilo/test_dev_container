# Projeto com Backend Python e Frontend Streamlit

Este repositório contém uma aplicação que utiliza:

- **Backend Python**: API desenvolvida em Python, exposta na porta 8000
- **Frontend Streamlit**: Interface de usuário interativa, acessível na porta 8501
- **Dev Container**: Ambiente de desenvolvimento isolado e reproduzível

## Estrutura do Projeto

```
.
├── backend/            # Serviço de API Python
│   └── Dockerfile      # Configuração do container do backend
├── streamlit/          # Interface de usuário Streamlit
│   └── Dockerfile      # Configuração do container do frontend
└── .devcontainer/      # Configuração do ambiente de desenvolvimento
    ├── devcontainer.json
    ├── docker-compose.yml
    └── Dockerfile
```

## Como Executar

1. Abra o projeto no VS Code com a extensão Dev Containers instalada
2. Selecione "Reopen in Container" quando solicitado
3. Os serviços backend (porta 8000) e Streamlit (porta 8501) serão iniciados automaticamente
4. Acesse a interface Streamlit em `http://localhost:8501`

## Ambiente de Desenvolvimento

O ambiente de desenvolvimento é configurado usando Dev Containers, o que garante:

- Consistência entre ambientes de desenvolvimento
- Todas as dependências pré-instaladas
- Containers isolados para backend e frontend
- Python 3.9 como linguagem principal
- Ferramenta `uv` instalada para gerenciamento de pacotes Python

## Dockerfile do Dev Container

O arquivo `.devcontainer/Dockerfile` é fundamental para o desenvolvimento com VS Code, pois:

- Define a imagem base Python 3.9 usada pelo VS Code ao abrir o projeto em um container
- Configura o ambiente de desenvolvimento com todas as ferramentas necessárias pré-instaladas
- Instala o gerenciador de pacotes `uv` para otimizar a instalação de dependências Python
- Funciona em conjunto com `devcontainer.json` para personalizar a experiência de desenvolvimento
- Oferece um ambiente isolado do sistema operacional host, evitando conflitos de dependências e preservando ferramentas como o *git*

Este contêiner específico do VS Code é separado dos contêineres de aplicação (backend e streamlit), permitindo um ambiente de desenvolvimento completo.

## Volumes

Os volumes Docker garantem que as alterações nos arquivos locais sejam refletidas nos containers:

- `../backend:/app`: Código do backend
- `../streamlit:/app`: Código do frontend Streamlit
- `..:/workspaces`: Todo o repositório
