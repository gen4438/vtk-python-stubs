"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkOpenGLVertexArrayObject(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkOpenGLVertexArrayObject - The VertexArrayObject class uses, or
    emulates, vertex array objects.
    
    Superclass: vtkObject
    
    These are extremely useful for setup/tear down of vertex attributes,
    and can offer significant performance benefits when the hardware
    supports them.
    
    It should be noted that this object is very lightweight, and it
    assumes the objects being used are correctly set up. Even without
    support for VAOs this class caches the array locations, types, etc
    and avoids repeated look ups. It it bound to a single ShaderProgram
    object.
    """
    def AddAttributeArray(self, vtkShaderProgram, vtkOpenGLBufferObject, string, p_int, p_int_1, p_int_2, p_int_3, bool):
        """
        V.AddAttributeArray(vtkShaderProgram, vtkOpenGLBufferObject,
            string, int, int, int, int, bool) -> bool
        C++: bool AddAttributeArray(vtkShaderProgram *program,
            vtkOpenGLBufferObject *buffer, const std::string &name,
            int offset, size_t stride, int elementType,
            int elementTupleSize, bool normalize)
        V.AddAttributeArray(vtkShaderProgram, vtkOpenGLVertexBufferObject,
             string, int, bool) -> bool
        C++: bool AddAttributeArray(vtkShaderProgram *program,
            vtkOpenGLVertexBufferObject *buffer, const std::string &name,
            int offset, bool normalize)
        """
        ...
    
    def AddAttributeArrayWithDivisor(self, vtkShaderProgram, vtkOpenGLBufferObject, string, p_int, p_int_1, p_int_2, p_int_3, bool, p_int_4, bool_1):
        """
        V.AddAttributeArrayWithDivisor(vtkShaderProgram,
            vtkOpenGLBufferObject, string, int, int, int, int, bool, int,
            bool) -> bool
        C++: bool AddAttributeArrayWithDivisor(vtkShaderProgram *program,
            vtkOpenGLBufferObject *buffer, const std::string &name,
            int offset, size_t stride, int elementType,
            int elementTupleSize, bool normalize, int divisor,
            bool isMatrix)
        """
        ...
    
    def AddAttributeMatrixWithDivisor(self, vtkShaderProgram, vtkOpenGLBufferObject, string, p_int, p_int_1, p_int_2, p_int_3, bool, p_int_4, p_int_5):
        """
        V.AddAttributeMatrixWithDivisor(vtkShaderProgram,
            vtkOpenGLBufferObject, string, int, int, int, int, bool, int,
            int) -> bool
        C++: bool AddAttributeMatrixWithDivisor(vtkShaderProgram *program,
             vtkOpenGLBufferObject *buffer, const std::string &name,
            int offset, size_t stride, int elementType,
            int elementTupleSize, bool normalize, int divisor,
            int tupleOffset)
        """
        ...
    
    def Bind(self):
        """
        V.Bind()
        C++: void Bind()
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
        V.NewInstance() -> vtkOpenGLVertexArrayObject
        C++: vtkOpenGLVertexArrayObject *NewInstance()
        """
        ...
    
    def Release(self):
        """
        V.Release()
        C++: void Release()
        """
        ...
    
    def ReleaseGraphicsResources(self):
        """
        V.ReleaseGraphicsResources()
        C++: void ReleaseGraphicsResources()
        """
        ...
    
    def RemoveAttributeArray(self, string):
        """
        V.RemoveAttributeArray(string) -> bool
        C++: bool RemoveAttributeArray(const std::string &name)
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOpenGLVertexArrayObject
        C++: static vtkOpenGLVertexArrayObject *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetForceEmulation(self, bool):
        """
        V.SetForceEmulation(bool)
        C++: void SetForceEmulation(bool val)
        """
        ...
    
    def ShaderProgramChanged(self):
        """
        V.ShaderProgramChanged()
        C++: void ShaderProgramChanged()
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

