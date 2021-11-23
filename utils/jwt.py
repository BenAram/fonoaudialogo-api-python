import hmac
import hashlib
import base64
import json

class JWT:
    @staticmethod
    def encode(obj, secret_key):
        header = json.dumps({
            'typ': 'JWT',
            'alg': 'HS256'
        }).encode()

        payload = json.dumps(obj).encode()

        b64_header = base64.urlsafe_b64encode(header).decode()
        b64_payload = base64.urlsafe_b64encode(payload).decode()

        signature = hmac.new(
            key=secret_key.encode(), 
            msg=f'{b64_header}.{b64_payload}'.encode(),
            digestmod=hashlib.sha256
        ).digest()

        token = f'{b64_header}.{b64_payload}.{base64.urlsafe_b64encode(signature).decode()}'
        return token

    def decode(jwt, secret_key):
        b64_header, b64_payload, b64_signature = jwt.split('.')
        b64_signature_checker = base64.urlsafe_b64encode(
            hmac.new(
                key=secret_key.encode(),
                msg=f'{b64_header}.{b64_payload}'.encode(),
                digestmod=hashlib.sha256
            ).digest()
        ).decode()

        payload = json.loads(base64.urlsafe_b64decode(b64_payload))
        
        if b64_signature_checker != b64_signature:
            raise Exception('Assinatura inválida')
        
        return payload