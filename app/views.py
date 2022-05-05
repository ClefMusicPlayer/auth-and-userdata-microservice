from .app import app




# for heartbeat
@app.route('/keep_alive')
def keep_alive():
    return 'OK'