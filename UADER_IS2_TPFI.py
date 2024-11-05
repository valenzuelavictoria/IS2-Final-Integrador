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

    # Consultar datos de la sede en CorporateData
    print("\nConsulta de datos de la sede")
    print(interfaz.consultar_datos_sede(config_data["session_id"], config_data["cpu_id"], config_data["id"]))

    # Consultar CUIT de la sede en CorporateData
    print("\nConsultando el CUIT de la sede")
    print(interfaz.consultar_cuit(config_data["session_id"], config_data["cpu_id"], config_data["id"]))

    # Generar un nuevo ID de secuencia en CorporateData
    print("\nGenerando un nuevo ID de secuencia")
    print(interfaz.generar_id_secuencia(config_data["session_id"], config_data["cpu_id"], config_data["id"]))

    # Listar todos los datos en CorporateData
    print("\nListando todos los datos")
    print(interfaz.listar_corporate_data())

    # Registrar log en CorporateLog
    print("\nRegistrando acción")
    print(interfaz.registrar_log())

    # Listar logs por CPU en CorporateLog
    print("\nListando logs asociados al CPU")
    print(interfaz.listar_logs_por_cpu())

if __name__ == "__main__":
    main()
