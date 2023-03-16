# act10

Objects son la abstracción de Python para los datos. 
Todos los datos en un programa Python están representados por objetos o por relaciones entre objetos. 

Esta compartimentación es el concepto central de la programación orientada a objetos.
Se construyen objetos que almacenan datos y contienen tipos específicos de funcionalidad.

Todo en Python es un objeto, desde números a funciones. 
El lenguaje provee ciertos mecanismos para no tener que usar explícitamente técnicas de orientación a objetos.

Programación orientada a objetos

Sus beneficios son los siguientes:

Encapsulamiento
Permite empaquetar el código dentro de una unidad (objeto) donde se puede determinar el ámbito de actuación.

Abstracción
Permite generalizar los tipos de objetos a través de las clases y simplificar el programa.

Herencia
Permite reutilizar código al poder heredar atributos y comportamientos de una clase a otra.

Polimorfismo
Permite crear múltiples objetos a partir de una misma pieza flexible de código.


Creando objetos
Iniciamos con crear la primera clase. Modelado de algunos de los droides de la saga StarWars:

class StarWarsDroid:
    pass
c3po = StarWarsDroid()
r2d2 = StarWarsDroid()
bb8 = StarWarsDroid()

type(c3po)
__main__.StarWarsDroid
type(r2d2)
__main__.StarWarsDroid
type(bb8)
__main__.StarWarsDroid
blue_droid = StarWarsDroid()
golden_droid = StarWarsDroid()

golden_droid.name = 'C-3PO'

blue_droid.name = 'R2-D2'
blue_droid.height = 1.09
blue_droid.num_feet = 3
blue_droid.partner_droid = golden_droid  # otro droide como atributo
golden_droid.name
'C-3PO'

blue_droid.num_feet
3
