import logging
import time

import fonlaboristo
from flask import jsonify, Flask, request
from fonlaboristo.job import Job

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
f = fonlaboristo.Queue()


@f.task()
def my_task(wait_time):
    print(f'executing tasks with parameters {wait_time}')
    time.sleep(wait_time)
    return wait_time


@app.route('/task/', methods=['POST'])
def run_task():
    job = my_task(int(request.json['wait_time']))  # returns a job object containing the status of the job, instead of executing my_task directly
    return jsonify({
        'job': job.id,
        'state': job.state,
    })


@app.route('/task/<job_id>')
def get_task(job_id):
    job = Job(job_id)
    return jsonify({
        'job': job.id,
        'state': job.state,
        'result': job.result,
    })
