# coding: utf-8
"""
Este modulo tem como objetivo demonstrar usos comuns da bilbioteca os
"""
import os

def print_function(x,y,z):
    print y

def using_os_path():
    
    print "neste sistema o separador de diretorios e: " ,os.sep

    root = os.path.abspath(r"C:")
    
    print root
    print os.path.exists(root)
    
    paths = [ r"C:\Arquivos de Programas",
              r"C:\Arquivos de Programas\Adobe",
              r"C:\Arquivos de Programas x86\ESRI" ]

    print "Prefixo comum ", os.path.commonprefix(paths)
    print "Diretorio pai de " , paths[-1], os.path.dirname(paths[-1])
    print "Tamanho de ", root, os.path.getsize(root), " bytes"
    print "Ultimo acesso a ", root,os.path.getatime(root)
    
    esri_path = os.path.abspath(r"C:\Program Files (x86)\ArcGIS")

    os.path.walk(esri_path,print_function,None)

if __name__ == "__main__":
    using_os_path()

    raw_input("digite qualquer coisa para sair")