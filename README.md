# Flask Gemini Chat API

Una API REST construida con Flask que integra Google Gemini AI para crear un sistema de chat inteligente.

## Características

- 🔐 Autenticación JWT
- 🤖 Integración con Google Gemini AI
- 📝 Historial de conversaciones
- ✅ Validación de datos con Marshmallow
- 🧪 Pruebas unitarias

## Instalación

1. Clona el repositorio
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura las variables de entorno en `.env`:
```
GEMINI_API_KEY=tu_api_key_aqui
SECRET_KEY=tu_secret_key_aqui
FLASK_ENV=development
```

## Uso

### Ejecutar la aplicación
```bash
python run.py
```

### Ejecutar pruebas
```bash
python -m unittest tests.test_api
```

## API Endpoints

| Ruta | Método | Descripción | JWT Requerido |
|------|--------|-------------|---------------|
| `/auth/register` | POST | Registrar usuario | ❌ |
| `/auth/login` | POST | Iniciar sesión | ❌ |
| `/chat/send` | POST | Enviar mensaje a Gemini | ✔️ |
| `/chat/history` | GET | Obtener historial | ✔️ |

### Ejemplos de uso

#### Registro
```bash
curl -X POST http://localhost:5000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "123456"}'
```

#### Login
```bash
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "123456"}'
```

#### Enviar mensaje
```bash
curl -X POST http://localhost:5000/chat/send \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"content": "Hola, ¿cómo estás?"}'
```

## Estructura del Proyecto

```
my_flask_gemini/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py
│   │   └── chat.py
│   ├── schemas.py
│   └── utils.py
├── tests/
├── requirements.txt
├── .env
└── run.py
```