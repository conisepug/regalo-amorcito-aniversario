import os
import time

def limpiar_pantalla():
    # Limpia la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def efecto_carga(texto):
    print(f"\n[PROCESANDO] {texto}", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

def caja_fuerte():
    limpiar_pantalla()
    print("=" * 65)
    print("        SISTEMA DE SEGURIDAD CRIPTOGRÁFICA - PROTOCOLO ANIVERSARIO        ")
    print("=" * 65)
    print("[ALERTA] Archivo 'Nuestra_Historia_1_Anio.dat' detectado.")
    print("[ESTADO] El archivo está fuertemente cifrado mediante algoritmo Love-256.")
    print("[INFO]   Para generar la llave de descifrado, responda las preguntas.")
    print("=" * 65)
    input("\nPresiona ENTER para iniciar la secuencia de desencriptación...")

    # ----- PREGUNTA 1 -----
    while True:
        limpiar_pantalla()
        print("--- CAPA DE SEGURIDAD 1/4: EL ORIGEN ---")
        print("\nPregunta: ¿Qué día comenzamos a hablar? (Formato: DD/MM/AAAA)")
        respuesta = input(">> Respuesta: ").strip()
        
        if respuesta == "22/05/2025":
            efecto_carga("Verificando fecha en la base de datos de recuerdos")
            print("[OK] Capa 1 desbloqueada con éxito.")
            time.sleep(1.5)
            break
        else:
            print("\n[ERROR] Clave incorrecta. Registro no encontrado en el historial. Intenta de nuevo.")
            time.sleep(2)

    # ----- PREGUNTA 2 -----
    while True:
        limpiar_pantalla()
        print("--- CAPA DE SEGURIDAD 2/4: PRIMERA CITA ---")
        print("\nPregunta: ¿Cuál fue la primera película que vimos en el cine?")
        respuesta = input(">> Respuesta: ").strip().lower()
        
        # Acepta la respuesta si contiene "mision imposible" o "misión imposible"
        if "mision imposible" in respuesta or "misión imposible" in respuesta:
            efecto_carga("Analizando registros de taquilla emocional")
            print("[OK] Capa 2 desbloqueada con éxito.")
            time.sleep(1.5)
            break
        else:
            print("\n[ERROR] Acceso denegado. Esa película no causó el impacto requerido. Intenta de nuevo.")
            time.sleep(2)

    # ----- PREGUNTA 3 -----
    while True:
        limpiar_pantalla()
        print("--- CAPA DE SEGURIDAD 3/4: SINCRONIZACIÓN TELEPÁTICA ---")
        print("\nPregunta: ¿Qué palabra diremos cuando nos hagan decir la misma al mismo tiempo?")
        respuesta = input(">> Respuesta: ").strip().lower()
        
        if respuesta == "lulankali":
            efecto_carga("Sincronizando canales de telecomunicación mental")
            print("[OK] Capa 3 desbloqueada con éxito.")
            time.sleep(1.5)
            break
        else:
            print("\n[ERROR] Frecuencia incorrecta. Las mentes no están alineadas. Intenta de nuevo.")
            time.sleep(2)

    # ----- PREGUNTA 4 -----
    while True:
        limpiar_pantalla()
        print("--- CAPA DE SEGURIDAD 4/4: COMBUSTIBLE EXCLUSIVO ---")
        print("\nPregunta: ¿Qué almorzamos el día que fuimos a ver la película de la F1?")
        respuesta = input(">> Respuesta: ").strip().lower()
        
        if respuesta == "sushi":
            efecto_carga("Calculando calorías y momentos felices")
            print("[OK] ¡Última capa desbloqueada!")
            time.sleep(1.5)
            break
        else:
            print("\n[ERROR] Integridad del almuerzo fallida. El sistema exige mejor comida. Intenta de nuevo.")
            time.sleep(2)

    # ----- DESBLOQUEO FINAL -----
    limpiar_pantalla()
    efecto_carga("Generando llave maestra y desencriptando archivo")
    limpiar_pantalla()
    
    print("=" * 65)
    print("               ¡ACCESO CONCEDIDO - ARCHIVO DESBLOQUEADO!             ")
    print("=" * 65)
    time.sleep(0.5)
    
    # Corazón en Arte ASCII
    print("""
         @@@@@@@   @@@@@@@      
       @@@@@@@@@@@@@@@@@@@@@    
      @@@@@@@@@@@@@@@@@@@@@@@   
      @@@@@@@@@@@@@@@@@@@@@@@   
       @@@@@@@@@@@@@@@@@@@@@    
         @@@@@@@@@@@@@@@@@      
           @@@@@@@@@@@@@        
             @@@@@@@@@          
               @@@@@            
                 @              
    """)
    
    # Tu mensaje personalizado
    print("¡Feliz primer año, amorcito! ❤️")
    print("\nSi estás leyendo esto, significa que superaste todas las pruebas")
    print("super hiper mega difíciles jiji. Gracias por")
    print("ser la felicidad de mis días. Espero te haya gustado esta sorpresita")
    print("la hice con mucho mucho muuuucho cariño!!.")
    print("\n¡El primer año de muchos más!! Te amo con toda mi alma")
    print("=" * 65)
    
    # Evita que la ventana se cierre de golpe al final
    input("\nPresiona ENTER para cerrar el sistema de seguridad...")

if __name__ == "__main__":
    caja_fuerte()