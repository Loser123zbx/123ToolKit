# -*- coding: utf-8 -*-

import wx
import wx.xrc

import gettext
import os
import hostEditor
import core
from core import Log

_ = gettext.gettext



PANEL_TRANSPARENCY = 220
CONTROL_TRANSPARENCY = 255

hostsText :list = hostEditor.readHosts() 
hosts :dict = hostEditor.getHostsDict()
host :list = list(hosts.keys())
ip :list = list(hosts.values())

def readHosts() -> None:  # 定义一个名为updateHosts的函数
	# 获取主机字典，通过hostEditor.getHostsDict()方法
	hosts = hostEditor.getHostsDict()
	# 将字典的键（主机名）转换为列表
	host = list(hosts.keys())
	# 将字典的值（IP地址）转换为列表
	ip = list(hosts.values())

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
		self.add.Bind( wx.EVT_BUTTON, self.addHost )

	def addHost(self, event):
		_log:Log = Log(Log.Info, "正在添加屏蔽网站")
		Add : str = self.inputBox.GetValue()
		AddItems = Add.split("\n")
		AddItems = [item for item in AddItems if item != ' ']         
		AddItems = [item for item in AddItems if item[0] != '#']         
		for i in AddItems:
			hostsText.append("0.0.0.0 "+ i +" #屏蔽网站")
		try:
			with open("C:\Windows\System32\drivers\etc\hosts", "w", encoding="utf-8") as f:
				f.write("\n".join(hostsText))
			_log:Log = Log(Log.Info, "添加成功")
			_log.log()
			wx.MessageBox(_(u"添加成功"), _(u"提示"), wx.OK | wx.ICON_INFORMATION)
		except PermissionError:
			_log:Log = Log(Log.Error, "没有权限修改hosts文件，请以管理员身份运行程序")
			_log.log()


	def __del__( self ):
		pass


#--------------------------------------------------------------------------
#  Class EditHost
#---------------------------------------------------------------------------

