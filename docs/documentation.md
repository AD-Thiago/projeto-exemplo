# Documentação do Projeto

## Visão Geral

Este projeto é um exemplo de estrutura completa para projetos de análise de dados em Python. Ele inclui:

- Estrutura organizada de código
- Testes automatizados
- Documentação completa
- Configurações de desenvolvimento
- Exemplos práticos

## Arquitetura

### Estrutura de Diretórios

```
projeto-exemplo/
├── README.md              # Documentação principal
├── .gitignore             # Arquivos a serem ignorados pelo Git
├── requirements.txt       # Dependências do projeto
├── setup.py               # Configuração de instalação
├── src/                   # Código fonte principal
│   ├── __init__.py        # Inicialização do pacote
│   └── main.py            # Módulo principal
├── tests/                 # Testes automatizados
│   ├── __init__.py        # Inicialização dos testes
│   └── test_main.py       # Testes do módulo principal
├── docs/                  # Documentação
│   └── documentation.md   # Este arquivo
└── data/                  # Dados do projeto
    └── sample_data.csv    # Dados de exemplo
```

### Componentes Principais

#### DataAnalyzer

Classe principal para análise de dados com as seguintes funcionalidades:

- **Carregamento de dados**: Lê dados de arquivos CSV ou gera dados de exemplo
- **Análise exploratória**: Calcula estatísticas descritivas e identifica padrões
- **Visualizações**: Cria gráficos para explorar os dados
- **Relatórios**: Gera resumos detalhados da análise

#### Métodos Principais

##### `load_data()`
- Carrega dados de um arquivo CSV
- Se o arquivo não existir, gera dados de exemplo
- Retorna um DataFrame pandas

##### `analyze()`
- Realiza análise exploratória dos dados
- Calcula estatísticas descritivas
- Identifica valores ausentes
- Analisa variáveis categóricas e numéricas
- Retorna um dicionário com os resultados

##### `create_visualizations()`
- Cria visualizações dos dados
- Gera histogramas para variáveis numéricas
- Cria gráficos de barras para variáveis categóricas
- Salva os gráficos em arquivos PNG

## Instalação e Uso

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/AD-Thiago/projeto-exemplo.git
cd projeto-exemplo
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Instale o projeto em modo desenvolvimento:
```bash
pip install -e .
```

### Uso Básico

#### Executar o script principal:
```bash
python src/main.py
```

#### Usar como biblioteca:
```python
from src.main import DataAnalyzer

# Criar uma instância do analisador
analyzer = DataAnalyzer("caminho/para/seus/dados.csv")

# Carregar e analisar os dados
data = analyzer.load_data()
results = analyzer.analyze()

# Criar visualizações
analyzer.create_visualizations("caminho/para/salvar/graficos/")
```

## Desenvolvimento

### Executar Testes

```bash
# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=src

# Executar testes específicos
pytest tests/test_main.py::TestDataAnalyzer::test_analyze
```

### Formatar Código

```bash
# Formatar com black
black src/ tests/

# Verificar estilo com flake8
flake8 src/ tests/

# Verificar tipos com mypy
mypy src/
```

### Estrutura de Testes

Os testes estão organizados na pasta `tests/` e seguem a convenção:

- `test_*.py` para arquivos de teste
- `Test*` para classes de teste
- `test_*` para métodos de teste

#### Cobertura de Testes

- **Testes unitários**: Testam funções e métodos individuais
- **Testes de integração**: Testam o fluxo completo da aplicação
- **Testes de qualidade de dados**: Verificam a integridade dos dados gerados

## Configuração

### Variáveis de Ambiente

O projeto suporta configuração via variáveis de ambiente. Crie um arquivo `.env`:

```env
# Configurações de dados
DATA_PATH=data/sample_data.csv
OUTPUT_PATH=output/

# Configurações de logging
LOG_LEVEL=INFO
LOG_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(message)s

# Configurações de visualização
PLOT_STYLE=seaborn
PLOT_DPI=300
```

### Personalização

Você pode personalizar o comportamento do analisador:

```python
# Personalizar geração de dados
analyzer = DataAnalyzer()
analyzer.data = your_custom_data

# Personalizar visualizações
analyzer.create_visualizations(
    save_path="custom/path/",
    style="ggplot",
    dpi=150
)
```

## Extensões e Melhorias

### Funcionalidades Futuras

- [ ] Suporte a múltiplos formatos de dados (Excel, JSON, SQL)
- [ ] Modelos de machine learning integrados
- [ ] Dashboard interativo com Streamlit
- [ ] API REST para análise de dados
- [ ] Integração com bancos de dados
- [ ] Relatórios automatizados em PDF
- [ ] Processamento em lote
- [ ] Cache de resultados

### Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commite suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

#### Guidelines de Contribuição

- Siga o estilo de código (PEP 8)
- Escreva testes para novas funcionalidades
- Documente suas mudanças
- Mantenha os commits organizados
- Use mensagens de commit descritivas

## Troubleshooting

### Problemas Comuns

#### ImportError
```
ImportError: No module named 'src'
```
**Solução**: Certifique-se de que o projeto foi instalado em modo desenvolvimento:
```bash
pip install -e .
```

#### FileNotFoundError
```
FileNotFoundError: [Errno 2] No such file or directory: 'data/sample_data.csv'
```
**Solução**: O sistema gerará dados de exemplo automaticamente. Para usar seus próprios dados, coloque-os na pasta `data/`.

#### MemoryError
```
MemoryError: Unable to allocate array
```
**Solução**: Reduza o tamanho dos dados ou use processamento em chunks:
```python
for chunk in pd.read_csv('large_file.csv', chunksize=1000):
    # Processe cada chunk
    pass
```

## Suporte

- **Email**: thiago@analisandodados.com
- **GitHub Issues**: [Reportar problemas](https://github.com/AD-Thiago/projeto-exemplo/issues)
- **Documentação**: Este arquivo

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Changelog

### v0.1.0 (2025-11-03)
- Versão inicial do projeto
- Implementação da classe DataAnalyzer
- Testes básicos
- Documentação inicial
- Estrutura completa do projeto
