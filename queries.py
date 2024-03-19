def query1() -> str:
    return (
        "SELECT STUDENT_POPULATION_CODE_REF AS NAME, STUDENT_POPULATION_PERIOD_REF AS PERIOD, STUDENT_POPULATION_YEAR_REF AS DATE, COUNT(*) AS CNT FROM STUDENTS "
        "GROUP BY NAME, DATE, PERIOD")


def query2() -> str:
    return (
        "SELECT STUDENT_POPULATION_CODE_REF AS NAME, STUDENT_POPULATION_PERIOD_REF AS PERIOD, STUDENT_POPULATION_YEAR_REF AS DATE, 100 * SUM(ATTENDANCE_PRESENCE) / COUNT(*) FROM ATTENDANCE "
        "INNER JOIN STUDENTS ON STUDENTS.STUDENT_EPITA_EMAIL = ATTENDANCE.ATTENDANCE_STUDENT_REF "
        "GROUP BY NAME, PERIOD "
        "ORDER BY NAME")


def query3(name, year, period) -> str:
    return (
        "SELECT EMAIL, FIRST_NAME, LAST_NAME, COUNT(case when S >= 10 then 1 end) AS VAL, COUNT(*) AS TOTAL FROM "
        "(SELECT DISTINCT STUDENT_EPITA_EMAIL AS EMAIL, CONTACT_FIRST_NAME AS FIRST_NAME, CONTACT_LAST_NAME AS LAST_NAME, GRADE_COURSE_CODE_REF, SUM(GRADE_SCORE) / COUNT(*) AS S FROM STUDENTS "
        "INNER JOIN CONTACTS ON STUDENTS.STUDENT_CONTACT_REF = CONTACTS.CONTACT_EMAIL "
        "INNER JOIN GRADES ON STUDENTS.STUDENT_EPITA_EMAIL = GRADES.GRADE_STUDENT_EPITA_EMAIL_REF "
        "WHERE STUDENT_POPULATION_CODE_REF = '" + name + "' AND STUDENT_POPULATION_YEAR_REF = " + year + " AND STUDENT_POPULATION_PERIOD_REF = '" + period + "' "
                                                                                                                                                             "GROUP BY EMAIL, GRADE_COURSE_CODE_REF "
                                                                                                                                                             "ORDER BY EMAIL) "
                                                                                                                                                             "GROUP BY EMAIL")


def query4(name, year, period) -> str:
    return (
        "SELECT DISTINCT ATTENDANCE_COURSE_REF AS CODE, COURSE_NAME AS COURSE, COUNT(*) / 2 AS VAL FROM ATTENDANCE "
        "INNER JOIN COURSES ON COURSES.COURSE_CODE = ATTENDANCE_COURSE_REF  "
        "INNER JOIN STUDENTS ON STUDENTS.STUDENT_EPITA_EMAIL = ATTENDANCE_STUDENT_REF "
        "WHERE STUDENT_POPULATION_CODE_REF = '" + name + "' AND STUDENT_POPULATION_PERIOD_REF = '" + period + "' AND STUDENT_POPULATION_YEAR_REF = " + year + " "
                                                                                                                                                              "GROUP BY ATTENDANCE_STUDENT_REF, CODE "
                                                                                                                                                              "ORDER BY CODE")


def query5(name, year, period) -> str:
    return (
        "SELECT GRADE_STUDENT_EPITA_EMAIL_REF AS EMAIL, CONTACT_FIRST_NAME AS FIRST_NAME, CONTACT_LAST_NAME AS LAST_NAME, COURSE_NAME, SUM(GRADE_SCORE) / COUNT(*) AS AVG FROM GRADES "
        "INNER JOIN STUDENTS ON GRADE_STUDENT_EPITA_EMAIL_REF = STUDENTS.STUDENT_EPITA_EMAIL "
        "INNER JOIN COURSES ON GRADE_COURSE_CODE_REF = COURSES.COURSE_CODE "
        "INNER JOIN CONTACTS ON STUDENT_CONTACT_REF = CONTACTS.CONTACT_EMAIL "
        "WHERE STUDENT_POPULATION_PERIOD_REF = '" + period + "' AND STUDENT_POPULATION_YEAR_REF = " + year + " AND STUDENT_POPULATION_CODE_REF = '" + name + "' "
                                                                                                                                                             "GROUP BY EMAIL, COURSE_NAME "
                                                                                                                                                             "ORDER BY EMAIL")
