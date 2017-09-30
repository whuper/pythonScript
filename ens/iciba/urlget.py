# -*- coding: utf-8 -*-

import os
import urllib2
import sqlite3
class Crawler:
  def main(self):

    folder_size = 500

    conn = sqlite3.connect('D:/nodejs/electron/electron-ui-route/assets/wenhaotest.db')
    cursor = conn.cursor()
    #result = cursor.execute("SELECT id,words from english LIMIT 1500 OFFSET 4000")
    #result = cursor.execute("SELECT id,words from dict where id > 419")
    result = cursor.execute("SELECT id,words from dict where id in (433,452,1672,1800,2050,2322,2563,2810,3557,5247,5356,5574,5666,5676,5942,6319,7167,7394,7697,7718,7804,8164,8676,8791,8808,9114,9124,9315,9339,10707,10882,10928,11101,11629,11937,11938,11939,11940,11941,11942,11943,11944,11945,11946,11947,11948,11949,11950,11951,11952,11953,11954,11955,11956,11957,11958,11959,11960,11961,11962,11963,11964,11965,11966,11967,11968,11969,11970,11971,11972,11973,11974,11975,11976,11977,11978,11979,11980,11981,11982,11983,11984,11985,11986,11987,11988,11989,11990,11991,11992,11993,11994,11995,11996,11997,11998,11999,12000,12001,12002,12003,12004,12005,12006,12007,12008,12009,12010,12011,12012,12013,12014,12015,12016,12017,12018,12019,12020,12021,12022,12023,12024,12025,12026,12027,12028,12029,12030,12031,12032,12033,12034,12035,12036,12037,12038,12039,12040,12041,12042,12043,12044,12045,12046,12047,12048,12049,12050,12051,12052,12053,12054,12055,12056,12057,12058,12059,12060,12061,12062,12063,12064,12065,12066,12067,12068,12069,12070,12071,12072,12073,12074,12075,12076,12077,12078,12079,12080,12081,12334,12844,12889,12893,13035,13080,13235,13483,13488,13512,13581,13978,14225,14236,14551,14824,15008,15055,15177,15200,15240,15303)")
    wordlist = result.fetchall()
    cursor.close()
    conn.close()
    for row in wordlist:
        word_id = row[0]
        word = row[1].strip()
     
        req = urllib2.Request('http://dict.youdao.com/dictvoice?audio=' + word + '&type=2')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0)')

        urllib2.socket.setdefaulttimeout(10) # 超时10秒
        try:
            response = urllib2.urlopen(req)
            #获取文件流
            data = response.read()
        except:
            file_object = open('log.txt', 'a')
            file_object.write(word + '###' + str(word_id))
            file_object.close()
        else:
            print(word + '###' + str(word_id))

        
       
        #根据id大小来放进相应的文件夹
        folder_name = 'within_' + str( ( int( (word_id - 1) / folder_size) + 1) * folder_size )
        save_path = './audios_15328/' + folder_name

        # 如果不存在,创建目录
        if not os.path.exists(save_path):
           os.mkdir(save_path)

        #写入文件
        with open(save_path + '/' + word + '.mp3','wb') as bitfile:
            bitfile.write(data)  
            bitfile.close()

if __name__ == '__main__':
  me=Crawler()
  me.main()
