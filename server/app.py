#!/usr/bin/env python3
from queries import get_attrition, get_percentage_of_attrition_that_worked_overtime, insert_row
from flask import Flask, jsonify, request
import psycopg2
import os


app = Flask(__name__)


connection = psycopg2.connect(
    host=os.getenv('POSTGRES_HOST'),
    port=os.getenv('POSTGRES_PORT'),
    database=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'))

cursor = connection.cursor()


# Healthcheck endpoint
@app.route('/readyz')
def readyz():
    return 'Server is ready! Beep boop beep!', 200

@app.route('/attrition')
def attrition():
    return jsonify({ 'attrition': get_attrition(cursor) }), 200

@app.route('/attrition-overtime')
def attrition_overtime():
    return jsonify({
        'attrition-overtime': get_percentage_of_attrition_that_worked_overtime(cursor)
    }), 200

@app.route('/add-row', methods=['POST'])
def add_row():
    body = request.get_json()

    try:
        insert_row(cursor,
                   body['employeeNumber'],
                   body['attrition'])

        return jsonify({
            'employeeNumber': body['employeeNumber'],
            'attrition': body['attrition']
        }), 200
    except:
        # In production, should log this error also
        connection.rollback()
        return jsonify({
            'reason': f"Error inserting employee {body['employeeNumber']}",
        }), 400
