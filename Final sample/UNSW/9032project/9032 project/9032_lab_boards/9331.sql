-- COMP9311 18s2 Assignment 1
-- Schema for the myPhotos.net photo-sharing site
--
-- Written by:
--    Name:  Ran Bai
--    Student ID:  z5187292
--    Date:  01/09/2018
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

create domain VisibilityValue as 
     varchar(14)  check (value in ('private','friends','family','friends+family','public'));
	 
create domain SafetyValue as
     varchar(10)  check (value in ('safe','moderate','restricted'));
	 
create domain RateValue as
     integer      check (value in (1, 2, 3, 4, 5));
-- Tables (you must add more)

create table People (
	id                 serial,
	email_address      EmailValue not null,
	family_name        NameValue,	
	given_names        NameValue not null,
    displayed_name     LongNameValue not null, 
	primary key (id)
);

create table Users (
    date_registered     date not null,
	password    	    text not null,
    birthday    		date,
    gender      		GenderValue,
    website     		URLValue,
    id          		integer references People(id),	
	portrait            integer,
	primary key (id)
);

create table Groups (
	id                   serial,
	title                text not null,
	"mode"               GroupModeValue not null,
	ownedBy              integer not null references Users(id),
	primary key (id)
);

create table Users_member_Groups(
     user_id              integer references Users(id),
	 group_id             integer references Groups(id),
	 primary key (user_id,group_id)
);

create table Contact_lists (
	id                   serial,
	title                text not null,
	ownedBy              integer references Users(id) not null,
	"type"               ContactListTypeValue default null,
	primary key (id)
);

create table Discussions (
    id                   serial,
    title                NameValue,
	primary key (id)
);

create table Photos (
	id                   serial,
	title                NameValue not null unique,
	description          text,
	date_taken           date,
	date_uploaded        date not null,
	file_size            integer not null,
	visibility           VisibilityValue not null,
	safety_level         SafetyValue not null,
	technical_details    text,
	ownedBy              integer references Users(id) not null,
	discussion_id        integer references Discussions (id),
	primary key (id)
);

alter table Users add foreign key (portrait) references Photos(id) deferrable;

create table Groups_has_Discussions (
    group_id             integer references Groups(id),
	discussion_id        integer references Discussions(id),
	primary key (group_id, discussion_id)
);

create table Comments (
    id                   serial, 
	when_posted          timestamp not null,    
	content              text not null,
	containedBy          integer references Discussions(id) not null,  
	author               integer references Users(id) not null, 
	primary key (id)
);

create table People_member_Contact_lists (
    people_id            integer references People(id),
	contact_lists_id     integer references Contact_lists(id),
    primary key (people_id,contact_lists_id)
);

create table Collections (
    id                   serial,
	title				 NameValue	not	null,
	keys				 integer	not	null references Photos(id), 
	description          text,
	user_collection      integer,
	group_collection     integer,
	constraint DisjointTotal check(
	(user_collection is null and group_collection is not null)
	or 
	(user_collection is not null and group_collection is null)
	),
	primary	key	(id)
);

create table Photos_in_Collections (
    photo_id             integer references Photos(id),
	collection_id        integer references Collections(id),
    "order"              integer   not null,
    primary key (photo_id, collection_id)
);

create table User_Collections (
    id                   integer references Collections(id),
    ownedBy              integer references Users(id) not null,         
	primary key (id)
);
create table Group_Collections (
    id                   integer references Collections(id),
    ownedBy              integer references Groups(id) not null,      
    primary key (id)	
);

create table Tags (
    id                   serial,
	name                 NameValue not null,  
	freq                 integer not null default 0 check( freq >= 0),
	primary key (id)
);

create table Users_rates_Photos (
    user_id              integer references Users(id),
	photo_id             integer references Photos(id),
	rating               RateValue,
    when_rated           timestamp not null,
	primary key (user_id, photo_id)
);

create table Users_tag_Photos_has_Tags (
    user_id              integer references Users(id),
	photo_id             integer references Photos(id),
	tag_id               integer references Tags(id),
	when_tagged          timestamp not null,
	primary key (user_id, photo_id, tag_id)
);