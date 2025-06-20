from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils import get_gemini_response
from app.models import ChatMessage

chat_bp = Blueprint('chat', __name__, url_prefix='/chat')

@chat_bp.route('/send', methods=['POST'])
@jwt_required()
def send_message():
    try:
        user_id = int(get_jwt_identity())
        print(f"User ID: {user_id}")
        
        data = request.get_json()
        print(f"Request data: {data}")
        
        if not data or 'content' not in data:
            print("Error: No content in request")
            return jsonify({'error': 'Content required'}), 400
        
        user_input = data['content']
        print(f"User input: {user_input}")
        
        # Guardar mensaje del usuario
        user_message = ChatMessage(user_id, 'user', user_input)
        user_message.save()
        print("User message saved")
        
        # Obtener respuesta de Gemini
        print("Calling Gemini...")
        result = get_gemini_response(user_input)
        print(f"Gemini result: {result}")
        
        if not result['success']:
            print(f"Gemini error: {result['error']}")
            return jsonify({'error': result['error']}), result.get('code', 500)
        
        # Guardar respuesta del asistente
        assistant_message = ChatMessage(user_id, 'assistant', result['response'])
        assistant_message.save()
        print("Assistant message saved")
        
        response_data = {
            'message': user_input,
            'response': result['response'],
            'timestamp': assistant_message.timestamp.isoformat()
        }
        print(f"Sending response: {response_data}")
        
        return jsonify(response_data)
    except Exception as e:
        print(f"Chat error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Chat error: {str(e)}'}), 500

@chat_bp.route('/test', methods=['POST'])
@jwt_required()
def test_jwt():
    try:
        user_id = int(get_jwt_identity())
        data = request.get_json()
        return jsonify({
            'user_id': user_id,
            'message': 'JWT funciona correctamente',
            'received_data': data
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chat_bp.route('/history', methods=['GET'])
@jwt_required()
def get_history():
    user_id = int(get_jwt_identity())
    messages = ChatMessage.get_user_history(user_id)
    
    return jsonify({
        'history': [{
            'role': msg.role,
            'content': msg.content,
            'timestamp': msg.timestamp.isoformat()
        } for msg in messages]
    })