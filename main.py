#! /usr/bin/env python

import sys
import sqlite3
import task

def get_kargs():
    '''
    prog arg1 arg2 -key1 karg1 -key2 karg2
    '''
    args = []
    kargs = {}
    keys = []

    for i, s in enumerate(sys.argv[1:]):
        print(s)
        if s.startswith('-'):
            key = s.strip('-')
            keys.append(key)
            kargs[key] = []
        else:
            if len(keys) == 0:
                args.append(s)
            else:
                key = keys[-1]                
                kargs[key].append(s)

    return (args, kargs)


def get_dbfile():
    return 'test.db'


def create_table(conn, tableName, schema):        
    sql = 'CREATE TABLE {tab} ({sm})'.format(tab=tableName, sm= schema)
    c = conn.cursor()
    c.execute(sql)


def test():
    args, kargs = get_kargs()
    print(args, kargs)

def mainloop():
    conn = sqlite3.connect(get_dbfile())

    # create all tables
    create_table(conn, 'task', task.Task.schema)


    # close
    conn.commit()
    conn.close()




if __name__ == '__main__':
    #test()
    mainloop()
    


            
