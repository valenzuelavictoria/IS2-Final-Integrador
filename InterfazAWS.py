import json
from CorporateLog import CorporateLog
from CorporateData import CorporateData

class InterfazAWS:
    def __init__(self, session_id, cpu_id):
        self.session_id = session_id
        self.cpu_id = cpu_id
        self.log_instance = CorporateLog.getInstance()
        self.data_instance = CorporateData.getInstance()

    def registrar_log(self):
        result = self.log_instance.post(self.session_id)
        return json.dumps({"resultado_registro": result})

    def consultar_datos_sede(self, session_id, cpu_id, sede_id):
        data = self.data_instance.getData(session_id, cpu_id, sede_id)
        return json.dumps({"datos_sede": data})

    def consultar_cuit(self, session_id, cpu_id, sede_id):
        cuit = self.data_instance.getCUIT(session_id, cpu_id, sede_id)
        return json.dumps({"cuit": cuit})

    def generar_id_secuencia(self, session_id, cpu_id, sede_id):
        new_seq_id = self.data_instance.getSeqID(session_id, cpu_id, sede_id)
        return json.dumps({"nuevo_id_secuencia": int(new_seq_id["idSeq"])})

    def listar_corporate_data(self):
        # Llama a listCorporateData desde CorporateData
        data = self.data_instance.listCorporateData()
        return data  # Devuelve directamente el JSON generado

    def listar_logs_por_cpu(self):
        # Llama a listCorporateLog desde CorporateData, pasando el cpu_id
        logs = self.data_instance.listCorporateLog(self.cpu_id)
        return logs  # Devuelve directamente el JSON generado

    def listar_logs(self, filtro="cpu"):
        logs = self.log_instance.list()

        if filtro == "cpu":
            return json.dumps({"logs_por_cpu": logs}, indent=4)
        elif filtro == "session":
            logs_filtrados = [log for log in logs if log["sessionid"] == self.session_id]
            return json.dumps({"logs_por_sesion": logs_filtrados}, indent=4)
        else:
            return json.dumps({"error": "Filtro no válido. Use 'cpu' o 'session'."})
