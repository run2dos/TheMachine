from tkinter import *
from tkinter import ttk

class LottoWindow:

    def __init__(self, master):
        
        self.frame_target = ttk.Frame(master, borderwidth=10)
        self.frame_target.grid(row=0, column=0)

        self.target_label = ttk.Label(self.frame_target, text='Target')
        self.target_label.grid(row=0, column=1, rowspan=2)
        
        self.target_label1 = ttk.Label(self.frame_target, text='1').grid(row=0, column=2, padx=10)
        self.target_label2 = ttk.Label(self.frame_target, text='2').grid(row=0, column=3, padx=10)
        self.target_label3 = ttk.Label(self.frame_target, text='3').grid(row=0, column=4, padx=10)
        self.target_label4 = ttk.Label(self.frame_target, text='4').grid(row=0, column=5, padx=10)
        self.target_label5 = ttk.Label(self.frame_target, text='5').grid(row=0, column=6, padx=10)
        self.target_labelP = ttk.Label(self.frame_target, text='P').grid(row=0, column=7, padx=10)
 


        self.targetVar1 = StringVar()
        self.targetVar1.set('00')
        self.targetVar2 = StringVar()
        self.targetVar2.set('00')
        self.targetVar3 = StringVar()
        self.targetVar3.set('00')
        self.targetVar4 = StringVar()
        self.targetVar4.set('00')
        self.targetVar5 = StringVar()
        self.targetVar5.set('00')
        self.targetVarP = StringVar()
        self.targetVarP.set('00')

        self.target_labelt1 = ttk.Label(self.frame_target, text='11', relief=SUNKEN, justify=CENTER, textvariable=self.targetVar1).grid(row=1, column=2, padx=10)
        self.target_labelt2 = ttk.Label(self.frame_target, text='21', relief=SUNKEN, justify=CENTER, textvariable=self.targetVar2).grid(row=1, column=3, padx=10)
        self.target_labelt3 = ttk.Label(self.frame_target, text='31', relief=SUNKEN, justify=CENTER, textvariable=self.targetVar3).grid(row=1, column=4, padx=10)
        self.target_labelt4 = ttk.Label(self.frame_target, text='41', relief=SUNKEN, justify=CENTER, textvariable=self.targetVar4).grid(row=1, column=5, padx=10)
        self.target_labelt5 = ttk.Label(self.frame_target, text='51', relief=SUNKEN, justify=CENTER, textvariable=self.targetVar5).grid(row=1, column=6, padx=10)
        self.target_labeltP = ttk.Label(self.frame_target, text='09', relief=SUNKEN, justify=CENTER, textvariable=self.targetVarP).grid(row=1, column=7, padx=10)


        self.frame_main_grid = ttk.Frame(master)
        self.frame_main_grid.grid(row=2, column=0)

        self.target_label = ttk.Label(self.frame_main_grid, text='Main  ')
        self.target_label.grid(row=0, column=0)

        self.grid_RA_C1 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=1, column=2, padx=12)
        self.grid_RA_C2 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=1, column=3, padx=10)
        self.grid_RA_C3 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=1, column=4, padx=10)
        self.grid_RA_C4 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=1, column=5, padx=10)
        self.grid_RA_C5 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=1, column=6, padx=10)
        self.grid_RA_CP = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=1, column=7, padx=10)

        self.grid_RB_C1 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=2, column=2, padx=10)
        self.grid_RB_C2 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=2, column=3, padx=10)
        self.grid_RB_C3 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=2, column=4, padx=10)
        self.grid_RB_C4 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=2, column=5, padx=10)
        self.grid_RB_C5 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=2, column=6, padx=10)
        self.grid_RB_CP = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=2, column=7, padx=10)

        self.grid_RC_C1 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=3, column=2, padx=10)
        self.grid_RC_C2 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=3, column=3, padx=10)
        self.grid_RC_C3 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=3, column=4, padx=10)
        self.grid_RC_C4 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=3, column=5, padx=10)
        self.grid_RC_C5 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=3, column=6, padx=10)
        self.grid_RC_CP = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=3, column=7, padx=10)

        self.grid_RD_C1 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=4, column=2, padx=10)
        self.grid_RD_C2 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=4, column=3, padx=10)
        self.grid_RD_C3 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=4, column=4, padx=10)
        self.grid_RD_C4 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=4, column=5, padx=10)
        self.grid_RD_C5 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=4, column=6, padx=10)
        self.grid_RD_CP = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=4, column=7, padx=10)

        self.grid_RE_C1 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=5, column=2, padx=10)
        self.grid_RE_C2 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=5, column=3, padx=10)
        self.grid_RE_C3 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=5, column=4, padx=10)
        self.grid_RE_C4 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=5, column=5, padx=10)
        self.grid_RE_C5 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=5, column=6, padx=10)
        self.grid_RE_CP = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=5, column=7, padx=10)

        self.grid_RF_C1 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=6, column=2, padx=10)
        self.grid_RF_C2 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=6, column=3, padx=10)
        self.grid_RF_C3 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=6, column=4, padx=10)
        self.grid_RF_C4 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=6, column=5, padx=10)
        self.grid_RF_C5 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=6, column=6, padx=10)
        self.grid_RF_CP = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=6, column=7, padx=10)

        self.grid_RG_C1 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=7, column=2, padx=10)
        self.grid_RG_C2 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=7, column=3, padx=10)
        self.grid_RG_C3 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=7, column=4, padx=10)
        self.grid_RG_C4 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=7, column=5, padx=10)
        self.grid_RG_C5 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=7, column=6, padx=10)
        self.grid_RG_CP = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=7, column=7, padx=10)

        self.grid_RH_C1 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=8, column=2, padx=10)
        self.grid_RH_C2 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=8, column=3, padx=10)
        self.grid_RH_C3 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=8, column=4, padx=10)
        self.grid_RH_C4 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=8, column=5, padx=10)
        self.grid_RH_C5 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=8, column=6, padx=10)
        self.grid_RH_CP = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=8, column=7, padx=10)

        self.grid_RI_C1 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=9, column=2, padx=10)
        self.grid_RI_C2 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=9, column=3, padx=10)
        self.grid_RI_C3 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=9, column=4, padx=10)
        self.grid_RI_C4 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=9, column=5, padx=10)
        self.grid_RI_C5 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=9, column=6, padx=10)
        self.grid_RI_CP = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=9, column=7, padx=10)

        self.grid_RJ_C1 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=10, column=2, padx=10)
        self.grid_RJ_C2 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=10, column=3, padx=10)
        self.grid_RJ_C3 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=10, column=4, padx=10)
        self.grid_RJ_C4 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=10, column=5, padx=10)
        self.grid_RJ_C5 = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=10, column=6, padx=10)
        self.grid_RJ_CP = ttk.Label(self.frame_main_grid, text='00', relief=SUNKEN, justify=CENTER).grid(row=10, column=7, padx=10)


        self.grid_row_label1 = ttk.Label(self.frame_main_grid, text='1').grid(row=0, column=2, padx=10)
        self.grid_row_label2 = ttk.Label(self.frame_main_grid, text='2').grid(row=0, column=3, padx=10)
        self.grid_row_label3 = ttk.Label(self.frame_main_grid, text='3').grid(row=0, column=4, padx=10)
        self.grid_row_label4 = ttk.Label(self.frame_main_grid, text='4').grid(row=0, column=5, padx=10)
        self.grid_row_label5 = ttk.Label(self.frame_main_grid, text='5').grid(row=0, column=6, padx=10)
        self.grid_row_labelP = ttk.Label(self.frame_main_grid, text='P').grid(row=0, column=7, padx=10)


        self.grid_col_labelA = ttk.Label(self.frame_main_grid, text='A').grid(row=1, column=0)
        self.grid_col_labelB = ttk.Label(self.frame_main_grid, text='B').grid(row=2, column=0)
        self.grid_col_labelC = ttk.Label(self.frame_main_grid, text='C').grid(row=3, column=0)
        self.grid_col_labelD = ttk.Label(self.frame_main_grid, text='D').grid(row=4, column=0)
        self.grid_col_labelE = ttk.Label(self.frame_main_grid, text='E').grid(row=5, column=0)
        self.grid_col_labelF = ttk.Label(self.frame_main_grid, text='F').grid(row=6, column=0)
        self.grid_col_labelG = ttk.Label(self.frame_main_grid, text='G').grid(row=7, column=0)
        self.grid_col_labelH = ttk.Label(self.frame_main_grid, text='H').grid(row=8, column=0)
        self.grid_col_labelI = ttk.Label(self.frame_main_grid, text='I').grid(row=9, column=0)
        self.grid_col_labelJ = ttk.Label(self.frame_main_grid, text='J').grid(row=10, column=0)


        self.frame_populate = ttk.Frame(master, borderwidth=10)
        self.frame_populate.grid(row=0, column=2, rowspan=5)

        self.populate_targetButton = ttk.Button(self.frame_populate, text="Populate Target")
        self.populate_targetButton.grid(padx=5, pady=10, row=0, column=0, columnspan=4)
        self.populate_targetButton.config(command=self.populate_target)

        self.combox_target = ttk.Combobox(self.frame_populate)
        self.combox_target.grid(padx=5, pady=10, row=1, column=0, columnspan=4)

        self.populate_gridButton = ttk.Button(self.frame_populate, text="Populate Grid")
        self.populate_gridButton.grid(padx=10, pady=10, row=2, column=0, columnspan=4)

        self.combox_maingrid = ttk.Combobox(self.frame_populate)
        self.combox_maingrid.grid(padx=5, pady=10, row=3, column=0, columnspan=4)

        self.populate_moveButton = ttk.Button(self.frame_populate, text="Make Move")
        self.populate_moveButton.grid(padx=10, pady=10, row=4, column=0, columnspan=4)

        self.combox_makemove = ttk.Combobox(self.frame_populate)
        self.combox_makemove.grid(padx=5, pady=10, row=5, column=0, columnspan=4)

        self.pos1_xlabel = ttk.Label(self.frame_populate, text='X').grid(padx=5, pady=5, row=6, column=0)

        self.pos1_ylabel = ttk.Label(self.frame_populate, text='Y').grid(padx=5, pady=5, row=6, column=1)

        self.pos2_xlabel = ttk.Label(self.frame_populate, text='X').grid(padx=5, pady=5, row=6, column=2)

        self.pos2_ylabel = ttk.Label(self.frame_populate, text='Y').grid(padx=5, pady=5, row=6, column=3)


        self.pos1_xlabel = ttk.Label(self.frame_populate, text='A', relief=SUNKEN, justify=CENTER).grid(padx=5, pady=5, row=7, column=0)

        self.pos1_ylabel = ttk.Label(self.frame_populate, text='B', relief=SUNKEN, justify=CENTER).grid(padx=5, pady=5, row=7, column=1)

        self.pos2_xlabel = ttk.Label(self.frame_populate, text='A', relief=SUNKEN, justify=CENTER).grid(padx=5, pady=5, row=7, column=2)

        self.pos2_ylabel = ttk.Label(self.frame_populate, text='B', relief=SUNKEN, justify=CENTER).grid(padx=5, pady=5, row=7, column=3)

    def populate_target(self):
        print('Populating target')
        self.targetVar1.set('01')
        self.targetVar2.set('02')
        self.targetVar3.set('03')
        self.targetVar4.set('04')
        self.targetVar5.set('05')
        self.targetVarP.set('0P')


def main():

    root = Tk()
    lottoWindow = LottoWindow(root)
    root.mainloop()


main()