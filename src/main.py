#!/usr/bin/env python3
"""Módulo principal do projeto."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DataAnalyzer:
    """Classe para análise de dados."""
    
    def __init__(self, data_path: str = "data/sample_data.csv"):
        """Inicializa o analisador de dados.
        
        Args:
            data_path (str): Caminho para o arquivo de dados.
        """
        self.data_path = Path(data_path)
        self.data = None
        
    def load_data(self) -> pd.DataFrame:
        """Carrega os dados do arquivo.
        
        Returns:
            pd.DataFrame: Dados carregados.
        """
        try:
            if self.data_path.exists():
                self.data = pd.read_csv(self.data_path)
                logger.info(f"Dados carregados: {self.data.shape}")
                return self.data
            else:
                logger.warning("Arquivo de dados não encontrado. Gerando dados de exemplo...")
                return self.generate_sample_data()
        except Exception as e:
            logger.error(f"Erro ao carregar dados: {e}")
            return self.generate_sample_data()
    
    def generate_sample_data(self) -> pd.DataFrame:
        """Gera dados de exemplo para demonstração.
        
        Returns:
            pd.DataFrame: Dados de exemplo.
        """
        np.random.seed(42)
        n_samples = 1000
        
        data = {
            'id': range(1, n_samples + 1),
            'categoria': np.random.choice(['A', 'B', 'C', 'D'], n_samples),
            'valor': np.random.normal(100, 25, n_samples),
            'data': pd.date_range('2023-01-01', periods=n_samples, freq='D'),
            'ativo': np.random.choice([True, False], n_samples, p=[0.7, 0.3])
        }
        
        self.data = pd.DataFrame(data)
        logger.info(f"Dados de exemplo gerados: {self.data.shape}")
        return self.data
    
    def analyze(self) -> dict:
        """Realiza análise exploratória dos dados.
        
        Returns:
            dict: Resultados da análise.
        """
        if self.data is None:
            self.load_data()
        
        analysis = {
            'shape': self.data.shape,
            'columns': list(self.data.columns),
            'dtypes': self.data.dtypes.to_dict(),
            'missing_values': self.data.isnull().sum().to_dict(),
            'numeric_summary': self.data.describe().to_dict() if len(self.data.select_dtypes(include=[np.number]).columns) > 0 else {},
            'categorical_summary': {col: self.data[col].value_counts().to_dict() 
                                  for col in self.data.select_dtypes(include=['object', 'category']).columns}
        }
        
        return analysis
    
    def create_visualizations(self, save_path: str = "plots/") -> None:
        """Cria visualizações dos dados.
        
        Args:
            save_path (str): Caminho para salvar os gráficos.
        """
        if self.data is None:
            self.load_data()
        
        save_dir = Path(save_path)
        save_dir.mkdir(exist_ok=True)
        
        # Configuração do estilo
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # Gráfico 1: Distribuição de valores numéricos
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            fig, axes = plt.subplots(1, len(numeric_cols), figsize=(15, 5))
            if len(numeric_cols) == 1:
                axes = [axes]
            
            for i, col in enumerate(numeric_cols):
                if col != 'id':  # Pula colunas de ID
                    self.data[col].hist(bins=30, ax=axes[i])
                    axes[i].set_title(f'Distribuição de {col}')
                    axes[i].set_xlabel(col)
                    axes[i].set_ylabel('Frequência')
            
            plt.tight_layout()
            plt.savefig(save_dir / 'distribuicoes.png', dpi=300, bbox_inches='tight')
            plt.close()
        
        # Gráfico 2: Variáveis categóricas
        categorical_cols = self.data.select_dtypes(include=['object', 'category', 'bool']).columns
        if len(categorical_cols) > 0:
            fig, axes = plt.subplots(1, len(categorical_cols), figsize=(15, 5))
            if len(categorical_cols) == 1:
                axes = [axes]
            
            for i, col in enumerate(categorical_cols):
                self.data[col].value_counts().plot(kind='bar', ax=axes[i])
                axes[i].set_title(f'Contagem de {col}')
                axes[i].set_xlabel(col)
                axes[i].set_ylabel('Contagem')
                axes[i].tick_params(axis='x', rotation=45)
            
            plt.tight_layout()
            plt.savefig(save_dir / 'categoricas.png', dpi=300, bbox_inches='tight')
            plt.close()
        
        logger.info(f"Visualizações salvas em {save_dir}")


def main():
    """Função principal."""
    logger.info("Iniciando análise de dados...")
    
    # Inicializa o analisador
    analyzer = DataAnalyzer()
    
    # Carrega e analisa os dados
    data = analyzer.load_data()
    analysis_results = analyzer.analyze()
    
    # Exibe resultados
    print("\n=== RESULTADO DA ANÁLISE ===")
    print(f"Formato dos dados: {analysis_results['shape']}")
    print(f"Colunas: {analysis_results['columns']}")
    print(f"Valores ausentes: {analysis_results['missing_values']}")
    
    # Cria visualizações
    analyzer.create_visualizations()
    
    logger.info("Análise concluída com sucesso!")
    
    return analysis_results


if __name__ == "__main__":
    main()
