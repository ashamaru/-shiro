# Api for kurisu db.xml

from xml.etree import ElementTree


def validate_db_path(db_path):
    print(db_path)
    return True


class DBHandel(object):
    db_path = None
    root = None
    meta = None
    content = None
    current_table = 'content'

    def __init__(self, db_path):
        if validate_db_path(db_path) is False:
            raise Exception
        self.db_path = db_path
        self.root = ElementTree.parse(self.db_path)
        for elem in self.root:
            if elem.tag == 'meta':
                self.meta = elem
            elif elem.tag == 'content':
                self.content = elem
        if self.meta is None or self.content is None:
            raise Exception

    def set_current_table(self, table):
        self.current_table = table

    def select(self, table, mood, id):
        print(self.content, table, mood, id)
        return False

    def insert(self, table, mood, reply):
        print(self.content, table, mood, reply)
        return False

    def delete(self, table, mood, reply):
        print(self.content, table, mood, reply)
        return False

    def update(self, table, mood, reply):
        print(self.content, table, mood, reply)
        return False

    def write(self):
        return False


class XmlDBHandel(DBHandel):

    def __init__(self, db_path):
        super(XmlDBHandel, self).__init__(db_path)
