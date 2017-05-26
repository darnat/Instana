from .base import BaseCollection


class Medias(BaseCollection):
    """
    Medias Collection
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the Collection Medias
        """
        super().__init__(*args, **kwargs)
        self._next_max_id = None
