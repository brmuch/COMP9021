-- Schema for simple company database

create table Employees (
	tfn         char(11) check(tfn ~ '^[0-9]{3}-[0-9]{3}-[0-9]{3}$'),
	givenName   varchar(30) not null,
	familyName  varchar(30),  
	hoursPweek  float check(hoursPweek >= 0 and hoursPweek <= 168),

	primary key(tfn)
);

create table Departments (
	id          char(3) check(id ~ '^0{2}[1-3]$'),
	name        varchar(100) unique,
	manager     char(11) unique references Employees(tfn),
	
	primary key(id)
	
);

create table DeptMissions (
	department  char(3) references Departments(id),
	keyword     varchar(20),
	
	primary key(department,keyword)
);

create table WorksFor (
	employee    char(11) references Employees(tfn),
	department  char(3) references Departments(id),
	percentage  float check(percentage > 0 and percentage <= 100),
	
	primary key(employee,department)
);