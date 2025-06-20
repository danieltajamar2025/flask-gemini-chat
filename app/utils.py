import google.generativeai as genai
from flask import current_app
import requests
from requests.exceptions import Timeout, RequestException

def get_gemini_response(user_input, timeout=30):
    try:
        genai.configure(api_key=current_app.config['GEMINI_API_KEY'])
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(user_input)
        
        # Verificar si la respuesta tiene contenido
        if hasattr(response, 'text') and response.text:
            return {'success': True, 'response': response.text}
        elif hasattr(response, 'candidates') and response.candidates:
            # Intentar obtener el texto del primer candidato
            candidate = response.candidates[0]
            if hasattr(candidate, 'content') and candidate.content:
                return {'success': True, 'response': candidate.content.parts[0].text}
        
        return {'success': False, 'error': 'No se pudo obtener respuesta de Gemini', 'code': 500}
        
    except Exception as e:
        error_msg = str(e)
        if 'quota' in error_msg.lower():
            return {'success': False, 'error': 'Límite de API alcanzado', 'code': 429}
        elif 'api_key' in error_msg.lower():
            return {'success': False, 'error': 'API Key inválida', 'code': 401}
        else:
            return {'success': False, 'error': f'Error: {error_msg}', 'code': 500}