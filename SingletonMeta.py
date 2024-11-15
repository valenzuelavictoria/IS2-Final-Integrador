class SingletonMeta(type):
    """ Metaclase para implementar Singleton. """
    _instances = {}

    def _call_(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super()._call_(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]