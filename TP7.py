def simplification0(exp):
    somme = 0
    expNew = ""
    action = "+" # variable pour savoir le sign de la variable 
    cpt = 0 #Variable pour savoir la position de l'inconnu dans la nouvelle expression 
    for caractere in exp:
        if (caractere.isdigit()): #Il s'agit d'un nombre entier 
            if(action == "+") :
                somme += int(caractere)
            else :
                somme -= int(caractere)
        elif (caractere == "+" or caractere == "-") : #Il s'agit des symboles + ou -
            action = caractere
        else : #Il s'agit des inconnus x et y 
            if cpt == 0 :
                expNew += caractere
            else :
                expNew += action + caractere
            cpt +=1
    if(somme >0):   
        expNew += "+" + str(somme)
    else :
         expNew += str(somme)   
    return expNew
