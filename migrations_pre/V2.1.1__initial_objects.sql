

CREATE OR REPLACE SCHEMA DATA.REPORT;

CREATE OR REPLACE TABLE DATA.REPORT.REPORT_DATA AS (SELECT PASSENGERID ,PCLASS, NAME, SEX, AGE, SIBSP, PARCH,FARE, EMARKED FROM DATA.RAW.TITANIC_TRAIN_RAW);