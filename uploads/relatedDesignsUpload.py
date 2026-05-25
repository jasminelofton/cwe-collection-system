import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db import *

related_design_list = """
access control, algorithmic complexity, api errors, attack surface reduction, audit, authentication, authentication errors, authorize actors, automated dynamic analysis, automated static analysis, automatic memory management, bad coding practices, black box method, build hardening, c secure coding standards, cache encryption, code quality, coding standards, compilation hardening, control flow, control flow management, cross-site scripting, cryptography, data authenticity, data type casting, data validation, data verification, dead code, default error pages, documentation, ejb guidelines, encapsulation, encryption, end condition, enforcement by conversion, entropy, environment hardening, error handling, error messages, exception checks, exception handling, exceptional conditions, exceptions, excessive code complexity, expiration keys, expired code, fault tolerance, file handling, file processing, filtering, firewall, firmware, flags, frameworks, function design, function errors, fuzz testing, grammar, handle exceptions, hash functions, identity validation, identity verification, improper adherence to coding standards, improper locking, incorrect control flow, incorrect regular expression, inefficient regular expression complexity, initialization, input validation, input validation unexpected date, installation integrity, internal compromise, jni call error handling, language selection, libraries, locking functionality, logging, logic design, manual static analysis, mapping objects, memory buffer errors, memory management, mvc frameworks, neutralization, null pointer dereference, numeric errors, object design, output encoding, output validation, parameter handling, parameterization, password requirements, permissions, pointer issues, policy, privilege management, proper initialization, proper locking apis, properly verify ownership, protect credentials, punycode, race conditions, reentrant functions, resource cleanup, resource limitation, resource locking, resource management, resource management errors, resource-locking validation checks, return values, safe temp file function, secure attributes, secure design principles, secure encryption, secure method, secure transport, sensitive data, sensitive information, separation of privileges, signals, sql injection, standardized method, string errors, sufficient authentication, sufficient verification, symlink, synchronization, system configuration, terminating condition, testing, testing of comparison logic, timeouts, unauthorized actors, undefined behavior, unique identifiers, unmaintained code, unprotected native code, user interface, user interface security issues, weak authentication, wrong status code
"""

# connect to database
connection = create_database("cwe.db")
cursor = connection.cursor()

# drop the table if needed
drop_table("Relateds", cursor, connection)

# create related table
create_related_table(cursor, connection)

# split list into keywords index
relateds = [r.strip() for r in related_design_list.strip().split(',')]

# add all keywords
for related in relateds:
    insert_related(related, cursor, connection)


records = select_records_related_table(cursor)

for related_id, related in records:
    print(related_id, related)
