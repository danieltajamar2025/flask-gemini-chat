# 🚀 Flask Gemini Chat - Proyecto Entregable

## 📋 Información del Proyecto
- **Nombre**: Flask Gemini Chat API
- **Tecnologías**: Flask, SQLAlchemy, JWT, Google Gemini AI
- **Base de datos**: SQLite
- **Frontend**: HTML, CSS, JavaScript

## 🛠️ Instalación y Ejecución

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Configurar variables de entorno
Editar el archivo `.env`:
```
GEMINI_API_KEY=tu_api_key_aqui
SECRET_KEY=tu_secret_key_aqui
```

### 3. Inicializar base de datos
```bash
python init_db.py
```

### 4. Ejecutar aplicación
```bash
python run.py
```

### 5. Acceder a la aplicación
Abrir navegador en: `http://localhost:5000`

## 🧪 Ejecutar Tests
```bash
python -m unittest tests.test_api -v
```

## 📁 Estructura del Proyecto
```
my_flask_gemini/
├── app/
│   ├── routes/          # Rutas de la API
│   ├── static/          # CSS y JavaScript
│   ├── templates/       # HTML
│   ├── __init__.py      # Configuración Flask
│   ├── config.py        # Configuración
│   ├── models.py        # Modelos SQLAlchemy
│   ├── schemas.py       # Validación
│   └── utils.py         # Utilidades Gemini
├── tests/               # Pruebas unitarias
├── requirements.txt     # Dependencias
├── .env                # Variables de entorno
├── run.py              # Punto de entrada
└── README.md           # Documentación
```

## ✅ Funcionalidades Implementadas
- [x] Autenticación JWT (registro/login)
- [x] Integración con Google Gemini AI
- [x] Historial de conversaciones persistente
- [x] Interfaz web responsive
- [x] Validación de datos
- [x] Manejo de errores
- [x] Pruebas unitarias
- [x] Documentación completa

## 🔗 API Endpoints
| Endpoint | Método | Descripción | Auth |
|----------|--------|-------------|------|
| `/auth/register` | POST | Registro de usuario | ❌ |
| `/auth/login` | POST | Inicio de sesión | ❌ |
| `/chat/send` | POST | Enviar mensaje a Gemini | ✅ |
| `/chat/history` | GET | Obtener historial | ✅ |

## 👤 Usuario de Prueba
- Email: test@example.com
- Password: 123456

## 📝 Notas Importantes
- Requiere API Key válida de Google Gemini
- Base de datos SQLite se crea automáticamente
- Tokens JWT válidos por 24 horas