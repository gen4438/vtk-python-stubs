"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkHyperTreeGridSource(__vtkmodules_vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    """
    vtkHyperTreeGridSource - Create a synthetic grid of hypertrees.
    
    Superclass: vtkHyperTreeGridAlgorithm
    
    This class uses input parameters, most notably a string descriptor,
    to generate a vtkHyperTreeGrid instance representing the
    corresponding tree-based AMR grid. This descriptor uses the following
    conventions, e.g., to describe a 1-D ternary subdivision with 2 root
    cells L0    L1        L2 RR  | .R. ... | ... For this tree:
     HTG:       .
              /   \
     L0:     .     .
            /|\   /|\
     L1:   c . c c c c
            /|\
     L2:   c c c The top level of the tree is not considered a grid level
    NB: For ease of legibility, white spaces are allowed and ignored.
    
    @par Thanks: This class was written by Philippe Pebay, Joachim
    Pouderoux, and Charles Law, Kitware 2013 This class was modified by
    Guenole Harel and Jacques-Bernard Lekien 2014 This class was modified
    by Philippe Pebay, 2016 This work was supported by Commissariat a
    l'Energie Atomique (CEA/DIF) CEA, DAM, DIF, F-91297 Arpajon, France.
    """
    def ConvertDescriptorStringToBitArray(self, string):
        """
        V.ConvertDescriptorStringToBitArray(string) -> vtkBitArray
        C++: vtkBitArray *ConvertDescriptorStringToBitArray(
            const std::string &)
        
        Helpers to convert string descriptors & mask to bit arrays
        """
        ...
    
    def ConvertMaskStringToBitArray(self, string):
        """
        V.ConvertMaskStringToBitArray(string) -> vtkBitArray
        C++: vtkBitArray *ConvertMaskStringToBitArray(const std::string &)
        
        Helpers to convert string descriptors & mask to bit arrays
        """
        ...
    
    def GenerateInterfaceFieldsOff(self):
        """
        V.GenerateInterfaceFieldsOff()
        C++: virtual void GenerateInterfaceFieldsOff()
        
        Set/get whether cell-centered interface fields should be
        generated. Default: false
        """
        ...
    
    def GenerateInterfaceFieldsOn(self):
        """
        V.GenerateInterfaceFieldsOn()
        C++: virtual void GenerateInterfaceFieldsOn()
        
        Set/get whether cell-centered interface fields should be
        generated. Default: false
        """
        ...
    
    def GetBranchFactor(self):
        """
        V.GetBranchFactor() -> int
        C++: virtual unsigned int GetBranchFactor()
        
        Set/Get the subdivision factor in the grid refinement scheme
        """
        ...
    
    def GetBranchFactorMaxValue(self):
        """
        V.GetBranchFactorMaxValue() -> int
        C++: virtual unsigned int GetBranchFactorMaxValue()
        
        Set/Get the subdivision factor in the grid refinement scheme
        """
        ...
    
    def GetBranchFactorMinValue(self):
        """
        V.GetBranchFactorMinValue() -> int
        C++: virtual unsigned int GetBranchFactorMinValue()
        
        Set/Get the subdivision factor in the grid refinement scheme
        """
        ...
    
    def GetDescriptor(self):
        """
        V.GetDescriptor() -> string
        C++: virtual char *GetDescriptor()
        
        Set/Get the string used to describe the grid.
        """
        ...
    
    def GetDescriptorBits(self):
        """
        V.GetDescriptorBits() -> vtkBitArray
        C++: virtual vtkBitArray *GetDescriptorBits()
        
        Set/Get the bitarray used to describe the grid.
        """
        ...
    
    def GetDimensions(self):
        """
        V.GetDimensions() -> (int, int, int)
        C++: virtual unsigned int *GetDimensions()
        
        Set/Get the number of root cells + 1 in each dimension of the
        grid
        """
        ...
    
    def GetGenerateInterfaceFields(self):
        """
        V.GetGenerateInterfaceFields() -> bool
        C++: virtual bool GetGenerateInterfaceFields()
        
        Set/get whether cell-centered interface fields should be
        generated. Default: false
        """
        ...
    
    def GetGridScale(self):
        """
        V.GetGridScale() -> (float, float, float)
        C++: virtual double *GetGridScale()
        
        Set/Get the scale to be applied to root cells in each dimension
        of the grid
        """
        ...
    
    def GetMask(self):
        """
        V.GetMask() -> string
        C++: virtual char *GetMask()
        
        Set/Get the string used to as a material mask.
        """
        ...
    
    def GetMaskBits(self):
        """
        V.GetMaskBits() -> vtkBitArray
        C++: virtual vtkBitArray *GetMaskBits()
        
        Set/Get the bitarray used as a material mask.
        """
        ...
    
    def GetMaxDepth(self):
        """
        V.GetMaxDepth() -> int
        C++: unsigned int GetMaxDepth()
        
        Return the maximum number of levels of the hypertree.
        \post positive_result: result>=1
        """
        ...
    
    def GetMaximumLevel(self):
        """
        V.GetMaximumLevel() -> int
        C++: unsigned int GetMaximumLevel()
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Override GetMTime because we delegate to a vtkQuadric.
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
    
    def GetOrientation(self):
        """
        V.GetOrientation() -> int
        C++: virtual unsigned int GetOrientation()
        
        Set/Get the orientation of the grid (in 1D and 2D)
        """
        ...
    
    def GetOrigin(self):
        """
        V.GetOrigin() -> (float, float, float)
        C++: virtual double *GetOrigin()
        
        Set/Get the origin of the grid
        """
        ...
    
    def GetQuadric(self):
        """
        V.GetQuadric() -> vtkQuadric
        C++: virtual vtkQuadric *GetQuadric()
        
        Set/Get the quadric function.
        """
        ...
    
    def GetQuadricCoefficients(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetQuadricCoefficients([float, float, float, float, float,
            float, float, float, float, float])
        C++: void GetQuadricCoefficients(double[10])
        V.GetQuadricCoefficients() -> (float, ...)
        C++: double *GetQuadricCoefficients()
        
        Helpers to set/get the 10 coefficients of the quadric function
        """
        ...
    
    def GetTransposedRootIndexing(self):
        """
        V.GetTransposedRootIndexing() -> bool
        C++: virtual bool GetTransposedRootIndexing()
        
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ...
    
    def GetUseDescriptor(self):
        """
        V.GetUseDescriptor() -> bool
        C++: virtual bool GetUseDescriptor()
        
        Set/get whether the descriptor string should be used. NB:
        Otherwise a quadric definition is expected. Default: true
        """
        ...
    
    def GetUseMask(self):
        """
        V.GetUseMask() -> bool
        C++: virtual bool GetUseMask()
        
        Set/get whether the material mask should be used. NB: This is
        only used when UseDescriptor is ON Default: false
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
        V.NewInstance() -> vtkHyperTreeGridSource
        C++: vtkHyperTreeGridSource *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkHyperTreeGridSource
        C++: static vtkHyperTreeGridSource *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetBranchFactor(self, p_int):
        """
        V.SetBranchFactor(int)
        C++: virtual void SetBranchFactor(unsigned int _arg)
        
        Set/Get the subdivision factor in the grid refinement scheme
        """
        ...
    
    def SetDescriptor(self, string):
        """
        V.SetDescriptor(string)
        C++: virtual void SetDescriptor(const char *_arg)
        
        Set/Get the string used to describe the grid.
        """
        ...
    
    def SetDescriptorBits(self, vtkBitArray):
        """
        V.SetDescriptorBits(vtkBitArray)
        C++: virtual void SetDescriptorBits(vtkBitArray *)
        
        Set/Get the bitarray used to describe the grid.
        """
        ...
    
    def SetDimensions(self, int_tuple):
        """
        V.SetDimensions((int, ...))
        C++: void SetDimensions(const unsigned int *dims)
        V.SetDimensions(int, int, int)
        C++: void SetDimensions(unsigned int, unsigned int, unsigned int)
        
        Set/Get the number of root cells + 1 in each dimension of the
        grid
        """
        ...
    
    def SetGenerateInterfaceFields(self, bool):
        """
        V.SetGenerateInterfaceFields(bool)
        C++: virtual void SetGenerateInterfaceFields(bool _arg)
        
        Set/get whether cell-centered interface fields should be
        generated. Default: false
        """
        ...
    
    def SetGridScale(self, p_float, p_float_1, p_float_2):
        """
        V.SetGridScale(float, float, float)
        C++: virtual void SetGridScale(double _arg1, double _arg2,
            double _arg3)
        V.SetGridScale((float, float, float))
        C++: virtual void SetGridScale(const double _arg[3])
        V.SetGridScale(float)
        C++: void SetGridScale(double scale)
        
        Set/Get the scale to be applied to root cells in each dimension
        of the grid
        """
        ...
    
    def SetIndexingModeToIJK(self):
        """
        V.SetIndexingModeToIJK()
        C++: void SetIndexingModeToIJK()
        
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ...
    
    def SetIndexingModeToKJI(self):
        """
        V.SetIndexingModeToKJI()
        C++: void SetIndexingModeToKJI()
        
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ...
    
    def SetLevelZeroMaterialIndex(self, vtkIdTypeArray):
        """
        V.SetLevelZeroMaterialIndex(vtkIdTypeArray)
        C++: virtual void SetLevelZeroMaterialIndex(vtkIdTypeArray *)
        
        Set the index array used to as a material mask.
        """
        ...
    
    def SetMask(self, string):
        """
        V.SetMask(string)
        C++: virtual void SetMask(const char *_arg)
        
        Set/Get the string used to as a material mask.
        """
        ...
    
    def SetMaskBits(self, vtkBitArray):
        """
        V.SetMaskBits(vtkBitArray)
        C++: virtual void SetMaskBits(vtkBitArray *)
        
        Set/Get the bitarray used as a material mask.
        """
        ...
    
    def SetMaxDepth(self, p_int):
        """
        V.SetMaxDepth(int)
        C++: void SetMaxDepth(unsigned int levels)
        
        Set the maximum number of levels of the hypertrees.
        \pre positive_levels: levels>=1
        \post is_set: this->GetLevels()==levels
        \post min_is_valid: this->GetMinLevels()<this->GetLevels()
        """
        ...
    
    def SetMaximumLevel(self, p_int):
        """
        V.SetMaximumLevel(int)
        C++: void SetMaximumLevel(unsigned int levels)
        """
        ...
    
    def SetOrigin(self, p_float, p_float_1, p_float_2):
        """
        V.SetOrigin(float, float, float)
        C++: virtual void SetOrigin(double _arg1, double _arg2,
            double _arg3)
        V.SetOrigin((float, float, float))
        C++: virtual void SetOrigin(const double _arg[3])
        
        Set/Get the origin of the grid
        """
        ...
    
    def SetQuadric(self, vtkQuadric):
        """
        V.SetQuadric(vtkQuadric)
        C++: virtual void SetQuadric(vtkQuadric *)
        
        Set/Get the quadric function.
        """
        ...
    
    def SetQuadricCoefficients(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.SetQuadricCoefficients([float, float, float, float, float,
            float, float, float, float, float])
        C++: void SetQuadricCoefficients(double[10])
        
        Helpers to set/get the 10 coefficients of the quadric function
        """
        ...
    
    def SetTransposedRootIndexing(self, bool):
        """
        V.SetTransposedRootIndexing(bool)
        C++: virtual void SetTransposedRootIndexing(bool _arg)
        
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ...
    
    def SetUseDescriptor(self, bool):
        """
        V.SetUseDescriptor(bool)
        C++: virtual void SetUseDescriptor(bool _arg)
        
        Set/get whether the descriptor string should be used. NB:
        Otherwise a quadric definition is expected. Default: true
        """
        ...
    
    def SetUseMask(self, bool):
        """
        V.SetUseMask(bool)
        C++: virtual void SetUseMask(bool _arg)
        
        Set/get whether the material mask should be used. NB: This is
        only used when UseDescriptor is ON Default: false
        """
        ...
    
    def UseDescriptorOff(self):
        """
        V.UseDescriptorOff()
        C++: virtual void UseDescriptorOff()
        
        Set/get whether the descriptor string should be used. NB:
        Otherwise a quadric definition is expected. Default: true
        """
        ...
    
    def UseDescriptorOn(self):
        """
        V.UseDescriptorOn()
        C++: virtual void UseDescriptorOn()
        
        Set/get whether the descriptor string should be used. NB:
        Otherwise a quadric definition is expected. Default: true
        """
        ...
    
    def UseMaskOff(self):
        """
        V.UseMaskOff()
        C++: virtual void UseMaskOff()
        
        Set/get whether the material mask should be used. NB: This is
        only used when UseDescriptor is ON Default: false
        """
        ...
    
    def UseMaskOn(self):
        """
        V.UseMaskOn()
        C++: virtual void UseMaskOn()
        
        Set/get whether the material mask should be used. NB: This is
        only used when UseDescriptor is ON Default: false
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


