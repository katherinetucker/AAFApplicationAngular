#########################################################################################
###https://pypi.python.org/pypi/voluptuous
###Need to create schema objects for incoming JSON
###See URL for guite to validation class
###Wrap validation call in try/except and return error messages as results to web service
#########################################################################################
from voluptuous import Schema, All, Any, Length, Required, Datetime, Boolean, Email
import datetime

def IsValid(schema, data):
    return schema(data)

def ValidateAsstReq(data):
    return IsValid(assistance_schema, data)

test_schema = Schema( { Required(1) : 'one', 
                        Required(2) : All(Any(str, unicode), Length(min=1)),
                        Required('3') : int,
                        4 : [ Any(str, unicode), 5, 'five' ]} )

date_schema = Schema({'$date' : int })

personnel_schema = Schema( { 'fname' : Any(str, unicode),
                              'initial' : Any(str, unicode),
                              'lname' : Any(str, unicode),
                              'age' : int,
                              'relationship' : str } )

applicant_schema = Schema( { 'first_name' : Any(str, unicode),
                              'middle_name' : Any(str, unicode),
                              'last_name' : Any(str, unicode),
                              'employee_id' : int,
                              'status' : ['full_time', 'part_time'],
                              'position' : Any(str, unicode),
                              'store_dept_no' : int,
                              'permanenet_address' : ['own', 'rent'],
                              'address1' : str,
                              'address2' : str,
                              'city' : str,
                              'state' : str, #needs review
                              'zip' : str, #needs review
                              'day_phone' : str, #needs review
                              'night_phone' : str, #needs review
                              'email' : Email() } )

incident_schema = Schema( { 'event_date' : date_schema,
                              'event_description' : str } )

requested_schema = Schema( { 'amount_requested' : float,
                              'shelter' : ['temporary', 'eviction', 'homeless'],
                              'funeral' : Boolean(),
                              'utilities' : Boolean(),
                              'fire' : Boolean(),
                              'naturalDisaster' : Boolean(),
                              'other' : Boolean() } )

recieved_schema = Schema( { 'assist_salv_army' : float,
                              'assist_red_cross' : float,
                              'assist_govt' : float,
                              'assist_employer' : float,
                              'assist_other' : float } )

submit_schema = Schema( { 'sumbit_name' : str,
                              'submit_date' : date_schema,
                              'signature' : str } )

assistance_schema = Schema( { 'applicantInfo' : applicant_schema,
                              'eligiblePersonnel' : [personnel_schema],
                              'incidentInfo' : incident_schema,
                              'assistanceRequested' : requested_schema,
                              'assistanceRecieved' : recieved_schema,
                              'submitDetails' : submit_schema } )

if __name__ == '__main__':
    print type(1485382223700)
    print(IsValid(test_schema, { 1: 'one', 2 : 'three' , '3' : 2, 4 : ['4', 5, '6'] }))
    print(IsValid(date_schema, {"$date": 1485382223700}))
    print(ValidateAsstReq({ 'applicantInfo' : { 'first_name' : 'Trevor', 'store_dept_no' : 23 }, 'incidentInfo' : { 'event_date' : {"$date": 1485382223700} }, 'assistanceRequested': { 'funeral' : False} } ))
