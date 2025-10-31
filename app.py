from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class Calculadora(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def Sumar(ctx, a, b):
        return a + b

# Application (contrato SOAP)
application = Application(
    [Calculadora],
    tns='urn:calculadora',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# WSGI app que sirve SOAP + ?wsdl
app = WsgiApplication(application)

# Soporte para ejecución local opcional (no requerido por Render)
if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server("0.0.0.0", 8000, app)
    print("Local: http://127.0.0.1:8000  (WSDL en /?wsdl)")
    server.serve_forever()
