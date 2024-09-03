import machine
import time

# Configuración del pin ADC (Ejemplo: Pin GP26)
pin_adc = machine.ADC(26)

# Definir los umbrales de voltaje para considerar un latido
umbral_superior = 1.2
umbral_inferior = 0.1

# Definir el intervalo de tiempo para calcular el BPM (en segundos)
intervalo_bpm = 2  # Calcular el BPM cada 5 segundos

# Variables para contar el número de latidos y el tiempo transcurrido
num_latidos = 0
ha_ocurrido_latido = False
tiempo_inicio_bpm = time.time()

# Abrir el archivo en modo escritura
with open('voltage_data.txt', 'w') as f:
    # Leer el primer valor analógico
    valor_analogico_previo = pin_adc.read_u16()  # Lee un valor de 16 bits
    
    while True:
        # Leer el valor analógico actual
        valor_analogico_actual = pin_adc.read_u16()  # Lee un valor de 16 bits
        
        # Convertir el valor analógico a voltaje (0 a 5V)
        voltaje_actual = (valor_analogico_actual / 65535.0) * 30
        
        # Imprimir el voltaje actual
        print("Voltaje:", voltaje_actual)
        
        # Guardar el voltaje actual en el archivo
        f.write("{:.2f}\n".format(voltaje_actual))
        f.flush()  # Asegura que los datos sean escritos en el archivo inmediatamente
        
        # Verificar si se ha superado el umbral superior
        if voltaje_actual > umbral_superior:
            ha_ocurrido_latido = True
        
        # Verificar si ha ocurrido un latido y se ha vuelto al umbral inferior
        if ha_ocurrido_latido and voltaje_actual <= umbral_inferior:
            num_latidos += 1
            ha_ocurrido_latido = False
        
        # Verificar si ha pasado el intervalo de tiempo para calcular el BPM
        tiempo_transcurrido_bpm = time.time() - tiempo_inicio_bpm
        if tiempo_transcurrido_bpm >= intervalo_bpm:
            # Calcular los latidos por minuto (BPM)
            bpm = (num_latidos / tiempo_transcurrido_bpm) * 60
            
            # Imprimir los latidos por minuto
            print("Latidos por minuto (BPM):", bpm)
            
            # Reiniciar el conteo de latidos y el tiempo para el próximo cálculo de BPM
            num_latidos = 0
            tiempo_inicio_bpm = time.time()
        
        # Agregar un retardo para controlar la frecuencia de muestreo
        time.sleep(0.13)  # Ajusta según sea necesario

