"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkExtractSelectedArraysOverTime(__vtkmodules_vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    """
    vtkExtractSelectedArraysOverTime - extracts a selection over time.
    
    Superclass: vtkMultiBlockDataSetAlgorithm
    
    vtkExtractSelectedArraysOverTime extracts a selection over time. This
    is combination of two filters, an vtkExtractSelection filter followed
    by vtkExtractDataArraysOverTime, to do its work.
    
    The filter has two inputs - 0th input is the temporal data to
    extracted, while the second input is the selection (vtkSelection) to
    extract. Based on the type of the selection, this filter setups up
    properties on the internal vtkExtractDataArraysOverTime instance to
    produce a reasonable extract.
    
    The output is a vtkMultiBlockDataSet. See
    vtkExtractDataArraysOverTime for details on how the output is
    structured.
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
    
    def GetNumberOfTimeSteps(self):
        """
        V.GetNumberOfTimeSteps() -> int
        C++: virtual int GetNumberOfTimeSteps()
        
        Get the number of time steps
        """
        ...
    
    def GetReportStatisticsOnly(self):
        """
        V.GetReportStatisticsOnly() -> bool
        C++: virtual bool GetReportStatisticsOnly()
        
        Instead of breaking a selection into a separate time-history
        table for each (block,ID)-tuple, you may call
        ReportStatisticsOnlyOn(). Then a single table per block of the
        input dataset will report the minimum, maximum, quartiles, and
        (for numerical arrays) the average and standard deviation of the
        selection over time.
        
        * The default is off to preserve backwards-compatibility.
        """
        ...
    
    def GetSelectionExtractor(self):
        """
        V.GetSelectionExtractor() -> vtkExtractSelection
        C++: vtkExtractSelection *GetSelectionExtractor()
        
        Set/get the vtkExtractSelection instance used to obtain array
        values at each time step. By default, vtkExtractSelection is
        used.
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
        V.NewInstance() -> vtkExtractSelectedArraysOverTime
        C++: vtkExtractSelectedArraysOverTime *NewInstance()
        """
        ...
    
    def ReportStatisticsOnlyOff(self):
        """
        V.ReportStatisticsOnlyOff()
        C++: virtual void ReportStatisticsOnlyOff()
        
        Instead of breaking a selection into a separate time-history
        table for each (block,ID)-tuple, you may call
        ReportStatisticsOnlyOn(). Then a single table per block of the
        input dataset will report the minimum, maximum, quartiles, and
        (for numerical arrays) the average and standard deviation of the
        selection over time.
        
        * The default is off to preserve backwards-compatibility.
        """
        ...
    
    def ReportStatisticsOnlyOn(self):
        """
        V.ReportStatisticsOnlyOn()
        C++: virtual void ReportStatisticsOnlyOn()
        
        Instead of breaking a selection into a separate time-history
        table for each (block,ID)-tuple, you may call
        ReportStatisticsOnlyOn(). Then a single table per block of the
        input dataset will report the minimum, maximum, quartiles, and
        (for numerical arrays) the average and standard deviation of the
        selection over time.
        
        * The default is off to preserve backwards-compatibility.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtractSelectedArraysOverTime
        C++: static vtkExtractSelectedArraysOverTime *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetReportStatisticsOnly(self, bool):
        """
        V.SetReportStatisticsOnly(bool)
        C++: virtual void SetReportStatisticsOnly(bool _arg)
        
        Instead of breaking a selection into a separate time-history
        table for each (block,ID)-tuple, you may call
        ReportStatisticsOnlyOn(). Then a single table per block of the
        input dataset will report the minimum, maximum, quartiles, and
        (for numerical arrays) the average and standard deviation of the
        selection over time.
        
        * The default is off to preserve backwards-compatibility.
        """
        ...
    
    def SetSelectionConnection(self, vtkAlgorithmOutput):
        """
        V.SetSelectionConnection(vtkAlgorithmOutput)
        C++: void SetSelectionConnection(vtkAlgorithmOutput *algOutput)
        
        Convenience method to specify the selection connection (2nd input
        port)
        """
        ...
    
    def SetSelectionExtractor(self, vtkExtractSelection):
        """
        V.SetSelectionExtractor(vtkExtractSelection)
        C++: virtual void SetSelectionExtractor(vtkExtractSelection *)
        
        Set/get the vtkExtractSelection instance used to obtain array
        values at each time step. By default, vtkExtractSelection is
        used.
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

