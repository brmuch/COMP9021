-- COMP9311 18s2 Assignment 1
-- Schema for the myPhotos.net photo-sharing site
--
-- Written by:
--    Name:  <<YOUR NAME GOES HERE>>
--    Student ID:  <<YOUR STUDENT ID GOES HERE>>
--    Date:  ??/09/2018
--
-- Conventions:
-- * all entity table names are plural
-- * most entities have an artifical primary key called "id"
-- * foreign keys are named after either:
--   * the relationship they represent
--   * the table being referenced

-- Domains (you may add more)

create domain URLValue as
	varchar(100) check (value like 'http://%');

create domain EmailValue as
	varchar(100) check (value like '%@%.%');

create domain GenderValue as
	varchar(6) check (value in ('male','female'));

create domain GroupModeValue as
	varchar(15) check (value in ('private','by-invitation','by-request'));

create domain ContactListTypeValue as
	varchar(10) check (value in ('friends','family'));

create domain NameValue as varchar(50);

create domain LongNameValue as varchar(100);

create domain ShareWith as 
	varchar(20) check (value in ('private','friends','family','friends+family','public'));
	
create domain Security as
	varchar(15) check (value in ('safe','moderate','restricted'));

create domain Rating as
	integer(1) check (value in (1, 2, 3, 4, 5));


-- Tables (you must add more)

create table People (
	id          serial,
	family_name NameValue,
	given_names NameValue not null,
	displayed_name LongNameValue not null,
	email_address EmailValue not null,
	primary key (id)
);

create table Users (
	password text not null,
	birthday date,
	gender GenderValue,
	website URLValue,
	date_registered date not null,
	portrait NameValue like '%.jpeg' references Photos(title),
	id         serial references People(id),
	primary key (id)
);

create table Groups (
	id serial,
	title text not null,
	ownedBy integer references Users(id) not null,
	"mode" GroupModeValue not null,
	primary key (id)
);

create table Users_member_Groups  (
	user_id integer references Users(id),
	group_id integer references Groups(id),
	
	primary key (user_id, group_id)
);

create table Contact_lists (
	id serial,
	ownedBy integer references Users(id) not null,
	title text not null,
	"type" ContactListTypeValue default null,
	primary key (id)
);

create table People_member_Contact_Lists (
	person_id integer references People(id),
	contact_list_id integer references Contact_lists(id),
	primary key (person_id, contact_list_id)
);

create table Photos (
	id serial,
	title NameValue not null unique,
	description text,
	date_taken date,
	date_uploaded date not null,
	file_size integer not null,
	visibility ShareWith not null,
	safety_level Security not null,
	technical_details text,
	ownedBy integer references Users(id) not null,
	primary key (id)
);

create table Tags (
	id serial,
	name NameValue not null,
	freq integer,
	primary key (id)
)

create table Photos_has_Tags (
	photo_id integer references Photos(id),
	tag_id integer references Tags(id),
	when_tagged date not null,
	primary key (photo_id, tag_id)
)

create table Users_rates_Photos (
	user_id integer references Users(id),
	photo_id integer references Photos(id),
	rating Rating,
	when_rated date not null,
	primary key (user_id, photo_id)
)

create table Collections (
	id serial,
	title NameValue not null,
	description text,
	photo integer references Photos (id),
	primary key (id)
)

create table Photos_in_Collections (
	photo_id integer references Photos(id),
	collection_id integer references Collections(id),
	"order" integer,
	primary key (photo_id, collection_id)
)

create table Comments (
	id serial,
	content text not null,
	discussion_id integer references Discussions (id),
	user_id integer references Users (id),
	when_posted date not null,
	author     
	primary key (id)
)

create table Discussions (
	id serial,
	title NameValue,
	primary key (id)
)