from django.db.backends.postgresql.base import DatabaseWrapper as PgDatabaseWrapper
from django.db.backends.postgresql.features import DatabaseFeatures as PgDatabaseFeatures


class DatabaseFeatures(PgDatabaseFeatures):
    supports_ignore_conflicts = False


class DatabaseWrapper(PgDatabaseWrapper):
    features_class = DatabaseFeatures