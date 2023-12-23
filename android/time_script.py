from random import randint
import time
import pymysql

class in_in:
    def test(self):
        self.db = pymysql.connect(host="localhost",user="root",password="4444",database="db" )
        for _ in range(100):
            random = randint(0, 200)
            cur = self.db.cursor()
            cur.execute('SELECT app_coins.price FROM app_coins' )
            for old in cur:
                old_price = old
            print(old_price[0])
            
            cur.execute(f"UPDATE app_coins SET old_price = {old_price[0]}")
            self.db.commit()
            cur.execute(f"UPDATE app_coins SET price = {random}")
            self.db.commit()
            time.sleep(10)
        print('stopped')

if __name__ == "__main__":
    app = in_in()
    
    app.test()



