import boto3
import json
import uuid
from InterfazAWS import InterfazAWS

def listar_logs_por_cpu():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CorporateLog')
    cpu_id = str(uuid.getnode()) 

    try:
        response = table.scan(
            FilterExpression="CPUid = :CPUid",
            ExpressionAttributeValues={":CPUid": cpu_id}
        )
        logs = response.get('Items', [])
        return json.dumps({"logs_por_cpu": logs}, indent=4)
    except Exception as e:
        return json.dumps({"error": f"Error al acceder a la base de datos: {e}"})

if _name_ == "_main_":

    config_data = {
        "session_id": str(uuid.uuid4()),
        "cpu_id": str(uuid.getnode()),
        "id": "UADER-FCyT-IS2",
    }

    i3 = InterfazAWS(config_data["session_id"], config_data["cpu_id"])

    print('Registrando log:', i3.registrar_log())

    print(listar_logs_por_cpu())