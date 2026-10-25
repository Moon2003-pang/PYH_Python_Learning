slang_dic={"觉醒年代":"电视剧",
           "YYDS":"永远单身"
}

slang_dic["双减"]="从未实现"


query=input("请输入要查询的词语:")
if query in slang_dic:
    print("您查询的"+query+"在词典里")
    print(slang_dic[query])
else:
    print("您查询的"+query+"不在词典里")
    print("当前词典收录的词条数目为："+str(len(slang_dic)))