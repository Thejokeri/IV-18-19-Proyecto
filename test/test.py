import sys
sys.path.insert(0, './src/')
from pdfupload import PDFUpload

pdfupload = PDFUpload()

# Test del Status

def testStatus():
    assert pdfupload.Status() == "OK"

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

# Test del DeleteStore

def testDeleteStore():
    assert pdfupload.DeleteStore() == True

# Test de verificar la existencia del usuario

def testIsUser():
    assert pdfupload.IsUser(1) == False
    assert pdfupload.IsUser(1.0) == False
    assert pdfupload.IsUser('test') == False
    pdfupload.DeleteStore()

# Test de creacion de usuario

def testCreateUser():
    assert pdfupload.CreateUser('') == False
    assert pdfupload.CreateUser(1) == False
    assert pdfupload.CreateUser(1.0) == False
    assert pdfupload.CreateUser('test') == True
    pdfupload.DeleteStore()

# Test de eliminacion del usuario

def testDeleteUser():
    assert pdfupload.DeleteUser('') == False
    assert pdfupload.DeleteUser(1) == False
    assert pdfupload.DeleteUser(1.0) == False
    assert pdfupload.DeleteUser('test') == False

    pdfupload.CreateUser('test')
    assert pdfupload.DeleteUser('test') == True
    pdfupload.DeleteStore()

# Test de verificar la existencia del archivo

def testIsFile():
    assert pdfupload.IsFile(1,1) == False
    assert pdfupload.IsFile(1.0,1.0) == False
    assert pdfupload.IsFile(1,1.0) == False
    assert pdfupload.IsFile(1.0,1) == False
    assert pdfupload.IsFile('test','pdftest.pdf') == False
    pdfupload.DeleteStore()

# Test de agregar el archivo

def testAddNewFile():
    assert pdfupload.AddNewFile('','') == False
    assert pdfupload.AddNewFile(1,1) == False
    assert pdfupload.AddNewFile(1.0,1) == False
    assert pdfupload.AddNewFile(1,1.0) == False
    assert pdfupload.AddNewFile(1.0,1.0) == False
    assert pdfupload.AddNewFile('test','pdftest') == False

    pdfupload.CreateUser('test')
    assert pdfupload.AddNewFile('test','pdftest.pdf') == True
    pdfupload.DeleteStore()

# Test de eliminacion del archivo

def testDeleteFile():
    assert pdfupload.DeleteFile('','') == False
    assert pdfupload.DeleteFile(1,1) == False
    assert pdfupload.DeleteFile(1.0,1) == False
    assert pdfupload.DeleteFile(1,1.0) == False
    assert pdfupload.DeleteFile(1.0,1.0) == False
    assert pdfupload.DeleteFile('test','pdftest') == False

    pdfupload.CreateUser('test')
    pdfupload.AddNewFile('test', 'pdftest.pdf')
    assert pdfupload.DeleteFile('test','pdftest.pdf') == True
    pdfupload.DeleteStore()

# Test de la busqueda de archivos

def testSearchFile():
    assert len(pdfupload.SearchFile('','')) == 0
    assert len(pdfupload.SearchFile(1,1)) == 0
    assert len(pdfupload.SearchFile(1.0,1)) == 0
    assert len(pdfupload.SearchFile(1,1.0)) == 0
    assert len(pdfupload.SearchFile(1.0,1.0)) == 0

    pdfupload.CreateUser('test')
    pdfupload.AddNewFile('test', 'pdftest.pdf')
    assert len(pdfupload.SearchFile('test','pdf')) == 1
    pdfupload.AddNewFile('test', 'pdftest1.pdf')
    assert len(pdfupload.SearchFile('test','pdf')) == 2
