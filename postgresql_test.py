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


# try:
#     cur = conn.cursor()
#     table_name="table_customers"
#     sql =f"SELECT * FROM {table_name}"
#     cur.execute(sql)
#     rows=cur.fetchall()
#     for row in rows:
#         print(f"{list(enumerate(row))}")
# except psycopg2.Error as e:
#     print(e)


try:
    cur = conn.cursor()
    sql =f"SELECT tablename FROM pg_tables WHERE tablename NOT LIKE 'pg%' AND tablename NOT LIKE 'sql_%' ORDER BY tablename"
    cur.execute(sql)
    rows=cur.fetchall()
    for row in rows:
        print(f"{str(row[0])}")
except psycopg2.Error as e:
    print(e)

