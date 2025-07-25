# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
g0foam = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
g0foamDisplay = Show(g0foam, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# trace defaults for the display properties.
g0foamDisplay.Representation = 'Surface'
g0foamDisplay.ColorArrayName = ['POINTS', 'p']
g0foamDisplay.LookupTable = pLUT
g0foamDisplay.SelectTCoordArray = 'None'
g0foamDisplay.SelectNormalArray = 'None'
g0foamDisplay.SelectTangentArray = 'None'
g0foamDisplay.OSPRayScaleArray = 'p'
g0foamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
g0foamDisplay.SelectOrientationVectors = 'U'
g0foamDisplay.ScaleFactor = 0.002999999932944775
g0foamDisplay.SelectScaleArray = 'p'
g0foamDisplay.GlyphType = 'Arrow'
g0foamDisplay.GlyphTableIndexArray = 'p'
g0foamDisplay.GaussianRadius = 0.00014999999664723872
g0foamDisplay.SetScaleArray = ['POINTS', 'p']
g0foamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
g0foamDisplay.OpacityArray = ['POINTS', 'p']
g0foamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
g0foamDisplay.DataAxesGrid = 'GridAxesRepresentation'
g0foamDisplay.PolarAxes = 'PolarAxesRepresentation'
g0foamDisplay.ScalarOpacityFunction = pPWF
g0foamDisplay.ScalarOpacityUnitDistance = 0.0029758189580041195
g0foamDisplay.OpacityArrayName = ['POINTS', 'p']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
g0foamDisplay.ScaleTransferFunction.Points = [12245.490234375, 0.0, 0.5, 0.0, 271724.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
g0foamDisplay.OpacityTransferFunction.Points = [12245.490234375, 0.0, 0.5, 0.0, 271724.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# show color bar/color legend
g0foamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera(True)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1322, 784)

# current camera placement for renderView1
renderView1.CameraPosition = [0.014999999664723873, 0.004999999888241291, 0.06109054909012853]
renderView1.CameraFocalPoint = [0.014999999664723873, 0.004999999888241291, 0.0]
renderView1.CameraViewAngle = 18.103883005547154
renderView1.CameraParallelScale = 0.015811397580295733

# save screenshot
SaveScreenshot('./p.png', renderView1, ImageResolution=[1322, 784],
    TransparentBackground=1)

# set scalar coloring
ColorBy(g0foamDisplay, ('POINTS', 'T'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
g0foamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
g0foamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')

# layout/tab size in pixels
layout1.SetSize(1322, 784)

# current camera placement for renderView1
renderView1.CameraPosition = [0.014999999664723873, 0.004999999888241291, 0.06109054909012853]
renderView1.CameraFocalPoint = [0.014999999664723873, 0.004999999888241291, 0.0]
renderView1.CameraViewAngle = 18.103883005547154
renderView1.CameraParallelScale = 0.015811397580295733

# save screenshot
SaveScreenshot('./T.png', renderView1, ImageResolution=[1322, 784],
    TransparentBackground=1)

# set scalar coloring
ColorBy(g0foamDisplay, ('POINTS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(tLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
g0foamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
g0foamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# layout/tab size in pixels
layout1.SetSize(1322, 784)

# current camera placement for renderView1
renderView1.CameraPosition = [0.014999999664723873, 0.004999999888241291, 0.06109054909012853]
renderView1.CameraFocalPoint = [0.014999999664723873, 0.004999999888241291, 0.0]
renderView1.CameraViewAngle = 18.103883005547154
renderView1.CameraParallelScale = 0.015811397580295733

# save screenshot
SaveScreenshot('./U.png', renderView1, ImageResolution=[1322, 784],
    TransparentBackground=1)

# set scalar coloring
ColorBy(g0foamDisplay, ('POINTS', 'rho'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
g0foamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
g0foamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'rho'
rhoLUT = GetColorTransferFunction('rho')

# get opacity transfer function/opacity map for 'rho'
rhoPWF = GetOpacityTransferFunction('rho')

# layout/tab size in pixels
layout1.SetSize(1322, 784)

# current camera placement for renderView1
renderView1.CameraPosition = [0.014999999664723873, 0.004999999888241291, 0.06109054909012853]
renderView1.CameraFocalPoint = [0.014999999664723873, 0.004999999888241291, 0.0]
renderView1.CameraViewAngle = 18.103883005547154
renderView1.CameraParallelScale = 0.015811397580295733

# save screenshot
SaveScreenshot('./rho.png', renderView1, ImageResolution=[1322, 784],
    TransparentBackground=1)

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# destroy renderView1
Delete(renderView1)
del renderView1

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
g0foamDisplay = Show(g0foam, spreadSheetView1, 'SpreadSheetRepresentation')

# assign view to a particular cell in the layout
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

# export view
ExportView('./solution.csv', view=spreadSheetView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(400, 400)

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).