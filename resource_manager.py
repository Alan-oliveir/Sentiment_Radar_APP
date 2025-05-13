"""
Módulo para carregar e injetar recursos CSS e JavaScript no Streamlit
"""
import os

import streamlit as st


class ResourceManager:
    """
    Gerenciador de recursos para injetar CSS e JavaScript no Streamlit.
    """
    
    @staticmethod
    def load_resource(file_path):
        """
        Carrega o conteúdo de um arquivo de recurso.
        
        Args:
            file_path (str): Caminho para o arquivo
            
        Returns:
            str: Conteúdo do arquivo ou string vazia se não existir
        """
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        return ""
    
    @staticmethod
    def inject_css(css_file_path):
        """
        Injeta o conteúdo de um arquivo CSS no Streamlit.
        
        Args:
            css_file_path (str): Caminho para o arquivo CSS
        """
        css_content = ResourceManager.load_resource(css_file_path)
        if css_content:
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    
    @staticmethod
    def inject_js(js_file_path):
        """
        Injeta o conteúdo de um arquivo JavaScript no Streamlit.
        
        Args:
            js_file_path (str): Caminho para o arquivo JavaScript
        """
        js_content = ResourceManager.load_resource(js_file_path)
        if js_content:
            st.markdown(f"<script>{js_content}</script>", unsafe_allow_html=True)
    
    @staticmethod
    def ensure_static_dir():
        """
        Certifica-se de que o diretório static existe.
        
        Returns:
            str: Caminho para o diretório static
        """
        static_dir = "static"
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)
        return static_dir
    
    @staticmethod
    def create_file_if_not_exists(file_path, content):
        """
        Cria um arquivo com o conteúdo especificado se ele não existir.
        
        Args:
            file_path (str): Caminho para o arquivo
            content (str): Conteúdo a ser escrito no arquivo
        """
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
