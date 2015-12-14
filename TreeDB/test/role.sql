drop table if exists `role`;
create table `role`(
	`role_id` bigint(16) not null auto_increment,
	`account_id` int(11) not null,
	`channel_id` int(11) not null,
	`name` varchar(16) not null,
	`level` smallint(4) not null default 0,
	`coin` int(11) not null default 0,
	`gold` int(11) not null default 0,
	unique key `role_id` (`role_id`),
	unique key `name` (`name`)
) engine=INNODB default charset=utf8;
