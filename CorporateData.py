import boto3
from botocore.exceptions import BotoCoreError, ClientError
import logging
import json
from decimal import Decimal
from SingletonMeta import SingletonMeta

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

class CorporateData(metaclass=SingletonMeta):
    """Clase que maneja los datos corporativos con implementación Singleton."""
    
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('CorporateData')
    
    @staticmethod
    def getInstance():
        """Método estático para obtener la instancia única de CorporateData."""
        return CorporateData()

    def getData(self, uuid, uuidCPU, id):
        logging.debug(f"getData: Buscando datos para ID de sede {id} con session ID {uuid} y CPU ID {uuidCPU}")
        try:
            response = self.table.get_item(Key={'id': id})
            if 'Item' in response:
                return {
                    "ID": response['Item'].get("id"),
                    "Domicilio": response['Item'].get("domicilio"),
                    "Localidad": response['Item'].get("localidad"),
                    "CodigoPostal": response['Item'].get("cp"),
                    "Provincia": response['Item'].get("provincia")
                }
            else:
                return {"error": "Registro no encontrado"}
        except Exception as e:
            logging.error(f"Error en getData: {e}")
            return {"error": f"Error al acceder a la base de datos: {e}"}

    def getCUIT(self, uuid, uuidCPU, id):
        try:
            response = self.table.get_item(Key={'id': id})
            if 'Item' in response:
                return {"CUIT": response['Item'].get("CUIT")}
            else:
                return {"error": "Registro no encontrado"}
        except (BotoCoreError, ClientError) as error:
            return {"error": f"Error al acceder a la base de datos: {error}"}

    def getSeqID(self, uuid, uuidCPU, id):
        try:
            response = self.table.get_item(Key={'id': id})
            if 'Item' in response:
                idSeq = response['Item'].get("idreq", 0) + 1
                self.table.update_item(
                    Key={'id': id},
                    UpdateExpression="set idreq = :val",
                    ExpressionAttributeValues={':val': idSeq}
                )
                return {"idSeq": idSeq}
            else:
                return {"error": "Registro no encontrado"}
        except (BotoCoreError, ClientError) as error:
            return {"error": f"Error al acceder a la base de datos: {error}"}
    
    def listCorporateData(self):
        """Listar todos los datos de CorporateData."""
        try:
            response = self.table.scan()
            data = response.get('Items', [])
            return json.dumps({"corporate_data": data}, indent=4, default=decimal_default)
        except Exception as e:
            logging.error(f"Error en listCorporateData: {e}")
            return {"error": f"Error al acceder a la base de datos: {e}"}
    
    def listCorporateLog(self, cpu_id):
        """Listar todos los logs en CorporateLog asociados a un CPU específico."""
        try:
            log_table = self.dynamodb.Table('CorporateLog')
            response = log_table.scan(
                FilterExpression="CPUid = :CPUid",
                ExpressionAttributeValues={":CPUid": cpu_id}
            )
            logs = response.get('Items', [])
            return json.dumps({"logs_por_cpu": logs}, indent=4, default=decimal_default)
        except Exception as e:
            logging.error(f"Error en listCorporateLog: {e}")
            return {"error": f"Error al acceder a la base de datos: {e}"}
