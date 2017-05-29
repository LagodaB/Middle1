import csv
import re
import sqlite3

def write_csv(email, count, date):
    with open('test.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((email, count, date))

def email(data):
    data_set = []
    all_pattern = re.compile('^From ([\w\.]+@[\w\.]+) [A-Z][a-z]{2}\s([A-Z][a-z]{2})', re.M)
    emails_pattern = re.compile('^From ([\w\.]+@[\w\.]+) [A-Z][a-z]{2}\s[A-Z][a-z]{2}', re.M)
    data_all = all_pattern.findall(data)
    emails = emails_pattern.findall(data)
    lats_date_all = {email:date for email,date in data_all}
    write_csv('email', 'count', 'date')

    for i in set(emails):
        #print i, emails.count(i), lats_date_all[i]
        write_csv(i, emails.count(i), lats_date_all[i])
        data_set.append((i, emails.count(i), lats_date_all[i]))
    return data_set

if __name__ == "__main__":
    data = open('mbox.txt', 'rU').read()
    up = email(data)
    print 'up', up

    conn = sqlite3.connect('mod4.sqlite')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS DATA")
    cur.execute("CREATE TABLE DATA (email TEXT, count INTEGER, date TEXT)")
    for email, count, date in up:
        cur.execute("INSERT INTO DATA (email,date,count) VALUES (?,?,?)",(email,date,count))
        
   
    conn.commit()
    sqlstr = 'SELECT email, count, date FROM DATA Order BY date, count DESC, DATA.date, DATA.count'

    for row in cur.execute(sqlstr) :
        print row

    cur.close()
   
    conn.close()



