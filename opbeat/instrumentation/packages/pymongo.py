from opbeat.instrumentation.packages.base import AbstractInstrumentedModule
from opbeat.traces import trace


class PyMongoInstrumentation(AbstractInstrumentedModule):
    name = 'pymongo'

    instrument_list = [
        ("pymongo.collection", "Collection.aggregate"),
        ("pymongo.collection", "Collection.bulk_write"),
        ("pymongo.collection", "Collection.count"),
        ("pymongo.collection", "Collection.create_index"),
        ("pymongo.collection", "Collection.create_indexes"),
        ("pymongo.collection", "Collection.delete_many"),
        ("pymongo.collection", "Collection.delete_one"),
        ("pymongo.collection", "Collection.distinct"),
        ("pymongo.collection", "Collection.drop"),
        ("pymongo.collection", "Collection.drop_index"),
        ("pymongo.collection", "Collection.drop_indexes"),
        ("pymongo.collection", "Collection.ensure_index"),
        ("pymongo.collection", "Collection.find"),
        ("pymongo.collection", "Collection.find_and_modify"),
        ("pymongo.collection", "Collection.find_one"),
        ("pymongo.collection", "Collection.find_one_and_delete"),
        ("pymongo.collection", "Collection.find_one_and_replace"),
        ("pymongo.collection", "Collection.find_one_and_update"),
        ("pymongo.collection", "Collection.group"),
        ("pymongo.collection", "Collection.inline_map_reduce"),
        ("pymongo.collection", "Collection.insert"),
        ("pymongo.collection", "Collection.insert_many"),
        ("pymongo.collection", "Collection.insert_one"),
        ("pymongo.collection", "Collection.map_reduce"),
        ("pymongo.collection", "Collection.reindex"),
        ("pymongo.collection", "Collection.remove"),
        ("pymongo.collection", "Collection.rename"),
        ("pymongo.collection", "Collection.replace_one"),
        ("pymongo.collection", "Collection.save"),
        ("pymongo.collection", "Collection.update"),
        ("pymongo.collection", "Collection.update_many"),
        ("pymongo.collection", "Collection.update_one"),
    ]

    def call(self, module, method, wrapped, instance, args, kwargs):
        instance_name = instance.name or instance.filename
        cls_name, method_name = method.split('.', 1)
        signature = '.'.join([instance_name, method_name])
        with trace(signature, "db.pymongo.query"):
            return wrapped(*args, **kwargs)