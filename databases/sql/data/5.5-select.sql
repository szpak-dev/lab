SELECT u.id as user_id,u.username,u.password,up.rank,up.email FROM trans.users u JOIN trans.user_profiles up ON up.user_id=u.id;