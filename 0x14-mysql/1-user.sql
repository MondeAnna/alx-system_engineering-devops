-- create assessor user
CREATE USER IF NOT EXISTS "holberton_user"@"localhost"
            IDENTIFIED BY "projectcorrection280hbtn";

GRANT ALL
   ON *.*
   TO "holberton_user"@"localhost";
