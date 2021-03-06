CREATE TABLE IF NOT EXISTS employees (
    age SMALLINT,
    attrition BOOLEAN,
    business_travel TEXT,
    daily_rate INTEGER,
    department TEXT,
    distance_from_home INTEGER,
    education SMALLINT,
    education_field TEXT,
    employee_count SMALLINT,
    employee_number INTEGER,
    environment_satisfaction SMALLINT,
    gender TEXT,
    hourly_rate SMALLINT,
    job_involvement SMALLINT,
    job_level SMALLINT,
    job_role TEXT,
    job_satisfaction SMALLINT,
    marital_status TEXT,
    monthly_income INTEGER,
    monthly_rate INTEGER,
    num_companies_worked SMALLINT,
    over18 BOOLEAN,
    over_time BOOLEAN,
    percent_salary_hike SMALLINT,
    performance_rating SMALLINT,
    relationship_satisfaction SMALLINT,
    standard_hours SMALLINT,
    stock_option_level SMALLINT,
    total_working_years SMALLINT,
    training_times_last_year SMALLINT,
    work_life_balance SMALLINT,
    years_at_company SMALLINT,
    years_in_current_role SMALLINT,
    years_since_last_promotion SMALLINT,
    years_with_curr_manager SMALLINT,

    PRIMARY KEY (employee_number)
);