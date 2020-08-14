## Encontrando el tesoro

Ahora mostremos al jugador como un píxel blanco. Tendrás que usar la palanca de mando Sense HAT para navegar hacia donde creas que se encuentra escondido el tesoro.

El Sense Hat físico tiene una palanca de mando pequeña. Puedes ver una foto en el emulador:

![screenshot](images/treasure-joystick.png)

In the emulator you can use the arrow keys for the direction buttons on the joystick and Enter (Return) for pressing the middle button.

Ahora agreguemos un píxel que el jugador pueda mover a donde cree que el tesoro está oculto. El jugador es un píxel blanco.

+ Ahora muestre la ubicación del jugador con un píxel blanco:
    
    ![screenshot](images/treasure-player.png)
    
    `x` y `y` son las coordenadas del jugador.

+ Hagamos que el píxel blanco se mueva con la palanca de mando. Cada vez que el jugador presiona una de las flechas del teclado en la palanca de mando, necesitamos borrar el píxel actual y dibujar uno en la nueva ubicación. Comencemos permitiendo que el jugador se mueva en la dirección y (arriba y abajo):
    
    ![screenshot](images/treasure-move-y.png)

+ Prueba tu código presionando las flechas hacia arriba y hacia abajo en el teclado.
    
    ![screenshot](images/treasure-arrow-keys.png)
    
    ¿Qué sucede cuando alcanzas el borde superior y presionas hacia arriba?
    
    ![screenshot](images/treasure-error.png)
    
    If the y position goes below 0 or above 7 then you'll get an error when you try and set the pixel colour.

+ Agreguemos una marca de verificación para asegurarnos que el píxel permanezca en el monitor:
    
    ![screenshot](images/treasure-move-check.png)

+ Ahora agreguemos movimiento en la dirección x. Añade el código resaltado:
    
    ![screenshot](images/treasure-move.png)

+ Una vez que te hayas movido a la ubicación donde crees que el tesoro está oculto, debes oprimir el botón central de la palanca de mando. En el emulador deberás presionar el botón Enter (Retorno) en el teclado.
    
    Si el jugador está en la misma ubicación que el tesoro, entonces lo ha encontrado y el píxel se pone verde por 1 segundo.
    
    Si el jugador ha elegido la ubicación incorrecta, el píxel se pone rojo por 1 segundo.
    
    ![screenshot](images/treasure-check.png)
    
    `break` means we don't need to wait for more events after the player has chosen a location, we can stop repeating the loop.