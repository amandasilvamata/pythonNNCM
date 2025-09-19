# --- tempo de vida fumante ---

dias = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Há quantos anos você fuma? "))
anos = anos * 360

tempo = (((dias * anos * 10)/60)/24)

anos = anos / 360

print("Fumando %d cigarros por dia em %d anos você terá perdido %.1f dias da sua vida" %(dias, anos, tempo))
