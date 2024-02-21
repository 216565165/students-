import pymysql
db = pymysql.connect(host='localhost',
                     user='root',
                     password='15013227986',
                     database='py01')
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS student01")
sql="""
CREATE TABLE student01(
id int(8) NOT NULL AUTO_INCREMENT,
name varchar(255) NOT NULL,
category varchar(50) NOT NULL ,
PRIMARY KEY (id)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8"""
cursor.execute(sql)
db.close()