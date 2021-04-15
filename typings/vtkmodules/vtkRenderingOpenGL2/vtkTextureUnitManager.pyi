"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkTextureUnitManager(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkTextureUnitManager - allocate/free texture units.
    
    Superclass: vtkObject
    
    vtkTextureUnitManager is a central place used by shaders to reserve a
    texture unit ( Allocate() ) or release it ( Free() ).
    
    Don't create a vtkTextureUnitManager, query it from the
    vtkOpenGLRenderWindow
    
    @sa
    vtkOpenGLRenderWindow
    """
    def Allocate(self):
        """
        V.Allocate() -> int
        C++: virtual int Allocate()
        V.Allocate(int) -> int
        C++: virtual int Allocate(int unit)
        
        Reserve a texture unit. It returns its number. It returns -1 if
        the allocation failed (because there are no more texture units
        left).
        \post valid_result: result==-1 || result>=0 &&
            result<this->GetNumberOfTextureUnits())
        \post allocated: result==-1 || this->IsAllocated(result)
        """
        ...
    
    def Free(self, p_int):
        """
        V.Free(int)
        C++: virtual void Free(int textureUnitId)
        
        Release a texture unit.
        \pre valid_textureUnitId: textureUnitId>=0 &&
            textureUnitId<this->GetNumberOfTextureUnits()
        \pre allocated_textureUnitId: this->IsAllocated(textureUnitId)
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
    
    def GetNumberOfTextureUnits(self):
        """
        V.GetNumberOfTextureUnits() -> int
        C++: int GetNumberOfTextureUnits()
        
        Number of texture units supported by the OpenGL context.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize()
        
        Update the number of hardware texture units for the current
        context
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
    
    def IsAllocated(self, p_int):
        """
        V.IsAllocated(int) -> bool
        C++: bool IsAllocated(int textureUnitId)
        
        Tell if texture unit `textureUnitId' is already allocated.
        \pre valid_textureUnitId_range : textureUnitId>=0 &&
        textureUnitId<this->GetNumberOfTextureUnits()
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
        V.NewInstance() -> vtkTextureUnitManager
        C++: vtkTextureUnitManager *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTextureUnitManager
        C++: static vtkTextureUnitManager *SafeDownCast(vtkObjectBase *o)
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


