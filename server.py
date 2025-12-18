from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse

class MiServidor(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/enviar':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')

            datos = urllib.parse.parse_qs(post_data)
            
            nombre = datos.get('nombre', [''])[0]
            email = datos.get('email', [''])[0]
            asunto = datos.get('asunto', [''])[0]
            mensaje = datos.get('mensaje', [''])[0]

            print("")
            print(f"NUEVO MENSAJE RECIBIDO:")
            print(f"De: {nombre} ({email})")
            print(f"Asunto: {asunto}")
            print(f"Mensaje: {mensaje}")
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            html_respuesta = f"""
            <html>
            <body style="background: #000; color: #fff; font-family: sans-serif; text-align: center; padding-top: 100px;">
                <h1 style="color: #ffb300;">¡Mensaje Recibido! 🚀</h1>
                <p>Gracias <strong>{nombre}</strong>, he recibido tu mensaje sobre "<em>{asunto}</em>".</p>
                <p>Te responderé pronto a {email}.</p>
                <br>
                <a href="/Laboratorio-IDWEB-F/home.html" style="color: #fff; border: 1px solid #ffb300; padding: 10px 20px; text-decoration: none; border-radius: 20px;">Volver al inicio</a>
            </body>
            </html>
            """
            self.wfile.write(html_respuesta.encode('utf-8'))
        else:
            self.send_error(404, "Ruta no encontrada")

# Iniciar servidor
print("Servidor corriendo en http://localhost:8000/Laboratorio-IDWEB-F/home.html")
HTTPServer(('localhost', 8000), MiServidor).serve_forever()