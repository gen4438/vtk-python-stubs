"""
This type stub file was generated by pyright.
"""

from .vtkObject import vtkObject

class vtkPriorityQueue(vtkObject):
    """
    vtkPriorityQueue - a list of ids arranged in priority order
    
    Superclass: vtkObject
    
    vtkPriorityQueue is a general object for creating and manipulating
    lists of object ids (e.g., point or cell ids). Object ids are sorted
    according to a user-specified priority, where entries at the top of
    the queue have the smallest values.
    
    This implementation provides a feature beyond the usual ability to
    insert and retrieve (or pop) values from the queue. It is also
    possible to pop any item in the queue given its id number. This
    allows you to delete entries in the queue which can useful for
    reinserting an item into the queue.
    
    @warning
    This implementation is a variation of the priority queue described in "Data Structures &
    Algorithms" by Aho, Hopcroft, Ullman. It creates a balanced,
    partially ordered binary tree implemented as an ordered array. This
    avoids the overhead associated with parent/child pointers, and
    frequent memory allocation and deallocation.
    """
    def Allocate(self, p_int, p_int_1):
        """
        V.Allocate(int, int)
        C++: void Allocate(vtkIdType sz, vtkIdType ext=1000)
        
        Allocate initial space for priority queue.
        """
        ...
    
    def DeleteId(self, p_int):
        """
        V.DeleteId(int) -> float
        C++: double DeleteId(vtkIdType id)
        
        Delete entry in queue with specified id. Returns priority value
        associated with that id; or VTK_DOUBLE_MAX if not in queue.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Given a the name of a base class of this class type, return the
        distance of inheritance between this class type and the named
        class (how many generations of inheritance are there between this
        class and the named class). If the named class is not in this
        class's inheritance tree, return a negative value. Valid
        responses will always be nonnegative. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Given a the name of a base class of this class type, return the
        distance of inheritance between this class type and the named
        class (how many generations of inheritance are there between this
        class and the named class). If the named class is not in this
        class's inheritance tree, return a negative value. Valid
        responses will always be nonnegative. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def GetNumberOfItems(self):
        """
        V.GetNumberOfItems() -> int
        C++: vtkIdType GetNumberOfItems()
        
        Return the number of items in this queue.
        """
        ...
    
    def GetPriority(self, p_int):
        """
        V.GetPriority(int) -> float
        C++: double GetPriority(vtkIdType id)
        
        Get the priority of an entry in the queue with specified id.
        Returns priority value of that id or VTK_DOUBLE_MAX if not in
        queue.
        """
        ...
    
    def Insert(self, p_float, p_int):
        """
        V.Insert(float, int)
        C++: void Insert(double priority, vtkIdType id)
        
        Insert id with priority specified. The id is generally an index
        like a point id or cell id.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Return 1 if this class is the same type of (or a subclass of) the
        named class. Returns 0 otherwise. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Return 1 if this class type is the same type of (or a subclass
        of) the named class. Returns 0 otherwise. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkPriorityQueue
        C++: vtkPriorityQueue *NewInstance()
        """
        ...
    
    def Peek(self, p_int, p_float):
        """
        V.Peek(int, float) -> int
        C++: vtkIdType Peek(vtkIdType location, double &priority)
        V.Peek(int) -> int
        C++: vtkIdType Peek(vtkIdType location=0)
        
        Peek into the queue without actually removing anything. Returns
        the id and the priority.
        """
        ...
    
    def Pop(self, p_int, p_float):
        """
        V.Pop(int, float) -> int
        C++: vtkIdType Pop(vtkIdType location, double &priority)
        V.Pop(int) -> int
        C++: vtkIdType Pop(vtkIdType location=0)
        
        Removes item at specified location from tree; then reorders and
        balances tree. The location == 0 is the root of the tree. If
        queue is exhausted, then a value < 0 is returned. (Note: the
        location is not the same as deleting an id; id is mapped to
        location.)
        """
        ...
    
    def Reset(self):
        """
        V.Reset()
        C++: void Reset()
        
        Empty the queue but without releasing memory. This avoids the
        overhead of memory allocation/deletion.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPriorityQueue
        C++: static vtkPriorityQueue *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def __delattr__(self, *args, **kwargs):
        """ Implement delattr(self, name). """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        ...
    
    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        ...
    
    def __setattr__(self, *args, **kwargs):
        """ Implement setattr(self, name, value). """
        ...
    
    def __str__(self, *args, **kwargs) -> str:
        """ Return str(self). """
        ...
    
    __this__ = ...
    __dict__ = ...
    __vtkname__ = ...


