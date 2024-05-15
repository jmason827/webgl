from flask import Flask, jsonify, request
from flask_cors import CORS # Import the extension

# sys.path.append('D:\docs\jdm\py')
# import mgudb_jdm as db  # Import assuming 'my_module.py'

app = Flask(__name__)
CORS(app)

@app.route('/get-tblfinal-records')
def get_tblfinal_records(org='G1'):
	process = request.args.get('process')
	cell = request.args.get('cell')
	sysn = request.args.get('sysn')
	bay = request.args.get('bay')
	print(process, cell, sysn, bay)
	where_clause = f"""WHERE tf.tDateTime
	BETWEEN cast('2024-03-05' as datetime) at time zone 'Central Standard Time'
	AND cast('2024-03-06' as datetime) at time zone 'Central Standard Time'
	AND tf.Station LIKE '%G1%%FCT%'
	AND tf.result = 0"""
	dbrows = db.get_records_given_where_clause(where_clause, org, order='desc')
	dbrows = db.get_mgu22_fail_item_names(dbrows, org)
	return jsonify(dbrows.rows)

def main():
	pass

if __name__ == '__main__':
	main()
