import json
import datetime
import hmac
import hashlib

SECRET_KEY = b'!@uhewfnlk'
EXPIRATION_WINDOW_MINUTES = 5

def generate_signature(message, secret):
    return hmac.new(secret, message.encode('utf-8'), hashlib.sha256).hexdigest()

def is_signature_expired(timestamp_str, current_time=None):
    request_time = datetime.datetime.strptime(timestamp_str, '%Y%m%dT%H%M%SZ')
    current_time = current_time or datetime.datetime.utcnow()
    time_diff = current_time - request_time
    expired = time_diff > datetime.timedelta(minutes=EXPIRATION_WINDOW_MINUTES)
    return expired

def lambda_handler(event, context):
    results = []
    
    if isinstance(event, list):
        for test_case in event:
            description = test_case.get('description', 'No description')
            payload = test_case.get('payload', 'default_payload')
            timestamp_str = test_case.get('timestamp', '')
            current_time_str = test_case.get('current_time', '')
            expected_expired = test_case.get('expected_expired', False)
            
            timestamp = datetime.datetime.strptime(timestamp_str, '%Y%m%dT%H%M%SZ')
            current_time = datetime.datetime.strptime(current_time_str, '%Y%m%dT%H%M%SZ')
            
            message = f"{payload}|{timestamp_str}"
            signature = generate_signature(message, SECRET_KEY)
            
            expired = is_signature_expired(timestamp_str, current_time)
            
            result = {
                'description': description,
                'payload': payload,
                'timestamp': timestamp_str,
                'signature': signature,
                'expected_expired': expected_expired,
                'expired': expired,
                'message': '✅ Signature is valid.' if not expired else '❌ Signature expired.',
                'test_passed': expected_expired == expired
            }
            
            results.append(result)
    
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'Invalid input format, expected a list of test cases.'
            })
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }
