-- Database: r3view

DROP DATABASE r3view;
CREATE DATABASE r3view
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

GRANT TEMPORARY, CONNECT ON DATABASE r3view TO PUBLIC;
GRANT CREATE, CONNECT ON DATABASE r3view TO postgres;
GRANT TEMPORARY ON DATABASE r3view TO postgres WITH GRANT OPTION;
