import sys
sys.path.insert(0, './src/')
from pdfupload import PDFUpload

pdfupload = PDFUpload()

# Test del CheckArguments

def testCheckArguments():
    assert pdfupload.CheckArguments() == False
    assert pdfupload.CheckArguments('') == False
    assert pdfupload.CheckArguments(1) == False
    assert pdfupload.CheckArguments(1.0) == False
    assert pdfupload.CheckArguments('','') == False
    assert pdfupload.CheckArguments(1,1) == False
    assert pdfupload.CheckArguments(1,1.0) == False
    assert pdfupload.CheckArguments(1.0,1) == False
    assert pdfupload.CheckArguments(1.0,1.0) == False
    assert pdfupload.CheckArguments('test') == True
    assert pdfupload.CheckArguments('test','pdftest.pdf') == True

# Test de verificar la existencia del usuario

def testIsUser():
    assert pdfupload.IsUser(1) == False
    assert pdfupload.IsUser(1.0) == False
    assert pdfupload.IsUser('test') == False

# Test de verificar la existencia del archivo

def testIsFile():
    assert pdfupload.IsFile(1,1) == False
    assert pdfupload.IsFile(1.0,1.0) == False
    assert pdfupload.IsFile(1,1.0) == False
    assert pdfupload.IsFile(1.0,1) == False
    assert pdfupload.IsFile('test','pdftest.pdf') == False

# Test de la busqueda de archivos

def testSearchFile():
    assert pdfupload.SearchFile('','') == False
    assert pdfupload.SearchFile(1,1) == False
    assert pdfupload.SearchFile(1.0,1) == False
    assert pdfupload.SearchFile(1,1.0) == False
    assert pdfupload.SearchFile(1.0,1.0) == False