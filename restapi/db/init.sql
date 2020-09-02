CREATE DATABASE bot;
use bot;

CREATE TABLE registered (email VARCHAR(250),id VARCHAR(250));
-- INSERT INTO registered VALUES ('prajwalnadagouda2311@gmail.com',"Y2lzY29zcGFyazovL3VzL1JPT00vMjQ4NzE4NjEtOWNmMi0zYWM2LThjN2MtZGM3ZjA1ZGE1NjEw");


CREATE TABLE holiday (occasion_Date DATE, month VARCHAR(20),occasion VARCHAR(255),floater BOOLEAN);

CREATE TABLE helpdesk (empid INT, empname VARCHAR(255),emailid VARCHAR(255),contact VARCHAR(255));

create table employee(empid INT ,NAMEEMP VARCHAR(255), email VARCHAR(255), dob DATE, managerid VARCHAR(255));

insert into employee values(1001, "Aswath", "askuma@akamai.com", '1998-05-16', "5001");
insert into employee values(1002, "Prajwal", "pnadagou@akamai.com", '1998-08-27', "5001");
insert into employee values(5001, "Aman", "aman@akamai.com", '1988-04-19', "7001");
insert into employee values(1003, "Ornella", "odsouza@akamai.com", '1999-07-21', "5002");
insert into employee values(5002, "Saran", "saran@akamai.com", '1979-07-23', "7002");
insert into employee values(7001, "Jack", "jack@akamai.com", '1969-12-18', "10001");


INSERT INTO helpdesk VALUES(2001, "ARUN KUMAR", "akumar@akamai.com", "9849120945");
INSERT INTO helpdesk VALUES(2002, "SEJAL MISHRA", "smishra@akamai.com", "9674120945");
INSERT INTO helpdesk VALUES(2003, "NAMAN MITTAL", "nmittal@akamai.com", "9845698345");
INSERT INTO helpdesk VALUES(2004, "SAHANA MURTHY", "smurthy@akamai.com", "9849109876");
INSERT INTO helpdesk VALUES(2005, "VENKAT SHETTY", "vshetty@akamai.com", "9841234545");


INSERT INTO holiday VALUES('2020-01-01','JANUARY','NEW YEAR',1);
INSERT INTO holiday VALUES('2020-01-15','JANUARY','MAKARA SANKRANTHI',1);
INSERT INTO holiday VALUES('2020-01-26','JANUARY','REPUBLIC DAY',0);
INSERT INTO holiday VALUES('2020-02-21','FEBRUARY','MAHA SHIVARATHRI',1);
INSERT INTO holiday VALUES('2020-03-10','MARCH','HOLI',1);
INSERT INTO holiday VALUES('2020-03-25','MARCH','CHANDRAMANA UGADI',1);
INSERT INTO holiday VALUES('2020-04-10','APRIL','GOOD FRIDAY',1);
INSERT INTO holiday VALUES('2020-04-14','APRIL','TAMIL NEW YEAR',1);
INSERT INTO holiday VALUES('2020-05-01','MAY','MAY DAY',0);
INSERT INTO holiday VALUES('2020-05-25','MAY','RAMZAN',1);
INSERT INTO holiday VALUES('2020-08-11','AUGUST','SRI KRISHNA JANMASHTAMI',1);
INSERT INTO holiday VALUES('2020-08-15','AUGUST','INDEPENDENCE DAY',0);
INSERT INTO holiday VALUES('2020-10-02','OCTOBER','GANDHI JAYANTHI',0);
INSERT INTO holiday VALUES('2020-10-26','OCTOBER','VIJAYA DASHAMI',1);
INSERT INTO holiday VALUES('2020-10-30','OCTOBER','ID MILAD',1);
INSERT INTO holiday VALUES('2020-11-01','NOVEMBER','KANNADA RAJYOTSAVA',0);
INSERT INTO holiday VALUES('2020-11-16','NOVEMBER','DEEPAVALI',1);
INSERT INTO holiday VALUES('2020-12-25','DECEMBER','CHRISTMAS',1);
