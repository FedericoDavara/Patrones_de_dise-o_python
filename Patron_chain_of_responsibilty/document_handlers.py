class ApprovalHandler:
    def __init__(self, successor=None):
        self._successor = successor

    def set_successor(self, successor):
        self._successor = successor

    def process_document(self, documento):
        if self._successor:
            self._successor.process_document(documento)

class ApprovalHandler1(ApprovalHandler):
    def process_document(self, documento):
        if documento == "Documento número 1":
            print("El documento numero 1 fue aprobado por el manejador de aprobacion 1")
        else:
            super().process_document(documento)

class ApprovalHandler2(ApprovalHandler):
    def process_document(self, documento):
        if documento == "Documento número 2":
            print("El documento numero 2 fue aprobado por el manejador de aprobacion 2")
        else:
            super().process_document(documento)

class ApprovalHandler3(ApprovalHandler):
    def process_document(self, documento):
        if documento == "Documento número 3":
            print("El documento numero 3 fue aprobado por el manejador de aprobacion 3")
        else:
            print("El documento no se pudo aprobar")