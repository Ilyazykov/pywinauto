import ctypes

class AtSpiElementInfo(ElementInfo):
    
    """Wrapper for at-spi"""
    
    def __init__(self, handle = None):
        """Create element by handle"""
        raise NotImplementedError()
    
    def set_cache_strategy(self, cached):
        """Set a cache strategy for frequently used attributes of the element"""
        raise NotImplementedError()
    
        @property
    def handle(self):
        "Return the handle of the element"
        raise NotImplementedError()

    @property
    def name(self):
        "Return the name of the element"
        raise NotImplementedError()

    @property
    def rich_text(self):
        "Return the text of the element"
        raise NotImplementedError()

    @property
    def control_id(self):
        "Return the ID of the control"
        raise NotImplementedError()

    @property
    def process_id(self):
        "Return the ID of process that controls this element"
        raise NotImplementedError()

    @property
    def framework_id(self):
        "Return the framework of the element"
        raise NotImplementedError()
    
    @property
    def class_name(self):
        "Return the class name of the element"
        raise NotImplementedError()

    @property
    def enabled(self):
        "Return True if the element is enabled"
        raise NotImplementedError()
        
    @property
    def visible(self):
        "Return True if the element is visible"
        raise NotImplementedError()
       
    @property
    def parent(self):
        "Return the parent of the element"
        raise NotImplementedError()

    def children(self, **kwargs):
        "Return children of the element"
        raise NotImplementedError()

    def descendants(self, **kwargs):
        "Return descendants of the element"
        raise NotImplementedError()

    @property
    def rectangle(self):
        "Return rectangle of element"
        raise NotImplementedError()

    def dump_window(self):
        "Dump an element to a set of properties"
        raise NotImplementedError()