#!/usr/bin/python
import psycopg2
import random,string
import os

os.system('systemctl restart postgresql-{{postgresql_ver}}')

new_password = ''.join(random.sample(string.ascii_letters + string.digits, 8))

with open('/credentials/password.txt','r') as f:
  old_password = f.read().split(':')[2].replace('\n','')

conn = psycopg2.connect(user="postgres", password=old_password, host="127.0.0.1", port="5432")
cursor=conn.cursor()
cursor.execute("ALTER USER postgres WITH PASSWORD '%s';"%(new_password))
cursor.execute("ALTER USER awx WITH PASSWORD '%s';"%(new_password))
conn.commit()
conn.close()

with open('/credentials/password.txt','w') as f:
  f.write('''postgresql username:postgres
  postgresql password:{0}

  ---For AWX ---
  database name: awx
  database username: awx
  database password: {0}
  '''.format(new_password))

with open("/etc/rc.local","r") as f:
  lines = f.readlines()
with open("/etc/rc.local","w") as f_w:
  for line in lines:
    if "/root/init.py" in line:
      continue
    f_w.write(line)

os.remove('/root/init.py')