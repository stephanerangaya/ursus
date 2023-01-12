from collections import UserDict
from . import ContextProcessor


class RelatedEntriesProcessor(ContextProcessor):
    """
    Replaces reference to entries with the entries themselves. It only applies to
    entry fields that start with 'related_'.

    For example:
    {
        'guides/moving-to-berlin': {
            'related_guides': [
                'guides/find-a-flat.md',
                'glossary/Anmeldung.md',
            ]
        }
    }
    """
    class RelatedEntryReferenceDict(UserDict):
        def __init__(self, data, reference_data):
            self.reference_data = reference_data
            super().__init__(data)

        def _get_reference(self, key):
            return self.reference_data[key]

        def __getitem__(self, key):
            if key.startswith('related_') and key in self.data:
                related_uris = self.data[key]
                if isinstance(related_uris, str):
                    self._get_reference(self.data['key'])
                else:
                    return [
                        self._get_reference(uri) for uri in related_uris
                    ]
            return super().__getitem__(key)

    def __init__(self, **config):
        pass

    def process(self, full_context: dict):
        for uri, entry in full_context['entries'].items():
            full_context['entries'][uri] = self.RelatedEntryReferenceDict(entry, full_context['entries'])

        return full_context