import boto3
import json
import uuid

# Producirá un listado de todas las entradas contenidas en la tabla
# CorporateLog para una clave de CPU determinada.

def listar_logs_por_cpu():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CorporateLog')
    cpu_id = str(uuid.getnode())  # ID CPU ACTUAL

    try:
        response = table.scan(
            FilterExpression="CPUid = :CPUid",
            ExpressionAttributeValues={":CPUid": cpu_id}
        )
        logs = response.get('Items', [])
        return json.dumps({"logs_por_cpu": logs}, indent=4)
    except Exception as e:
        return json.dumps({"error": f"Error al acceder a la base de datos: {e}"})

if __name__ == "__main__":
    print(listar_logs_por_cpu())
