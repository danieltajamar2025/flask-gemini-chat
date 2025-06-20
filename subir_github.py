import os
import subprocess

def ejecutar_comando(comando):
    try:
        result = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(f"$ {comando}")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"Error: {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"Error ejecutando comando: {e}")
        return False

def subir_a_github():
    print("=== SUBIENDO PROYECTO A GITHUB ===\n")
    
    # 1. Inicializar git
    print("1. Inicializando repositorio Git...")
    if not ejecutar_comando("git init"):
        return False
    
    # 2. Agregar archivos
    print("\n2. Agregando archivos...")
    if not ejecutar_comando("git add ."):
        return False
    
    # 3. Primer commit
    print("\n3. Creando commit inicial...")
    if not ejecutar_comando('git commit -m "Proyecto Flask Gemini Chat completo"'):
        return False
    
    # 4. Configurar rama principal
    print("\n4. Configurando rama principal...")
    ejecutar_comando("git branch -M main")
    
    print("\n=== PASOS SIGUIENTES ===")
    print("1. Ve a https://github.com y crea un nuevo repositorio")
    print("2. Nombra el repositorio: flask-gemini-chat")
    print("3. NO inicialices con README (ya tienes uno)")
    print("4. Copia la URL del repositorio")
    print("5. Ejecuta estos comandos:")
    print("   git remote add origin https://github.com/TU-USUARIO/flask-gemini-chat.git")
    print("   git push -u origin main")
    
    return True

if __name__ == "__main__":
    subir_a_github()