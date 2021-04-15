"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkOpenGLVertexBufferObjectCache(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkOpenGLVertexBufferObjectCache - manage vertex buffer objects
    shared within a context
    
    Superclass: vtkObject
    
    This class allows mappers to share VBOs. Specifically it is used by
    the V..B..O..Group to see if a VBO already exists for a given
    vtkDataArray.
    """
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
    
    def GetVBO(self, vtkDataArray, p_int):
        """
        V.GetVBO(vtkDataArray, int) -> vtkOpenGLVertexBufferObject
        C++: vtkOpenGLVertexBufferObject *GetVBO(vtkDataArray *array,
            int destType)
        
        Returns the vertex buffer object which holds the data array's
        data. If such a VBO does not exist a new empty VBO will be
        created you need to append to. The return value has been
        registered, you are responsible for deleting it. The data array
        pointers are also registered.
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
        V.NewInstance() -> vtkOpenGLVertexBufferObjectCache
        C++: vtkOpenGLVertexBufferObjectCache *NewInstance()
        """
        ...
    
    def RemoveVBO(self, vtkOpenGLVertexBufferObject):
        """
        V.RemoveVBO(vtkOpenGLVertexBufferObject)
        C++: void RemoveVBO(vtkOpenGLVertexBufferObject *vbo)
        
        Removes all references to a given vertex buffer object.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOpenGLVertexBufferObjectCache
        C++: static vtkOpenGLVertexBufferObjectCache *SafeDownCast(
            vtkObjectBase *o)
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


