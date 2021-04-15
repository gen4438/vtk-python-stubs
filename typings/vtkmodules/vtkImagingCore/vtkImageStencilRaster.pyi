"""
This type stub file was generated by pyright.
"""

from .object import object

class vtkImageStencilRaster(object):
    """
    vtkImageStencilRaster - This is a helper class for stencil creation.
    
    It is a raster with infinite resolution in the X direction
    (approximately, since it uses double precision).  Lines that
    represent polygon edges can be drawn into this raster, and then
    filled given a tolerance.
    
    vtkImageStencilRaster(const int wholeExtent[2])
    """
    def FillStencilData(self, vtkImageStencilData, , p_int_6, p_int_7):
        """
        V.FillStencilData(vtkImageStencilData, (int, int, int, int, int,
            int), int, int)
        C++: void FillStencilData(vtkImageStencilData *data,
            const int extent[6], int xj=0, int yj=1)
        
        Fill the specified extent of a vtkImageStencilData with the
        raster, after permuting the raster according to xj and yj.
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> float
        C++: double GetTolerance()
        """
        ...
    
    def InsertLine(self, , ):
        """
        V.InsertLine((float, float), (float, float))
        C++: void InsertLine(const double p1[2], const double p2[2])
        V.InsertLine((float, float), (float, float), bool, bool)
        C++: void InsertLine(const double[2], const double[2], bool, bool)
        
        Insert a line into the raster, given the two end points.
        """
        ...
    
    def PrepareForNewData(self, ):
        """
        V.PrepareForNewData((int, int))
        C++: void PrepareForNewData(const int allocateExtent[2]=nullptr)
        
        Reset the raster to its original state, but keep the same whole
        extent. Pre-allocate the specified 1D allocateExtent, which must
        be within the whole extent.
        """
        ...
    
    def SetTolerance(self, p_float):
        """
        V.SetTolerance(float)
        C++: void SetTolerance(double tol)
        
        The tolerance for float-to-int conversions.
        """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __hash__(self, *args, **kwargs) -> int:
        """ Return hash(self). """
        ...
    
    def __init__(self, const_int_wholeExtent, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        ...
    
    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        ...
    


