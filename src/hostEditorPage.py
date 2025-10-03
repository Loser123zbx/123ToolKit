# -*- coding: utf-8 -*-

import wx
import wx.xrc

import gettext
import os
import hostEditor
import core
from core import Log

_ = gettext.gettext


hosts = hostEditor.getHostsDict()
host = list(hosts.keys())
ip = list(hosts.values())
PANEL_TRANSPARENCY = 220
CONTROL_TRANSPARENCY = 255



#--------------------------------------------------------------------------
#  Class BlockAdd
#---------------------------------------------------------------------------

class BlockAdd ( wx.Dialog ):

	def __init__(self, parent):
		wx.Dialog.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 567,250 ), style = wx.DEFAULT_DIALOG_STYLE)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		root = wx.BoxSizer(wx.HORIZONTAL)

		self.inputBox = wx.TextCtrl(self, wx.ID_ANY, _(u"#若需屏蔽多个网站，请在不同行填写网站域名"), wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
		root.Add(self.inputBox, 1, wx.ALL|wx.EXPAND, 5)

		tools = wx.BoxSizer(wx.VERTICAL)

		self.add = wx.Button(self, wx.ID_ANY, _(u"屏蔽网站"), wx.DefaultPosition, wx.DefaultSize, 0)
		tools.Add(self.add, 0, wx.ALL, 5)

		self.m_bitmap3 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
		tools.Add(self.m_bitmap3, 1, wx.ALL|wx.EXPAND, 5)


		root.Add(tools, 0, wx.EXPAND, 5)


		self.SetSizer( root )
		self.Layout()

		self.Centre(wx.BOTH)

	def __del__( self ):
		pass


#--------------------------------------------------------------------------
#  Class EditHost
#---------------------------------------------------------------------------

class EditHost ( wx.Dialog ):

	def __init__(self, parent ,host):
		wx.Dialog.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 554,156 ), style = wx.DEFAULT_DIALOG_STYLE)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		root = wx.BoxSizer(wx.VERTICAL)

		self.host = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL)
		self.host.SetValue(host)
		root.Add(self.host, 1, wx.ALL|wx.EXPAND, 5)

		self.save = wx.Button(self, wx.ID_ANY, _(u"保存"), wx.DefaultPosition, wx.DefaultSize, 0)
		root.Add(self.save, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5)


		self.SetSizer( root )
		self.Layout()

		self.Centre(wx.BOTH)

	def __del__( self ):
		pass




#--------------------------------------------------------------------------
#  Class main
#---------------------------------------------------------------------------

class main ( wx.Frame ):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,460 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		self.SetBackgroundColour(wx.Colour( 239, 235, 235 ))
		self.SetTransparent(PANEL_TRANSPARENCY)
		self.BackgroundColour = wx.Colour( 153, 204, 255 )
		
		self.SetFont( wx.Font( 12, 70, 90, 90, False, "Consolas" ) )
		root = wx.BoxSizer(wx.HORIZONTAL)

		itemsChoices = []
		self.items = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, itemsChoices, wx.LB_MULTIPLE)
		self.items.SetTransparent(CONTROL_TRANSPARENCY)
		root.Add(self.items, 1, wx.ALL|wx.EXPAND, 5)

		tools = wx.BoxSizer(wx.VERTICAL)

		self.edit = wx.Button(self, wx.ID_ANY, _(u"编辑选中的Host规则"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.edit.SetTransparent(CONTROL_TRANSPARENCY)
		tools.Add(self.edit, 0, wx.TOP|wx.EXPAND, 5)

		self.save = wx.Button(self, wx.ID_ANY, _(u"保存框内的Host规则"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.save.SetTransparent(CONTROL_TRANSPARENCY)
		tools.Add(self.save, 0, wx.EXPAND, 5)

		self.block = wx.Button(self, wx.ID_ANY, _(u"屏蔽网站"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.block.SetTransparent(CONTROL_TRANSPARENCY)
		tools.Add(self.block, 0, wx.EXPAND, 5)

		self.m_checkBox1 = wx.CheckBox(self, wx.ID_ANY, _(u"在选择框显示对应IP"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_checkBox1.SetTransparent(CONTROL_TRANSPARENCY)
		tools.Add(self.m_checkBox1, 0, wx.ALL, 5)

		self.choseingItem = wx.StaticText(self, wx.ID_ANY, _(u"选中项:"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.choseingItem.SetTransparent(CONTROL_TRANSPARENCY)
		tools.Add(self.choseingItem, 0, wx.ALL, 5)

		self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_bitmap1.SetTransparent(CONTROL_TRANSPARENCY)
		tools.Add(self.m_bitmap1, 1, wx.ALL|wx.EXPAND, 5)


		root.Add(tools, 1, wx.EXPAND, 5)


		self.SetSizer( root )
		self.Layout()

		self.Centre(wx.BOTH)

		self.items.SetItems(host)
		self.items.Bind(wx.EVT_LISTBOX, self.onSelect)
		
		self.edit.Bind(wx.EVT_BUTTON, self.onEdit)


	def onSelect(self, event):
		"""
		选中项时的事件
		- 更改侧边文本
		"""
		Selections = self.items.GetSelections()
		_log:Log = Log(Log.Info, f"选择项: {Selections}")
		_log.log()
		if len(Selections) == 1:	
			self.choseingItem.SetLabel(_(u"选中项:")+self.items.GetStringSelection())
		elif len(Selections) > 1:
			self.choseingItem.SetLabel(_(u"选中项:")+str(len(self.items.GetSelections())))
			print(Selections)

		print(self.items.GetSelections())

	def onEdit(self, event):
		"""
		编辑选中的Host规则
		- 如果未选中则提示
		- 否则弹出编辑框
		"""
		if self.items.GetStringSelection() == "":
			wx.MessageBox(_(u"请先选择一个Host规则"), _(u"提示"), wx.OK | wx.ICON_INFORMATION)
		else:
			self.editHost = EditHost(self, self.items.GetStringSelection() + " " + hosts[self.items.GetStringSelection()])
		self.editHost.ShowModal()
		self.editHost.Destroy()

	def __del__( self ):
		pass




if __name__ == '__main__':
	log:Log = Log(Log.Info, "- ")
	app = wx.App()
	main(None).Show()
	app.MainLoop()