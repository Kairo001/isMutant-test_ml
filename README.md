# Exámen mercado libre
Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Mens.
Me ha contratado para que desarrolle un proyecto que detecte si un humano es mutante basándose en su secuencia de ADN.
Para eso me ha pedido crear un programa con un método o función con la siguiente firma:

boolean isMutant(String[] dna)

En donde recibiré como parámetro un array de Strings que representan cada fila de una tabla de (NxN) con la secuencia del ADN. Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representa cada base nitrogenada del ADN.

Sabré si un humano es mutante, si encuentro más de una secuencia de cuatro letras iguales, de forma oblicua, horizontal o vertical.

Teniendo esto en cuenta esto, esta aplicación tiene los siguientes dos API Rest:

- POST -> /mutant/ : Recibe json con un solo par nombre/valor, donde el nombre tiene que ser "dna" y el valor tiene que ser la secuencia de ADN como un array de strigns. 
- GET -> /stats/ : Retorna un json con las estadisticas de las verificaciones de ADN.

## Configuración para despliegue local
1. Clonar este repositorio.
2. Crear un entorno virtual de python.
```sh
virtualenv name_env
```
3. Activar el entorno vitual.
- Windows
```sh
name_env\Scripts\activate.bat
```
- Linux
```sh
source name_env/bin/activate
```
4. Installar todas las dependencias del proyecto.
```sh
pip install -r requirements.txt
```
5. Ejecutar el siguiente comando.
```sh
python manage.py runserver
```
