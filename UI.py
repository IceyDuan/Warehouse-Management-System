import tkinter as tk
from tkinter import messagebox
from function import ProductManageSystem
from tkinter import ttk
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="PIL.PngImagePlugin")
import locale




class Windows:
    def __init__(self, master, product_system):
        self.master = master  # 主窗口
        self.product_system = product_system

        # 设置窗口大小
        width, height = 400, 400
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # 计算窗口居中位置
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # 设置窗口的大小和位置
        self.master.geometry(f"{width}x{height}+{x}+{y}")
        self.master.title("Warehouse Management System")  # 设置窗口标题

        # 标题标签
        self.lbl = tk.Label(self.master, text='Warehouse Management System', font=('microsoft yahei', 15), fg='Black')
        self.lbl.place(x=40, y=0)
        self.lbl1 = tk.Label(self.master, text='Please：', font=('microsoft yahei', 15), fg='Black')
        self.lbl1.place(x=40, y=30)

        self.f1 = None

        # 增加复选框的变量
        self.sort_by_date = tk.IntVar()  # 0 表示不排序，1 表示按成绩排序
        self.sort_order = tk.StringVar()  # 选择排序顺序：'asc' 为升序，'desc' 为降序

        self.create_widgets()

    def create_widgets(self):
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300

        # 增加产品信息按钮
        self.btn1 = tk.Button(self.f1, text='Add Product Information', font=('microsoft yahei', 12), width=23, fg='Black',
                              command=self.add_info)
        self.btn1.config(bg='#FFFFFF')
        self.btn1.place(x=80, y=0)

        # 修改产品信息按钮
        self.btn2 = tk.Button(self.f1, text='Modify Product Information', font=('microsoft yahei', 12), width=23, fg='Black',
                              command=self.modify_info)
        self.btn2.config(bg='#FFFFFF')
        self.btn2.place(x=80, y=50)

        # 删除产品信息按钮
        self.btn3 = tk.Button(self.f1, text='Delete Product Information', font=('microsoft yahei', 12), width=23, fg='Black',
                              command=self.delete_info)
        self.btn3.config(bg='#FFFFFF')
        self.btn3.place(x=80, y=100)

        # 查询产品信息按钮
        self.btn4 = tk.Button(self.f1, text='Search Product Information', font=('microsoft yahei', 12), width=23, fg='Black',
                              command=self.search_info)
        self.btn4.config(bg='#FFFFFF')
        self.btn4.place(x=80, y=150)

        # 显示所有产品信息按钮
        self.btn5 = tk.Button(self.f1, text='All Product Information', font=('microsoft yahei', 12), width=23, fg='Black',
                              command=self.display)
        self.btn5.config(bg='#FFFFFF')
        self.btn5.place(x=80, y=200)

        # 增加一个复选框，用于选择是否按日期排序
        self.chk = tk.Checkbutton(self.f1, text='Sort by date', variable=self.sort_by_date)
        self.chk.place(x=80, y=250)

        # 增加下拉菜单用于选择排序方式（升序或降序）
        self.sort_menu = ttk.Combobox(self.f1, textvariable=self.sort_order,width=5)
        self.sort_menu['values'] = ('asc', 'desc')  # 设置选项
        self.sort_menu.place(x=180, y=250)

        self.f1.place(x=0, y=80)

    def add_info(self):
        """添加产品信息"""
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300
        self.lf = tk.LabelFrame(self.f1, text='Add Product Information')

        self.Name = tk.Label(self.lf, text='Name')
        self.Name.pack()
        self.Name_entry = tk.Entry(self.lf)
        self.Name_entry.pack()

        self.ID = tk.Label(self.lf, text='ID')
        self.ID.pack()
        self.ID_entry = tk.Entry(self.lf)
        self.ID_entry.pack()

        self.Amount = tk.Label(self.lf, text='Amount')
        self.Amount.pack()
        self.Amount_entry = tk.Entry(self.lf)
        self.Amount_entry.pack()

        self.Time = tk.Label(self.lf, text='Entry time')
        self.Time.pack()
        self.Time_entry = tk.Entry(self.lf)
        self.Time_entry.pack()

        def cmd1():
            msg = self.product_system.add_product(self.Name_entry.get(), self.ID_entry.get(), self.Amount_entry.get(),
                                                  self.Time_entry.get())
            messagebox.showinfo('Notice', msg)
            self.Name_entry.delete(0, 'end')
            self.ID_entry.delete(0, 'end')
            self.Amount_entry.delete(0, 'end')
            self.Time_entry.delete(0, 'end')

        self.btn1 = tk.Button(self.lf, text='Back', command=self.create_widgets)
        self.btn1.pack(side='left')

        self.btn2 = tk.Button(self.lf, text='Confirm', command=cmd1)
        self.btn2.pack(side='right')

        self.lf.place(x=120, y=40)
        self.f1.place(x=0, y=80)

    def modify_info(self):
        """修改产品信息"""
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300
        self.lf = tk.LabelFrame(self.f1, text='Revise Product Information')

        self.index1 = -1

        # 检索产品编号是否存在
        def cmd2(ID):
            if ID == '':
                tk.messagebox.showinfo('Notice', 'Please input product ID！')
            else:
                self.index1, msg = self.product_system.judge(ID)
                tk.messagebox.showinfo('Notice', msg)

        self.old_ID = tk.Label(self.lf, text='ID')
        self.old_ID.pack()
        self.old_ID_entry = tk.Entry(self.lf)
        self.old_ID_entry.pack()
        self.btn = tk.Button(self.lf, text='Retrieve', command=lambda: cmd2(self.old_ID_entry.get()))
        self.btn.pack()

        # 修改信息
        self.Name = tk.Label(self.lf, text='Name')
        self.Name.pack()
        self.Name_entry = tk.Entry(self.lf)
        self.Name_entry.pack()

        self.ID = tk.Label(self.lf, text='ID')
        self.ID.pack()
        self.ID_entry = tk.Entry(self.lf)
        self.ID_entry.pack()

        self.Amount = tk.Label(self.lf, text='Amount')
        self.Amount.pack()
        self.Amount_entry = tk.Entry(self.lf)
        self.Amount_entry.pack()

        self.Time = tk.Label(self.lf, text='Entry time')
        self.Time.pack()
        self.Time_entry = tk.Entry(self.lf)
        self.Time_entry.pack()

        def cmd():
            if self.index1 != -1:
                msg = self.product_system.modify_product(self.index1,
                                                         self.Name_entry.get(),
                                                         self.ID_entry.get(),
                                                         self.Amount_entry.get(),
                                                         self.Time_entry.get())
                tk.messagebox.showinfo('Notice', msg)
                self.old_ID_entry.delete(0, 'end')
                self.Name_entry.delete(0, 'end')
                self.ID_entry.delete(0, 'end')
                self.Amount_entry.delete(0, 'end')
                self.Time_entry.delete(0, 'end')
            else:
                tk.messagebox.showinfo('Notice', 'Please retrieve product ID first！')

        self.btn1 = tk.Button(self.lf, text='Back', command=self.create_widgets)
        self.btn1.pack(side='left')
        self.btn2 = tk.Button(self.lf, text='Confirm', command=cmd)
        self.btn2.pack(side='right')
        self.lf.place(x=120, y=0)
        self.f1.place(x=0, y=80)

    def delete_info(self):
        """删除产品信息"""
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300
        self.lf = tk.LabelFrame(self.f1, text='Delete Product Information')

        self.index1 = -1

        # 检索产品编号是否存在
        def cmd2(no):
            if no == '':
                tk.messagebox.showinfo('Notice', 'Please input ID！')
            else:
                self.index1, msg = self.product_system.judge(no)
                tk.messagebox.showinfo('Notice', msg)

        self.old_ID = tk.Label(self.lf, text='ID')
        self.old_ID.pack()
        self.old_ID_entry = tk.Entry(self.lf)
        self.old_ID_entry.pack()

        self.btn = tk.Button(self.lf, text='Retrieve', command=lambda: cmd2(self.old_ID_entry.get()))
        self.btn.pack(side='left')

        self.btn1 = tk.Button(self.lf, text='Delete', command=lambda: tk.messagebox.showinfo('Notice',self.product_system.delete_product(self.index1)))
        self.btn1.pack(side='right')

        self.btn2 = tk.Button(self.lf, text='Back', command=self.create_widgets)
        self.btn2.pack()

        self.lf.place(x=120, y=0)
        self.f1.place(x=0, y=80)

    def search_info(self):
        """查找产品信息"""
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300
        self.lf = tk.LabelFrame(self.f1, text='Search Product Information')

        self.ID = tk.Label(self.lf, text='product ID')
        self.ID.pack()
        self.ID_entry = tk.Entry(self.lf)
        self.ID_entry.pack()

        def cmd3(ID):
            result = self.product_system.search_product(ID)
            tk.messagebox.showinfo('Notice', result)

        self.btn = tk.Button(self.lf, text='Back', command=self.create_widgets)
        self.btn.pack(side='left')

        self.btn1 = tk.Button(self.lf, text='Confirm', command=lambda: cmd3(self.ID_entry.get()))
        self.btn1.pack(side='right')

        self.lf.place(x=120, y=0)
        self.f1.place(x=0, y=80)

    def display(self):
        """显示所有产品信息，按复选框选择是否排序"""
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300
        self.lf = tk.LabelFrame(self.f1, text='Product Information')

        # 检查复选框的状态，决定是否按信息排序
        sort_by_date = bool(self.sort_by_date.get())

        # 获取排序顺序（asc 或 desc）
        sort_order = self.sort_order.get()

        # 传递排序顺序参数到后端
        descending = True if sort_order == 'desc' else False

        # 获取排序后的产品信息
        str1 = self.product_system.display_products(sort_by_score=sort_by_date, descending=descending)

        self.text = tk.Text(self.lf, width=56, height=15)
        self.text.insert(0.0, str1)
        self.text.pack()

        self.btn1 = tk.Button(self.lf, text='Back', command=self.create_widgets)
        self.btn1.pack()

        self.lf.place(x=0, y=40)
        self.f1.place(x=0, y=80)

if __name__ == '__main__':
    root = tk.Tk()
    root['width'] = 400
    root['height'] = 400
    root.title("Warehouse Management System")
    product_system = ProductManageSystem()
    Windows(root, product_system)
    root.mainloop()