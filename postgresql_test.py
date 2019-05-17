import psycopg2
try:
    host_ip = "192.168.17.146"
    user = "postgres"
    password = "postgres"
    database = "testDB"
    conn = psycopg2.connect(
        host=f"{host_ip}", user=f"{user}", password=f"{password}", database=f"{database}")
    print(f"连接{database}数据库成功")
except psycopg2.Error as e:
    print(e)


try:
    cur = conn.cursor()
    sql = "SELECT * FROM customers"
    cur.execute(sql)
    rows=cur.fetchall()
    for row in rows:
        print(f"{list(enumerate(row))}")
except psycopg2.Error as e:
    print(e)
