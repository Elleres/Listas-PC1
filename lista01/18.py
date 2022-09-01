mb = float(input("Digite o tamanho do arquivo em MB: "))
vel = float(input("Digite a velocidade da internet em Mbps: "))
tempo_seg = (mb * 8)/vel
tempo_min = tempo_seg / 60
rest_seg = tempo_min - int(tempo_seg/60)
print(
    f"O tempo de download do arquivo com essa velocidade é de {int(tempo_min)} minutos e {int(rest_seg* 60)} segundos aproximadamente")
