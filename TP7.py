def simplification0(exp):
    somme = 0
    expNew = ""
    action = "+"
    cpt = 0
    for caractere in exp:
        if (caractere.isdigit()):
            if(action == "+") :
                somme += int(caractere)
            else :
                somme -= int(caractere)
        elif (caractere == "+" or caractere == "-") :
            action = caractere
        else :
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
