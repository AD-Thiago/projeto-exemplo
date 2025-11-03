#!/usr/bin/env python3
"""Testes para o módulo principal."""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import DataAnalyzer


class TestDataAnalyzer:
    """Testes para a classe DataAnalyzer."""
    
    def setup_method(self):
        """Configuração para cada teste."""
        self.analyzer = DataAnalyzer()
    
    def test_initialization(self):
        """Testa a inicialização da classe."""
        assert isinstance(self.analyzer, DataAnalyzer)
        assert self.analyzer.data is None
        assert isinstance(self.analyzer.data_path, Path)
    
    def test_generate_sample_data(self):
        """Testa a geração de dados de exemplo."""
        data = self.analyzer.generate_sample_data()
        
        # Verifica se é um DataFrame
        assert isinstance(data, pd.DataFrame)
        
        # Verifica o formato
        assert data.shape[0] == 1000  # 1000 linhas
        assert data.shape[1] == 5     # 5 colunas
        
        # Verifica as colunas
        expected_columns = ['id', 'categoria', 'valor', 'data', 'ativo']
        assert list(data.columns) == expected_columns
        
        # Verifica os tipos de dados
        assert data['id'].dtype == 'int64'
        assert data['categoria'].dtype == 'object'
        assert data['valor'].dtype == 'float64'
        assert data['ativo'].dtype == 'bool'
    
    def test_load_data_without_file(self):
        """Testa o carregamento de dados quando o arquivo não existe."""
        # Define um caminho que não existe
        self.analyzer.data_path = Path("arquivo_inexistente.csv")
        
        data = self.analyzer.load_data()
        
        # Deve gerar dados de exemplo
        assert isinstance(data, pd.DataFrame)
        assert data.shape[0] == 1000
    
    def test_analyze(self):
        """Testa a função de análise."""
        # Gera dados de exemplo primeiro
        self.analyzer.generate_sample_data()
        
        analysis = self.analyzer.analyze()
        
        # Verifica se é um dicionário
        assert isinstance(analysis, dict)
        
        # Verifica as chaves esperadas
        expected_keys = ['shape', 'columns', 'dtypes', 'missing_values', 
                        'numeric_summary', 'categorical_summary']
        assert all(key in analysis for key in expected_keys)
        
        # Verifica alguns valores
        assert analysis['shape'] == (1000, 5)
        assert len(analysis['columns']) == 5
        assert 'categoria' in analysis['categorical_summary']
    
    def test_analyze_empty_data(self):
        """Testa a análise com dados vazios."""
        self.analyzer.data = pd.DataFrame()
        
        analysis = self.analyzer.analyze()
        
        assert analysis['shape'] == (0, 0)
        assert analysis['columns'] == []
    
    def test_create_visualizations(self, tmp_path):
        """Testa a criação de visualizações."""
        # Gera dados de exemplo
        self.analyzer.generate_sample_data()
        
        # Define um diretório temporário para salvar os gráficos
        plot_dir = tmp_path / "plots"
        
        # Cria as visualizações
        self.analyzer.create_visualizations(str(plot_dir))
        
        # Verifica se o diretório foi criado
        assert plot_dir.exists()
    
    def test_data_quality(self):
        """Testa a qualidade dos dados gerados."""
        data = self.analyzer.generate_sample_data()
        
        # Verifica se não há valores nulos
        assert data.isnull().sum().sum() == 0
        
        # Verifica se as categorias estão corretas
        categories = data['categoria'].unique()
        assert set(categories).issubset({'A', 'B', 'C', 'D'})
        
        # Verifica se os valores estão em um range razoável
        assert data['valor'].min() > 0
        assert data['valor'].max() < 200
        
        # Verifica se os IDs são únicos
        assert len(data['id'].unique()) == len(data)


# Testes de integração
def test_main_workflow():
    """Testa o fluxo principal do programa."""
    from main import main
    
    # Executa a função principal
    result = main()
    
    # Verifica se retornou um dicionário com os resultados
    assert isinstance(result, dict)
    assert 'shape' in result
    assert 'columns' in result


if __name__ == "__main__":
    pytest.main([__file__])
