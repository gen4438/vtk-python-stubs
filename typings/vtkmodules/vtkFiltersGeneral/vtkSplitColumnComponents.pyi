"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkSplitColumnComponents(__vtkmodules_vtkCommonExecutionModel.vtkTableAlgorithm):
    """
    vtkSplitColumnComponents - split multicomponent table columns
    
    Superclass: vtkTableAlgorithm
    
    Splits any columns in a table that have more than one component into
    individual columns. Single component columns are passed through
    without any data duplication. NamingMode can be used to control how
    columns with multiple components are labelled in the output, e.g., if
    column names "Points" had three components this column would be split
    into "Points (0)", "Points (1)", and Points (2)" when NamingMode is
    NUMBERS_WITH_PARENS, into Points_0, Points_1, and Points_2 when
    NamingMode is NUMBERS_WITH_UNDERSCORES, into "Points (X)", "Points
    (Y)", and "Points (Z)" when NamingMode is NAMES_WITH_PARENS, and into
    Points_X, Points_Y, and Points_Z when NamingMode is
    NAMES_WITH_UNDERSCORES.
    """
    def CalculateMagnitudesOff(self):
        """
        V.CalculateMagnitudesOff()
        C++: virtual void CalculateMagnitudesOff()
        
        If on this filter will calculate an additional magnitude column
        for all columns it splits with two or more components. Default is
        on.
        """
        ...
    
    def CalculateMagnitudesOn(self):
        """
        V.CalculateMagnitudesOn()
        C++: virtual void CalculateMagnitudesOn()
        
        If on this filter will calculate an additional magnitude column
        for all columns it splits with two or more components. Default is
        on.
        """
        ...
    
    def GetCalculateMagnitudes(self):
        """
        V.GetCalculateMagnitudes() -> bool
        C++: virtual bool GetCalculateMagnitudes()
        
        If on this filter will calculate an additional magnitude column
        for all columns it splits with two or more components. Default is
        on.
        """
        ...
    
    def GetNamingMode(self):
        """
        V.GetNamingMode() -> int
        C++: virtual int GetNamingMode()
        
        Get/Set the array naming mode. Description is
        NUMBERS_WITH_PARENS.
        """
        ...
    
    def GetNamingModeMaxValue(self):
        """
        V.GetNamingModeMaxValue() -> int
        C++: virtual int GetNamingModeMaxValue()
        
        Get/Set the array naming mode. Description is
        NUMBERS_WITH_PARENS.
        """
        ...
    
    def GetNamingModeMinValue(self):
        """
        V.GetNamingModeMinValue() -> int
        C++: virtual int GetNamingModeMinValue()
        
        Get/Set the array naming mode. Description is
        NUMBERS_WITH_PARENS.
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
        V.NewInstance() -> vtkSplitColumnComponents
        C++: vtkSplitColumnComponents *NewInstance()
        """
        ...
    
    def ORIGINAL_ARRAY_NAME(self):
        """
        V.ORIGINAL_ARRAY_NAME() -> vtkInformationStringKey
        C++: static vtkInformationStringKey *ORIGINAL_ARRAY_NAME()
        
        These are keys that get added to each output array to make it
        easier for downstream filters to know which output array were
        extracted from which input array.
        
        If either of these keys are missing, then the array was not
        extracted at all.
        
        `ORIGINAL_COMPONENT_NUMBER` of -1 indicates magnitude.
        """
        ...
    
    def ORIGINAL_COMPONENT_NUMBER(self):
        """
        V.ORIGINAL_COMPONENT_NUMBER() -> vtkInformationIntegerKey
        C++: static vtkInformationIntegerKey *ORIGINAL_COMPONENT_NUMBER()
        
        These are keys that get added to each output array to make it
        easier for downstream filters to know which output array were
        extracted from which input array.
        
        If either of these keys are missing, then the array was not
        extracted at all.
        
        `ORIGINAL_COMPONENT_NUMBER` of -1 indicates magnitude.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSplitColumnComponents
        C++: static vtkSplitColumnComponents *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetCalculateMagnitudes(self, bool):
        """
        V.SetCalculateMagnitudes(bool)
        C++: virtual void SetCalculateMagnitudes(bool _arg)
        
        If on this filter will calculate an additional magnitude column
        for all columns it splits with two or more components. Default is
        on.
        """
        ...
    
    def SetNamingMode(self, p_int):
        """
        V.SetNamingMode(int)
        C++: virtual void SetNamingMode(int _arg)
        
        Get/Set the array naming mode. Description is
        NUMBERS_WITH_PARENS.
        """
        ...
    
    def SetNamingModeToNamesWithParens(self):
        """
        V.SetNamingModeToNamesWithParens()
        C++: void SetNamingModeToNamesWithParens()
        
        Get/Set the array naming mode. Description is
        NUMBERS_WITH_PARENS.
        """
        ...
    
    def SetNamingModeToNamesWithUnderscores(self):
        """
        V.SetNamingModeToNamesWithUnderscores()
        C++: void SetNamingModeToNamesWithUnderscores()
        
        Get/Set the array naming mode. Description is
        NUMBERS_WITH_PARENS.
        """
        ...
    
    def SetNamingModeToNumberWithParens(self):
        """
        V.SetNamingModeToNumberWithParens()
        C++: void SetNamingModeToNumberWithParens()
        
        Get/Set the array naming mode. Description is
        NUMBERS_WITH_PARENS.
        """
        ...
    
    def SetNamingModeToNumberWithUnderscores(self):
        """
        V.SetNamingModeToNumberWithUnderscores()
        C++: void SetNamingModeToNumberWithUnderscores()
        
        Get/Set the array naming mode. Description is
        NUMBERS_WITH_PARENS.
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
    NAMES_WITH_PARENS = ...
    NAMES_WITH_UNDERSCORES = ...
    NUMBERS_WITH_PARENS = ...
    NUMBERS_WITH_UNDERSCORES = ...
    __dict__ = ...
    __vtkname__ = ...


