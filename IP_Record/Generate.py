import pandas
import re

S_data = pandas.read_excel("ip.xlsx", "IP", index_col=None, na_values=["NA"])
with pandas.ExcelWriter("IP_分配.xlsx") as excel_data :
    for ip_value in S_data["IP"] :
        match_object = re.match(r"(\d+.\d+.\d+.)\d+.*",ip_value ,re.I)
        if match_object != None :
            print(match_object[1])
            to_data = pandas.DataFrame({"IP":[], "状态":[], "备注":[], "跳转":[]}, dtype="str")
            for i in range(1,254) :
                to_data.at[i,"IP"] = match_object[1] + str(i)
            to_data.at[1,"跳转"] = '=HYPERLINK("#总表!A1","跳转到总表")'
            to_data.to_excel(excel_data,sheet_name=match_object[1] + "0_24位", index=False)
            #to_data.drop(to_data.index,inplace=True)