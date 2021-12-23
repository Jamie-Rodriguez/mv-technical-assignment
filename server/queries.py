#!/usr/bin/env python3
import psycopg2 # Only used for typehints


def get_attrition(cursor: psycopg2.extensions.cursor) -> float:
    cursor.execute("""
        SELECT COUNT(*) FILTER (WHERE attrition) ::FLOAT / COUNT(*)
        FROM employees;
        """)
    return cursor.fetchall()[0][0]

def get_percentage_of_attrition_that_worked_overtime(cursor: psycopg2.extensions.cursor) -> float:
    cursor.execute("""
        SELECT COUNT(*) FILTER (WHERE over_time) ::FLOAT / COUNT(*)
        FROM employees
        WHERE attrition;
        """)
    return cursor.fetchall()[0][0]

def insert_row(cursor: psycopg2.extensions.cursor, employee_number: int, attrition: bool) -> None:
    cursor.execute("""
        INSERT INTO employees (employee_number, attrition)
        VALUES (%s, %s)
        RETURNING employee_number;
        """,
        (employee_number, attrition))
