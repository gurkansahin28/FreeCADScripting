import FreeCAD as App # type: ignore
import txt
from datetime import datetime


#------------------------------------------------------------
# create a new document
def doc(doc_name='MyDoc', created_by='Owner', company='Company', license_type='All rights reserved', license_url='https://en.wikipedia.org/wiki/All_rights_reserved'):
    """
    Creates a new FreeCAD document with metadata and optional properties.

    Args:
        doc_name (str): The name for the new document. Default is 'MyDoc'.
        created_by (str): The creator's name. Default is 'Owner'.
        company (str): The company's name. Default is 'Company'.
        license_type (str): The license type for the document. Default is 'All rights reserved'.
        license_url (str): The URL for the license details. Default is 'https://en.wikipedia.org/wiki/All_rights_reserved'.

    Returns:
        App.Document: The newly created FreeCAD document object.

    Example:
        new_doc = create_document('FunnyDoc', created_by='John Doe', company='Funny Designs', license_type='MIT', license_url='https://opensource.org/licenses/MIT')
    """
    # Validate the document name
    if not doc_name or not isinstance(doc_name, str):
        raise ValueError("Document name must be a non-empty string.")

    # Create the document
    doc = App.newDocument(doc_name)

    # Add metadata to the document
    doc.Comment = 'A FreeCAD Document to design'
    doc.Company = company
    doc.CreatedBy = created_by
    doc.Label = doc_name
    doc.License = license_type
    doc.LicenseURL = license_url

    # Print a confirmation message
    msg = f"Document '{doc_name}' created successfully by '{created_by}'."
    txt.toRv(msg)
    doc.recompute()
    
    return doc




#------------------------------------------------------------
def docs(doc_names):
    '''Create new document via a list.
        Args:
            docNames (list): a list of documents to create
        Return:
            It doesn't return anything.
        Example:
            docNames = ['DummyDoc', 'FunnyDoc', 'FluffyDoc']
            ml.newDocs(docNames)
    '''
    for doc_name in doc_names:
        doc(doc_name)
    txt.toRv('Documents were created.')
    pass




#------------------------------------------------------------
# creating a unique name for the new document
def uniqueName(topic='Doc'):
    '''Create a unique name using the date-time functions.
        Args:
            topic (str): a topic for the document name
        Return:
            specificDocName (str): a name to create a new document
        Example:
            docName = ml.uniqDocName(topic = 'Solid')
    
    '''
    ## Obtaining the date time information
    # Now
    now = datetime.now()
    # extracting the year as two-digit year
    year = now.strftime('%y')
    # extracting the month from the now
    month = now.month
    # extracting the day from the now
    day = now.day
    # extracting the hour from the now
    hour = now.strftime('%H')
    # extracting the minute from the now
    minutes = now.minute
    # extracting the seconds from the now
    seconds = now.strftime('%S')
    # preparing the docName
    unique_name = f'{topic}_{year}{month}{day}_{hour}{minutes}{seconds}'
    # returning a string as a specific unique name
    txt.toRv(msg=f'{unique_name}: The unique doc name created!')
    return unique_name



#------------------------------------------------------------
# creating a document with unique name given a topic
def uniqueDoc(topic = 'Doc'):
    '''Create a unique document through given topic.
        Args:
            topic (str): a topic for the new document.
        Return: 
            doc (object): a new document.
        Example:
            doc = newUniqDoc('Sketch')
    '''
    unique_name = uniqueName(topic)
    doc_obj = doc(unique_name)
    return doc_obj
#------------------------------------------------------------


