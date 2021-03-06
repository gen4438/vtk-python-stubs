"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore
import vtkmodules.vtkRenderingCore as __vtkmodules_vtkRenderingCore

VTK_SKIP_RETURN_CODE = ...
class vtkTesting(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkTesting - a unified VTK regression testing framework
    
    Superclass: vtkObject
    
    This is a VTK regression testing framework. Looks like this:
    
    
     vtkTesting* t = vtkTesting::New();
    
    
     Two options for setting arguments
    
    
     Option 1:
     for ( cc = 1; cc < argc; cc ++ )
       {
       t->AddArgument(argv[cc]);
       }
    
    
     Option 2:
     t->AddArgument("-D");
     t->AddArgument(my_data_dir);
     t->AddArgument("-V");
     t->AddArgument(my_valid_image);
    
    
     ...
    
    
     Two options of doing testing:
    
    
     Option 1:
     t->SetRenderWindow(renWin);
     int res = t->RegressionTest(threshold);
    
    
     Option 2:
     int res = t->RegressionTest(test_image, threshold);
    
    
     ...
    
    
     if (res == vtkTesting::PASSED)
       {
       Test passed
       }
     else
       {
       Test failed
       }
    """
    def AddArgument(self, string):
        """
        V.AddArgument(string)
        C++: void AddArgument(const char *argv)
        
        Pass the command line arguments into this class to be processed.
        Many of the Get methods such as GetValidImage and GetBaselineRoot
        rely on the arguments to be passed in prior to retrieving these
        values. Just call AddArgument for each argument that was passed
        into the command line
        """
        ...
    
    def CleanArguments(self):
        """
        V.CleanArguments()
        C++: void CleanArguments()
        
        This method delete all arguments in vtkTesting, this way you can
        reuse it in a loop where you would have multiple testing.
        """
        ...
    
    def CompareAverageOfL2Norm(self, vtkDataSet, vtkDataSet_1, p_float):
        """
        V.CompareAverageOfL2Norm(vtkDataSet, vtkDataSet, float) -> int
        C++: int CompareAverageOfL2Norm(vtkDataSet *pdA, vtkDataSet *pdB,
            double tol)
        V.CompareAverageOfL2Norm(vtkDataArray, vtkDataArray, float) -> int
        C++: int CompareAverageOfL2Norm(vtkDataArray *daA,
            vtkDataArray *daB, double tol)
        
        Compute the average L2 norm between all point data data arrays of
        types float and double present in the data sets "dsA" and "dsB"
        (this includes instances of vtkPoints) Compare the result of each
        L2 comutation to "tol".
        """
        ...
    
    def FrontBufferOff(self):
        """
        V.FrontBufferOff()
        C++: virtual void FrontBufferOff()
        
        Use the front buffer first for regression test comparisons. By
        default use back buffer first, then try the front buffer if the
        test fails when comparing to the back buffer.
        """
        ...
    
    def FrontBufferOn(self):
        """
        V.FrontBufferOn()
        C++: virtual void FrontBufferOn()
        
        Use the front buffer first for regression test comparisons. By
        default use back buffer first, then try the front buffer if the
        test fails when comparing to the back buffer.
        """
        ...
    
    def GetArgument(self, string):
        """
        V.GetArgument(string) -> string
        C++: char *GetArgument(const char *arg)
        
        Search for a specific argument by name and return its value
        (assumed to be the next on the command tail). Up to caller to
        delete the returned string.
        """
        ...
    
    def GetBorderOffset(self):
        """
        V.GetBorderOffset() -> int
        C++: virtual int GetBorderOffset()
        
        Number of pixels added as borders to avoid problems with window
        decorations added by some window managers.
        """
        ...
    
    def GetDataRoot(self):
        """
        V.GetDataRoot() -> string
        C++: const char *GetDataRoot()
        
        Get some parameters from the command line arguments, env, or
        defaults
        """
        ...
    
    def GetFrontBuffer(self):
        """
        V.GetFrontBuffer() -> int
        C++: virtual vtkTypeBool GetFrontBuffer()
        
        Use the front buffer first for regression test comparisons. By
        default use back buffer first, then try the front buffer if the
        test fails when comparing to the back buffer.
        """
        ...
    
    def GetImageDifference(self):
        """
        V.GetImageDifference() -> float
        C++: virtual double GetImageDifference()
        
        Get the image difference.
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
    
    def GetRenderWindow(self):
        """
        V.GetRenderWindow() -> vtkRenderWindow
        C++: virtual vtkRenderWindow *GetRenderWindow()
        
        Set and get the render window that will be used for regression
        testing.
        """
        ...
    
    def GetTempDirectory(self):
        """
        V.GetTempDirectory() -> string
        C++: const char *GetTempDirectory()
        
        Get some parameters from the command line arguments, env, or
        defaults
        """
        ...
    
    def GetValidImageFileName(self):
        """
        V.GetValidImageFileName() -> string
        C++: const char *GetValidImageFileName()
        
        Set/Get the name of the valid image file
        """
        ...
    
    def GetVerbose(self):
        """
        V.GetVerbose() -> int
        C++: virtual int GetVerbose()
        
        Get/Set verbosity level. A level of 0 is quiet.
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
    
    def IsFlagSpecified(self, string):
        """
        V.IsFlagSpecified(string) -> int
        C++: int IsFlagSpecified(const char *flag)
        
        Is some arbitrary user flag ("-X", "-Z" etc) specified
        """
        ...
    
    def IsInteractiveModeSpecified(self):
        """
        V.IsInteractiveModeSpecified() -> int
        C++: int IsInteractiveModeSpecified()
        
        Is the interactive mode specified?
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
    
    def IsValidImageSpecified(self):
        """
        V.IsValidImageSpecified() -> int
        C++: int IsValidImageSpecified()
        
        Is a valid image specified on the command line areguments?
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkTesting
        C++: vtkTesting *NewInstance()
        """
        ...
    
    def RegressionTest(self, p_float):
        """
        V.RegressionTest(float) -> int
        C++: virtual int RegressionTest(double thresh)
        V.RegressionTest(string, float) -> int
        C++: virtual int RegressionTest(const std::string &pngFileName,
            double thresh)
        V.RegressionTest(vtkAlgorithm, float) -> int
        C++: virtual int RegressionTest(vtkAlgorithm *imageSource,
            double thresh)
        
        Perform the test and return the result. Delegates to
        RegressionTestAndCaptureOutput, sending the output to cout.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTesting
        C++: static vtkTesting *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetBorderOffset(self, p_int):
        """
        V.SetBorderOffset(int)
        C++: virtual void SetBorderOffset(int _arg)
        
        Number of pixels added as borders to avoid problems with window
        decorations added by some window managers.
        """
        ...
    
    def SetDataRoot(self, string):
        """
        V.SetDataRoot(string)
        C++: virtual void SetDataRoot(const char *_arg)
        
        Get some parameters from the command line arguments, env, or
        defaults
        """
        ...
    
    def SetFrontBuffer(self, p_int):
        """
        V.SetFrontBuffer(int)
        C++: void SetFrontBuffer(vtkTypeBool frontBuffer)
        
        Use the front buffer first for regression test comparisons. By
        default use back buffer first, then try the front buffer if the
        test fails when comparing to the back buffer.
        """
        ...
    
    def SetRenderWindow(self, vtkRenderWindow):
        """
        V.SetRenderWindow(vtkRenderWindow)
        C++: virtual void SetRenderWindow(vtkRenderWindow *rw)
        
        Set and get the render window that will be used for regression
        testing.
        """
        ...
    
    def SetTempDirectory(self, string):
        """
        V.SetTempDirectory(string)
        C++: virtual void SetTempDirectory(const char *_arg)
        
        Get some parameters from the command line arguments, env, or
        defaults
        """
        ...
    
    def SetValidImageFileName(self, string):
        """
        V.SetValidImageFileName(string)
        C++: virtual void SetValidImageFileName(const char *_arg)
        
        Set/Get the name of the valid image file
        """
        ...
    
    def SetVerbose(self, p_int):
        """
        V.SetVerbose(int)
        C++: virtual void SetVerbose(int _arg)
        
        Get/Set verbosity level. A level of 0 is quiet.
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
    DO_INTERACTOR = ...
    FAILED = ...
    NOT_RUN = ...
    PASSED = ...
    ReturnValue = ...
    __dict__ = ...
    __vtkname__ = ...


class vtkTestingInteractor(__vtkmodules_vtkRenderingCore.vtkRenderWindowInteractor):
    """
    vtkTestingInteractor - A RenderWindowInteractor for testing
    
    Superclass: vtkRenderWindowInteractor
    
    Provides a Start() method that passes arguments to a test for
    regression testing and returns. This permits programs that run as
    tests to exit gracefully during the test run without needing
    interaction.
    @sa
    vtkTestingObjectFactory
    """
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Type and printing information.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Type and printing information.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Type and printing information.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Type and printing information.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkTestingInteractor
        C++: vtkTestingInteractor *NewInstance()
        
        Type and printing information.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTestingInteractor
        C++: static vtkTestingInteractor *SafeDownCast(vtkObjectBase *o)
        
        Type and printing information.
        """
        ...
    
    def Start(self):
        """
        V.Start()
        C++: void Start() override;
        
        Start the event loop. This is provided so that you do not have to
        implement your own event loop. You still can use your own event
        loop if you want.
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


class vtkTestingObjectFactory(__vtkmodules_vtkCommonCore.vtkObjectFactory):
    """
    vtkTestingObjectFactory - Object overrides used during testing
    
    Superclass: vtkObjectFactory
    
    Some vtk examples and tests need to perform differently when they are
    run as tests versus when they are run as individual programs. Many
    tests/examples are interactive and eventually call
    vtkRenderWindowInteration::Start() to initialie the interaction. But,
    when run as tests, these programs should exit. This factory overrides
    vtkRenderWindowInteractor so that the Start() method just returns. To
    use this factory:
    """
    def GetDescription(self):
        """
        V.GetDescription() -> string
        C++: const char *GetDescription() override;
        
        Return a descriptive string describing the factory.
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
    
    def GetVTKSourceVersion(self):
        """
        V.GetVTKSourceVersion() -> string
        C++: const char *GetVTKSourceVersion() override;
        
        All sub-classes of vtkObjectFactory should must return the
        version of VTK they were built with.  This should be implemented
        with the macro VTK_SOURCE_VERSION and NOT a call to
        vtkVersion::GetVTKSourceVersion. As the version needs to be
        compiled into the file as a string constant. This is critical to
        determine possible incompatible dynamic factory loads.
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
        V.NewInstance() -> vtkTestingObjectFactory
        C++: vtkTestingObjectFactory *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTestingObjectFactory
        C++: static vtkTestingObjectFactory *SafeDownCast(
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


__loader__ = ...
__spec__ = ...
