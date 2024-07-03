from http.server import BaseHTTPRequestHandler, HTTPServer
from mysql.connector import connect


def get_data(table):
    """Получение данных из СУБД MySQL"""
    conn = connect(host="localhost", user='root', password='sanasuol', database='world')
    cursor = conn.cursor()
    query = f"SELECT * FROM `{table}` LIMIT 25;"  # читаем 25 строк из таблицы
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


class CustomHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        """Отправка веб-страницы"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        rivers = [f'<li>{c[1]}</li>' for c in get_data('river')]
        cities = [f'<li>{c[1]}</li>' for c in get_data('city')]
        html = f'''
        <html>
            <head>
                <meta charset="utf-8">
                <title>HTTP-сервер</title>
            </head>
            <body>
                <h1>Реки</h1>
                <ul>
                    {''.join(rivers)}
                </ul>
                <h1>Города</h1>
                <ul>
                    {''.join(cities)}
                </ul>
            </body>
        </html>
        '''
        self.wfile.write(html.encode())


def run_server():
    """Запуск веб-сервера"""
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CustomHttpRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
