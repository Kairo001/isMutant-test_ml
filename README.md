# Exámen mercado libre
Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Mens.
Me a contratado para que desarrolles un proyecto que detecte si un humano es mutante basándose en su secuencia de ADN.
Para eso me ha pedido crear un programa con un método o función con la siguiente firma:

boolean isMutant(String[] dna)

En donde recibiré como parámetro un array de Strings que representan cada fila de una tabla de (NxN) con la secuencia del ADN. Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representa cada base nitrogenada del ADN.

Sabré si un humano es mutante, si encuentro más de una secuencia de cuatro letras iguales, de forma oblicua, horizontal o vertical.

Teniendo esto en cuenta esto, esta aplicación tiene los siguientes dos API Rest:

- POST -> /mutant/ : Recibe json con la secuencia de ADN. 
- GET -> /stats/ : Retorna un json con las estadisticas de las verificaciones de ADN.

