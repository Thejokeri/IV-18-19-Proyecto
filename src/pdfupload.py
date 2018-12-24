#!/usr/bin/python
import json
import os


class PDFUpload:
    def __init__(self):
        try:
            if os.path.isfile('datauser.json') and os.path.isfile('userfile.json') and os.path.isfile('datafile.json'):
                pathuser = 'datauser.json'
                pathuserfile = 'userfile.json'
                pathfile = 'datafile.json'
            elif os.path.isfile('/data/datauser.json') and os.path.isfile('/data/userfile.json') and os.path.isfile('/data/datafile.json'):
                pathuser = '/data/datauser.json'
                pathuserfile = '/data/userfile.json'
                pathfile = '/data/datafile.json'
            elif os.path.isfile('./data/datauser.json') and os.path.isfile('./data/userfile.json') and os.path.isfile('./data/datafile.json'):
                pathuser = './data/datauser.json'
                pathuserfile = './data/userfile.json'
                pathfile = './data/datafile.json'
            elif os.path.isfile('../data/datauser.json') and os.path.isfile('../data/userfile.json') and os.path.isfile('../data/datafile.json'):
                pathuser = '../data/datauser.json'
                pathuserfile = '../data/userfile.json'
                pathfile = '../data/datafile.json'
            else:
                raise IOError("No se encuentra 'datauser.json y 'datafile.json'")

            with open(pathuser, "r") as f:
                self.user = json.load(f)
            with open(pathfile, "r") as f:
                self.file = json.load(f)
            with open(pathuserfile, "r") as f:
                self.userfile = json.load(f)
        except IOError as fallo:
            print("Error {:s} leyendo el fichero datauser.json, userfile.json y datafile.json".format(fallo))   
            
    def Status(self):
        """
        Return the status of the class
        
        Returns:
        string: return OK
        """
        return "OK"

    def CheckArguments(self, text='none', text1='none'):
        """
        Check if the arguments are not int, float or None. Must be a string

        Parameters:
        text -- first argument. Default 'none'
        text1 -- second argument. Default 'none'

        Returns:
        bool: if the arguments are string
        """
        if text != 'none':
            if type(text) is int or type(text) is float or not text:
                salida = False
            else:
                salida = True
        else:
            if text != 'none' and text1 != 'none':
                if (type(text) is int or type(text) is float) and (type(text1) is int or type(text1) is float) and (not text or not text1):
                    salida = False
                else:
                    salida = True
            else:
                salida = False

        return salida

    def DeleteStore(self):
        """
        Clear the storage

        Returns:
        bool: if the dictionary is empty
        """
        self.user.clear()
        self.file.clear()
        return not bool(self.user) and not bool(self.file)
        
    
    def IsUser(self, user):
        """ 
        Check if the user exists in the dictionary.
    
        Parameters: 
        user -- the id of the user to find.
    
        Returns: 
        bool: if the user exist or not.
    
        """
        check = self.CheckArguments(user)
        found = False
        
        if check:
            for i in range(len(self.user["usuarios"])):
                if self.user["usuarios"][i]["nombre"] == user:
                    found = True
                    data = self.user["usuarios"][i]
                    break
            if found:
                return data
            else:
                return found
        else:
            return check 


    def CreateUser(self, user):
        """ 
        Add a new user to the dictionary. Must be an different user that is not in the dictionary.
    
        Parameters: 
        user -- the id of the user.
    
        Returns: 
        bool: created succesfully.
    
        """
        salida = self.CheckArguments(user)
        
        if salida:
            s = set()
            self.user.update({user : s})
            return self.IsUser(user)

        return salida

    def DeleteUser(self, user):
        """ 
        Delete a user from the dictionary. Must exist the user in the dictionary.
    
        Parameters: 
        user -- the id of the user.
    
        Returns: 
        bool: delete succesfully.
    
        """
        salida = self.CheckArguments(user)
        
        if salida:
            if self.IsUser(user):
                self.almacen.pop(user, None)
                return True
            else:
                return False
        
        return salida

    # Tocar esto
    def IsFile(self, user, f):
        """ 
        Check if the path exists in the dictionary and if the pdf file is on the file system.
    
        Parameters: 
        path -- the path of the pdf file to find.
    
        Returns: 
        bool: if the pdf exist or not.
    
        """
        check = self.CheckArguments(user, f)
        found = False
        
        usuario = self.IsUser(user)

        if check:
            if usuario:
                for i in range(len(self.userfile["archivos"][usuario["id"]]["path_file"])):
                    if f in self.userfile["archivos"][usuario["id"]]["path_file"][i]:
                        found = True
                        path_file = self.userfile["archivos"][usuario["id"]]["path_file"][i]
                        data = self.file[path_file]
                        break
                if found:
                    return data
                else:
                    return found
            else:
                return usuario
        else:
            return check 

    def AddNewFile(self, user, f):
        """ 
        Add a new file to the dictionary. The name of the file must be different from the others in the same directory.
    
        Parameters: 
        user -- the id of the user.
        f -- the file of the user.
    
        Returns: 
        bool: added succesfully.
    
        """
        salida = self.CheckArguments(user, f)

        if salida:
            if self.IsUser(user):
                self.almacen[user].add(f)
                return self.IsFile(user,f)
            else:
                return False
        
        return salida

    def DeleteFile(self, user, f):
        """ 
        Add a new file to the dictionary. The name of the file must be different from the others in the same directory.
    
        Parameters: 
        path -- the path of the file.
    
        Returns: 
        bool: added succesfully.
    
        """
        salida = self.CheckArguments(user,f)
        
        if salida:
            if self.IsUser(user) and self.IsFile(user,f):
                self.almacen[user].remove(f)
                return True
            else:
                return False

        return salida

    # Tocar esto
    def SearchFile(self, user, search):
        """
        Search all the files that are similar to name.

        Parameters:
        user -- the id of the user.
        search -- the search of the user's storage.

        Returns:
        Array: the files resulting from the search
        """
        check = self.CheckArguments(user)
        usuario = self.IsUser(user)
        
        matching = []

        if check:
            if usuario:
                for i in range(len(self.userfile["archivos"][usuario["id"]]["path_file"])):
                    if search in self.userfile["archivos"][usuario["id"]]["path_file"][i]:
                        matching.append(self.userfile["archivos"][usuario["id"]]["path_file"][i])
            else:
                return usuario
        else:
            return check 

        return matching

if __name__ == '__main__':
    pdfupload = PDFUpload()
