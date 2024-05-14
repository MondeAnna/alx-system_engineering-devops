-- create replica user
CREATE USER IF NOT EXISTS "replica_user"@"%"
            IDENTIFIED BY "projectcorrection280hbtn";

GRANT REPLICATION SLAVE
                 ON *.*
                 TO "replica_user"@"%";
