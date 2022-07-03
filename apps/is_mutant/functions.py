
def detect_errors(adn:list):
    for i in range(len(adn)):
        if len(adn[i]) != len(adn):
            return True, "DNA error, it is not an NxN matrix"
        for j in range(len(adn[i])):
            character = adn[i][j]
            if character not in "ATCG":
                return True, "DNA error, does not meet the letters."
    
    return False, "Sin errores"
    
def is_mutant(adn:list):
    [error,msn] = detect_errors(adn)
    if error:
        return True, False, msn
    pos_success = []
    for i in range(len(adn)):
        for j in range(len(adn[i])):
            character = adn[i][j]
            pos = [i,j]
            if pos in pos_success:
                continue
            
            try:
                if adn[i-1][j-1] == character and adn[i+1][j+1] == character and adn[i+2][j+2] == character:
                    pos_success += [[i-1,j-1],[i,j],[i+1,j+1],[i+2,j+2]]
            except:
                pass
            try:
                if adn[i][j-1] == character and adn[i][j+1] == character and adn[i][j+2] == character:
                    pos_success += [[i,j-1],[i,j],[i,j+1],[i,j+2]]
            except:
                pass
            try:        
                if adn[i-1][j+1] == character and adn[i+1][j-1] == character and adn[i+2][j-2] == character:
                    pos_success += [[i-1,j+1],[i,j],[i+1,j-1],[i+2,j-2]]
            except:
                pass
            try:  
                if adn[i-1][j] == character and adn[i+1][j] == character and adn[i+2][j] == character:
                    pos_success += [[i-1,j],[i,j],[i+1,j],[i+2,j]]
            except:
                pass
            
            if len(pos_success) == 8:
                return False, True, "The human is mutant."
            
    return False, False, "The human is not mutant."