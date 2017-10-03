# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# StorageType: Enum of possible storage types.
StorageType = str

# UsageForType: Usage for a storage type.
class UsageForType(ChromeTypeBase):
    def __init__(self,
                 storageType: Union['StorageType'],
                 usage: Union['float'],
                 ):

        self.storageType = storageType
        self.usage = usage


class Storage(PayloadMixin):
    """ 
    """
    @classmethod
    def clearDataForOrigin(cls,
                           origin: Union['str'],
                           storageTypes: Union['str'],
                           ):
        """Clears storage for origin.
        :param origin: Security origin.
        :type origin: str
        :param storageTypes: Comma separated origin names.
        :type storageTypes: str
        """
        return (
            cls.build_send_payload("clearDataForOrigin", {
                "origin": origin,
                "storageTypes": storageTypes,
            }),
            None
        )

    @classmethod
    def getUsageAndQuota(cls,
                         origin: Union['str'],
                         ):
        """Returns usage and quota in bytes.
        :param origin: Security origin.
        :type origin: str
        """
        return (
            cls.build_send_payload("getUsageAndQuota", {
                "origin": origin,
            }),
            cls.convert_payload({
                "usage": {
                    "class": float,
                    "optional": False
                },
                "quota": {
                    "class": float,
                    "optional": False
                },
                "usageBreakdown": {
                    "class": [UsageForType],
                    "optional": False
                },
            })
        )

    @classmethod
    def trackCacheStorageForOrigin(cls,
                                   origin: Union['str'],
                                   ):
        """Registers origin to be notified when an update occurs to its cache storage list.
        :param origin: Security origin.
        :type origin: str
        """
        return (
            cls.build_send_payload("trackCacheStorageForOrigin", {
                "origin": origin,
            }),
            None
        )

    @classmethod
    def untrackCacheStorageForOrigin(cls,
                                     origin: Union['str'],
                                     ):
        """Unregisters origin from receiving notifications for cache storage.
        :param origin: Security origin.
        :type origin: str
        """
        return (
            cls.build_send_payload("untrackCacheStorageForOrigin", {
                "origin": origin,
            }),
            None
        )

    @classmethod
    def trackIndexedDBForOrigin(cls,
                                origin: Union['str'],
                                ):
        """Registers origin to be notified when an update occurs to its IndexedDB.
        :param origin: Security origin.
        :type origin: str
        """
        return (
            cls.build_send_payload("trackIndexedDBForOrigin", {
                "origin": origin,
            }),
            None
        )

    @classmethod
    def untrackIndexedDBForOrigin(cls,
                                  origin: Union['str'],
                                  ):
        """Unregisters origin from receiving notifications for IndexedDB.
        :param origin: Security origin.
        :type origin: str
        """
        return (
            cls.build_send_payload("untrackIndexedDBForOrigin", {
                "origin": origin,
            }),
            None
        )



class CacheStorageListUpdatedEvent(BaseEvent):

    js_name = 'Storage.cacheStorageListUpdated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 origin: Union['str', dict],
                 ):
        if isinstance(origin, dict):
            origin = str(**origin)
        self.origin = origin

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class CacheStorageContentUpdatedEvent(BaseEvent):

    js_name = 'Storage.cacheStorageContentUpdated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 origin: Union['str', dict],
                 cacheName: Union['str', dict],
                 ):
        if isinstance(origin, dict):
            origin = str(**origin)
        self.origin = origin
        if isinstance(cacheName, dict):
            cacheName = str(**cacheName)
        self.cacheName = cacheName

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class IndexedDBListUpdatedEvent(BaseEvent):

    js_name = 'Storage.indexedDBListUpdated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 origin: Union['str', dict],
                 ):
        if isinstance(origin, dict):
            origin = str(**origin)
        self.origin = origin

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class IndexedDBContentUpdatedEvent(BaseEvent):

    js_name = 'Storage.indexedDBContentUpdated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 origin: Union['str', dict],
                 databaseName: Union['str', dict],
                 objectStoreName: Union['str', dict],
                 ):
        if isinstance(origin, dict):
            origin = str(**origin)
        self.origin = origin
        if isinstance(databaseName, dict):
            databaseName = str(**databaseName)
        self.databaseName = databaseName
        if isinstance(objectStoreName, dict):
            objectStoreName = str(**objectStoreName)
        self.objectStoreName = objectStoreName

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
