#Imports
from tkinter import *
from tkinter import filedialog
import pandas as pd
import numpy as np
import boto3
import io
import os
import datetime
import sys, traceback
import tkinter as tk

class DynamicGrid(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.text = tk.Text(self, wrap="char", borderwidth=0, highlightthickness=0,
                            state="disabled")
        #self.text.pack(fill="both", expand=True)
 
#make sure user can see all columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
 
#set s3 resources
s3_resource=boto3.resource('s3')
s3_client=boto3.client('s3')
 
#base of the GUI
root=Tk()
root.title('Escanor')
root.configure(background='RoyalBlue3')
width, height=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
 
#set up the frames
outputsFrame=Frame(root, highlightbackground="black", highlightthickness=1)
operationsFrame=Text(root, highlightbackground="black", highlightthickness=1)
cleanFrame=DynamicGrid(operationsFrame, highlightbackground="black", highlightthickness=1)
transformFrame=DynamicGrid(operationsFrame, highlightbackground="black", highlightthickness=1)
analyseFrame=DynamicGrid(operationsFrame, highlightbackground="black", highlightthickness=1)
makerFrame=DynamicGrid(operationsFrame, highlightbackground="black", highlightthickness=1)
outputsFrame.configure(background='RoyalBlue3')
operationsFrame.configure(background='RoyalBlue3')
cleanFrame.configure(background='RoyalBlue3')
transformFrame.configure(background='RoyalBlue3')
analyseFrame.configure(background='RoyalBlue3')
makerFrame.configure(background='RoyalBlue3')
operationsFrame.grid(row=0, column=1, sticky='nsew')
cleanFrame.grid(row=0, column=1, sticky='nsew')
transformFrame.grid(row=1, column=1, sticky='new')
analyseFrame.grid(row=2, column=1, sticky='new')
makerFrame.grid(row=3, column=1, sticky='new')
outputsFrame.grid(row=0, column=0, padx=10, rowspan=2, sticky='ns')
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
operationsFrame.grid_columnconfigure(1, weight=1)
outputsFrame.grid_rowconfigure(0, weight=1)
  
 
#canvas for code and output for results
canvas=Text(outputsFrame, width=100, height=30, borderwidth=1, bg = "RoyalBlue3", fg="white")
output=Text(outputsFrame, width=100, height=20 ,borderwidth=1, wrap="none", bg = "RoyalBlue3", fg ="white")
scrollb=Scrollbar(outputsFrame, orient=HORIZONTAL)
scrollb.grid(row=26,sticky='new')
scrollb.config(command=output.xview)
output.config(yscrollcommand=scrollb.set)
 
#datatypes available for casting
DATATYPES=[
("String", "str"),
("Integer", "int64"),
("Float", "float"),
]

MATHAMATICS=[
("Sum", "+"),
("Subtract", "-"),
("Mulitiply", "*"),
("Divide", "/"),
]
v=StringVar()
 

#start functions here TODO: make these nice and neat, organise them btter
def reader():
                credFNameEntry.delete('1.0', END)
                credEntry.delete('1.0', END)
                global credFName
                credFName=filedialog.askopenfilename(initialdir=r"")
                credFNameEntry.insert(END, credFName)
                with open(credFName, "r") as f:
                                credEntry.insert(END, f.read())
 
def writer():
                fileName=credFNameEntry.get('1.0', END)
                with open(fileName.rstrip(), 'w') as cred_obj:
                                cred_obj.write(credEntry.get('1.0', 'end-1c'))
                cred_obj.close()
 
def S3BucketData():
                global df
                targetObject=s3_client.get_object(Bucket=bucketEntry.get('1.0', 'end-1c'), Key=keyEntry.get('1.0', 'end-1c'))['Body'].read()
                if sheetEntry.get('1.0', 'end-1c') == '':
                                df=pd.read_excel(io.BytesIO(targetObject), encoding='utf-8')
                else:
                                df=pd.read_excel(io.BytesIO(targetObject), encoding='utf-8', sheet_name=sheetEntry.get('1.0', 'end-1c'))
               
def checker():
    try:
        output.insert('1.0', "Data as at: " + str(datetime.datetime.now()) +'\n' + df.to_string() + '\n\n')
    except Exception as e:
        output.insert('1.0', '\n'+str(e)+'\n')
 
def dropBlankColumns():
                global df
                try:
                    df=df
                    df=df.loc[:, ~df.columns.str.contains('^Unnamed')]
                except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')
 
def castDataTypeWindowPop():
                dataTypeCastWindow=Toplevel(root, height=100, width=100)
                global nameofColumnToChangeDataType
                nameofColumnToChangeDataType=Entry(dataTypeCastWindow)
                nameofColumnToChangeDataType.pack()
                for text, mode in DATATYPES:
                                button=Radiobutton(dataTypeCastWindow, text=text, variable=v, value=mode).pack()
                enterButton=Button(dataTypeCastWindow,command=executeDataCast, text="Cast it!", highlightbackground="goldenrod2").pack()
 
def executeDataCast():
                global df
                try:
                    df=df
                    dataType=v.get()
                    column=nameofColumnToChangeDataType.get()
                    df[column] = df[column].astype(dataType)
                    canvas.insert('1.0', f"\ndf[{column}] = df[{column}].astype[{dataType}]")
                except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')

def findNullsWindowPop():
                findNullsWindow=Toplevel(root, height=100, width=100)
                global nameofColumnToCheckForNulls
                nameofColumnToCheckForNulls=Entry(findNullsWindow)
                nameofColumnToCheckForNulls.pack()
                FindButton=Button(findNullsWindow,command=executefindnulls, text="Find Them!", highlightbackground="goldenrod2").pack()

## TO DO: this needs its output written  
def executefindnulls():
                global dfnulls
                global df
                try:
                    df=df
                    column=nameofColumnToCheckForNulls.get()
                    df=df[df[column].isna()]
                    output.insert('1.0', df.to_string())
                    canvas.insert('1.0', f"\ndf=df[df[{column}].isna()]")
                except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')
  
def melterWindowPop():
                melterWindow=Toplevel(root, height=100, width=100)
                global pivoncolumns
                global pivwithcolumns
                global rowvalue
                global colvalue
                global df
                pivoncolumns=Entry(melterWindow)
                pivoncolumns.pack()
                pivwithcolumns=Entry(melterWindow)
                pivwithcolumns.pack()
                rowvalue=Entry(melterWindow)
                rowvalue.pack()
                colvalue=Entry(melterWindow)
                colvalue.pack()
                meltbutton= Button(melterWindow, command=melter, text = 'Melt/Pivot', highlightbackground="goldenrod2")
                meltbutton.pack()
                

def melter():
    ##make sure your variables follow the same pattern in how their written for readability
    global df
    try:
        nameOfRowValues= rowvalue.get()
        nameOfColumnValues= colvalue.get()
        pivotOnColumns=pivoncolumns.get()
        pivotWithColumns=pivwithcolumns.get()
        df=df
        df=pd.melt(df, id_vars=pivotOnColumns,
             value_vars=pivotWithColumns.split(', '),
             value_name=nameOfRowValues,
             var_name=nameOfColumnValues)
        output.insert('1.0', df)
        canvas.insert('1.0', f"""\npd.melt(df, id_vars={[pivotOnColumns]},
            value_vars={pivotWithColumns}.split(', '),
            value_name={nameOfRowValues},
            var_name={nameOfColumnValues})""")
    except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')

## you can easily make a xls version of this, remember to alter the inital dir
def opencsv():
    try:
        path=filedialog.askopenfilename(initialdir="/Desktop",title="Select a file")
        global df
        df=pd.read_csv(filepath_or_buffer=str(path))
    except Exception as e:
        output.insert('1.0', '\n'+str(e)+'\n')

def openxls():
    try:
        path=filedialog.askopenfilename(initialdir="/Desktop",title="Select a file")
        global df
        df=pd.read_excel(filepath_or_buffer=str(path))
    except Exception as e:
        output.insert('1.0', '\n'+str(e)+'\n')

    
## TO DO: let them name their results themselves, not you. 
def makecsv():
    try:
        df.to_csv(path_or_buf=str(path)+ "results.csv")
    except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')   
 
def AWSCredsPop():
    AWSCredsPopFrame=Toplevel(root, height=100, width=100)
    credFNameEntry=Text(AWSCredsPopFrame, width=50, height=1)
    credFNameEntry.grid(row=0, column=0)
    credFNameEntry.insert(INSERT, "Credential File Name Here")
    credEntry=Text(AWSCredsPopFrame, width=25, height=5)
    credEntry.grid(row =2, column=0)
    credEntry.insert(INSERT, "Credential details here")
    readButton=Button(AWSCredsPopFrame, command=reader, text="Find credentials", highlightbackground="goldenrod2")
    readButton.grid(row=1, column=0)
    writeButton =  Button(AWSCredsPopFrame, command=writer, text="Write credentials", highlightbackground="goldenrod2")
    writeButton.grid(row=3, column=0)
    
def AWSBucketPop():
    AWSBucketKeyPop=Toplevel(root, height=100, width=100)
    bucketEntry=Text(AWSBucketKeyPop, width=25, height=0).grid(row=4, column=0)
    bucketEntry.insert(INSERT, "Bucket Name Here") #CHANGE THIS POST TESTING
    keyEntry=Text(AWSBucketKeyPop, width=25, height=0).grid(row=5, column=0)
    keyEntry.insert(INSERT, "Key path") #CHANGE THIS POST TESTING
    sheetEntry=Text(AWSBucketKeyPop, width=25, height=0).grid(row=6, column=0)
    sheetEntry.insert(INSERT, "Sheet. Delete if N/A") #CHANGE POST TESTING
    S3BucketDataButton=Button(AWSBucketKeyPop, command=S3BucketData, text = "Get data", highlightbackground="goldenrod2").grid(row=8, column=0)

def printDatatypes():
    global df
    try:
        df=df
        output.insert('1.0',(df.dtypes))
        canvas.insert('1.0', f"""\n(df.dtypes)""")
    except Exception as e:
                output.insert('1.0', '\n'+str(e)+'\n')

def columnLowerCase():
    global df
    try:
        df=df
        df.columns=map(str.lower, df.columns)
        canvas.insert('1.0', f"""\ndf.columns=map(str.lower, df.columns)""")
    except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')

def columnRemoveSpaces():
    global df
    try:
        df=df
        df.columns=df.columns.str.replace(' ', '_')
        canvas.insert('1.0', f"""\ndf.columns=df.columns.str.replace(' ', '_')""")
    except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')

## TO DO: This is cute, but what if its the sum of two columns per row.
## probably will never need the sum of all
def SummOp():
    global df
    try:
        df=df
        res=df.groupby([groupByColumns.get()])[columnToSum.get()].sum()
        output.insert('1.0', res)
        canvas.insert('1.0', f"""res=df.groupby([{groupByColumns}.get()])[{columnToSum}.get()].sum()""")
    except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')

def summerPop():
    summerPopUp=Toplevel(root, height=100, width=100)
    global groupByColumns
    global df
    global columnToSum
    df=df
    groupByColumns=Entry(summerPopUp)
    groupByColumns.insert(END, 'Group by Columns')
    columnToSum=Entry(summerPopUp)
    columnToSum.insert(END, 'Column to Sum')
    groupByColumns.grid(row=0, column=0)
    columnToSum.grid(row=1, column=0)
    SummColumnButton=Button(summerPopUp, command=SummOp, text='Sum Column', highlightbackground="goldenrod2")
    SummColumnButton.grid(row=2, column=0, pady=10, sticky= 'ew')

def stripWhiteSpace():
    global df
    try:
        df=df
        columToStrip=columnsToStrip.get()
        df[columnToStrip] = df[columnToStrip].str.strip()
        output.insert('1.0', df)
        canvas.insert('1.0', f"""df[{columnToStrip}] = df[{columnToStrip}].str.strip()""")
    except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')

def stripPop():
    stripPopUp=Toplevel(root, height=100, width=100)
    global columnToStrip
    global df
    df=df
    columnsToStrip=Entry(stripPopUp)
    columnsToStrip.grid(row=0, column=0)
    stripColumnButton=Button(stripPopUp, command=stripWhiteSpace, text='strip White Space', highlightbackground="goldenrod2")
    stripColumnButton.grid(row=1, column=0, pady=10, sticky= 'ew')


def replacer():
    global df
    global valuetoReplace
    global relaceWith
    try:
        df=df
        df[columnToRep.get()] = df[columnToRep.get()].replace(valuetoReplace.get(), replaceWith.get())
        output.insert('1.0', df)
        canvas.insert('1.0', f"""df[{columnToRep.get()}] = df[{columnToRep.get()}].replace({valuetoReplace.get()}, {replaceWith.get()})""")
    except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')

def replacerPop():
    replacerPopUp=Toplevel(root, height=100, width=100)
    global columnToRep
    global df
    global valuetoReplace
    global replaceWith
    df=df
    columnToRep=Entry(replacerPopUp)
    valuetoReplace=Entry(replacerPopUp)
    replaceWith=Entry(replacerPopUp)
    columnToRep.grid(row=0, column=0)
    valuetoReplace.grid(row=1, column=0)
    replaceWith.grid(row=2, column=0)
    replacerButton=Button(replacerPopUp, command=replacer, text='Replace', highlightbackground="goldenrod2")
    replacerButton.grid(row=3, column=0, pady=10, sticky= 'ew')

def saver():
    global df
    global dfsaved
    try:
        dfsaved=df
    except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')

def restore():
    global df
    global dfsaved
    try:
        df=dfsaved
    except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')

def lengthOfData():
    global df
    try:
        output.insert('1.0', len(df.index))
    except Exception as e:
        output.insert('1.0', '\n'+str(e)+'\n')

def memoryConsumption():
    global df
    try:
        output.insert('1.0', '\n'+ str(df.memory_usage(index=True).sum())+' mb\n')
    except Exception as e:
        output.insert('1.0', '\n'+str(e)+'\n')

def driveConsumption():
    global df
    try:
        output.insert('1.0', '\n'+ str(float(sys.getsizeof(df)/1000000))+'\n')
    except Exception as e:
        output.insert('1.0', '\n'+str(e)+'\n')


def mathematicsFeatures():
                mathWindow=Toplevel(root, height=100, width=100)
                global resultColumnName
                global firstColumn
                global secondColumn
                resultColumnName=Entry(mathWindow)
                resultColumnName.pack()
                firstColumn=Entry(mathWindow)
                firstColumn.pack()
                secondColumn=Entry(mathWindow)
                secondColumn.pack()
                for text, operation in MATHAMATICS:
                                button=Radiobutton(mathWindow, text=text, variable=v, value=operation).pack()
                enterButton=Button(mathWindow,command=executeMathematics, text="Operate!", highlightbackground="goldenrod2").pack()
 
def executeMathematics():
                global df
                global resultColumnName
                global firstColumn
                global secondColumn
                try:
                    df=df
                    resultColumnName=resultColumnName.get()
                    firstColumn=firstColumn.get()
                    secondColumn=secondColumn.get()
                    op=v.get()
                    if op == "Sum":
                        df[resultColumnName] = df[firstColumn] + df[secondColumn]
                        canvas.insert('1.0', f"\ndf[{resultColumnName}] = df[{firstColumn}] + df[{secondColumn}]")
                    elif op == "Subtract":
                        df[resultColumnName] = df[firstColumn] - df[secondColumn]
                        canvas.insert('1.0', f"\ndf[{resultColumnName}] = df[{firstColumn}] - df[{secondColumn}]")
                    elif op == "Mulitiply":
                        df[resultColumnName] = df[firstColumn] * df[secondColumn]
                        canvas.insert('1.0', f"\ndf[{resultColumnName}] = df[{firstColumn}] * df[{secondColumn}]")
                    elif op == "Divide":
                        df[resultColumnName] = df[firstColumn] / df[secondColumn]
                        canvas.insert('1.0', f"\ndf[{resultColumnName}] = df[{firstColumn}] / df[{secondColumn}]")
                except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')
    

## TO DO:
## row sum
## row multi
## row divide
## filter for value - see and shape
## rename columns function
## none of your entry fields have descriptions to prompt
## join function
## union function


def dropPop():
    replacerPopUp=Toplevel(root, height=100, width=100)
    global columnsToDrop
    global df
    df=df
    columnsToDrop=Entry(replacerPopUp).pack()
    replacerButton=Button(dropPop, command=dropper, text='Replace', highlightbackground="goldenrod2")
    replacerButton.pack()

def dropper():
    global df
    global columnsToDrop
    try:
        df=df.drop(columns=columnsToDrop.get().split(', '))
    except Exception as e:
                    output.insert('1.0', '\n'+str(e)+'\n')


#layouts start here TODO: need to separate the buttons from teh layout
canvas.grid(row=0, column=0, sticky='nsew')
output.grid(row=13, column=0, rowspan=10, pady=(10, 40), sticky='nsew') 
dfCheckButton=Button(outputsFrame, command=checker, text="Check Data", highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=12, column=0, sticky= 'ew')

cleanLabel=Label(cleanFrame, text="Data Cleaning Tools", bg = "RoyalBlue3", fg='white').pack()
dropBlanksButton=Button(cleanFrame, command=dropBlankColumns, text="Drop Blank Columns", highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
columnLowerCaseButton=Button(cleanFrame, command=columnLowerCase, text='Column titles lower case', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
columnRemoveSpacesButton=Button(cleanFrame, command=columnRemoveSpaces, text='Remove Spaces in Headers', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
stripWhiteSpaceButton=Button(cleanFrame, command=stripPop, text='Strip White Space', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
replaceValuesButton=Button(cleanFrame, command=replacerPop, text='Replace Value in Col', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)

# cleanLabel=Label(cleanFrame, text="Data Cleaning Tools", bg = "RoyalBlue3", fg='white').grid(row=0, column=1, pady=(0, 5))
# dropBlanksButton=Button(cleanFrame, command=dropBlankColumns, text="Drop Blank Columns", highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=0, sticky='nsew')
# columnLowerCaseButton=Button(cleanFrame, command=columnLowerCase, text='Column titles lower case', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=1, sticky='nsew')
# columnRemoveSpacesButton=Button(cleanFrame, command=columnRemoveSpaces, text='Remove Spaces in Headers', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=2, sticky='nsew')
# stripWhiteSpaceButton=Button(cleanFrame, command=stripPop, text='Strip White Space', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=2, column=0, sticky='nsew')
# replaceValuesButton=Button(cleanFrame, command=replacerPop, text='Replace Value in Col', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=2, column=1, sticky='nsew')


transformLabel=Label(transformFrame, text="Transformation Tools", bg = "RoyalBlue3", fg='white').pack()
DataTypesButton=Button(transformFrame, command=castDataTypeWindowPop, text="Cast Data Types", highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
meltWindowbutton=Button(transformFrame, command=melterWindowPop, text='Melt Data', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
mathopsbtn=Button(transformFrame, text="Do Math", command=mathematicsFeatures, highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)


#transformLabel=Label(transformFrame, text="Transformation Tools", bg = "RoyalBlue3", fg='white').grid(row=0, column=1, pady=(0, 5))
#DataTypesButton=Button(transformFrame, command=castDataTypeWindowPop, text="Cast Data Types", highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=0, sticky='nsew')
#meltWindowbutton=Button(transformFrame, command=melterWindowPop, text='Melt Data', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=1, sticky='nsew')
#mathopsbtn=Button(transformFrame, text="Do Math", command=mathematicsFeatures, highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=2, sticky='nsew')

AnalyseLabel=Label(analyseFrame, text="Analytical Tools", bg = "RoyalBlue3", fg='white').pack()
nullCheckWindowbutton=Button(analyseFrame, command=findNullsWindowPop, text='Find Nulls', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack()
printDTypesButton=Button(analyseFrame, command=printDatatypes, text='Print Data Types', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
SummColumnButton=Button(analyseFrame, command=summerPop, text='Sum Column', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
lengthofdatabtn=Button(analyseFrame, text="Count Rows", command=lengthOfData, highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
memoryofdatabtn=Button(analyseFrame, text="Memory Usage Estimate", command=memoryConsumption, highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
sizeofdatabtn=Button(analyseFrame, text="Byte Size", command=driveConsumption, highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)

# AnalyseLabel=Label(analyseFrame, text="Analytical Tools", bg = "RoyalBlue3", fg='white').grid(row=0, column=1, pady=(0, 5))
# nullCheckWindowbutton=Button(analyseFrame, command=findNullsWindowPop, text='Find Nulls', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=0, sticky='nsew')
# printDTypesButton=Button(analyseFrame, command=printDatatypes, text='Print Data Types', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=1, sticky='nsew')
# SummColumnButton=Button(analyseFrame, command=summerPop, text='Sum Column', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=2, sticky='nsew')
# lengthofdatabtn=Button(analyseFrame, text="Count Rows", command=lengthOfData, highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=3, sticky='nsew')
# memoryofdatabtn=Button(analyseFrame, text="Memory Usage Estimate", command=memoryConsumption, highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=4, sticky='nsew')
# sizeofdatabtn=Button(analyseFrame, text="Byte Size", command=driveConsumption, highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=2, column=2, sticky='nsew')

subactionsLabel=Label(makerFrame, text="Sub-actions", bg = "RoyalBlue3", fg='white').pack()
SaveDF=Button(makerFrame, command=saver, text='Save DF', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
restoreDF=Button(makerFrame, command=restore, text='Restore DF', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)
tocsv_btn=Button(makerFrame, text="Make CSV", command=makecsv, highlightbackground="goldenrod2", wraplength=100, width=15, height=2).pack(side=LEFT)

# subactionsLabel=Label(makerFrame, text="Sub-actions", bg = "RoyalBlue3", fg='white').grid(row=0, column=1, pady=(0, 5))
# SaveDF=Button(makerFrame, command=saver, text='Save DF', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=0, sticky='nsew')
# restoreDF=Button(makerFrame, command=restore, text='Restore DF', highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=1, sticky='nsew')
# tocsv_btn=Button(makerFrame, text="Make CSV", command=makecsv, highlightbackground="goldenrod2", wraplength=100, width=15, height=2).grid(row=1, column=2, sticky='nsew')


#menubar placeholder
menubar=Menu(root, tearoff=0)
root.config(menu=menubar)
dataMenu=Menu(menubar, tearoff=0)
fileMenu=Menu(menubar, tearoff=0)
dataMenu.add_command(label="AWS credentials", command=AWSCredsPop)
dataMenu.add_command(label="CSV Data", command=opencsv)
dataMenu.add_command(label="Excel Data", command=openxls)
dataMenu.add_command(label="Make CSV", command=makecsv)
menubar.add_cascade(label="File", menu=fileMenu)
menubar.add_cascade(label="Add Data", menu=dataMenu)
fileMenu.add_command(label="Quit!", command=root.quit)

 
root.mainloop()