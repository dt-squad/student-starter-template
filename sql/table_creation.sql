-- >>>>>>>>>>>>>>>> COMPLAINTS

-- Enum creation of complaint stage options
CREATE TYPE complaint_stages AS enum(
    'Member_MP_Enquiry',
    'Stage 1',
    'Stage 2',
    'Ombudsman',
)

-- Table creation for complaints which will have multiple jobs linked under one complaint case
CREATE TABLE complaints(
    id INTEGER PRIMARY KEY,
    -- Normally in  format RBK-COMP-XXXXXX
    complaint_number VARCHAR(20) UNIQUE,
    -- Use enum to set the complaint stage
    stage complaint_stages,
    
    -- Address and postcode for complaint
    address VARCHAR(100),
    postcode VARCHAR(10),
)

-- >>>>>>>>>>>>>>>> JOBS

-- Creates table for the jobs
CREATE TABLE jobs(
   id INTEGER PRIMARY KEY,

   -- In format RBKXXXXXX
   job_number VARCHAR(50) NOT NULL UNIQUE,

    -- Address and postcode for job
   address VARCHAR(100),
   postcode VARCHAR(10),

   -- References complaints table to select a complaint if the job is a complaint
   complaint_id UUID REFERENCES complaints(id)
);

-- >>>>>>>>>>>>>>>> STAGES AND HISTORY

-- Creates job_stages table without adding a column to add later
CREATE TABLE job_stages(
    id INTEGER PRIMARY KEY,
    title VARCHAR()
)

-- ALTER TABLE table_name 
-- ADD COLUMN  column_name1 data_type, 
-- ADD COLUMN  column_name1 data_type,

-- Constraints; Not required but used for making rules?

-- Adding column to the date table, using the date data-type
ALTER TABLE job_stages
ADD COLUMN date date


-- Stages history table to save the job stage changes for data reports in the future
CREATE TABLE job_stages_history(
    id INTEGER PRIMARY KEY,
    job_id INTEGER REFERENCES jobs(id),
    job_stages_id INTEGER REFERENCES job_stages(id),
    for_scaffold BOOLEAN
);

-- Deleting the column due to an 'unintentional learning curve'
alter table job_stages
DROP COLUMN date;

-- Adding a column to the correct table
alter table job_stages_history
ADD COLUMN date date

-->>>>>>>>>>>>>>>> Resource

-- Creates table for resources such as different subcontractors or Direct Line Operatives(DLOs).
-- I realised I haven't been using UUID so I will use it here.
CREATE TABLE resource(
    id UUID PRIMARY KEY,
    name VARCHAR(60),
    subcontractor BOOLEAN
)

-- Creates table to add a contact to each resource.
CREATE TABLE resource_contact(
    id UUID PRIMARY KEY,
    resource_id UUID REFERENCES resource(id),
    subcontractor BOOLEAN,
    name VARCHAR(60),
    email VARCHAR(60),
    phone INTEGER,
    role VARCHAR(40)
);

-- Creates table for a selection of trades to be added
CREATE TABLE resource_trades(
    id UUID PRIMARY KEY,
    trade VARCHAR(40)
)

-- >>>>>>>>>>>>>>>> Scaffold

-- Creates Enum to list each stage of a scaffold.
CREATE TYPE scaffold_status AS Enum(
    'Requested',
    'Sent to commercial',
    'Sent to RBK',
    'Approved',
    'Risk assessments',
    'Permit to erect',
    'Handover checks',
    'Permit to load',
    'Work Completed',
    'Off-hire notice',
    'Strike'
)

-- Creates a table to collect scaffold data, connecting the scaffold to a job and assigning a resource.
CREATE TABLE scaffold_requests(
    id INTEGER PRIMARY KEY,
    job_id INTEGER REFERENCES jobs(id),
    use VARCHAR(100),
    status scaffold_status,
    recource_id UUID REFERENCES resource(id)
)

-- Enum list of different elevations of a building scaffold can be erected on.
CREATE TYPE scaffold_elevation AS Enum(
    'Front',
    'Left',
    'Right',
    'Rear',
)

-- Table of every scaffold elevation, each elevation is attached to a scaffold request and contains the dimensions of each scaffold.
CREATE TABLE scaffold_elevations(
    id INTEGER PRIMARY KEY,
    scaffold_id INTEGER REFERENCES scaffold_requests(id),
    elevation scaffold_elevation,
    height INTEGER,
    width INTEGER,
    chimney BOOLEAN,
    notes VARCHAR(250)
)

-- Enum of types of scaffold media that can be uploaded.
CREATE TYPE scaffold_media Type Enum(
    'Request',
    'TG20',
    'Handover Certificate',
    'Scaffold Tag',
    'Scaffold Picture',
    'Inspection',
    'Other'
)

-- Table to contain media items as a file, a link will later be added into the <FilePath> column to display images and documents.
CREATE TABLE scaffold_media(
    id INTEGER PRIMARY KEY,
    scaffold_id INTEGER REFERENCES scaffold_requests(id),
    FilePath VARCHAR(255),
    type scaffold_media
)

-- Table which can be used to create a list of checklist items to later be used to validate risk assessments and documentation.
CREATE TABLE scaffold_checklist_item(
    id INTEGER PRIMARY KEY,
    scaffold_id INTEGER REFERENCES scaffold_requests(id),
    check_item VARCHAR(30)
)

-- >>>>>>>>>>>>>>>> Data Manipulation

-- First Attempt at adding data to the complaints table.
INSERT INTO complaints(complaint_number, stage, address, postcode)
Values('RBKR-COMP-123456', Ombudsman, '12 Lorum Ipsum', 'EX479LE' )

-- After debugging in DBeaver:
-- ID was required as not set to UUID (I will test with the Resource table in the future how this differs). 
-- Ombudsman also had to be in quotations, I realised this makes sense due to the data travels as a value from the front end to python.
INSERT INTO complaints(id, complaint_number, stage, address, postcode)
Values('1', 'RBKR-COMP-123456', 'Ombudsman', '12 Lorum Ipsum', 'EX479LE' )

-- Attempt at adding a job to the table using a foreign key to the complaint row ID '1'
INSERT INTO jobs(id, job_number, address, postcode, complaint_id)
Values('1', 'RBK123456', '12 Lorum Ipsum', 'EX479LE', '1')

-- Inserting the first job stage into job stages
INSERT INTO job_stages(id, title)
Values('1', 'Job Raised')

-- Attempting multiple inserts with only one table decleration
INSERT INTO job_stages(id, title)
Values('2', 'Initial Appointment')
Values('3', 'Variation Requested')
Values('4', 'Variation sent to RBK')


-- It didnt work
INSERT INTO job_stages(id, title)
Values('2', 'Initial Appointment'),

INSERT INTO job_stages(id, title)
Values('3', 'Variation Requested')

INSERT INTO job_stages(id, title)
Values('4', 'Variation sent to RBK')

-- Swapping columns between tables again. Same tables, different columns (Unintentional practice)
alter table job_stages
ADD COLUMN for_scaffold BOOLEAN

alter table job_stages_history
DROP COLUMN for_scaffold


-- Inserting a job stage history to the previous job, with the status raised
INSERT INTO job_stages_history(id, job_id, job_stages_id)
Values('1', '1', '1')

--Inserting the date to see if the correct row is updated
INSERT INTO job_stages_history(id, date)
Values('1' '12/06/2026')

UPDATE job_stages_history
SET date = '2020-08-01'
WHERE job_stages_history_id = 1;

