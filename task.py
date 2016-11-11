from property import Property

class Task:
    properties = (Property('ID', 'int primary key'),
                  Property('initDate', 'date'),
                  Property('name', 'text'), 
                  Property('detail', 'text'),
                  Property('person_ID', 'int'), )

    
    schema = ', '.join(['{0} {1}'.format(p.name, p.typ) for p in properties])
