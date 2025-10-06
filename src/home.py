# -*- coding: utf-8 -*-

import wx
import wx.xrc
import wx.richtext
import gettext
import hostEditorPage
_ = gettext.gettext


PANEL_TRANSPARENCY = 220
#--------------------------------------------------------------------------
#  Class main
#---------------------------------------------------------------------------

class main ( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = "123ToolKit", pos = wx.DefaultPosition, size = wx.Size( 800,460 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
        self.SetTransparent(PANEL_TRANSPARENCY)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour( 239, 235, 235 ))

        root = wx.BoxSizer(wx.HORIZONTAL)

        self.sidebar = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.sidebar.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ))

        sidebarRoot = wx.BoxSizer(wx.VERTICAL)

        self.storage = wx.Button(self.sidebar, wx.ID_ANY, _(u"存储"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.storage.SetTransparent(255)
        sidebarRoot.Add(self.storage, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5)

        self.host = wx.Button(self.sidebar, wx.ID_ANY, _(u"Host"), wx.DefaultPosition, wx.DefaultSize, 0)
        sidebarRoot.Add(self.host, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5)

        self.o = wx.Button(self.sidebar, wx.ID_ANY, _(u""), wx.DefaultPosition, wx.DefaultSize, 0)
        sidebarRoot.Add(self.o, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5)


        self.sidebar.SetSizer( sidebarRoot )
        self.sidebar.Layout()
        sidebarRoot.Fit( self.sidebar )
        root.Add(self.sidebar, 0, wx.EXPAND, 5)

        self.ifm = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.ifm.SetScrollRate( 5, 5 )
        informations = wx.BoxSizer(wx.VERTICAL)

        self.bitmap = wx.StaticBitmap(self.ifm, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        informations.Add(self.bitmap, 0, wx.ALL, 5)

        self.text = wx.richtext.RichTextCtrl(self.ifm, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS)
        self.text.SetTransparent(255)
        self.text.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
        self.text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        self.text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        self.text.AppendText(_(u"欢迎使用！"))

        informations.Add(self.text, 1, wx.EXPAND |wx.ALL, 5)


        self.ifm.SetSizer( informations )
        self.ifm.Layout()
        informations.Fit( self.ifm )
        root.Add(self.ifm, 1, wx.EXPAND, 5)


        self.SetSizer( root )
        self.Layout()

        self.Centre(wx.BOTH)

        self.host.Bind(wx.EVT_BUTTON, self.onHost)

    def onHost(self, event):
        app = wx.App()
        frame = hostEditorPage.main(None)
        frame.Show()
        app.MainLoop()
    

    def __del__( self ):
        pass




if __name__ == '__main__':
	app = wx.App()
	frame = main(None)
	frame.Show()
	app.MainLoop()
