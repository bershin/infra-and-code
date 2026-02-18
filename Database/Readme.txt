CREATE ROLE hr NOSUPERUSER NOCREATEDB NOLOGIN;
CREATE USER suzy NOSUPERUSER NOCREATEDB LOGIN PASSWORD 'pass123';
ALTER ROLE suszy WITH PASSWORD 'StrongPassword123';
SELECT rolname, rolsuper, rolcreatedb, rolcanlogin
FROM pg_roles
WHERE rolname IN ('hr', 'accounting');


GRANT accounting TO suzy;
SELECT
    pg_get_userbyid(member)  AS member_role,
    pg_get_userbyid(roleid)  AS granted_role
FROM pg_auth_members;

REVOKE ALL ON DATABASE northwind FROM public;
GRANT CONNECT ON DATABASE northwind TO hr;

REVOKE ALL ON SCHEMA public FROM public;
GRANT CREATE ON SCHEMA public TO accounting;
GRANT USAGE ON SCHEMA public TO accounting;

REVOKE SELECT ON ALL TABLES IN SCHEMA public FROM accounting;
GRANT SELECT (employeeid, lastname, firstname, title) 
ON employees
TO accounting;

CREATE POLICY accounting_orders ON orders
FOR SELECT
TO accounting
USING (orderdate >= '1998-01-01');


==========
SELECT rolname FROM pg_roles;
DROP ROLE role_name;
DROP ROLE hr,accounting,suzy,bobby,sales,jill;


REVOKE ALL PRIVILEGES ON DATABASE northwind FROM accounting;
REASSIGN OWNED BY accounting TO postgres;
DROP OWNED BY accounting;
DROP ROLE accounting;