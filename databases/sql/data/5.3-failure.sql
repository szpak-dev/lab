BEGIN TRANSACTION;

INSERT INTO trans.users(username,password) VALUES('username','p4ssw0rd');
INSERT INTO trans.user_profiles(user_id,rank,email)VALUES((SELECT MAX(id) FROM trans.users),'TOO LONG RANK NAME','email@example.com');

END TRANSACTION;