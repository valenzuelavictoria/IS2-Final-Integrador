import uuid
from InterfazAWS import InterfazAWS
import logging

# Configuración de logging para errores críticos.
logging.basicConfig(level=logging.ERROR)

def main():
    # Datos para consultas
    config_data = {
        "session_id": str(uuid.uuid4()),
        "cpu_id": str(uuid.getnode()),
        "id": "UADER-FCyT-IS2",
    }

    # Crear instancia de InterfazAWS

    interfaz = InterfazAWS(config_data["session_id"], config_data["cpu_id"])

    # Verificacion de implementacion de singleton
    i2 = InterfazAWS(config_data["session_id"], config_data["cpu_id"])

    if interfaz == i2:
        print('iguales')
    else:
        print('diferentes')


    # Consultar datos de la sede en CorporateData
    print("\nConsultando datos de la sede")
    print(interfaz.consultar_datos_sede(config_data["session_id"], config_data["cpu_id"], config_data["id"]))

    # # Consultar CUIT de la sede en CorporateData
    print("\nConsultando el CUIT de la sede")
    print(interfaz.consultar_cuit(config_data["session_id"], config_data["cpu_id"], config_data["id"]))

    # Generar un nuevo ID de secuencia en CorporateData
    print("\nGenerando ID de secuencia")
    print(interfaz.generar_id_secuencia(config_data["session_id"], config_data["cpu_id"], config_data["id"]))

    # Listar todos los datos en CorporateData
    print("\nListando datos de CorporateData")
    print(interfaz.listar_corporate_data())

    # Registrar log en CorporateLog
    print("\nRegistrando acción")
    print(interfaz.registrar_log())

    # Listar logs por CPU en CorporateLog
    print("\nListando logs asociados al CPU")
    print(interfaz.listar_logs_por_cpu())

    if _name_ == "_main_":
        main()