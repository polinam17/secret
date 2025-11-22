from django.urls import path
from django.db import connection
from django.http import HttpResponse

def users_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Данные из базы данных</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                background: white;
                color: #333;
            }
            h1 {
                text-align: center;
                margin-bottom: 30px;
                font-size: 24px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }
            th, td {
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }
            th {
                background-color: #f8f9fa;
                font-weight: bold;
            }
            tr:hover {
                background-color: #f5f5f5;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
            .footer {
                text-align: center;
                margin-top: 20px;
                color: #666;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Данные из базы данных</h1>
            
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Имя</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    for user in users:
        html += f"""
                    <tr>
                        <td>{user[0]}</td>
                        <td>{user[1]}</td>
                        <td>{user[2]}</td>
                    </tr>
        """
    
    html += f"""
                </tbody>
            </table>
            
            <div class="footer">
                Всего записей: {len(users)}
            </div>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html)

urlpatterns = [
    path('', users_list),
]