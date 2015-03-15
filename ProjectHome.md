A python module to make easier the integration of wxWidgets UI into Autodesk Maya software.

wxmaya takes care of integrate wxWidgets inside maya, making possible to use simple wxPython code with Maya to develop better and more os native user interfaces.

wxmaya takes care of make sure wxWidget threads are in sync with maya environment, avoiding problems like crashing and UI accessibility lost.

As a sample, wxmaya brings pyshell into maya, adding a nice and fast python shell with syntax-coloring and code-completion! (YES... Code Completion works with all maya modules, like maya.cmds and maya.OpenMaya!!!! =D )

After installing wxmaya into your PYTHONPATH or MAYA\_SCRIPT\_PATH, open maya and type:

import wxmaya
wxmaya.pyshell()

Obs: You must have wxPython installed on your box, or else wxmaya will fail to initialize.

For last but not least, the goal of wxmaya is to make wxpython works in maya, but also, wxmaya is intended to run OUTSIDE maya as well, allowing the same UI to be used inside maya or a standalone application. This allows for UI development of standalone applications that use maya python modules as a back end. When running maya module from a no-maya python session, maya initializes in batch mode, which basically means all UI is non-functional. wxmaya can field this void, allowing standalone python application to open and manipulate maya scenes with custom made wxPython UIs!