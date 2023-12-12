from http.server import BaseHTTPRequestHandler, HTTPServer
from mysql.connector import connect


def get_cities():
    conn = connect(host="localhost", user='root', password='1234', database='world')
    cursor = conn.cursor()
    query = "SELECT * FROM `city` LIMIT 25;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


class CustomHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        cities = [f'<li>{c[1]}</li>' for c in get_cities()]
        html = f'''
        <html>
            <head>
                <meta charset="utf-8">
                <title>HTTP-сервер</title>
            </head>
            <body>
                <h1>Города</h1>
                <ul>
                    {''.join(cities)}
                </ul>
            </body>
        </html>
        '''
        self.wfile.write(html.encode())


def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CustomHttpRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
