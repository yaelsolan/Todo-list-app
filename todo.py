import sqlite3
from bottle import route, run, debug, template, request, static_file

def db_connect():
    conn = sqlite3.connect('todo.db')
    print("Opened database successfully")
    return conn

def db_close(conn):
    conn.close()
    print("Close database successfully")

def handle_db(view):
    def wrapper(*args, **kwargs):
        conn = db_connect()
        cursor = conn.cursor()
        result = view(cursor, *args, **kwargs)
        conn.commit()
        db_close(conn)
        return result
    return wrapper


@route('/todo')
@handle_db
def todo_list(cursor):
    cursor.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = cursor.fetchall()
    output = template ('make_table', rows=result)
    return template('make_table', rows=result)
    
@route('/new', method='GET')
@handle_db
def new_item(cursor):

    new = request.GET.task.strip()

    cursor.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
    new_id = c.lastrowid

    return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id 
 
    if request.GET.save:

        new = request.GET.task.strip()

        cursor.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')
        
@route('/edit/<no:int>', method='GET')
@handle_db
def edit_item(cursor, no):

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        cursor.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        cursor.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = cur.fetchone()

        return template('edit_task', old=cur_data, no=no)    
        
@route('/item<item:re:[0-9]+>')
def show_item(curor, item):
    cursor.execute("SELECT task FROM todo WHERE id LIKE ?", (item,))
    result = cursor.fetchall()
    if not result:
        return 'This item number does not exist!'
    else:
        return 'Task: %s' % result[0] 
         
@route('/help')
def help():
    return static_file('help.html', root='/path/to/file')        
           
debug(True)
run(reloader=True)
