notas = {"Ana": [8.5, 9.0, 7.5], "Bruno": [6.0, 5.5, 4.0], "Carla": [7.0, 8.0, 9.0]}
media_ana = sum(notas['Ana'])/len(notas['Ana'])
media_Bruno = sum(notas['Bruno'])/len(notas['Bruno'])
media_Carla = sum(notas['Carla'])/len(notas['Carla'])
dicionario_final = {'Ana': media_ana, 'Bruno': media_Bruno, 'Carla': media_Carla}

print(dicionario_final)