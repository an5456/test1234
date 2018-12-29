import pymysql
import json


class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",
                                    port=3306,
                                    user="root",
                                    passwd="test123456",
                                    db="test",
                                    charset="utf8"
                                    )
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 查询一条数据
    def serch_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        res = json.dumps(result)
        return res


if __name__ == '__main__':
    op_sql = OperationMysql()
    op = op_sql.serch_one("select * from test1 where sex='nan'")
    print(type(op))
    print(op)