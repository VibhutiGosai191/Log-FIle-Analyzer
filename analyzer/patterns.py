import re

PATTERNS = {
    "FAILED_LOGIN": re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"),
    "SUCCESS_LOGIN": re.compile(r"Accepted password for .* from (\d+\.\d+\.\d+\.\d+)"),
    "INVALID_USER": re.compile(r"Invalid user .* from (\d+\.\d+\.\d+\.\d+)"),
    "PORT_SCAN": re.compile(r"scan from (\d+\.\d+\.\d+\.\d+)"),
    "SQL_INJECTION": re.compile(r"(UNION SELECT|SELECT \* FROM|DROP TABLE)", re.IGNORECASE),
}