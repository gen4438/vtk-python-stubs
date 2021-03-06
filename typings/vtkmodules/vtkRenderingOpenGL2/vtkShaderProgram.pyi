"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkShaderProgram(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkShaderProgram - a glsl shader program
    
    Superclass: vtkObject
    
    This class contains the vertex, fragment, geometry shaders that
    combine to make a shader program
    """
    def CompiledOff(self):
        """
        V.CompiledOff()
        C++: virtual void CompiledOff()
        
        Set/Get flag for if this program is compiled
        """
        ...
    
    def CompiledOn(self):
        """
        V.CompiledOn()
        C++: virtual void CompiledOn()
        
        Set/Get flag for if this program is compiled
        """
        ...
    
    def DisableAttributeArray(self, string):
        """
        V.DisableAttributeArray(string) -> bool
        C++: bool DisableAttributeArray(const char *name)
        
        Disable the named attribute array. Return false if the attribute
        array is not contained in the linked shader program.
        """
        ...
    
    def EnableAttributeArray(self, string):
        """
        V.EnableAttributeArray(string) -> bool
        C++: bool EnableAttributeArray(const char *name)
        
        Enable the named attribute array. Return false if the attribute
        array is not contained in the linked shader program.
        """
        ...
    
    def FindAttributeArray(self, string):
        """
        V.FindAttributeArray(string) -> int
        C++: int FindAttributeArray(const char *name)
        """
        ...
    
    def FindUniform(self, string):
        """
        V.FindUniform(string) -> int
        C++: int FindUniform(const char *name)
        """
        ...
    
    def GetCompiled(self):
        """
        V.GetCompiled() -> bool
        C++: virtual bool GetCompiled()
        
        Set/Get flag for if this program is compiled
        """
        ...
    
    def GetError(self):
        """
        V.GetError() -> string
        C++: std::string GetError()
        
        Get the error message (empty if none) for the shader program.
        """
        ...
    
    def GetFileNamePrefixForDebugging(self):
        """
        V.GetFileNamePrefixForDebugging() -> string
        C++: virtual char *GetFileNamePrefixForDebugging()
        
        When developing shaders, it's often convenient to tweak the
        shader and re-render incrementally. This provides a mechanism to
        do the same. To debug any shader program, set
        `FileNamePrefixForDebugging` to a file path e.g.
        `/tmp/myshaders`. Subsequently, when `Bind()` is called on the
        shader program, it will check for files named `VS.glsl`,
        `GS.glsl` and `FS.glsl` for vertex shader, geometry shader and
        fragment shader codes respectively. If a file doesn't exist, then
        it dumps out the current code to that file. If the file exists,
        then the shader is recompiled to use the contents of that file.
        Thus, after the files have been dumped in the first render, you
        can open the files in a text editor and update as needed. On
        following render, the modified contexts from the file will be
        used.
        
        This is only intended for debugging during development and should
        not be used in production.
        """
        ...
    
    def GetFragmentShader(self):
        """
        V.GetFragmentShader() -> vtkShader
        C++: virtual vtkShader *GetFragmentShader()
        
        Get the fragment shader for this program
        """
        ...
    
    def GetGeometryShader(self):
        """
        V.GetGeometryShader() -> vtkShader
        C++: virtual vtkShader *GetGeometryShader()
        
        Get the geometry shader for this program
        """
        ...
    
    def GetHandle(self):
        """
        V.GetHandle() -> int
        C++: int GetHandle()
        
        Get the handle of the shader program.
        """
        ...
    
    def GetMD5Hash(self):
        """
        V.GetMD5Hash() -> string
        C++: std::string GetMD5Hash()
        
        Set/Get the md5 hash of this program
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
    
    def GetTransformFeedback(self):
        """
        V.GetTransformFeedback() -> vtkTransformFeedback
        C++: virtual vtkTransformFeedback *GetTransformFeedback()
        
        Get/Set a TransformFeedbackCapture object on this shader program.
        """
        ...
    
    def GetUniformGroupUpdateTime(self, p_int):
        """
        V.GetUniformGroupUpdateTime(int) -> int
        C++: vtkMTimeType GetUniformGroupUpdateTime(int)
        
        Set/Get times that can be used to track when a set of uniforms
        was last updated. This can be used to reduce redundant
        SetUniformCalls
        """
        ...
    
    def GetVertexShader(self):
        """
        V.GetVertexShader() -> vtkShader
        C++: virtual vtkShader *GetVertexShader()
        
        Get the vertex shader for this program
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
    
    def IsAttributeUsed(self, string):
        """
        V.IsAttributeUsed(string) -> bool
        C++: bool IsAttributeUsed(const char *name)
        
        Return true if the compiled and linked shader has an attribute
        matching @a name.
        """
        ...
    
    def isBound(self):
        """
        V.isBound() -> bool
        C++: bool isBound()
        
        Check if the program is currently bound, or not.
        @return True if the program is bound, false otherwise.
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
    
    def IsUniformUsed(self, string):
        """
        V.IsUniformUsed(string) -> bool
        C++: bool IsUniformUsed(const char *)
        
        methods to inquire as to what uniforms/attributes are used by
        this shader.  This can save some compute time if the uniforms or
        attributes are expensive to compute
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkShaderProgram
        C++: vtkShaderProgram *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *win)
        
        release any graphics resources this class is using.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkShaderProgram
        C++: static vtkShaderProgram *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCompiled(self, bool):
        """
        V.SetCompiled(bool)
        C++: virtual void SetCompiled(bool _arg)
        
        Set/Get flag for if this program is compiled
        """
        ...
    
    def SetFileNamePrefixForDebugging(self, string):
        """
        V.SetFileNamePrefixForDebugging(string)
        C++: virtual void SetFileNamePrefixForDebugging(const char *_arg)
        
        When developing shaders, it's often convenient to tweak the
        shader and re-render incrementally. This provides a mechanism to
        do the same. To debug any shader program, set
        `FileNamePrefixForDebugging` to a file path e.g.
        `/tmp/myshaders`. Subsequently, when `Bind()` is called on the
        shader program, it will check for files named `VS.glsl`,
        `GS.glsl` and `FS.glsl` for vertex shader, geometry shader and
        fragment shader codes respectively. If a file doesn't exist, then
        it dumps out the current code to that file. If the file exists,
        then the shader is recompiled to use the contents of that file.
        Thus, after the files have been dumped in the first render, you
        can open the files in a text editor and update as needed. On
        following render, the modified contexts from the file will be
        used.
        
        This is only intended for debugging during development and should
        not be used in production.
        """
        ...
    
    def SetFragmentShader(self, vtkShader):
        """
        V.SetFragmentShader(vtkShader)
        C++: void SetFragmentShader(vtkShader *)
        
        Get the fragment shader for this program
        """
        ...
    
    def SetGeometryShader(self, vtkShader):
        """
        V.SetGeometryShader(vtkShader)
        C++: void SetGeometryShader(vtkShader *)
        
        Get the geometry shader for this program
        """
        ...
    
    def SetMD5Hash(self, string):
        """
        V.SetMD5Hash(string)
        C++: void SetMD5Hash(const std::string &hash)
        """
        ...
    
    def SetNumberOfOutputs(self, p_int):
        """
        V.SetNumberOfOutputs(int)
        C++: virtual void SetNumberOfOutputs(unsigned int _arg)
        """
        ...
    
    def SetTransformFeedback(self, vtkTransformFeedback):
        """
        V.SetTransformFeedback(vtkTransformFeedback)
        C++: void SetTransformFeedback(vtkTransformFeedback *tfc)
        
        Get/Set a TransformFeedbackCapture object on this shader program.
        """
        ...
    
    def SetUniform1fv(self, string, p_int, float_tuple):
        """
        V.SetUniform1fv(string, int, (float, ...)) -> bool
        C++: bool SetUniform1fv(const char *name, const int count,
            const float *f)
        """
        ...
    
    def SetUniform1iv(self, string, p_int, int_tuple):
        """
        V.SetUniform1iv(string, int, (int, ...)) -> bool
        C++: bool SetUniform1iv(const char *name, const int count,
            const int *f)
        
        Set the name uniform array to f with count elements
        """
        ...
    
    def SetUniform2f(self, string, ):
        """
        V.SetUniform2f(string, (float, float)) -> bool
        C++: bool SetUniform2f(const char *name, const float v[2])
        """
        ...
    
    def SetUniform2fv(self, string, p_int, float_tuple):
        """
        V.SetUniform2fv(string, int, (float, ...)) -> bool
        C++: bool SetUniform2fv(const char *name, const int count,
            const float *f)
        """
        ...
    
    def SetUniform2i(self, string, ):
        """
        V.SetUniform2i(string, (int, int)) -> bool
        C++: bool SetUniform2i(const char *name, const int v[2])
        """
        ...
    
    def SetUniform3f(self, string, ):
        """
        V.SetUniform3f(string, (float, float, float)) -> bool
        C++: bool SetUniform3f(const char *name, const double v[3])
        """
        ...
    
    def SetUniform3fv(self, string, p_int, float_tuple):
        """
        V.SetUniform3fv(string, int, (float, ...)) -> bool
        C++: bool SetUniform3fv(const char *name, const int count,
            const float *f)
        """
        ...
    
    def SetUniform3uc(self, string, ):
        """
        V.SetUniform3uc(string, (int, int, int)) -> bool
        C++: bool SetUniform3uc(const char *name,
            const unsigned char v[3])
        """
        ...
    
    def SetUniform4f(self, string, ):
        """
        V.SetUniform4f(string, (float, float, float, float)) -> bool
        C++: bool SetUniform4f(const char *name, const float v[4])
        """
        ...
    
    def SetUniform4fv(self, string, p_int, float_tuple):
        """
        V.SetUniform4fv(string, int, (float, ...)) -> bool
        C++: bool SetUniform4fv(const char *name, const int count,
            const float *f)
        """
        ...
    
    def SetUniform4uc(self, string, ):
        """
        V.SetUniform4uc(string, (int, int, int, int)) -> bool
        C++: bool SetUniform4uc(const char *name,
            const unsigned char v[4])
        """
        ...
    
    def SetUniformf(self, string, p_float):
        """
        V.SetUniformf(string, float) -> bool
        C++: bool SetUniformf(const char *name, float v)
        """
        ...
    
    def SetUniformGroupUpdateTime(self, p_int, p_int_1):
        """
        V.SetUniformGroupUpdateTime(int, int)
        C++: void SetUniformGroupUpdateTime(int, vtkMTimeType tm)
        
        Set/Get times that can be used to track when a set of uniforms
        was last updated. This can be used to reduce redundant
        SetUniformCalls
        """
        ...
    
    def SetUniformi(self, string, p_int):
        """
        V.SetUniformi(string, int) -> bool
        C++: bool SetUniformi(const char *name, int v)
        
        Set the name uniform value to int v.
        """
        ...
    
    def SetUniformMatrix(self, string, vtkMatrix3x3):
        """
        V.SetUniformMatrix(string, vtkMatrix3x3) -> bool
        C++: bool SetUniformMatrix(const char *name, vtkMatrix3x3 *v)
        V.SetUniformMatrix(string, vtkMatrix4x4) -> bool
        C++: bool SetUniformMatrix(const char *name, vtkMatrix4x4 *v)
        """
        ...
    
    def SetUniformMatrix3x3(self, string, *float):
        """
        V.SetUniformMatrix3x3(string, [float, ...]) -> bool
        C++: bool SetUniformMatrix3x3(const char *name, float *v)
        """
        ...
    
    def SetUniformMatrix4x4(self, string, *float):
        """
        V.SetUniformMatrix4x4(string, [float, ...]) -> bool
        C++: bool SetUniformMatrix4x4(const char *name, float *v)
        """
        ...
    
    def SetUniformMatrix4x4v(self, string, p_int, *float):
        """
        V.SetUniformMatrix4x4v(string, int, [float, ...]) -> bool
        C++: bool SetUniformMatrix4x4v(const char *name, const int count,
            float *v)
        """
        ...
    
    def SetVertexShader(self, vtkShader):
        """
        V.SetVertexShader(vtkShader)
        C++: void SetVertexShader(vtkShader *)
        
        Get the vertex shader for this program
        """
        ...
    
    def Substitute(self, string, string_1, string_2, bool):
        """
        V.Substitute(string, string, string, bool) -> bool
        C++: static bool Substitute(std::string &source,
            const std::string &search, const std::string &replace,
            bool all=true)
        V.Substitute(vtkShader, string, string, bool) -> bool
        C++: static bool Substitute(vtkShader *shader,
            const std::string &search, const std::string &replace,
            bool all=true)
        
        perform in place string substitutions, indicate if a substitution
        was done this is useful for building up shader strings which
        typically involve lots of string substitutions.
        
        \param[in] shader  The source shader object to perform
            substitutions on
        \param[in] search  The string to search for
        \param[in] replace The string replacement
        \param[in] all     Whether to replace all matches or just the
            first one
        \return    A boolean indicating whether the replacement was
            successful
        """
        ...
    
    def UseAttributeArray(self, string, p_int, p_int_1, p_int_2, p_int_3, NormalizeOption):
        """
        V.UseAttributeArray(string, int, int, int, int, NormalizeOption)
            -> bool
        C++: bool UseAttributeArray(const char *name, int offset,
            size_t stride, int elementType, int elementTupleSize,
            NormalizeOption normalize)
        
        Use the named attribute array with the bound BufferObject.
        @param name of the attribute (as seen in the shader program).
        @param offset into the bound BufferObject.
        @param stride The stride of the element access (i.e. the size of
            each
        element in the currently bound BufferObject). 0 may be used to
        indicate tightly packed data.
        @param elementType Tag identifying the memory representation of
            the
        element.
        @param elementTupleSize The number of elements per vertex (e.g. a
        3D
        position attribute would be 3).
        @param normalize Indicates the range used by the attribute data.
        See NormalizeOption for more information.
        @return false if the attribute array does not exist.
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
    CameraGroup = ...
    LightingGroup = ...
    NoNormalize = ...
    Normalize = ...
    NormalizeOption = ...
    UniformGroups = ...
    UserGroup = ...
    __dict__ = ...
    __vtkname__ = ...


