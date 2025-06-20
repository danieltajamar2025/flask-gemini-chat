import bcrypt
from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    chat_messages = db.relationship('ChatMessage', backref='user', lazy=True)
    
    def __init__(self, email, password):
        self.email = email
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'user' o 'assistant'
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, user_id, role, content):
        self.user_id = user_id
        self.role = role
        self.content = content
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_user_history(user_id):
        return ChatMessage.query.filter_by(user_id=user_id).order_by(ChatMessage.timestamp.asc()).all()