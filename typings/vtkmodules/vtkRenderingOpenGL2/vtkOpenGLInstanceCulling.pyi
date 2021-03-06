"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkOpenGLInstanceCulling(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkOpenGLInstanceCulling - Frustum culling and LOD management.
    
    Superclass: vtkObject
    
    This class is used to cull instances based on their transformation
    matrix. It was designed to improve performances when there is large
    number of instances in vtkOpenGLGlyph3DMapper.
    
    Each instance is tested on the GPU through vertex shader to know if
    it is inside of the frustum view. If it is, the distance to the
    camera is computed to select and send to the geometry shader the
    corresponding LOD index. The geometry shader register the instance to
    the corresponding vertex stream and therefore the corresponding
    transform feedback buffer in video memory.
    
    @warning   GL_ARB_gpu_shader5 extension is required.
    
    {.cpp}
    
    vtkNewculling; vtkIdType nbInstances = 1000000;
    
    // buffer of size 16*nbInstances containing transform matrices.
    vtkOpenGLBufferObject* bufferMatrix = ...;
    
    // buffer of size 4*nbInstances containing color buffer to pass
    through. vtkOpenGLBufferObject* bufferColor = ...;
    
    // Initialize LODs culling->InitLOD(polydata); // LOD0 : full
    geometry culling->AddLOD(2.0, 0.5); // LOD1 : after 2.0, 50%
    triangles culling->AddLOD(5.0, 0.99); // LOD2 : after 5.0, 1%
    triangles
    
    // Build shader and binds culling->BuildCullingShaders(ren, actor,
    nbInstances); culling->RunCullingShaders(nbInstances, bufferMatrix,
    bufferColor);
    
    // Get number of instances in LOD 0 int nbInstInLOD0 =
    culling->GetLOD(0).NumberOfInstances;
    
    // Get VBO and IBO of LOD 1 vtkOpenGLBufferObject* VBO1 =
    culling->GetLOD(1).PositionVBO; vtkOpenGLBufferObject* IBO1 =
    culling->GetLOD(1).IBO;
    
    // Get instances buffer of LOD 2 // buffer is interleaved [
    transformMatrix0 color0 transformMatrix1 color1 ... ]
    vtkOpenGLBufferObject* buffer2 = culling->GetLODBuffer(2);
    """
    def AddLOD(self, p_float, p_float_1):
        """
        V.AddLOD(float, float)
        C++: void AddLOD(float distance, float targetReduction)
        
        Add a level of detail. distance is the distance after which LOD
        is enabled targetReduction is the reduction factor applied on
        polydata (vtkDecimatePro is used)
        
        @sa vtkDecimatePro::SetTargetReduction
        """
        ...
    
    def BuildCullingShaders(self, vtkOpenGLShaderCache, p_int, bool):
        """
        V.BuildCullingShaders(vtkOpenGLShaderCache, int, bool)
        C++: void BuildCullingShaders(vtkOpenGLShaderCache *cache,
            vtkIdType numInstances, bool withNormals)
        
        Build culling shader program (if not created yet) and binds it.
        """
        ...
    
    def GetColorLOD(self):
        """
        V.GetColorLOD() -> bool
        C++: virtual bool GetColorLOD()
        
        Overload color with unique color per LOD.
        """
        ...
    
    def GetHelper(self):
        """
        V.GetHelper() -> vtkOpenGLHelper
        C++: vtkOpenGLHelper &GetHelper()
        
        Get helper structure.
        """
        ...
    
    def GetLODBuffer(self, p_int):
        """
        V.GetLODBuffer(int) -> vtkOpenGLBufferObject
        C++: vtkOpenGLBufferObject *GetLODBuffer(vtkIdType index)
        
        Get the transform feedback buffer generated by the culling
        program.
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
    
    def GetNumberOfLOD(self):
        """
        V.GetNumberOfLOD() -> int
        C++: vtkIdType GetNumberOfLOD()
        
        Get number of LOD currently declared.
        """
        ...
    
    def InitLOD(self, vtkPolyData):
        """
        V.InitLOD(vtkPolyData)
        C++: void InitLOD(vtkPolyData *pd)
        
        Initialize LOD with a polydata
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
        V.NewInstance() -> vtkOpenGLInstanceCulling
        C++: vtkOpenGLInstanceCulling *NewInstance()
        """
        ...
    
    def RunCullingShaders(self, p_int, vtkOpenGLBufferObject, vtkOpenGLBufferObject_1, vtkOpenGLBufferObject_2):
        """
        V.RunCullingShaders(int, vtkOpenGLBufferObject,
            vtkOpenGLBufferObject, vtkOpenGLBufferObject)
        C++: void RunCullingShaders(vtkIdType numInstances,
            vtkOpenGLBufferObject *matrixBuffer,
            vtkOpenGLBufferObject *colorBuffer,
            vtkOpenGLBufferObject *normalBuffer)
        
        Run the culling program and generate LOD buffers.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOpenGLInstanceCulling
        C++: static vtkOpenGLInstanceCulling *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetColorLOD(self, bool):
        """
        V.SetColorLOD(bool)
        C++: virtual void SetColorLOD(bool _arg)
        
        Overload color with unique color per LOD.
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


