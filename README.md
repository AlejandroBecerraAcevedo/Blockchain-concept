
# Simulación de Blockchain con Carteras Digitales, Transacciones y Minería de Bloques

Este proyecto simula el funcionamiento básico de una cadena de bloques (blockchain), implementando carteras digitales, transacciones y minería de bloques. Los usuarios pueden crear carteras protegidas con claves privadas generadas a partir de palabras aleatorias, realizar transferencias de tokens entre carteras y consultar el saldo de cada una. Las transacciones se agrupan en bloques, que deben ser minados utilizando un proceso de prueba de trabajo basado en la dificultad establecida. Para garantizar la integridad de los datos, cada bloque contiene un hash generado a partir de sus datos y la raíz de Merkle, que resume todas las transacciones del bloque. A través de este sistema, el proyecto demuestra los principios de una blockchain, donde las transacciones son seguras, verificables y descentralizadas.

Se debe tener en cuenta que este proyecto esta realizado 100% en python con la versión Python 3.12.5
y para ser ejecutado vasta con ejecutar la siguiente linea de comando:

#### Primer paso es abrir VScode

#### Clonar el repositorio:
```bash
git clone https://github.com/AlejandroBecerraAcevedo/Blockchain-concept.git
```

#### Entrar a la carpeta clonada

```bash
cd Blockchain-concept
```
#### Una vez dentro del repositorio local ejecutar la siguiente linea:

```bash
python ./main.py
```
o también

```bash
python3 ./main.py
```


Cuenta con los siguientes componentes:


## utils.py

### Este código consiste en dos clases: 

RandomWords y Hashing. La clase RandomWords genera una selección aleatoria de tres palabras de una lista predefinida, y la clase Hashing se usa para crear un hash SHA-256 de una cadena de entrada.


## root_hash.py

### Class Get_tree_root_hash:
Esta clase está diseñada para calcular la Merkle Root de una lista de transacciones. el Merkle Root es un único hash que representa la integridad de todo el conjunto de transacciones.

## data_base_chain.py

El código define una clase llamada DataBase que actúa como un almacén para gestionar carteras (wallets), bloques y transacciones en una cadena de bloques. 

### Almacenamiento de carteras: 

La clase permite añadir nuevas carteras al sistema y consultar las existentes a través de su clave pública. También puede verificar si una cartera ya está registrada y obtener su saldo.

### Gestión de transacciones: 

Las transacciones pueden añadirse a la base de datos, y cada transacción incluye detalles como el remitente, el receptor y la cantidad transferida. Se puede consultar todas las transacciones y encontrar una específica por el bloque al que pertenece.

### Manipulación de bloques: 

Los bloques que contienen transacciones pueden ser añadidos a la base de datos. Se imprimen los detalles de cada bloque (hash, raíz de Merkle, transacciones, etc.), y se puede consultar el bloque anterior o buscar uno específico por su hash.

## wallet.py

Este código define una clase llamada Wallet que representa una cartera digital dentro de un sistema basado en blockchain. Los elementos clave que maneja esta cartera son:

### Clave privada y clave pública: 

La clave privada de la cartera se genera a partir de un nombre y una clave privada inicial proporcionada. Esta clave privada se hashea usando la función de hash (Hashing), y luego la clave pública se deriva de un segundo hash de la clave privada.

### Balance de la cartera: 

La cartera comienza con un balance de 0, y tiene la capacidad de recibir depósitos mediante el método deposit.

### Gestión de transacciones: 

La cartera almacena un registro de todas las transacciones asociadas a ella. Se pueden añadir nuevas transacciones al registro mediante el método set_transaction.

### Métodos adicionales: 

La clase incluye métodos para obtener la clave privada, actualizar la clave pública y consultar el saldo de la cartera.

## transaction.py

Este código define una clase Transaction que representa una transacción en un sistema basado en blockchain. Los principales elementos que maneja son:

### Datos de la transacción: 

Al inicializar una transacción, se deben proporcionar el remitente (sender), el destinatario (recipient) y la cantidad (amount). Además, la transacción puede estar asociada a un bloque específico, y si no se especifica, el bloque se establece por defecto en -1.

### Cambio de bloque: 

La transacción tiene un método para cambiar el bloque al que pertenece (change_id_block), útil cuando la transacción se agrega a un nuevo bloque en la cadena de bloques.

### Representación en cadena: 

El método to_string() devuelve una representación de la transacción en formato de cadena para la creación del Hash Merkle Root.

## block.py

Este código define una clase Block que simula un bloque en una cadena de bloques (blockchain). Un bloque en la blockchain contiene transacciones y debe cumplir con ciertos criterios antes de ser aceptado, como calcular un hash que cumpla con una dificultad específica, lo que se conoce como "minado". Los elementos principales son:

### Atributos del bloque:

Cada bloque tiene un índice, una lista de transacciones, el hash del bloque anterior, un nonce (contador para el proceso de minería) y un hash propio que se calcula a partir de estos datos.
El bloque también incluye una "raíz de Merkle", que es un hash que representa todas las transacciones dentro del bloque. Este hash es clave para la integridad del bloque.
### Cálculo del hash:

El método calculate_hash() genera el hash del bloque concatenando el índice, el hash del bloque anterior, la raíz de Merkle y el nonce. Este hash se calcula usando el algoritmo SHA-256.

### Actualización de la raíz de Merkle:

El método update_merkle_root() utiliza la clase Get_tree_root_hash para generar la raíz de Merkle a partir de las transacciones del bloque. Esta raíz asegura que cualquier cambio en las transacciones sería detectado, ya que alteraría el hash.
### Minado del bloque:

El proceso de minería se realiza en el método mine_block(). Consiste en encontrar un hash que comience con un cierto número de ceros, lo cual depende de la dificultad establecida. El bloque sigue ajustando el nonce y re-calculando el hash hasta cumplir con la dificultad.

## main.py

Este código define una aplicación de simulación de una cadena de bloques (blockchain) con funcionalidad para crear carteras, realizar transacciones, minar bloques y verificar el estado de la cadena de bloques.

### Clase main:
Inicializa la aplicación creando el bloque génesis (primer bloque de la cadena) si aún no se ha creado.
### Opciones del menú:
Crear una cartera: Permite a los usuarios generar una nueva cartera con una clave pública y privada derivada de palabras aleatorias.
### Depositar (Prueba de concepto): 

Se parte pensando en que el bloque es un bloque n y que se tiene cierta cantidad de monedas, la función depositar consiste en inicializar una wallet con un número de coins que pueda transferir.

Añade una cantidad de tokens a la cartera de un usuario.
### Enviar monedas (): 

Permite transferir tokens de una cartera a otra siempre que el remitente tenga suficientes fondos.

### Minar un bloque: 
Minar un nuevo bloque que contiene las transacciones pendientes, validando las transacciones y añadiendo el bloque a la cadena, realizando la prueba de trabajo con cierta dificultad

### Ver la cadena de bloques: 

Muestra todos los bloques en la cadena con sus detalles.
### Ver las transacciones: 

Muestra las transacciones asociadas a una cartera específica.
### Ver el saldo: 
Consulta el saldo actual de una cartera.
### Salir: 

Finaliza la aplicación.


Este programa simula la funcionalidad básica de una blockchain, incluyendo la creación de carteras, la transferencia de tokens entre usuarios y el proceso de minería para validar y registrar transacciones.