from mongoengine import Document, EmbeddedDocument, IntField, StringField, \
                        ListField, EmbeddedDocumentField


class Job(EmbeddedDocument):
    jobID = StringField()
    executor = StringField(required=True)
    filename = StringField(required=True)
    description = StringField(required=True)
    os = StringField(required=True)
    user = StringField()
    timeCreated = StringField()
    timeDispatched = StringField()
    timeStarted = StringField()
    timeEnded = StringField()
    argv = ListField(StringField())
    exitCode = IntField()
    stdout = StringField()
    stderr = StringField()
    meta = {"db_alias": "agent_db"}


class Library(Document):
    jobs = ListField(EmbeddedDocumentField(Job))
    meta = {"db_alias": "agent_db"}


class Agent(Document):
    hostname = StringField(required=True)
    agentID = StringField(required=True)
    os = StringField(required=True)
    lastCheckin = StringField(required=True)
    jobsQueue = ListField(EmbeddedDocumentField(Job))
    jobsRunning = ListField(EmbeddedDocumentField(Job))
    jobsHistory = ListField(EmbeddedDocumentField(Job))
    meta = {"db_alias": "agent_db"}


class RegistrationKey(Document):
    regKey = StringField(required=True)
    meta = {"db_alias": "admin_db"}


class User(Document):
    name = StringField(required=True)
    username = StringField(required=True)
    passwordHash = StringField(required=True)
    meta = {"db_alias": "admin_db"}
