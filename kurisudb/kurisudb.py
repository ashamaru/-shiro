# Api for kurisu db.xml

from xml.etree import ElementTree
from kurisudb import settings


def validate_db_path(db_path):
    print(db_path)
    return True

# Decorator for DBHandleBase - capsulates the real handle depending on the storage engine
class DBHandel(object):
    db_path = None
    current_table = 'content'
    db_handle = None

    def __init__(self):
        db_storage = settings.DB_STORAGE
        db_url = settings.DB_DATABASE
        if db_storage is None or db_url is None:
            raise Exception
        # todo: validate db_settings
        if db_storage == 'db_xml':
            #create xml kurisudb handle
            self.db_handle = XmlDBHandel(db_url)
        else:
            raise Exception

    def set_current_table(self, table):
        self.current_table = table

    # returns string, not elem
    def selectReply(self, mood, id):
        return self.db_handle.selectReply(mood, id)

    # returns the length of the mood-section
    def getlength(self, mood):
        return self.db_handle.getlength(mood)

    # returns list of strings, not list of elements
    def selectAll(self, mood):
        return self.db_handle.selectAll(mood)

    def insert(self, mood, domain: str, reply):
        return self.db_handle.insert(mood, domain, reply)

    def insertSet(self, domain, set):
        return self.db_handle.insertSet(domain, set)

    def delete(self, mood, reply):
        return self.db_handle.delete(mood, reply)

    def update(self, reply):
        return self.db_handle.update(reply)

    def write(self):
        return self.db_handle.write()

class DBHandleMixin:
    db_path = None
    current_table = 'content'

    def __init__(self, db_path):
        # *
        # todo: implement factory
        # *
        return None

    def set_current_table(self, table):
        self.current_table = table

    def getlength(self, mood):
        pass

    # returns string, not elem
    def selectReply(self, mood, id):
        pass

    # returns list of strings, not list of elements
    def selectAll(self, mood):
        pass

    def insert(self, mood, domain: str, reply):
        raise Exception

    def insertSet(self, domain, set):
        pass

    def delete(self, mood, reply):
        pass

    def update(self, reply):
        pass

    def write(self):
        pass


class XmlDBHandel(DBHandleMixin):
    encoding = 'unicode'
    tree = None
    root = None
    meta = None
    content = None

    def __init__(self, db_path):
        if validate_db_path(db_path) is False:
            raise Exception
        self.db_path = db_path
        self.tree = ElementTree.parse(self.db_path)
        self.root = self.tree.getroot()
        for elem in self.root:
            if elem.tag == 'meta':
                self.meta = elem
            elif elem.tag == 'content':
                self.content = elem
        if self.meta is None or self.content is None:
            raise Exception

    def set_current_table(self, table):
        self.current_table = table

    def getlength(self, mood):
        mood_elem = self.content.find(mood)
        return int(mood_elem.get('count'))

    # returns string, not elem
    def selectReply(self, mood, id):
        mood_elem = self.content.find(mood)
        noe = int(mood_elem.get('count'))
        if id >= noe or id < 0:
            raise Exception
        if mood_elem is None:
            raise Exception
        reply = list(mood_elem)[id].text
        return reply

    # returns list of strings, not list of elements
    def selectAll(self, mood):
        mood_elem = self.content.find(mood)
        if mood_elem is None:
            raise Exception
        reply_list = []
        for elem in list(mood_elem):
            reply_list.append(elem.text)
        return reply_list

    def insert(self, mood, domain: str, reply):
        mood_elem = self.content.find(mood)
        if mood_elem is None:
            raise Exception
        new_elem = ElementTree.Element('reply', {'domain': domain})
        new_elem.text = reply;
        noe = int(mood_elem.get('count'))
        noe += 1
        mood_elem.append(new_elem)
        mood_elem.set(str(noe))
        self.tree.write(self.db_path, self.encoding)
        return True

    def insertSet(self, domain, set):
        raise Exception

    def delete(self, mood, reply):
        raise Exception

    def update(self, reply):
        raise Exception

    def write(self):
        raise Exception
