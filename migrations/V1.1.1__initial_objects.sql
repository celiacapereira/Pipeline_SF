CREATE OR REPLACE SCHEMA PRE.REPORT;
CREATE OR REPLACE TABLE PRE.REPORT.REPORT_DATA AS (SELECT PASSENGERID ,PCLASS, NAME, SEX, AGE, SIBSP, PARCH,FARE, EMARKED FROM PRE.RAW.TITANIC_TRAIN_RAW );