class EditHost ( wx.Dialog ):

	def __init__(self, parent ,hostIndex :list):
		self.hostIndex = hostIndex

		wx.Dialog.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 554,156 ), style = wx.DEFAULT_DIALOG_STYLE)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		root = wx.BoxSizer(wx.VERTICAL)

		self.host = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_DONTWRAP|wx.TE_MULTILINE)
		for i in hostIndex:
			self.host.AppendText(hostsText[int(i)])
		root.Add(self.host, 1, wx.ALL|wx.EXPAND, 5)

		self.save = wx.Button(self, wx.ID_ANY, _(u"保存"), wx.DefaultPosition, wx.DefaultSize, 0)
		root.Add(self.save, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5)


		self.SetSizer( root )
		self.Layout()

		self.Centre(wx.BOTH)

		self.save.Bind( wx.EVT_BUTTON, self.saveHost )

	def saveHost(self, event):
		newHost:list = []
		for i in hostsText:
			if i in self.hostIndex:
				pass
			else:
				newHost.append(i)

		newHost :str = "\n".join(newHost)
		newHost += str(self.host.GetValue())
		
		try: 
			with open("C:\Windows\System32\drivers\etc\hosts", "w", encoding="utf-8") as f:
				f.write(newHost)
			_log:Log = Log(Log.Info, "保存成功")
			_log.log()
			wx.MessageBox(_(u"保存成功"), _(u"提示"), wx.OK | wx.ICON_INFORMATION)

		except PermissionError:
			_log:Log = Log(Log.Error, "没有权限修改hosts文件，请以管理员身份运行程序")
			_log.log()

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
		self.items = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, itemsChoices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_MULTIPLE)
		self.items.SetTransparent(CONTROL_TRANSPARENCY)
		root.Add(self.items, 1, wx.ALL|wx.EXPAND, 5)

		tools = wx.BoxSizer(wx.VERTICAL)

		self.edit = wx.Button(self, wx.ID_ANY, _(u"编辑选中的Host规则/追加hosts规则"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.edit.SetTransparent(CONTROL_TRANSPARENCY)
		tools.Add(self.edit, 0, wx.TOP|wx.EXPAND, 5)

		self.delete = wx.Button(self, wx.ID_ANY, _(u"删除Host规则"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.delete.SetTransparent(CONTROL_TRANSPARENCY)
		tools.Add(self.delete, 0, wx.EXPAND, 5)

		self.block = wx.Button(self, wx.ID_ANY, _(u"屏蔽网站"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.block.SetTransparent(CONTROL_TRANSPARENCY)
		tools.Add(self.block, 0, wx.EXPAND, 5)

		self.showIp = wx.CheckBox(self, wx.ID_ANY, _(u"在选择框显示对应IP"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.showIp.SetTransparent(CONTROL_TRANSPARENCY)
		tools.Add(self.showIp, 0, wx.ALL, 5)

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

		self.block.Bind(wx.EVT_BUTTON, self.addBlock)

		self.delete.Bind(wx.EVT_BUTTON, self.onDelete)

		self.showIp.Bind(wx.EVT_CHECKBOX, self.onShowIp)

	def onShowIp(self, event):
		"""
		显示IP
		- 如果选中则显示IP
		- 否则不显示
		"""
		if not self.showIp.GetValue():
			self.items.SetItems(host)
		else:
			self.items.SetItems([])
			for i in range(len(host)):
				self.items.Append(host[i] + " : " + ip[i])
		self.Refresh()


	def onSelect(self, event):
		"""
		选中项时的事件
		- 更改侧边文本
		"""
		Selections = self.items.GetSelections()
		_log:Log = Log(Log.Info, _(u"选中:")+ host[self.items.GetSelections()[0]] + " 等 "
				  + str(len(self.items.GetSelections())) + " 项\n"
					+ str(self.items.GetSelections()) )
		_log.log()
		if len(Selections) == 1:	
			self.choseingItem.SetLabel(_(u"选中项:") + host[self.items.GetSelections()[0]])
		elif len(Selections) > 1:
			self.choseingItem.SetLabel(_(u"选中项:")+ host[self.items.GetSelections()[0]] + " 等 " + str(len(self.items.GetSelections())) + " 项")
			print(Selections)

		

	def onEdit(self, event):
		"""
		编辑选中的Host规则
		- 如果未选中则提示
		- 否则弹出编辑框
		"""
		Selections = self.items.GetSelections()
		self.editHost = EditHost(self, Selections)
		self.editHost.ShowModal()
		self.editHost.Destroy()
		readHosts()
		self.Refresh()


	def addBlock(self, event):
		"""
		屏蔽网站
		- 弹出输入框
		- 添加到hosts文件
		"""
		self.blockHost = BlockAdd(self)
		self.blockHost.ShowModal()
		self.blockHost.Destroy()
		readHosts()
		self.Refresh#]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\\'[][;plkjhgfdsdftghjklkjhgfdsaQASDFGHJK				self.Refresh()0-]

	def onDelete(self, event):
		"""
		删除选中的Host规则
		- 如果未选中则提示
		- 否则删除
		"""
		Selections = self.items.GetSelections()
		if len(Selections) == 0:
			wx.MessageBox(_(u"请先选中要删除的Host规则"), _(u"提示"), wx.OK | wx.ICON_INFORMATION)
		else:
			try:
				newHost = ""
				print(Selections)
				for i in range(len(hostsText)):
					if i not in Selections:
						newHost += hostsText[i] + "\n"
						print(hostsText[i])
				with open(r"C:\Windows\System32\drivers\etc\hosts", "w", encoding="utf-8") as f:
					f.write(newHost)
				print(newHost)
				_log:Log = Log(Log.Info, "删除成功")
				_log.log()
			except:
				_log:Log = Log(Log.Error, "删除失败")
				_log.log()
		self.Refresh()


	def __del__( self ):
		pass




if __name__ == '__main__':
	log:Log = Log(Log.Info, "- ")
	app = wx.App()
	main(None).Show()
	app.MainLoop()